from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.announcements import Announcement
from ..serializers.announcement_serializers import AnnouncementSerializer
from rest_framework.pagination import PageNumberPagination


@api_view(['GET'])
def get_announcement_data(request):
    try:
        if request.user.role not in ('JL', 'SL', 'PR', 'AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        dietplan = Announcement.objects.all()
        serializer = AnnouncementSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=404)
    
@api_view(['GET'])
def get_announcement_data_withid(request, announcement_id):
    """
    Fetch the appointment of a logged-in Announcement.
    """
    try:
        if request.user.role not in ('JL', 'SL', 'PR', 'AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        appointment = Announcement.objects.get(id=announcement_id)
        serializer = AnnouncementSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=404)
    
@api_view(['POST'])
def create_announcement_data(request):
    try:
        if request.user.role not in ('PR', 'AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Serialize and validate the data
        serializer = AnnouncementSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=404)
    
@api_view(['PUT'])
def update_announcement_data(request, announcement_id):
    """
    Update an existing appointment for a logged-in Announcement.
    """
    try:
        if request.user.role not in ('PR', 'AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['announcement_id'] = announcement.id

        # Fetch the specific appointment to update
        dietplan = Announcement.objects.get(id=announcement_id)

        # Serialize and validate the new data
        serializer = AnnouncementSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=404)


@api_view(['DELETE'])
def delete_announcement_data(request, announcement_id):
    try:
        if request.user.role not in ('PR', 'AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the specific appointment to delete
        dietplan = Announcement.objects.get(id=announcement_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Announcement deleted successfully."}, status=204)  # HTTP 204 No Content

    except Announcement.DoesNotExist:
        return Response({"error": "Announcement not found."}, status=404)
    
# @api_view(['GET'])
# def get_dietplan_data_with_name(request):
#     try:
        
#         patient_name_from_search =  request.GET.get('Announcement_name')
#         page_number_from_search = request.GET.get('page')

#         # Get the patient based on the logged-in user
#         patient = Announcement.objects.get(user=request.user)
#         print("Patient data:", patient)
#         all_dietplan = DietPlan.objects.filter(patient=patient)
#         paginator1 = PageNumberPagination()
#         paginator2 = PageNumberPagination()
#         paginator1.page_size = 5
#         paginator2.page_size = 5


#         # Check if any billing records are found for the patient
#         # if not billing_records.exists():
#         #     return Response({"error": "No billing records found for the provided patient name."}, status=404)
        
#         if patient_name_from_search == None:
#             result_page = paginator1.paginate_queryset(all_dietplan,request)
#             serializer1 = DietPlanSerializer (result_page,many=True)
#             total_pages = paginator1.page.paginator.num_pages
#             return Response({'count': paginator1.page.paginator.count, 'total_pages': total_pages, 'results':serializer1.data})
#         else:
#             print("###### line 49 ######", patient_name_from_search)
            
#             dietplan_records = DietPlan.objects.filter(patient__patient_name__icontains=patient_name_from_search, patient=patient)
#             result_page1 = paginator2.paginate_queryset(dietplan_records,request)

#             print("apointment records:", dietplan_records)
#              # Serialize the billing records and return the response
#             serializer = DietPlanSerializer(result_page1, many=True)
#             total_pages1 = paginator2.page.paginator.num_pages
#             return Response({'count': paginator2.page.paginator.count, 'total_pages': total_pages1, 'results': serializer.data})
            

#     except Announcement.DoesNotExist:
#         # If no patient is found, return an error response
#         return Response({"error": "Patient not found."}, status=404)