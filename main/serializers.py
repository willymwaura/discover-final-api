from django.db import models
from django.db.models import fields
from rest_framework import serializers
from.models import Feature

class FeatureSerializer(serializers.ModelSerializer):

    class Meta:
        model=Feature
        fields=['id','title','region','experience','nearby_town','image_url']

        
class SpecificSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feature
        fields=['id','title','region','experience','created','nearby_town','image_url','weather_text','degree_celcius','weather_url']