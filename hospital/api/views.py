from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospital.api.serializers import LanguageSerializer
from hospital.models import Language


@api_view(['GET'])
def language_list(request):
    tasks = Language.objects.all().order_by('-id')
    serializer = LanguageSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
def languages(request):
    if request.method == 'GET':
        data = Language.objects.all()
        serializer = LanguageSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LanguageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def language_datail(request, pk):
    try:
        student = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = LanguageSerializer(student, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)