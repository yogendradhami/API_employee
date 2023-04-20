from rest_framework import serializers
from API.models import Company

# create serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields= "__all__"