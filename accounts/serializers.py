from rest_framework import serializers
from .models import UserAccount


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserAccount(**validated_data)
        user.set_password(password)
        user.save()
        return user
