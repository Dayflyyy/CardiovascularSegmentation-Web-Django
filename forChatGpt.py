from django.contrib.auth import get_user_model

Doctor = get_user_model()

# 创建第一个医生
doctor1 = Doctor(
    username='zhangsan',
    password='123456',
    name='张三',
    sex='男',
    age=35,
    department='内科',
    phone='1234567890',
    email='zhangsan@example.com',
    introduction='张三是一位资深内科医生，擅长治疗各种慢性疾病。',
    photo='doctor_photo/zhangsan.jpg'
)

doctor1 = Doctor.objects.create_user(
    username='zhangsan',
    password='123456',
    name='张三',
    sex='男',
    age=35,
    department='内科',
    phone='1234567890',
    email='zhangsan@example.com',
    introduction='张三是一位资深内科医生，擅长治疗各种慢性疾病。',
    photo='doctor_photo/zhangsan.jpg'
)

# 创建第二个医生
doctor2 = Doctor(
    username='lisi',
    name='李四',
    sex='女',
    age=40,
    department='外科',
    phone='9876543210',
    email='lisi@example.com',
    introduction='李四是一位优秀的外科医生，有丰富的手术经验。',
    photo='doctor_photo/lisi.jpg'
)
doctor2.set_password('lisi234')  # 设置密码
doctor2.save()  # 保存医生对象

# 输出医生信息
print(doctor1)
print(doctor2)


{
    "username": "lisi",
    "password": "345678",
    "name": "李四",
    "sex": "女",
    "age": 30,
    "department": "外科",
    "phone": "1234567890",
    "email": "lisi@example.com",
    "introduction": "这里是李四的简介"
}
doctor1 = Doctor.objects.get(id=5)  # 假设ID为1的医生
doctor2 = Doctor.objects.get(id=6)  # 假设ID为2的医生
patient1 = Patient.objects.get(id=1)  # 假设ID为1的病人
patient2 = Patient.objects.get(id=2)  # 假设ID为2的病人
patient3 = Patient.objects.get(id=3)  # 假设ID为3的病人

medical_record1 = MedicalRecord.objects.create(
    patient_id=patient1,
    doctor=doctor1,
    content='病人1的病历内容...',
    disease=2,  # 假设是心绞痛
)

medical_record2 = MedicalRecord.objects.create(
    patient_id=patient2,
    doctor=doctor2,
    content='病人2的病历内容...',
    disease=3,  # 假设是心肌梗死
)

medical_record3 = MedicalRecord.objects.create(
    patient_id=patient3,
    doctor=doctor1,
    content='病人3的病历内容...',
    disease=1,  # 假设是冠状动脉粥样硬化症
)