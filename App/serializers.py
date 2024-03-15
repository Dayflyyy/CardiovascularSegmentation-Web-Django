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
    doctor_id = serializers.PrimaryKeyRelatedField(queryset=Doctor.objects.all(), write_only=True)
    record_patient_id = serializers.PrimaryKeyRelatedField(queryset=Patient.objects.all(),
                                                           write_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'content', 'disease', 'doctor_id', 'record_patient_id']  # 根据需要包含的字段调整
        depth = 1  # 根据需要调整深度

    def create(self, validated_data):
        doctor_id = validated_data.pop('doctor_id').id  # 获取 Doctor 对象的 id
        record_patient_id = validated_data.pop('record_patient_id').id  # 获取 Patient 对象的 id
        medical_record = MedicalRecord.objects.create(doctor_id=doctor_id, record_patient_id=record_patient_id,
                                                      **validated_data)
        return medical_record
