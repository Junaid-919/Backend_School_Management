from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models.upcommingevent import UpcomingEvent
from ..serializers.upcommingevent_serializers import UpcomingEventSerializer
from datetime import date

@api_view(['GET'])
def get_upcoming_events(request):
    try:
        if request.user.role not in ('SL', 'PR', 'AD', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        events = UpcomingEvent.objects.filter(event_date__gte=date.today()).order_by('event_date')
        serializer = UpcomingEventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
    
from datetime import datetime
    
    
@api_view(['POST', 'PUT'])
def create_upcoming_events(request):
    print("a")
    try:
        print("b")
        if request.user.role not in ('SL', 'PR', 'AD', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        print("c")
        if request.method == 'POST':
            print("1")
            data = request.data.copy()  # Make a mutable copy
            now = datetime.now().isoformat()  # Or use timezone.now() if using Django timezone
            data['created_at'] = now
            data['updated_at'] = now
            print("2")
            serializer = UpcomingEventSerializer(data=data)
            print("3")
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        elif request.method == 'PUT':
            event_id = request.data.get('id')
            if not event_id:
                return Response({"error": "Event ID is required for updating."}, status=status.HTTP_400_BAD_REQUEST)
            try:
                event = UpcomingEvent.objects.get(id=event_id)
            except UpcomingEvent.DoesNotExist:
                return Response({"error": "Event not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = UpcomingEventSerializer(event, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    