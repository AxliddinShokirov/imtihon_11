from main.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status

@api_view(['GET'])
def Xodimlar_list(request):
    xodimlar = Xodimlar_name.objects.all()
    serializer =Xodimlar_nameSerializer(xodimlar, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def Xodimlar_detail(request, id):
    try:
        xodim = Xodimlar_name.objects.get(id=id )
    except Xodimlar_name.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    serializer = Xodimlar_nameSerializer(xodim)
    return Response(serializer.data)

@api_view(['POST'])
def Xodimlar_create(request):
    serializer = Xodimlar_nameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)