from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models.fee_details import Fee_details 
from ..models.fee_structure import FeeStructure
from ..models.students import Student
from ..serializers.fee_details_serializers import FeedetailSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def get_fee_details(request):
    try:
        if request.user.role not in ('AD', 'PR'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
        fee_details = Fee_details.objects.all()
        serializer = FeedetailSerializer(fee_details, many=True)
        return Response(serializer.data)
    except Fee_details.DoesNotExist:
        return Response({"error": "Fee details not found."}, status=404)

@api_view(['GET'])
def get_fee_detail_by_id(request, fee_detail_id):
    if request.user.role not in ('AD'):
        return Response({"error": "Not Allowed to create attendence."}, status=400)
    fee_detail = get_object_or_404(Fee_details, pk=fee_detail_id)
    serializer = FeedetailSerializer(fee_detail)
    return Response(serializer.data)

from django.forms.models import model_to_dict

@api_view(['POST'])
def create_fee_detail(request):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
        data = request.data
        student_id = data.get('student')
        student = Student.objects.get(id=student_id)
        student_data = model_to_dict(student)
        print("student = ", student_data)
        course = student.course
        print("course = ", course)
        feestructure = FeeStructure.objects.get(course=course)

        total_fee = feestructure.total_fee_amount
        payment_amount = int(data.get('payment_amount', 0))
        total_due = total_fee - payment_amount

        fee_detail = Fee_details.objects.create(
            reciept_number=data.get('reciept_number'),
            payment_date=data.get('payment_date'),
            total_fee=total_fee,
            payment_amount=payment_amount,
            total_due=total_due,
            student=student,
            teacher_id=1
        )

        # Update student's fee paid and due
        student.fee_paid += payment_amount
        student.fee_due = total_fee - student.fee_paid
        student.save()

        serializer = FeedetailSerializer(fee_detail)
        return Response(serializer.data, status=201)
    except Student.DoesNotExist:
        return Response({"error": "Student not found."}, status=404)

@api_view(['PUT'])
def update_fee_detail(request, fee_detail_id):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        fee_detail = Fee_details.objects.get(pk=fee_detail_id)
        student = fee_detail.student
        course = student.course

        # Revert previous payment
        student.fee_paid -= fee_detail.payment_amount

        data = request.data
        payment_amount = int(data.get('payment_amount', 0))
        feestructure = FeeStructure.objects.get(course=course)
        total_fee = fee_detail.student.course.fee_structure.total_fee_amount
        total_due = total_fee - payment_amount
        # total_due = 35000 - payment_amount

        fee_detail.reciept_number = data.get('reciept_number')
        fee_detail.payment_date = data.get('payment_date')
        fee_detail.total_fee = total_fee
        fee_detail.payment_amount = payment_amount
        fee_detail.total_due = total_due
        fee_detail.teacher_id = data.get('teacher')
        fee_detail.save()

        # Update student's fee paid and due
        student.fee_paid += payment_amount
        student.fee_due = total_fee - student.fee_paid
        student.save()

        serializer = FeedetailSerializer(fee_detail)
        return Response(serializer.data)
    except Fee_details.DoesNotExist:
        return Response({"error": "Fee detail not found."}, status=404)

@api_view(['DELETE'])
def delete_fee_detail(request, fee_detail_id):
    try:
        if request.user.role not in ('AD'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        fee_detail = Fee_details.objects.get(pk=fee_detail_id)
        student = fee_detail.student

        # Revert fee paid by student
        student.fee_paid -= fee_detail.payment_amount
        student.fee_due = fee_detail.total_fee - student.fee_paid
        student.save()

        fee_detail.delete()
        return Response({"message": "Fee detail deleted successfully."})
    except Fee_details.DoesNotExist:
        return Response({"error": "Fee detail not found."}, status=404)



from django.db.models import Sum

@api_view(['GET'])
def fee_summary_view(request):
    summary = Fee_details.objects.aggregate(
        total_fee=Sum('total_fee'),
        total_paid=Sum('payment_amount'),
        total_due=Sum('total_due')
    )

    return Response({
        'total_fee_assigned': summary['total_fee'] or 0,
        'total_fee_paid': summary['total_paid'] or 0,
        'total_fee_due': summary['total_due'] or 0
    })