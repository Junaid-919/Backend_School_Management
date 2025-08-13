from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.exam_invigilator import ExamInvigilator
from ..serializers.exam_invigilator_serializers import ExamInvigilatorSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_invigilator_data(request):
    try:
        dietplan = ExamInvigilator.objects.all()
        serializer = ExamInvigilatorSerializer(dietplan, many=True)
        return Response(serializer.data)
    except ExamInvigilator.DoesNotExist:
        return Response({"error": "invigilator not found."}, status=404)
    
@api_view(['GET'])
def get_invigilator_withid(request, invigilator_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        appointment = ExamInvigilator.objects.get(id=invigilator_id)
        serializer = ExamInvigilatorSerializer(appointment,partial=True)
        return Response(serializer.data)
    except ExamInvigilator.DoesNotExist:
        return Response({"error": "invigilator not found."}, status=404)
    
@api_view(['POST'])
def create_invigilator_data(request):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Serialize and validate the data
        serializer = ExamInvigilatorSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except ExamInvigilator.DoesNotExist:
        return Response({"error": "invigilator not found."}, status=404)
    
@api_view(['PUT'])
def update_invigilator_data(request, invigilator_id):
    """
    Update an existing appointment for a logged-in Teacher.
    """
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['invigilator_id'] = ExamInvigilator.id

        # Fetch the specific appointment to update
        dietplan = ExamInvigilator.objects.get(id=invigilator_id)

        # Serialize and validate the new data
        serializer = ExamInvigilatorSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except ExamInvigilator.DoesNotExist:
        return Response({"error": "invigilator not found."}, status=404)


@api_view(['DELETE'])
def delete_invigilator_data(request, invigilator_id):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the specific appointment to delete
        dietplan = Section.objects.get(id=invigilator_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Section deleted successfully."}, status=204)  # HTTP 204 No Content

    except ExamInvigilator.DoesNotExist:
        return Response({"error": "invigilator not found."}, status=404)