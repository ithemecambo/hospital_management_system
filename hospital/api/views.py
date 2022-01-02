from rest_framework.decorators import api_view
from rest_framework.response import Response

from hospital.api.serializers import LanguageSerializer
from hospital.models import Language


@api_view(['GET'])
def language_list(request):
    tasks = Language.objects.all().order_by('-id')
    serializer = LanguageSerializer(tasks, many=True)
    return Response(serializer.data)