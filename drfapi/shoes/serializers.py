from email.policy import default
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Sneakers



# class SneakersSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length = 255)
#     description = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     have = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()

#     def create(self, validated_data):
#         return Sneakers.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get("name", instance.name)
#         instance.description = validated_data.get("description", instance.description)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.have = validated_data.get("have", instance.have)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

class SneakersSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Sneakers
        fields = "__all__"