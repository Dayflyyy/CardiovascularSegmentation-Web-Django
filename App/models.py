from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin


# Create your models here.

class DoctorManager(BaseUserManager):

    # 创建普通用户，传入要求参数
    def _create_user(self, name, sex, age, department, phone, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(name=name, sex=sex, age=age, department=department, phone=phone, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, name, sex, age, department, phone, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(name, sex, age, department, phone, email, password, **extra_fields)


# 医生数据表
class Doctor(AbstractUser, PermissionsMixin):
    # 个人主页
    name = models.CharField(verbose_name="姓名", max_length=20)
    sex = models.CharField(verbose_name="性别", max_length=10)
    age = models.IntegerField(verbose_name="年龄", default=0)
    department = models.CharField(verbose_name="科室", max_length=20)
    phone = models.CharField(verbose_name="电话", max_length=20)
    email = models.CharField(verbose_name="邮箱", max_length=50)
    introduction = models.TextField(verbose_name="简介", max_length=500, null=True, blank=True)
    # 使用url存储照片地址
    photo = models.ImageField(verbose_name="头像", upload_to="doctor_photo", null=True, blank=True)

    REQUIRED_FIELDS = ['name', 'sex', 'age', 'department', 'phone', 'email']

    def __str__(self):
        return self.username


# 病人数据表
class Patient(models.Model):
    name = models.CharField(verbose_name="姓名", max_length=20)
    sex = models.CharField(verbose_name="性别", max_length=10)
    age = models.IntegerField(verbose_name="年龄", default=0)
    phone = models.CharField(verbose_name="电话", max_length=20)
    # 病人对应一个医生，以外键形式存储
    doctor = models.ForeignKey(to='Doctor', to_field='id', verbose_name="医生", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="描述", max_length=500, null=True, blank=True)
    # 病人对应相应的ct图像和病历，外键，删除方法设置为删除时可以置空
    patient_ct_image = models.ForeignKey(to='NIfTIImage', to_field='id', verbose_name="CT图像",
                                         on_delete=models.SET_NULL,
                                         null=True,
                                         blank=True)
    # 病人对应相应的病历，外键
    record = models.ForeignKey(to='MedicalRecord', to_field='id', verbose_name="病历",
                                       on_delete=models.SET_NULL, null=True,
                                       blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "病人"
        verbose_name_plural = "病人"


# 病历数据表
class MedicalRecord(models.Model):
    record_patient = models.ForeignKey(to='Patient', to_field='id', verbose_name="病人", on_delete=models.CASCADE)
    doctor = models.ForeignKey(to='Doctor', to_field='id', verbose_name="医生", on_delete=models.CASCADE)
    content = models.TextField(verbose_name="内容", max_length=1000, null=True, blank=True)
    # 从多种病种中选择
    disease_choice = {
        1: "冠状动脉粥样硬化症",
        2: "心绞痛",
        3: "心肌梗死",
        4: "冠状动脉痉挛",
        5: "冠状动脉炎",
        6: "冠状动脉畸形",
    }
    disease = models.IntegerField(verbose_name="疾病类型", choices=disease_choice.items(), default=1)

    record_ct_image = models.ForeignKey(to='NIfTIImage', to_field='id', verbose_name="CT图像",
                                         on_delete=models.SET_NULL,
                                         null=True, blank=True)
    time_created = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    time_lastmodified = models.DateTimeField(verbose_name="最后修改时间", auto_now=True)

    def __str__(self):
        return self.content

    class Meta:
        verbose_name = "病历"
        verbose_name_plural = "病历"


# CT影像数据表
class NIfTIImage(models.Model):
    name = models.CharField(verbose_name='名称', max_length=255)
    file = models.FileField(verbose_name='文件', upload_to='nifti_images/')
    dimensions = models.CharField(verbose_name='维度', max_length=100)
    voxel_size = models.CharField(verbose_name='体素大小', max_length=100)
    data_type = models.CharField(verbose_name='数据类型', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'NIfTI图像'
        verbose_name_plural = 'NIfTI图像'
