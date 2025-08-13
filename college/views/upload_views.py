from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from ..models.uploads import Upload
from ..serializers.upload_serializers import UploadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])  # ✅ Add this
def create_upload_data(request):
    
    try:
        if request.user.role not in ('JL', 'SL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        # request_data1 = request.data.copy()
        request_data = dict(request.data)
        print("request_data = ", request_data)
        if isinstance(request_data.get('uploaded_by'), list):
            request_data['uploaded_by'] = request_data['uploaded_by'][0]
        if isinstance(request_data.get('upload_type'), list):
            request_data['upload_type'] = request_data['upload_type'][0]


        print("request_data after debug = ", request_data)
        serializer = UploadSerializer(data=request_data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)

    except Upload.DoesNotExist:  # corrected 'execpt' to 'except'
        return Response({"error": "Upload not found."}, status=404)


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_upload_data(request):
    try:
        # if request.user.role not in ('JL', 'SL'):
        #     return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        visits = Upload.objects.all()
        serializer  = UploadSerializer(visits, many=True)
        return Response(serializer.data)
    except Upload.DoesNotExist:  # corrected 'execpt' to 'except'
        return Response({"error": "Upload not found."}, status=404)


@api_view(['PUT', 'PATCH'])  # Support full or partial updates
# @permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])  # ✅ Handle form-data with files
def update_upload_data(request, upload_id):
    try:
        if request.user.role not in ('JL', 'SL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        visit_instance = Upload.objects.get(id=upload_id)

        request_data = request.data.copy()
        print("🔁 Update request data:", request_data)
        print("📁 Update request files:", request.FILES)

        serializer = UploadSerializer(
            visit_instance,
            data=request_data,
            context={'request': request},
            partial=True  # ✅ Allows partial update with PATCH
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

    except Upload.DoesNotExist:
        return Response({"error": "Upload not found."}, status=404)