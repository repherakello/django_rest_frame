from rest_framework import serializers
#from user.models import user- wrong approach
from django.contrib.auth import get_user_model
user =get_user_model

#A basic serializer can be defined as follows
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =user
        fields = "__all__"


# import json
# #REST
# #SERIALIZATION
# class ALX:
#     def __init__(self, name) ->None:
#         self.cohort_name =name
# cohort_1 = ALX("new fe fe fe ALX")
# cohort_2 =ALX("be")

# cohort_1_dict = {"cohort_name": cohort_1.cohort_name}
# with open("sample3.json","w") as file:
#     json.dump(cohort_1_dict,file)


             #VALIDATION 

from .models import MyModel

class MyModelSerializaer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['id', 'name', 'description','created_at']
    
    def validate(self, data):
        if len(data['name'])<5:
            raise serializers.ValidationError("Nmae Must be at least 5 characters long.")
        return data