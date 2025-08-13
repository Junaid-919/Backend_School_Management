from rest_framework.decorators import api_view
from ..models.college import College
from ..serializers.college_serializers import CollegeSerializers
from rest_framework.response import Response






@api_view(['GET'])
def get_college_data(request):
    try:
        dietplan = College.objects.all()
        serializer = CollegeSerializers(dietplan, many=True)
        return Response(serializer.data)
    except College.DoesNotExist:
        return Response({"error": "Student not found."}, status=404)