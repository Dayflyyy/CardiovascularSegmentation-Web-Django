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





def image_file_path(instance, filename):
    return os.path.join('instances', '{0}.dcm'.format(str(uuid.uuid4()).replace('-', '')))


def plugin_file_path(plugin, filename):
    return os.path.join('plugins', '{0}.zip'.format(str(uuid.uuid4()).replace('-', '')))


def processed_image_path(plugin, filename):
    return os.path.join('plugins', '{0}.zip'.format(str(uuid.uuid4()).replace('-', '')))


TAGS_TO_FIELDS = {
    # Patient
    'PatientName': 'patient_name',
    'PatientID': 'patient_id',
    'PatientAge': 'patient_age',
    'PatientBirthdate': 'patient_birthdate',
    'PatientSex': 'patient_sex',

    # Study
    'StudyInstanceUID': 'study_instance_uid',
    'StudyID': 'study_id',
    'StudyDate': 'study_date',
    'StudyDescription': 'study_description',
    'StudyTime': 'study_time',
    'AccessionNumber': 'accession_number',
    'ReferringPhysicianName': 'referring_physician_name',

    # Series
    'SeriesInstanceUID': 'series_instance_uid',
    'SeriesDate': 'series_date',
    'SeriesTime': 'series_time',
    'SeriesDescription': 'series_description',
    'Modality': 'modality',
    'SeriesNumber': 'series_number',
    'PatientPosition': 'patient_position',
    'BodyPartExamined': 'body_part_examined',

    # Instance
    'SOPInstanceUID': 'sop_instance_uid',
    'InstanceNumber': 'instance_number',
    'Rows': 'rows',
    'Columns': 'columns',
    'ColorSpace': 'color_space',
    'PhotometricInterpretation': 'photometric_interpretation',
    'BitsAllocated': 'bits_allocated',
    'BitsStored': 'bits_stored',
    'SmallestImagePixelValue': 'smallest_image_pixel_value',
    'LargestImagePixelValue': 'largest_image_pixel_value',
    'PixelAspectRation': 'pixel_aspect_ratio',
    'PixelSpacing': 'pixel_spacing'
}

FIELDS_TO_TAG = {
    # Patient
    'patient_name': 'PatientName',
    'patient_id': 'PatientID',
    'patient_age': 'PatientAge',
    'patient_birthdate': 'PatientBirthdate',
    'patient_sex': 'PatientSex',

    # Study
    'study_instance_uid': 'StudyInstanceUID',
    'study_id': 'StudyID',
    'study_date': 'StudyDate',
    'study_description': 'StudyDescription',
    'study_time': 'StudyTime',
    'accession_number': 'AccessionNumber',
    'referring_physician_name': 'ReferringPhysicianName',

    # Series
    'series_instance_uid': 'SeriesInstanceUID',
    'series_date': 'SeriesDate',
    'series_time': 'SeriesTime',
    'series_description': 'SeriesDescription',
    'modality': 'Modality',
    'series_number': 'SeriesNumber',
    'patient_position': 'PatientPosition',
    'body_part_examined': 'BodyPartExamined',
    'protocol_name': 'ProtocolName',

    # Instance
    'sop_instance_uid': 'SOPInstanceUID',
    'instance_number': 'InstanceNumber',
    'rows': 'Rows',
    'columns': 'Columns',
    'color_space': 'ColorSpace',
    'photometric_interpretation': 'PhotometricInterpretation',
    'bits_allocated': 'BitsAllocated',
    'bits_stored': 'BitsStored',
    'smallest_image_pixel_value': 'SmallestImagePixelValue',
    'largest_image_pixel_value': 'LargestImagePixelValue',
    'pixel_aspect_ratio': 'PixelAspectRation',
    'pixel_spacing': 'PixelSpacing'
}

DICOM_DATE_REGEX = re.compile("([0-9]{4})([0-9]{2})([0-9]{2})$")


class DicomModel(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def from_dataset(cls, model_instance=None, ds: Dataset = None):
        if model_instance is None:
            model_instance = cls()
        fields = cls._meta.get_fields()
        for field in fields:
            if isinstance(field, ManyToOneRel):
                continue
            if isinstance(field, ForeignKey) or isinstance(field, OneToOneField):
                continue
            elif isinstance(field, models.AutoField):
                continue
            elif isinstance(field, models.FileField) or isinstance(field, models.ImageField):
                continue
            elif isinstance(field, models.DateField):
                date_field_value = ds.get(FIELDS_TO_TAG[field.name], None)
                if date_field_value is None:
                    continue
                match = DICOM_DATE_REGEX.match(date_field_value)
                if match:
                    year, month, day = match.group(1), match.group(2), match.group(3)
                    setattr(model_instance, field.name, datetime.date(int(year), int(month), int(day)))
            elif isinstance(field, models.TimeField):
                pass  # To implement lately
            else:
                setattr(model_instance, field.name, ds.get(FIELDS_TO_TAG[field.name], None))
        return model_instance


class Patient(DicomModel):
    class Meta:
        db_table = 'patients'

    patient_name = models.CharField(verbose_name=_('Patient'), max_length=100, blank=True, null=True)
    patient_id = models.CharField(verbose_name=_('Patient ID'), max_length=100, blank=True, null=True)
    patient_sex = models.CharField(verbose_name=_('Patient Sex'), max_length=10, blank=True, null=True)
    patient_age = models.CharField(verbose_name=_('Patient Age'), max_length=30, blank=True, null=True)
    patient_birthdate = models.DateField(verbose_name=_('Patient Birthdate'), blank=True, null=True)


class Study(DicomModel):
    class Meta:
        db_table = 'studies'
        verbose_name_plural = 'Studies'

    study_instance_uid = models.CharField(verbose_name=_('Study Instance UID'), max_length=80, unique=True)
    study_id = models.CharField(verbose_name=_('Study ID'), max_length=100, blank=True, null=True)
    study_date = models.DateField(verbose_name=_('Study Date'), blank=True, null=True)
    study_description = models.CharField(verbose_name=_('Study Description'), max_length=300, blank=True, null=True)
    referring_physician_name = models.CharField(verbose_name=_('Referring Physician'), max_length=100, blank=True,
                                                null=True)
    patient = models.ForeignKey('core.Patient', related_name='studies', on_delete=models.CASCADE)


class Series(DicomModel):
    class Meta:
        db_table = 'series'
        verbose_name = 'Series'
        verbose_name_plural = 'Series'

    series_instance_uid = models.CharField(verbose_name=_('Series Instance UID'), max_length=80, unique=True)
    protocol_name = models.CharField(verbose_name=_('Protocol Name'), max_length=150, blank=True, null=True)
    modality = models.CharField(verbose_name=_('Modality'), max_length=80)
    series_number = models.CharField(verbose_name=_('Series Number'), max_length=80, blank=True, null=True)
    patient_position = models.CharField(verbose_name=_('Patient Position'), max_length=30)
    body_part_examined = models.CharField(verbose_name=_('Body Part Examined'), max_length=50, blank=True, null=True)
    study = models.ForeignKey('core.Study', related_name='series', on_delete=models.CASCADE)


class Instance(DicomModel):
    class Meta:
        db_table = 'instances'

    sop_instance_uid = models.CharField(verbose_name=_('SOP Instance UID'), max_length=80, unique=True)
    instance_number = models.IntegerField(verbose_name=_('Instance Number'))
    rows = models.IntegerField(verbose_name=_('Rows'))
    columns = models.IntegerField(verbose_name=_('Columns'))
    color_space = models.CharField(verbose_name=_('Color Space'), max_length=30, blank=True, null=True)
    photometric_interpretation = models.CharField(verbose_name=_('Photometric Interpretation'), max_length=30,
                                                  blank=True, null=True)
    smallest_image_pixel_value = models.PositiveIntegerField(verbose_name=_('Smallest Image Pixel Value'), blank=True,
                                                             null=True)
    largest_image_pixel_value = models.PositiveIntegerField(verbose_name=_('Largest Image Pixel Value'), blank=True,
                                                            null=True)
    pixel_aspect_ratio = models.CharField(verbose_name=_('Pixel Aspect Ratio'), max_length=30, blank=True, null=True)
    pixel_spacing = models.CharField(verbose_name=_('Pixel Spacing'), max_length=30, blank=True, null=True)
    image = models.FileField(upload_to=image_file_path)
    series = models.ForeignKey('core.Series', related_name='instances', on_delete=models.CASCADE)


class Plugin(models.Model):
    class Meta:
        db_table = 'plugins'

    name = models.CharField(verbose_name=_('Name'), max_length=100, unique=True, null=False)
    display_name = models.CharField(verbose_name=_('Display Name'), default='', max_length=150)
    version = models.CharField(verbose_name=_('Version'), max_length=20)
    author = models.CharField(verbose_name=_('Author'), max_length=100, blank=True, null=True)
    info = models.CharField(verbose_name=_('Information'), max_length=500, blank=True, null=True)
    docs = models.TextField(verbose_name=_('Documentation'), max_length=500, blank=True, null=True)
    modalities = JSONField(verbose_name=_('Modalities'), blank=True, null=True)
    tags = JSONField(verbose_name=_('Tags'), blank=True, null=True)
    params = JSONField(verbose_name=_('Parameters'), blank=True, null=True)
    result = JSONField(verbose_name=_('Result'))
    type = models.CharField(verbose_name=_('Type'), default='ANALYZER', max_length=40)
    plugin = models.FileField(upload_to=plugin_file_path, null=True, blank=True)
    is_installed = models.BooleanField(verbose_name=_('Is installed'), default=False)


class DicomNode(models.Model):
    class Meta:
        db_table = 'dicom_nodes'

    name = models.CharField(verbose_name=_('Name'), max_length=255, blank=True, null=True)
    remote_url = models.CharField(verbose_name=_('Peer URL'), max_length=255)
    instances_url = models.CharField(verbose_name=_('WADO Instances URL'), default='/instances', max_length=255)
    instance_file_url = models.CharField(verbose_name=_('WADO Instance Image URL'), default='/instances/{id}/file',
                                         max_length=255)


class ProcessingResult(models.Model):
    class Meta:
        db_table = 'processing_results'

    expire_date = models.DateTimeField()
    image = models.FileField(upload_to=processed_image_path, verbose_name=_('Image'), null=True, blank=True)
    json = JSONField(verbose_name=_('JSON'))
    session_token = models.CharField(max_length=255)