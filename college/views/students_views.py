from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.students import Student
from ..serializers.student_serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
import traceback
from ..models.student_marks import Student_marks
from ..serializers.student_marks_serializers import StudentMarksSerializer



@api_view(['GET'])
def get_student_data(request):
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        dietplan = Student.objects.all()
        serializer = StudentSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=404)
    
@api_view(['GET'])
def get_student_data_withid(request, student_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        appointment = Student.objects.get(id=student_id)
        serializer = StudentSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=404)
    
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_student_data(request):
    print("method is called")
    print("1 = ", request.user)
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        print("request_data:", request.data)
        print("request_files:", request.FILES)

        serializer = StudentSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
@parser_classes([MultiPartParser, FormParser])
def update_student_data(request, student_id):
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        print("request_data:", request.data)
        print("request_files:", request.FILES)

        student = Student.objects.get(id=student_id)

        serializer = StudentSerializer(student, data=request.data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def delete_student_data(request, student_id):
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the specific appointment to delete
        dietplan = Student.objects.get(id=student_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Student deleted successfully."}, status=204)  # HTTP 204 No Content

    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=404)


@api_view(['GET'])
def get_students_by_section_and_grade(request):
    if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    section_id = request.query_params.get('section_id')
    grade_id = request.query_params.get('grade_id')
    # course_id = request.query_params.get('course_id')

    filters = {}

    if section_id and section_id.lower() != 'null' and section_id != '':
        filters['section_id'] = section_id
    if grade_id and grade_id.lower() != 'null' and grade_id != '':
        filters['grade_id'] = grade_id
    # if course_id and course_id.lower() != 'null' and course_id != '':
    #     filters['course_id'] = course_id

    students = Student.objects.filter(**filters)
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def search_students_by_name(request):
    if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    name_query = request.query_params.get('student_name', '')

    if name_query:
        students = Student.objects.filter(student_name__icontains=name_query)
    else:
        students = Student.objects.all()
            
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def total_strength_by_grade(request):
    if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
    grade_id = request.query_params.get('grade_id')

    filters = {}

    if grade_id and grade_id.lower() != 'null' and grade_id != '':
        filters['grade_id'] = grade_id

    students = Student.objects.filter(**filters).count()

    return Response(students, status=status.HTTP_200_OK)


# @api_view(['GET'])
# def total_strength_by_course(request):
#     if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
#             return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
#     course_id = request.query_params.get('course_id')

#     filters = {}

#     if course_id and course_id.lower() != 'null' and course_id != '':
#         filters['course_id'] = course_id

#     students = Student.objects.filter(**filters).count()
#     serializer = StudentSerializer(students, many=True)
#     return Response(serializer.data, status=status.HTTP_200_OK)

    
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

from django.forms.models import model_to_dict
from django.db.models import Avg, Sum, Count


@api_view(['GET'])
def get_student_report_card(request, student_id):
    try:
        # Get all marks for the student
        marks = Student_marks.objects.filter(student_id=student_id)
        print("1")
        
        if not marks.exists():
            return Response({
                "error": f"No marks found for student ID {student_id}"
            }, status=status.HTTP_404_NOT_FOUND)

        
        marks_list = [model_to_dict(mark) for mark in marks]

        print("2 = ", marks_list)
        
        # Calculate average percentage
        total_marks = marks.aggregate(total=Sum('marks'))['total'] or 0
        print("3 = ", total_marks)
        total_subjects = marks.count()
        print("4 = ", total_subjects)
        max_possible_marks = total_subjects * 100  # Assuming each subject is out of 100
        print("5 = ", max_possible_marks)
        percentage = (total_marks / max_possible_marks * 100) if max_possible_marks > 0 else 0
        print("6 = ", percentage )
        
        # Serialize marks data
        serializer = StudentMarksSerializer(marks, many=True)
        print("7")
        
        # Prepare response data
        response_data = {
            'student_id': student_id,
            'marks': serializer.data,
            'total_marks': total_marks,
            'total_subjects': total_subjects,
            'percentage': round(percentage, 2)
        }

        print("report card = ", response_data)
        
        return Response(response_data, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({
            "error": str(e),
            "traceback": traceback.format_exc()
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)