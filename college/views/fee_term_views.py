from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers.fee_term_serializers import FeeTermSerializer



# Create FeeTerm
@api_view(['POST'])
def create_fee_term(request):
    serializer = FeeTermSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)