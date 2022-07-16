from dataclasses import fields
from rest_framework import routers, serializers, viewsets
from . import models as m


class Employeeseralizer(serializers.ModelSerializer):
    class Meta:
        model = m.Employee
        fields = '__all__'
