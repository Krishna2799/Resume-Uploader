from dataclasses import fields
from rest_framework import serializers
from API.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'email', 'dob',
                  'state', 'gender', 'location', 'pimage', 'rdoc']
