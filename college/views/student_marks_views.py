from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.student_marks_serializers import StudentMarksSerializer
from ..models.student_marks import Student_marks
from django.db.models import Q

@api_view(['POST'])
def create_student_marks_data(request):
    try:
        if request.user.role not in ('JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        print("Incoming data: ", data)

        grade = data.get('grade')
        section = data.get('section')
        exam = data.get('exam')
        subject = data.get('subject')
        marks_list = data.get('marks', [])

        if not marks_list:
            return Response({"error": "No marks data provided."}, status=status.HTTP_400_BAD_REQUEST)

        created = []
        errors = []

        for item in marks_list:
            student_data = {
                'grade': grade,
                'section': section,
                'subject': subject,
                'exam' : exam,
                'student': item.get('student_id'),
                'marks': item.get('marks'),
                'teacher': 1
            }

            serializer = StudentMarksSerializer(data=student_data)
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



@api_view(['GET'])
def get_marks_by_course_section_grade(request):
    print("role = ", request.user)
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    course_id = request.query_params.get('course_id')
    section_id = request.query_params.get('section_id')
    grade_id = request.query_params.get('grade_id')
    exam_id = request.query_params.get('exam_id')

    filters = {}

    # if course_id and course_id.lower() != 'null' and course_id != '':
    #     filters['student__course_id'] = course_id
    # if section_id and section_id.lower() != 'null' and section_id != '':
    #     filters['student__section_id'] = section_id
    # if grade_id and grade_id.lower() != 'null' and grade_id != '':
    #     filters['student__grade_id'] = grade_id
    if exam_id and exam_id.lower() != 'null' and exam_id != '':
        filters['exam_id'] = exam_id

    attendances = Student_marks.objects.filter(**filters)
    serializer = StudentMarksSerializer(attendances, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_marks_by_subject(request):
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    subject_id = request.query_params.get('subject_id')

    marks = Student_marks.objects.filter(subject_id=subject_id)
    serializer = StudentMarksSerializer(marks, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def get_marks_by_student(request):
    if request.user.role not in ('JL', 'SL'):
        return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    student_id = request.query_params.get('student_id')

    marks = Student_marks.objects.filter(student_id=student_id)
    serializer = StudentMarksSerializer(marks, many=True)
    return Response(serializer.data, status=200)




@api_view(['GET'])
def get_student_marks_report(request):
    # Get query parameters
    # course_id = request.GET.get('course_id')
    grade_id = request.GET.get('grade_id')
    section_id = request.GET.get('section_id')
    student_name = request.GET.get('student_name')

    # Validate input
    # if not all([course_id, grade_id, section_id, student_name]):
    #     return Response({'error': 'Missing required query parameters'}, status=400)

    try:
        student = Student.objects.get(
            # Q(course_id=course_id),
            Q(grade_id=grade_id),
            Q(section_id=section_id),
            Q(student_name__iexact=student_name.strip())
        )
    except Student.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)

    # Fetch marks for the student
    marks_qs = Student_marks.objects.filter(student=student).select_related('exam__subject')

    subjects_data = []
    total_max_marks = 0
    total_obtained_marks = 0

    for sm in marks_qs:
        subject = sm.exam.subject
        try:
            max_marks = int(subject.max_marks)
        except (ValueError, TypeError):
            max_marks = 0
        obtained_marks = sm.marks

        subjects_data.append({
            'subject_name': subject.subject_name,
            'subject_code': subject.subject_code,
            'max_marks': max_marks,
            'obtained_marks': obtained_marks,
        })

        total_max_marks += max_marks
        total_obtained_marks += obtained_marks

    response = {
        'student': {
            'id': student.id,
            'name': student.student_name,
            'enrollment_number': student.enrollment_number,
            # 'course': student.course.name,
            'grade': student.grade.name,
            'section': student.section.name,
        },
        'subjects': subjects_data,
        'total_max_marks': total_max_marks,
        'total_obtained_marks': total_obtained_marks,
    }

    return Response(response)
