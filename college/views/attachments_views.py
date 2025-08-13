from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from ..models.attachments import Attachment
from ..serializers.attachments_serializers import AttachmentSerializer


@api_view(['GET'])
def get_attachments_data(request):
    try:
        if request.user.role not in ('JL', 'SL'):
            return Response({"error": "Not Allowed to create attendence."}, status=status.HTTP_400_BAD_REQUEST)
        visits = Attachment.objects.all()
        serializer  = AttachmentSerializer(visits, many=True)
        return Response(serializer.data)
    except Attachment.DoesNotExist:  # corrected 'execpt' to 'except'
        return Response({"error": "Attachment not found."}, status=404)