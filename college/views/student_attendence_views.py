from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.student_attendence_serializers import StudentAttendenceSerializer
from ..models.student_attendence import Student_attendence
from django.contrib.auth.decorators import login_required
from ..models.students import Student
from django.db.models import Count, Q
from datetime import datetime, timedelta, date

# @login_required
@api_view(['POST'])
def create_student_attendence_data(request):
    # if user.role == 'PR':
        try:
            if request.user.role not in ('JL'):
                return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
            data = request.data
            print("Incoming data: ", data)

            grade = data.get('grade')
            section = data.get('section')
            # course = data.get('course')
            date = data.get('date')
            attendance_list = data.get('attendance', [])

            if not attendance_list:
                return Response({"error": "No attendance data provided."}, status=status.HTTP_400_BAD_REQUEST)

            created = []
            errors = []

            for item in attendance_list:
                student_data = {
                    'grade': grade,
                    'section': section,
                    # 'course' : course,
                    'date': date,
                    'student': item.get('student_id'),  # Make sure this matches the serializer's field name
                    'attendance': item.get('attendance'),
                    'teacher' : 1
                }

                serializer = StudentAttendenceSerializer(data=student_data)
                if serializer.is_valid():
                    serializer.save()
                    created.append(serializer.data)
                else:
                    print(f"Validation error for student {item.get('student_id')}: {serializer.errors}")
                    errors.append({'student_id': item.get('student_id'), 'errors': serializer.errors})

            if errors:
                return Response({
                    "created": created,
                    "errors": errors
                }, status=status.HTTP_207_MULTI_STATUS)

            return Response(created, status=status.HTTP_201_CREATED)

        except Exception as e:
            print("Unhandled exception: ", str(e))
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    # else:
    #     return Response("invalid user to create attendence", status=400)





@api_view(['GET'])
def get_attendance_by_course_section_grade(request):
    print("role = ", request.user.role)
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    # course_id = request.query_params.get('course_id')
    section_id = request.query_params.get('section_id')
    grade_id = request.query_params.get('grade_id')

    filters = {}

    # if course_id and course_id.lower() != 'null' and course_id != '':
    #     filters['student__course_id'] = course_id
    if section_id and section_id.lower() != 'null' and section_id != '':
        filters['student__section_id'] = section_id
    if grade_id and grade_id.lower() != 'null' and grade_id != '':
        filters['student__grade_id'] = grade_id

    attendances = Student_attendence.objects.filter(**filters)
    serializer = StudentAttendenceSerializer(attendances, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_students_count_by_attendance_present(request):
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    date = request.query_params.get('date')
    attendance1 = "present"

    attendance = Student_attendence.objects.filter(date=date, attendance=attendance1)
    serializer = StudentAttendenceSerializer(attendance, many=True)
    return Response(serializer.data, status=200)

@api_view(['GET'])
def get_students_count_by_attendance_absent(request):
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    date = request.query_params.get('date')
    attendance1 = "absent"

    attendance = Student_attendence.objects.filter(date=date, attendance=attendance1)
    serializer = StudentAttendenceSerializer(attendance, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_students_count_by_attendance_leave(request):
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    date = request.query_params.get('date')
    attendance1 = "leave"

    attendance = Student_attendence.objects.filter(date=date, attendance=attendance1)
    serializer = StudentAttendenceSerializer(attendance, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_attendance_by_course_section_grade_json(request):
    date = request.query_params.get('date')
    # course_id = request.query_params.get('course_id')
    section_id = request.query_params.get('section_id')
    grade_id = request.query_params.get('grade_id')

    filters = {}

    # if course_id and course_id.lower() != 'null' and course_id != '':
    #     filters['student__course_id'] = course_id
    if section_id and section_id.lower() != 'null' and section_id != '':
        filters['student__section_id'] = section_id
    if grade_id and grade_id.lower() != 'null' and grade_id != '':
        filters['student__grade_id'] = grade_id
    if date and grade_id.lower() != 'null' and date != '':
        filters['date'] = date

    # Optimize related fetch if needed
    attendance_records = Student_attendence.objects.select_related('student').filter(**filters)

    student_list = []
    for record in attendance_records:
        student = record.student
        student_list.append({
            "name": student.student_name,
            # "group": student.course.name if student.course else '',
            "status": record.attendance
        })

    return Response({"studentList": student_list}, status=200)




# @api_view(['GET'])
# def get_all_students_summary(request):
#     """
#     Fetch all students' data (total strength, present, absent, on leave, and student list)
#     with optional filtering by date, course_id, section_id, and grade_id.
#     """
#     date = request.query_params.get('date')
#     # course_id = request.query_params.get('course_id')
#     section_id = request.query_params.get('section_id')
#     grade_id = request.query_params.get('grade_id')

#     # Build filters for Student model (total strength)
#     student_filters = {}
#     # if course_id and course_id.lower() != 'null' and course_id != '':
#     #     student_filters['course__id'] = course_id
#     if section_id and section_id.lower() != 'null' and section_id != '':
#         student_filters['section__id'] = section_id
#     if grade_id and grade_id.lower() != 'null' and grade_id != '':
#         student_filters['grade__id'] = grade_id

#     # Total strength: count all students matching filters
#     total_strength = Student.objects.filter(**student_filters).count()

#     # Build filters for Student_attendence model
#     attendance_filters = {}
#     # if course_id and course_id.lower() != 'null' and course_id != '':
#     #     attendance_filters['student__course__id'] = course_id
#     if section_id and section_id.lower() != 'null' and section_id != '':
#         attendance_filters['student__section__id'] = section_id
#     if grade_id and grade_id.lower() != 'null' and grade_id != '':
#         attendance_filters['student__grade__id'] = grade_id
#     if date and date.lower() != 'null' and date != '':
#         attendance_filters['date'] = date

#     # Aggregate attendance counts
#     attendance_counts = Student_attendence.objects.filter(**attendance_filters).aggregate(
#         present=Count('id', filter=Q(attendance='present')),
#         absent=Count('id', filter=Q(attendance='absent')),
#         on_leave=Count('id', filter=Q(attendance='leave'))
#     )

#     # Fetch student list with attendance details
#     attendance_records = Student_attendence.objects.select_related('student').filter(**attendance_filters)
#     student_list = [
#         {
#             "name": record.student.student_name,
#             # "group": record.student.course.name if record.student.course else '',
#             "status": record.attendance
#         }
#         for record in attendance_records
#     ]

#     response_data = {
#         "totalStrength": total_strength,
#         "present": attendance_counts['present'] or 0,
#         "absent": attendance_counts['absent'] or 0,
#         "onLeave": attendance_counts['on_leave'] or 0,
#         "studentList": student_list
#     }

#     return Response(response_data, status=200)

@api_view(['GET'])
def get_all_students_summary(request):
    from_date_str = request.query_params.get('fromDate')
    to_date_str = request.query_params.get('toDate')
    range_type = request.query_params.get('rangeType')  # Accepts 'weekly' or 'monthly'
    grade_id = request.query_params.get('grade_id')

    try:
        # Use rangeType if provided
        today = date.today()
        if range_type:
            if range_type.lower() == 'weekly':
                from_date = today - timedelta(days=6)
                to_date = today
            elif range_type.lower() == 'monthly':
                from_date = today - timedelta(days=29)
                to_date = today
            else:
                return Response({"error": "Invalid rangeType. Use 'weekly' or 'monthly'."}, status=400)
        else:
            from_date = datetime.strptime(from_date_str, '%Y-%m-%d').date() if from_date_str else today
            to_date = datetime.strptime(to_date_str, '%Y-%m-%d').date() if to_date_str else today

        if from_date > to_date:
            return Response({"error": "fromDate cannot be after toDate"}, status=400)

    except ValueError:
        return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=400)

    # Filter relevant students
    student_qs = Student.objects.all()
    if grade_id and grade_id.lower() != 'null' and grade_id.strip() != '':
        student_qs = student_qs.filter(grade_id=grade_id)

    total_students = student_qs.count()
    student_ids = student_qs.values_list('id', flat=True)

    results = []
    current_date = from_date

    while current_date <= to_date:
        # Present on this date
        present_ids = Student_attendence.objects.filter(
            student_id__in=student_ids,
            date=current_date,
            attendance="present"
        ).values_list('student_id', flat=True)

        # On leave on this date
        leave_ids = Student_attendence.objects.filter(
            student_id__in=student_ids,
            date=current_date,
            attendance="leave"
        ).values_list('student_id', flat=True)

        # Future dates → zeros
        if current_date > today:
            present = 0
            on_leave = 0
            absent = 0
        else:
            present = len(set(present_ids))
            on_leave = len(set(leave_ids))
            absent = total_students - present - on_leave

        results.append({
            "Date": current_date.strftime('%Y-%m-%d'),
            "totalStudents": total_students,
            "present": present,
            "onLeave": on_leave,
            "absent": absent
        })

        current_date += timedelta(days=1)

    return Response(results, status=200)