# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from ..models.fee_structure import Feestructure
# from ..serializers.fee_serializers import FeestructureSerializer
# from rest_framework.pagination import PageNumberPagination
# from .workflow_views import start_workflow, complete_full_workflow, complete_step


# @api_view(['GET'])
# def get_fee_data(request):
#     try:
#         if request.user.role not in ('AD', 'PR'):
#             return Response({"error": "Not Allowed to create attendence."}, status=400)
#         dietplan = Feestructure.objects.all()
#         serializer = FeestructureSerializer(dietplan, many=True)
#         return Response(serializer.data)
#     except Feestructure.DoesNotExist:
#         return Response({"error": "Feestructure not found."}, status=404)
    
# @api_view(['GET'])
# def get_fee_data_withid(request, feestructure_id):
#     """
#     Fetch the appointment of a logged-in Teacher.
#     """
#     try:
#         if request.user.role not in ('AD', 'PR'):
#             return Response({"error": "Not Allowed to create attendence."}, status=400)
#         appointment = Feestructure.objects.get(id=feestructure_id)
#         serializer = FeestructureSerializer(appointment,partial=True)
#         return Response(serializer.data)
#     except Feestructure.DoesNotExist:
#         return Response({"error": "Feestructure not found."}, status=404)
    
# @api_view(['POST'])
# def create_fee_data(request):
#     try:
#         if request.user.role not in ('AD', 'PR'):
#             return Response({"error": "Not Allowed to create attendence."}, status=400)

#         request_data = request.data.copy()
#         print("request_data: ", request_data)

#         # Serialize and validate the data
#         serializer = FeestructureSerializer(data=request_data)
#         if serializer.is_valid():
#             leave_instance = serializer.save()
#             workflow_design_id = 2
#             instance = start_workflow(workflow_design_id)
#             print("instance = ", instance.data["id"])
#             instance_id = instance.data["id"]

#             leave_instance.instance_id = instance_id
#             leave_instance.save()

#             updated_serializer = FeestructureSerializer(leave_instance)
#             return Response(updated_serializer.data, status=201)  # HTTP 201 Created
#         else:
#         # Return validation errors
#             return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

#     except Feestructure.DoesNotExist:
#         return Response({"error": "Feestructure not found."}, status=404)
    
# @api_view(['PUT'])
# def update_fee_data(request, feestructure_id):
#     """
#     Update an existing appointment for a logged-in Teacher.
#     """
#     try:
#         if request.user.role not in ('AD', 'PR'):
#             return Response({"error": "Not Allowed to create attendence."}, status=400)
#         # Fetch the patient associated with the logged-in user

#         request_data = request.data.copy()
#         print("request_data: ", request_data)
#         request_data['feestructure_id'] = feestructure.id

#         # Fetch the specific appointment to update
#         dietplan = Feestructure.objects.get(id=feestructure_id)

#         # Serialize and validate the new data
#         serializer = FeestructureSerializer(dietplan, data=request.data, partial=True)
#         if serializer.is_valid():
#             # Save the updated appointment to the database
#             serializer.save()
#             return Response(serializer.data, status=200)  # HTTP 200 OK
#         else:
#             # Return validation errors
#             return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

#     except Feestructure.DoesNotExist:
#         return Response({"error": "Feestructure not found."}, status=404)


# @api_view(['DELETE'])
# def delete_fee_data(request, feestructure_id):
#     try:
#         if request.user.role not in ('AD', 'PR'):
#             return Response({"error": "Not Allowed to create attendence."}, status=400)
#         # Fetch the specific appointment to delete
#         dietplan = Feestructure.objects.get(id=feestructure_id)

#         # Delete the appointment
#         dietplan.delete()
#         return Response({"message": "Feestructure deleted successfully."}, status=204)  # HTTP 204 No Content

#     except Feestructure.DoesNotExist:
#         return Response({"error": "Feestructure not found."}, status=404)

    
# # @api_view(['GET'])
# # def get_dietplan_data_with_name(request):
# #     try:
        
# #         patient_name_from_search =  request.GET.get('Teacher_name')
# #         page_number_from_search = request.GET.get('page')

# #         # Get the patient based on the logged-in user
# #         patient = Teacher.objects.get(user=request.user)
# #         print("Patient data:", patient)
# #         all_dietplan = DietPlan.objects.filter(patient=patient)
# #         paginator1 = PageNumberPagination()
# #         paginator2 = PageNumberPagination()
# #         paginator1.page_size = 5
# #         paginator2.page_size = 5


# #         # Check if any billing records are found for the patient
# #         # if not billing_records.exists():
# #         #     return Response({"error": "No billing records found for the provided patient name."}, status=404)
        
# #         if patient_name_from_search == None:
# #             result_page = paginator1.paginate_queryset(all_dietplan,request)
# #             serializer1 = DietPlanSerializer (result_page,many=True)
# #             total_pages = paginator1.page.paginator.num_pages
# #             return Response({'count': paginator1.page.paginator.count, 'total_pages': total_pages, 'results':serializer1.data})
# #         else:
# #             print("###### line 49 ######", patient_name_from_search)
            
# #             dietplan_records = DietPlan.objects.filter(patient__patient_name__icontains=patient_name_from_search, patient=patient)
# #             result_page1 = paginator2.paginate_queryset(dietplan_records,request)

# #             print("apointment records:", dietplan_records)
# #              # Serialize the billing records and return the response
# #             serializer = DietPlanSerializer(result_page1, many=True)
# #             total_pages1 = paginator2.page.paginator.num_pages
# #             return Response({'count': paginator2.page.paginator.count, 'total_pages': total_pages1, 'results': serializer.data})
            

# #     except Teacher.DoesNotExist:
# #         # If no patient is found, return an error response
# #         return Response({"error": "Patient not found."}, status=404)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.fee_structure import FeeStructure
from ..serializers.fee_serializers import FeeStructureSerializer
from .workflow_views import start_workflow, complete_full_workflow, complete_step

@api_view(['POST'])
def create_fee_structure(request):
    if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
    request_data = request.data.copy()
    print("request_data = ", request_data)
    serializer = FeeStructureSerializer(data=request.data)
    if serializer.is_valid():
        leave_instance = serializer.save()
        workflow_design_id = 2
        instance = start_workflow(workflow_design_id)
        print("instance = ", instance.data["id"])
        instance_id = instance.data["id"]

        leave_instance.instance_id = instance_id
        leave_instance.save()

        updated_serializer = FeeStructureSerializer(leave_instance)
        return Response(updated_serializer.data, status=201)  # HTTP 201 Created
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_fee_data(request):
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
        dietplan = FeeStructure.objects.all()
        serializer = FeeStructureSerializer(dietplan, many=True)
        return Response(serializer.data)
    except FeeStructure.DoesNotExist:
        return Response({"error": "Feestructure not found."}, status=404)

@api_view(['POST'])
def reject_fee_structure(request, instance_id):

    try:
        reject = reject_workflow(instance_id)
        return Response({"leave is rejected."}, status=201)
    except:
        return Response({"error": "CustomUser not found."}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def approve_structure_principal(request, instance_id):
    try:
        if request.user.role not in ('PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
        return complete_full_workflow(instance_id)
    except CustomUser.DoesNotExist:
        return Response({"error": "CustomUser not found."}, status=400)