from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.grades import Grade
from ..serializers.grades_serializers import GradeSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_grade_data(request):
    try:
        dietplan = Grade.objects.all()
        serializer = GradeSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Grade.DoesNotExist:
        return Response({"error": "Grade not found."}, status=404)
    
@api_view(['GET'])
def get_grade_withid(request, grade_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        appointment = Grade.objects.get(id=grade_id)
        serializer = GradeSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Grade.DoesNotExist:
        return Response({"error": "Grade not found."}, status=404)
    
@api_view(['POST'])
def create_grade_data(request):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Serialize and validate the data
        serializer = GradeSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Grade.DoesNotExist:
        return Response({"error": "Grade not found."}, status=404)
    
@api_view(['PUT'])
def update_grade_data(request, grade_id):
    """
    Update an existing appointment for a logged-in Teacher.
    """
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['grade_id'] = grade.id

        # Fetch the specific appointment to update
        dietplan = Grade.objects.get(id=grade_id)

        # Serialize and validate the new data
        serializer = GradeSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Grade.DoesNotExist:
        return Response({"error": "Grade not found."}, status=404)


@api_view(['DELETE'])
def delete_grade_data(request, grade_id):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the specific appointment to delete
        dietplan = Grade.objects.get(id=grade_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Grade deleted successfully."}, status=204)  # HTTP 204 No Content

    except Grade.DoesNotExist:
        return Response({"error": "Grade not found."}, status=404)