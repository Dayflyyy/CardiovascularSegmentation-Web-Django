from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your views here.

from django.conf import settings
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import *
from .models import *
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)  # Django的信号机制
def generate_token(sender, instance=None, created=False, **kwargs):
    """
    创建用户时自动生成Token
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created and isinstance(instance, Doctor):
        token = Token.objects.create(user=instance)


class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        医生登录
        """
        name = request.data.get('name')
        password = request.data.get('password')
        if not name or not password:
            return Response({'error': '请输入用户名和密码'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': '用户名或密码不正确'}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        """
        医生退出登录
        """
        logout(request)
        return Response({'success': '成功退出登录'})

    @action(detail=False, methods=['post'])
    def register(self, request):
        """
        医生注册
        """
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'])
    def profile(self, request, pk=None):
        """
        获取医生个人信息
        """
        doctor = self.get_object()
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)

    def get_object(self):
        """
        获取当前登录的医生对象
        """
        return self.request.user


# 病人viewset
from rest_framework import permissions


class IsDoctorPatient(permissions.BasePermission):
    """
    Custom permission to only allow doctors to access their own patients.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a doctor and the object (patient) belongs to this doctor
        return obj.doctor == request.user


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated, IsDoctorPatient]

    def perform_create(self, serializer):
        # Automatically set the doctor to the current authenticated user
        serializer.save(doctor=self.request.user)

    def get_queryset(self):
        # Only return patients belonging to the current authenticated doctor
        return Patient.objects.filter(doctor=self.request.user)


# 病历viewset

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        """
        Override the list method to only return records related to the doctor.
        """
        doctor = request.user
        queryset = MedicalRecord.objects.filter(doctor=doctor)
        serializer = MedicalRecordSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        """
        Override the create method to set the doctor to the authenticated user.
        If the patient's medical record foreign key is empty,
        set it to the newly created medical record id.
        """
        print("request:")
        print(request.data)
        request.data['doctor'] = request.user.id
        serializer = self.get_serializer(data=request.data)

        for i in range(1, 11):
            print('#')
        print("before is_vaild")
        for i in range(1, 11):
            print('#')

        serializer.is_valid(raise_exception=True)

        for i in range(1, 11):
            print('#')
        print("after is_vaild")
        for i in range(1, 11):
            print('#')
        # print("serializer:")
        # print(serializer.data)
        self.perform_create(serializer)

        for i in range(1, 11):
            print('#')
        print("after create")
        for i in range(1, 11):
            print('#')

        headers = self.get_success_headers(serializer.data)

        # Check if patient_id is provided in the request data
        patient_id = request.data.get('patient_id')
        if patient_id:
            patient = Patient.objects.get(id=patient_id)
            if not patient.medical_record_id:
                patient.medical_record_id = serializer.data['id']
                patient.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        """
        Override the update method to ensure the doctor cannot be changed.
        """
        instance = self.get_object()
        request.data['doctor'] = instance.doctor.id
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        """
        Override the destroy method to ensure the doctor cannot delete other doctors' records.
        """
        instance = self.get_object()
        if request.user == instance.doctor:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
