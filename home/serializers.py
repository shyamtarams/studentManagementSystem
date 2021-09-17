from rest_framework import serializers
from .models import apiData

class dataSerializers(serializers.ModelSerializer):
    class Meta:
        model = apiData
        fields = ('id','name','contact','email')
        