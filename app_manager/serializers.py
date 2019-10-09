from rest_framework import serializers


class ApiBaseSerializer(serializers.Serializer):
    message = serializers.CharField(
        max_length=200
    )

