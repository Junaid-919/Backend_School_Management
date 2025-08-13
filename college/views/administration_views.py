from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.administration import Administration
from ..serializers.administration_serializers import AdministrationSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_administration_data(request):
    try:
        dietplan = Administration.objects.all()
        serializer = AdministrationSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Administration.DoesNotExist:
        return Response({"error": "Administration not found."}, status=404)
    
@api_view(['GET'])
def get_administration_data_withid(request, administration_id):
    """
    Fetch the appointment of a logged-in Administration.
    """
    try:
        appointment = Administration.objects.get(id=administration_id)
        serializer = AdministrationSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Administration.DoesNotExist:
        return Response({"error": "Administration not found."}, status=404)
    
@api_view(['POST'])
def create_administration_data(request):
    try:

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['administration_id'] = administration.id

        # Serialize and validate the data
        serializer = AdministrationSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Administration.DoesNotExist:
        return Response({"error": "Administration not found."}, status=404)
    
@api_view(['PUT'])
def update_administration_data(request, administration_id):
    """
    Update an existing appointment for a logged-in Administration.
    """
    try:
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['administration_id'] = administration.id

        # Fetch the specific appointment to update
        dietplan = Administration.objects.get(id=administration_id)

        # Serialize and validate the new data
        serializer = AdministrationSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Administration.DoesNotExist:
        return Response({"error": "Administration not found."}, status=404)


@api_view(['DELETE'])
def delete_administration_data(request, administration_id):
    try:

        # Fetch the specific appointment to delete
        dietplan = Administration.objects.get(id=administration_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Administration deleted successfully."}, status=204)  # HTTP 204 No Content

    except Administration.DoesNotExist:
        return Response({"error": "Patient not found."}, status=404)