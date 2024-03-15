# question
请求体：
```json
{
  "record_patient": 1,
  "doctor": 5,
  "content": "主诉：患者主要表现为胸闷、胸痛，严重时伴有心悸、气促。\n\n现病史：患者自感胸闷胸痛已有半年余，日渐加重，同时伴有心悸气促，夜间尤为明显。症状以行走约100米后加重为著。\n\n既往史：有高血压病史10年，未治疗。\n\n体格检查：血压160/100mmHg，心率80次/分，心音有力度，心尖搏动不隆起，肺部清音，双下肢无水肿。\n\n辅助检查：心电图示ST段下移0.5mV，T波倒置，左室高电压。\n冠脉造影示左主干、前降支、对侧回、右冠脉有不同程度狭窄，诊断为冠脉粥样硬化。",
  "disease": 2
}
```
报错：
django.db.utils.IntegrityError: (1048, "Column 'record_patient_id' cannot be null")

model：
```python
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
```

序列化器：
```python
class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'
        depth = 1
        extra_kwargs = {
            'record_patient': {
                'required': True
            }
            , 'doctor': {
                'required': True
            }
        }
```


为什么报错，什么地方出了问题