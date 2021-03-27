from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    email = models.EmailField(max_length=100)