from rest_framework.decorators import api_view
from rest_framework.response import Response
from users.models import CustomUser
from ..serializers.users_serializers import CustomUserSerializer
from rest_framework.decorators import APIView, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
def get_all_custom_users(request):
    if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
            return Response({"error": "Not Allowed to create attendence."}, status=400)
    roles = ['SL', 'JL']
    users = CustomUser.objects.filter(role__in=roles)
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)


class LoggedinprofileView(APIView):
        permission_classes = [IsAuthenticated]

        def get(self, request):
                try:
                        print("user = ", request.user)
                        if request.user.role not in ('AD', 'PR', 'SL', 'JL'):
                            return Response({"error": "Not Allowed to create attendence."}, status=400)
                        user = CustomUser.objects.get(username=request.user)
                        serializer = CustomUserSerializer(user)
                        return Response(serializer.data)
                except CustomUser.DoesNotExist:
                        return Response({'detail' : 'Not a user'}, status=400)