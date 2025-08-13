from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models.daily_login import Daily_login
from ..serializers.daily_login_serializers import DailyloginSerializer
from rest_framework.pagination import PageNumberPagination
from ..models.raise_leave import Raiseleave


@api_view(['GET'])
def get_login_data(request):
    try:
        if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        dietplan = Daily_login.objects.all()
        serializer = DailyloginSerializer(dietplan, many=True)
        return Response(serializer.data)
    except Daily_login.DoesNotExist:
        return Response({"error": "Daily_login not found."}, status=404)
    
@api_view(['GET'])
def get_login_withid(request, login_id):
    """
    Fetch the appointment of a logged-in Teacher.
    """
    try:
        if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        appointment = Daily_login.objects.get(id=login_id)
        serializer = DailyloginSerializer(appointment,partial=True)
        return Response(serializer.data)
    except Daily_login.DoesNotExist:
        return Response({"error": "Daily_login not found."}, status=404)
    
@api_view(['POST'])
def create_login_data(request):
    try:
        if request.user.role not in ('AD', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Serialize and validate the data
        serializer = DailyloginSerializer(data=request_data)
        if serializer.is_valid():
        # Save the appointment to the database
            serializer.save()
            return Response(serializer.data, status=201)  # HTTP 201 Created
        else:
        # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Daily_login.DoesNotExist:
        return Response({"error": "Daily_login not found."}, status=404)
    
@api_view(['PUT'])
def update_login_data(request, login_id):
    """
    Update an existing appointment for a logged-in Teacher.
    """
    try:
        # Fetch the patient associated with the logged-in user

        request_data = request.data.copy()
        print("request_data: ", request_data)

        # Fetch the specific appointment to update
        dietplan = Daily_login.objects.get(id=login_id)
        dietplan.logout_time = request_data["logout_time"]

        # Serialize and validate the new data
        serializer = DailyloginSerializer(dietplan, data=request.data, partial=True)
        if serializer.is_valid():
            # Save the updated appointment to the database
            serializer.save()
            return Response(serializer.data, status=200)  # HTTP 200 OK
        else:
            # Return validation errors
            return Response(serializer.errors, status=400)  # HTTP 400 Bad Request

    except Daily_login.DoesNotExist:
        return Response({"error": "Daily_login not found."}, status=404)


@api_view(['DELETE'])
def delete_login_data(request, login_id):
    try:

        # Fetch the specific appointment to delete
        dietplan = Daily_login.objects.get(id=login_id)

        # Delete the appointment
        dietplan.delete()
        return Response({"message": "Daily_login deleted successfully."}, status=204)  # HTTP 204 No Content

    except Daily_login.DoesNotExist:
        return Response({"error": "Daily_login not found."}, status=404)



from datetime import date, timedelta
import calendar
from django.utils.timezone import now
from django.db.models import Q


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_monthly_login_summary(request):
    user = request.user
    today = now().date()
    first_day = today.replace(day=1)

    # Step 1: Get weekdays from 1st of the month to today
    valid_working_days = [
        first_day + timedelta(days=i)
        for i in range((today - first_day).days + 1)
        if (first_day + timedelta(days=i)).weekday() < 6  # Mon–Fri only
    ]

    # Step 2: Logins in this range
    login_dates = set(
        Daily_login.objects.filter(
            user=user,
            login_date__range=(first_day, today)
        ).values_list('login_date', flat=True)
    )

    # Step 3: Leave dates in this range
    leaves = Raiseleave.objects.filter(
        user=user,
        date_of_leave__lte=today,
        return_date__gte=first_day
    )

    leave_dates = set()
    for leave in leaves:
        leave_range = [
            leave.date_of_leave + timedelta(days=i)
            for i in range((leave.return_date - leave.date_of_leave).days + 1)
        ]
        leave_dates.update([
            d for d in leave_range
            if first_day <= d <= today and d.weekday() < 5
        ])

    # Step 4: Present = login + leave
    present_days = login_dates.union(leave_dates)

    # Step 5: Absent = working days - present
    absent_days = [d for d in valid_working_days if d not in present_days]

    return Response({
        "total_logins": len(login_dates),
        "total_leaves": len(leave_dates),
        "total_absents": len(absent_days),
    })