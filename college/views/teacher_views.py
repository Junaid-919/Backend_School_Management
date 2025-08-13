from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.teachers import Teacher
from ..models.daily_login import Daily_login
from ..models.raise_leave import Raiseleave
from ..serializers.teacher_serializers import TeacherSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from django.utils.dateparse import parse_date
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser
from datetime import datetime, timedelta, date
from django.db.models import Q, Count


@api_view(['GET'])
def get_teacher_data(request):
    try:
        dietplan = Teacher.objects.all()
        serializer = TeacherSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=404)
    
@api_view(['GET'])
def get_teacher_data_withid(request, teacher_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        appointment = Teacher.objects.get(id=Teacher_id)
        serializer = TeacherSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=404)
    
@api_view(['POST'])
def create_teacher_data(request):
    try:

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['teacher_id'] = teacher.id

        # Serialize and validate the data
        serializer = TeacherSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=404)
    
@api_view(['PUT'])
def update_teacher_data(request, teacher_id):
    """
    Update an existing appointment for a logged-in Teacher.
    """
    try:
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)
        request_data['teacher_id'] = teacher.id

        # Fetch the specific appointment to update
        dietplan = Teacher.objects.get(id=teacher_id)

        # Serialize and validate the new data
        serializer = TeacherSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=404)


@api_view(['DELETE'])
def delete_teacher_data(request, teacher_id):
    try:

        # Fetch the specific appointment to delete
        dietplan = Teacher.objects.get(id=teacher_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Teacher deleted successfully."}, status=204)  # HTTP 204 No Content

    except Teacher.DoesNotExist:
        return Response({"error": "Teacher not found."}, status=404)


# @api_view(['GET'])
# def teacher_attendance_summary(request):
#     date_str = request.query_params.get('date')
#     grade_id = request.query_params.get('grade_id')
    
#     strength = CustomUser.objects.filter(grade_id=grade_id).count()

#     if not date_str:
#         return Response({"error": "date query param is required (YYYY-MM-DD)"}, status=status.HTTP_400_BAD_REQUEST)

#     try:
#         target_date = parse_date(date_str)
#         if not target_date:
#             raise ValueError
#     except ValueError:
#         return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

#     # Filter base queryset for teachers by grade_id (if provided)
#     teacher_qs = CustomUser.objects.all()
#     if grade_id:
#         teacher_qs = teacher_qs.filter(grade_id=grade_id)

#     # 1. Teachers who logged in on the date
#     logged_in_teachers = teacher_qs.filter(daily_login__login_date=target_date).distinct()
#     logged_in_ids = set(logged_in_teachers.values_list('id', flat=True))

#     # 2. Teachers who are on leave and did not log in
#     teacher_content_type = ContentType.objects.get_for_model(Teacher)
#     leave_teacher_ids = Raiseleave.objects.filter(
#         date_of_leave=target_date,
#         user_id__in=teacher_qs.values_list('id', flat=True)
#     ).values_list('user_id', flat=True)

#     leave_raisers = teacher_qs.filter(id__in=leave_teacher_ids).exclude(id__in=logged_in_ids)
#     leave_ids = set(leave_raisers.values_list('id', flat=True))

#     # 3. Teachers who neither logged in nor are on leave
#     all_teacher_ids = set(teacher_qs.values_list('id', flat=True))
#     absent_ids = all_teacher_ids - logged_in_ids - leave_ids

#     return Response({
#         "totalStaff": strength,
#         "present": len(logged_in_ids),
#         "onLeave": len(leave_ids),
#         "absents": len(absent_ids)
#     }, status=status.HTTP_200_OK)







@api_view(['GET'])
def teacher_attendance_summary(request):
    # """
    # Returns attendance summary of teachers for each day in a date range,
    # including total staff, present, on leave, and absent count per day.
    # Optional filtering by grade_id.
    # """
    # from_date_str = request.query_params.get('fromDate')
    # to_date_str = request.query_params.get('toDate')
    # grade_id = request.query_params.get('grade_id')

    # try:
    #     from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date() if from_date_str else date.today()
    #     to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() if to_date_str else date.today()
    # except ValueError:
    #     return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    # if from_date > to_date:
    #     return Response({"error": "fromDate cannot be after toDate"}, status=400)

    # # Filter teachers by role
    # teacher_qs = CustomUser.objects.filter(role__in=['AD', 'SL', 'JL'])
    # if grade_id and grade_id.lower() != 'null' and grade_id != '':
    #     teacher_qs = teacher_qs.filter(grade_id=grade_id)

    # total_staff = teacher_qs.count()
    # teacher_ids = teacher_qs.values_list('id', flat=True)

    # results = []
    # current_date = from_date

    # while current_date <= to_date:
    #     # Logged in on this date
    #     logged_in_ids = Daily_login.objects.filter(
    #         user_id__in=teacher_ids,
    #         login_date=current_date
    #     ).values_list('user_id', flat=True)

    #     # On leave on this date
    #     leave_ids = Raiseleave.objects.filter(
    #         user_id__in=teacher_ids,
    #         date_of_leave=current_date
    #     ).values_list('user_id', flat=True)

    #     if current_date > date.today():
    #         present = 0
    #         on_leave = 0
    #         absent = 0
    #     else:
    #         present = len(set(logged_in_ids))
    #         on_leave = len(set(leave_ids))
    #         absent = total_staff - present - on_leave

    #     results.append({
    #         "Date": current_date.strftime('%Y-%m-%d'),
    #         "totalStaff": total_staff,
    #         "present": present,
    #         "onLeave": on_leave,
    #         "absent": absent
    #     })

    #     current_date += timedelta(days=1)

    # return Response(results, status=200)

    """
    Returns attendance summary of teachers for each day in a date range,
    or for last 7 (weekly) or 30 (monthly) days.
    Optional filtering by grade_id.
    """
    from_date_str = request.query_params.get('fromDate')
    to_date_str = request.query_params.get('toDate')
    range_type = request.query_params.get('rangeType')  # Accepts 'weekly' or 'monthly'
    grade_id = request.query_params.get('grade_id')

    # Determine date range
    try:
        if range_type:
            today = date.today()
            if range_type.lower() == 'weekly':
                from_date = today - timedelta(days=6)
                to_date = today
            elif range_type.lower() == 'monthly':
                from_date = today - timedelta(days=29)
                to_date = today
            else:
                return Response({"error": "Invalid rangeType. Use 'weekly' or 'monthly'."}, status=400)
        else:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date() if from_date_str else date.today()
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() if to_date_str else date.today()

        if from_date > to_date:
            return Response({"error": "fromDate cannot be after toDate"}, status=400)

    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    # Filter relevant teachers (AD, SL, JL only)
    teacher_qs = CustomUser.objects.filter(role__in=['AD', 'SL', 'JL'])
    if grade_id and grade_id.lower() != 'null' and grade_id.strip() != '':
        teacher_qs = teacher_qs.filter(grade_id=grade_id)

    total_staff = teacher_qs.count()
    teacher_ids = teacher_qs.values_list('id', flat=True)

    results = []
    current_date = from_date

    while current_date <= to_date:
        # Get present teachers
        logged_in_ids = Daily_login.objects.filter(
            user_id__in=teacher_ids,
            login_date=current_date
        ).values_list('user_id', flat=True)

        # Get leave entries
        leave_ids = Raiseleave.objects.filter(
            user_id__in=teacher_ids,
            date_of_leave=current_date
        ).values_list('user_id', flat=True)

        # Handle future dates
        if current_date > date.today():
            present = 0
            on_leave = 0
            absent = 0
        else:
            present = len(set(logged_in_ids))
            on_leave = len(set(leave_ids))
            absent = total_staff - present - on_leave

        results.append({
            "Date": current_date.strftime('%Y-%m-%d'),
            "totalStaff": total_staff,
            "present": present,
            "onLeave": on_leave,
            "absent": absent
        })

        current_date += timedelta(days=1)

    return Response(results, status=200)
    
# @api_view(['GET'])
# def get_dietplan_data_with_name(request):
#     try:
        
#         patient_name_from_search =  request.GET.get('Teacher_name')
#         page_number_from_search = request.GET.get('page')

#         # Get the patient based on the logged-in user
#         patient = Teacher.objects.get(user=request.user)
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
            

#     except Teacher.DoesNotExist:
#         # If no patient is found, return an error response
#         return Response({"error": "Patient not found."}, status=404)