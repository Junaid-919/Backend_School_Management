from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.subjects import Subject
from ..serializers.subjects_serializers import SubjectSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_subject_data(request):
    try:
        dietplan = Subject.objects.all()
        serializer = SubjectSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found."}, status=404)
    
@api_view(['GET'])
def get_subject_withid(request, subject_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        appointment = Subject.objects.get(id=subject_id)
        serializer = SubjectSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Subject.DoesNotExist:
        return Response({"error": "Subject not found."}, status=404)
    
@api_view(['POST'])
def create_subject_data(request):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Serialize and validate the data
        serializer = SubjectSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Subject.DoesNotExist:
        return Response({"error": "Subject not found."}, status=404)
    
@api_view(['PUT'])
def update_subject_data(request, subject_id):
    """
    Update an existing appointment for a logged-in Teacher.
    """
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['subject_id'] = subject.id

        # Fetch the specific appointment to update
        dietplan = Subject.objects.get(id=subject_id)

        # Serialize and validate the new data
        serializer = SubjectSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Subject.DoesNotExist:
        return Response({"error": "Subject not found."}, status=404)


@api_view(['DELETE'])
def delete_subject_data(request, subject_id):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the specific appointment to delete
        dietplan = Section.objects.get(id=subject_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Section deleted successfully."}, status=204)  # HTTP 204 No Content

    except Subject.DoesNotExist:
        return Response({"error": "Subject not found."}, status=404)