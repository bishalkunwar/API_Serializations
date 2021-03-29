from rest_framework import serializers

class studentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    number = serializers.IntegerField()
    email = serializers.EmailField(max_length=100)

    def create(self, validated_data):
        return student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.number = validated_data.get('number', instance.number)
        instance.email = validated_data.get('created', instance.email)
        instance.save()
        return instance

#field level validation:
'''    def email_valids(self,value):
        if len(value) <=7 or value.len >=25:
            raise serializers.ValidationError('email length either short or excedding maximum')

        return value'''

#object level validation:
    def validate(self,data):
        name = data.get('name')
        number = data.get('number')
        email = data.get('email')

        if name.lower() == True or number.Int() == False or len(email) >=25:
            raise serializers.ValidationError('error on variables')

        return value
