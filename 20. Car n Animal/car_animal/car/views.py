from rest_framework.views import APIView
from rest_framework.response import Response
from . models import car
from . serializers import CarSerializer

# Create your views here.

class SelectCarView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                data=car.objects.get(pk=pk)
                serializer = CarSerializer(data, context={"request":request}, many=False)
                return Response(serializer.data)
            except:
                return Response("Could not find that car with id - "+ str(pk))
        data = car.objects.all()
        serializer = CarSerializer(data, context={"request":request}, many=True)
        return Response(serializer.data)

class AddCarView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class DeleteCarView(APIView):
    def delete(self, request, pk):
        event = car.objects.get(pk=pk)
        event.delete()
        return Response("Deletation Success")