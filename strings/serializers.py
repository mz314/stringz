from rest_framework import serializers
from strings.models import String, StringSet, StringStringSet, ScaleLength

# class BrandSerializer(serializers.ModelSerializer):


class ScaleLengthSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleLength
        fields = '__all__'

class StringSerializer(serializers.ModelSerializer):
    class Meta:
        model = String
        fields = '__all__'


class StringStringSetSerializer(serializers.ModelSerializer):
    string = StringSerializer()
    
    class Meta:
        model = StringStringSet
        fields = '__all__'

        
class StringSetSerializer(serializers.ModelSerializer):
    strings = StringStringSetSerializer(many=True)
    scale_lengths = ScaleLengthSerializer(many=True)
    class Meta:
        model = StringSet
        fields = '__all__'
       
