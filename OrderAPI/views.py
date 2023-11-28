from django.shortcuts import render
from .models import Logger
#rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
#serializer
from .serializers import LoggerSerializer
from rest_framework import generics
# Create your views here.
from OrderAPI.forms import LogForm
#serialize
from .serializers import AllSerializer
from django.shortcuts import get_object_or_404



def detail_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "detail.html", context)
 
 #another one
def display(request):
    new_record = Logger.objects.all()
    new_record_dict = {'record': new_record }
    return render(request, 'see.html', new_record_dict)


class Orderlist(APIView):
    def get(self, request):
        food = request.GET.get("food")
        if(food):
            return Response ({"message":f"Your {food} is ready"}, status.HTTP_200_OK)
        return Response({"message":"list of orders"}, status.HTTP_200_OK)
    def post(self, request):
        go = request.data.get('name')
        if go == None:
            return Response({"message":"Please input  name"}, status.HTTP_400_BAD_REQUEST)
        else:                 
            return Response({"message":"order created successfully" + go}, status.HTTP_201_CREATED)
#this one recieves an integer as query object
class List(APIView):
    def get(self, request, pk):
        return Response({"message":"The id of this order is " + str(pk)}, status.HTTP_200_OK)
    def post(self, request, pk):
        go = request.data.get('name')
        if go == None:
            return Response({"message":"Please input product Id"}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"order created successfully " + go}, status.HTTP_200_OK)
        
#Using serializers / generic views        
class Serial(generics.ListCreateAPIView):
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer
#This one displays a single record by recieving an id query
class Single(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Logger.objects.all()
    serializer_class = LoggerSerializer

#DeSerializer lesson 
@api_view(['GET', 'POST'])
@renderer_classes([TemplateHTMLRenderer])
def all(request):
    if request.method == 'GET':
        items = Logger.objects.select_related('place').all()
        place_name = request.query_params.get('place')
        to_age = request.query_params.get('to_age')
        serialized_item = AllSerializer(items, many=True)
        return Response(serialized_item.data, status = status.HTTP_200_OK) 
        #return Response({'data':serialized_item.data}, template_name='/dat.html')
    elif request.method == 'POST':
        serialized_item = AllSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data, status.HTTP_201_CREATED)
    
@api_view()
def one(request, id):
    item = get_object_or_404(Logger, pk=id)
    serialized = AllSerializer(item)
    return Response(serialized.data)

    

            

    