from django import forms
from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


# 创建医生的序列化
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
                'style': {'input_type': 'password'}
            }
        }


# 病人序列化

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'
        depth = 1


# 病历序列化
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'record_patient': {
                'required': True,
                'error_messages': {
                    'required': '请提供病人信息'
                }
            },
            'doctor': {
                'required': True,
                'error_messages': {
                    'required': '请提供医生信息'
                }
            }
        }
