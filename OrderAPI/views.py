from django.shortcuts import render
from .models import Logger
#rest framework
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, renderer_classes,permission_classes, throttle_classes
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
from django.core.paginator import Paginator, EmptyPage
#Authentifications
from rest_framework.permissions import IsAuthenticated
#Throttling
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle


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
#@renderer_classes([TemplateHTMLRenderer])
def all(request):
    if request.method == 'GET':
        items = Logger.objects.select_related('place').all()

        #search for items using query
        place_name = request.query_params.get('place')
        to_age = request.query_params.get('age')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage', default = 2)
        page = request.query_params.get('page', default = 1)
        if place_name:
            items = items.filter(place__slug = place_name)
        if to_age:
            items = items.filter(age = to_age)
        if search:
            items = items.filter(name__istartswith = search)
        if ordering:
            ordering_fields = ordering.split(",")
            items = items.order_by(*ordering_fields)

        paginator  = Paginator(items, per_page=perpage)
        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items=[]
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

#Authentication
@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"This message is a secret"})


@api_view()
@permission_classes([IsAuthenticated])
def manager(request):
    #check if an authenticated user belongs to a group (MANAGER)
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"This message is for the manager only"})
    else:
        return Response({"message":"You are not authorised to view this"}, status.HTTP_403_FORBIDDEN)

#Throttling

@api_view()
@throttle_classes([AnonRateThrottle])
def throttle(request):
    return Response({"message":"Throttle Success"})
 #for logged in users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([UserRateThrottle])
def throttle_user(request):
    return Response({"message":"Throttle Success for users only"})


    