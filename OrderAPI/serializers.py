from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Logger, Place

import random
import string
class LoggerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logger
        fields = '__all__'

# #add fiels i want to display using serializers
# class AllSerializer(serializers.Serializer):
#     id=serializers.IntegerField()
#     name=serializers.CharField(max_length=20)
#     email=serializers.EmailField(max_length=50)

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model= Place
        fields = '__all__'


#Operate on displayed fields using model serialiser
class AllSerializer(serializers.ModelSerializer):
    #Rename a displayed field
    time = serializers.DateField(source="order_time")
    #Add extra data in response
    status = serializers.BooleanField(default=True, read_only=False)
    alternate = serializers.SerializerMethodField(method_name = "alt_ID")
    place = PlaceSerializer(read_only = True)
    class Meta:
        model = Logger
        fields = ['id', 'name','email','address','age','status','time',"alternate", "place"]
        depth = 1
        #Create alternate key id
    def alt_ID(self, lid:Logger):
        alpha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        return str(lid.id) + alpha

    