from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from django.db.models import Max
from ..models.workflowdesign import WorkflowDesign
from ..models.workflowsteps import WorkflowStep
from ..models.workflowinstance import WorkflowInstance
from ..models.workflowinstancesteps import WorkflowInstanceStep
from ..serializers.workflowdesign_serializers import WorkflowDesignSerializer
from ..serializers.workflowstep_serializers import WorkflowStepSerializer
from ..serializers.workflowinstancedetail_serializers import WorkflowInstanceDetailSerializer
from ..serializers.workflowinstancestep_serializers import WorkflowInstanceStepSerializer
from ..serializers.workflowinstance_serializers import WorkflowInstanceSerializer


# @api_view(['POST'])
def start_workflow(workflow_design_id):
    try:
        workflow_design = WorkflowDesign.objects.get(id=workflow_design_id)
        first_step = WorkflowStep.objects.filter(workflow_design=workflow_design).order_by('step_order').first()

        if not first_step:
            return Response({'error': 'No steps defined for this workflow design.'}, status=400)

        instance = WorkflowInstance.objects.create(
            name=f"Workflow Instance {timezone.now()}",
            status="In Progress",
            created_at=timezone.now(),
            workflow_design=workflow_design,
            current_step=first_step
        )

        WorkflowInstanceStep.objects.create(
            workflow_instance=instance,
            workflow_step=first_step
        )

        serializer = WorkflowInstanceSerializer(instance)
        return Response(serializer.data, status=201)

    except WorkflowDesign.DoesNotExist:
        return Response({"error": "Workflow Design not found."}, status=404)


# @api_view(['POST'])
def complete_step(instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)
        current_step = instance.current_step

        instance_step = WorkflowInstanceStep.objects.get(
            workflow_instance=instance,
            workflow_step=current_step
        )

        instance_step.completed = True
        instance_step.completed_at = timezone.now()
        instance_step.completed_by = "sys"
        instance_step.save()

        next_step = WorkflowStep.objects.filter(
            workflow_design=instance.workflow_design,
            step_order__gt=current_step.step_order
        ).order_by('step_order').first()

        if next_step:
            instance.current_step = next_step
            WorkflowInstanceStep.objects.create(
                workflow_instance=instance,
                workflow_step=next_step
            )
        else:
            instance.status = "Completed"
            instance.current_step = None

        instance.save()
        return Response({'status': instance.status}, status=200)

    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow Instance not found."}, status=404)
    except WorkflowInstanceStep.DoesNotExist:
        return Response({"error": "Instance Step not found."}, status=404)


# @api_view(['GET'])
def get_workflow_instance(instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)
        serializer = WorkflowInstanceDetailSerializer(instance)
        return Response(serializer.data)
    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow Instance not found."}, status=404)



# @api_view(['POST'])
def complete_full_workflow(instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)

        # Get current step order
        current_step = instance.current_step
        if not current_step:
            return Response({"message": "Workflow already completed."}, status=200)

        current_order = current_step.step_order

        # Get remaining steps (greater than or equal to current)
        remaining_steps = WorkflowStep.objects.filter(
            workflow_design=instance.workflow_design,
            step_order__gte=current_order
        ).order_by('step_order')

        for step in remaining_steps:
            # Skip steps already completed
            instance_step, created = WorkflowInstanceStep.objects.get_or_create(
                workflow_instance=instance,
                workflow_step=step
            )
            if instance_step.completed:
                continue

            instance_step.completed = True
            instance_step.completed_at = timezone.now()
            instance_step.completed_by = "sys"
            instance_step.save()

        # Finalize the workflow
        instance.status = "Completed"
        instance.current_step = None
        instance.save()

        return Response({
            "message": f"Workflow instance {instance.id} completed successfully.",
            "status": instance.status
        }, status=200)

    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow instance not found."}, status=404)

    except Exception as e:
        return Response({"error": str(e)}, status=500)




# @api_view(['GET'])
def get_workflow_instance_steps( instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)
        steps = WorkflowInstanceStep.objects.filter(workflow_instance=instance)
        serializer = WorkflowInstanceStepSerializer(steps, many=True)
        return Response(serializer.data)
    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow Instance not found."}, status=404)


# @api_view(['GET'])
def get_workflow_design_for_instance(instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)
        serializer = WorkflowDesignSerializer(instance.workflow_design)
        return Response(serializer.data)
    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow Instance not found."}, status=404)


# @api_view(['GET'])
def get_max_workflow_instance_id(request):
    max_id = WorkflowInstance.objects.aggregate(Max('id'))['id__max']
    return Response({'max_id': max_id or 0})




@api_view(['POST'])
def reject_workflow(request, instance_id):
    try:
        instance = WorkflowInstance.objects.get(id=instance_id)

        if instance.status == "Completed":
            return Response({"message": "Cannot reject a completed workflow."}, status=400)

        # Mark current step as rejected (optional logic)
        current_step = instance.current_step
        if current_step:
            try:
                instance_step = WorkflowInstanceStep.objects.get(
                    workflow_instance=instance,
                    workflow_step=current_step
                )
                instance_step.completed = False  # Not completed
                instance_step.completed_by = "sys"
                instance_step.completed_at = timezone.now()
                instance_step.save()
            except WorkflowInstanceStep.DoesNotExist:
                pass

        # Mark workflow as rejected
        instance.status = "Rejected"
        instance.current_step = None
        instance.save()

        return Response({
            "message": f"Workflow instance {instance.id} rejected successfully.",
            "status": instance.status
        }, status=200)

    except WorkflowInstance.DoesNotExist:
        return Response({"error": "Workflow instance not found."}, status=404)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
