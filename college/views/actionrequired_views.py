from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.actionrequired import ActionRequired
from ..serializers.actionrequired_serializers import ActionRequiredSerializer
from datetime import date
from ..models.students import Student

@api_view(['GET'])
def get_action_required(request):
    try:
        if request.user.role not in ('SL', 'PR', 'AD', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # Get query parameters for filtering
        course_id = request.query_params.get('course_id')
        grade_id = request.query_params.get('grade_id')
        section_id = request.query_params.get('section_id')

        # Start with all actions
        actions = ActionRequired.objects.filter(due_date__gte=date.today()).select_related('student')

        # Apply filters based on student
        if course_id:
            actions = actions.filter(student__course_id=course_id)
        if grade_id:
            actions = actions.filter(student__grade_id=grade_id)
        if section_id:
            actions = actions.filter(student__section_id=section_id)

        serializer = ActionRequiredSerializer(actions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
import logging

   
logger = logging.getLogger(__name__)

@api_view(['POST', 'PUT'])
def manage_action_required(request):
    logger.debug(f"Request method: {request.method}, Data: {request.data}")
    try:
        if request.user.role not in ('SL', 'PR', 'AD', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'POST':
            serializer = ActionRequiredSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                logger.info("Created action successfully")
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            logger.error(f"Serializer errors: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'PUT':
            action_id = request.data.get('id')
            if not action_id:
                logger.error("Action ID missing in PUT request")
                return Response({"error": "Action ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                action = ActionRequired.objects.get(id=action_id)
            except ActionRequired.DoesNotExist:
                logger.error(f"Action not found: ID {action_id}")
                return Response({"error": "Action not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = ActionRequiredSerializer(action, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"Updated action ID: {action_id}")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Serializer errors in PUT: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        logger.exception(f"Unexpected error in manage_action_required: {str(e)}")
        return Response({"error": f"Internal server error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)