from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.contenttypes.models import ContentType

from ..models.raise_leave import Raiseleave
from ..models.students import Student
from ..models.teachers import Teacher
from ..serializers.leave_serializers import RaiseleaveSerializer
import traceback
import logging
from users.models import CustomUser 
from .workflow_views import start_workflow, complete_step, complete_full_workflow, reject_workflow

logger = logging.getLogger(__name__)


@api_view(['GET'])
def get_leave_data(request):
    """GET all raiseleave entries"""
    if request.user.role not in ('SL', 'JL', 'PR', 'AD'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    leaves = Raiseleave.objects.all()
    serializer = RaiseleaveSerializer(leaves, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def farward_leave_to_principal(request, instance_id):
    try:
        if request.user.role not in ('SL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        return complete_step(instance_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "CustomUser not found."}, status=400)


@api_view(['POST'])
def approve_leave_to_by_sl(request, instance_id):
    try:
        if request.user.role not in ('SL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        return complete_full_workflow(instance_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "CustomUser not found."}, status=400)


@api_view(['POST'])
def approve_leave_principal(request, instance_id):
    try:
        if request.user.role not in ('PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        return complete_full_workflow(instance_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "CustomUser not found."}, status=400)


@api_view(['POST'])
def create_leave_data(request):
    try:
        print("request_data = ", request.data)

        # Permission check
        if request.user.role not in ('SL', 'JL', 'AD'):
            return Response({"error": "Not allowed to create attendance."}, status=400)

        customuser = request.user

        # Attach user to the request data
        request_data = request.data.copy()
        request_data['user'] = customuser.id

        # Initialize serializer
        serializer = RaiseleaveSerializer(data=request_data)
        if serializer.is_valid():
            # Save the object without instance_id first
            leave_instance = serializer.save()

            # Now start workflow
            workflow_design_id = 1
            instance = start_workflow(workflow_design_id)
            instance_id = instance.data["id"]
            print("instance_id = ", instance_id)

            # Update the saved object with instance_id
            leave_instance.instance_id = instance_id
            leave_instance.save()

            # Re-serialize to include updated instance_id in response
            updated_serializer = RaiseleaveSerializer(leave_instance)
            return Response(updated_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)

    except CustomUser.DoesNotExist:
        return Response({"error": "CustomUser not found."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def reject_leave(request, instance_id):

    try:
        reject = reject_workflow(instance_id)
        return Response({"leave is rejected."}, status=201)
    except:
        return Response({"error": "CustomUser not found."}, status=status.HTTP_400_BAD_REQUEST)




