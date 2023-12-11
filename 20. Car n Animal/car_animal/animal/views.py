from rest_framework.views import APIView
from rest_framework.response import Response
from . models import animal
from . serializers import AnimalSerializer

# Create your views here.

class SelectAnimalView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data=animal.objects.get(pk=pk)
                serializer = AnimalSerializer(data, context={"request":request}, many=False)
                return Response(serializer.data)
            except:
                return Response("Could not find that animal with id - "+ str(pk))
        data =  animal.objects.all()
        serializer = AnimalSerializer(data, context={"request":request}, many=True)
        return Response(serializer.data)

class AddAnimalView(APIView):
    def post(self, request):
        serializer = AnimalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteAnimalView(APIView):
    def delete(self, request, pk):
        event = animal.objects.get(pk=pk)
        event.dlete()
        return Response("Deletion Success")