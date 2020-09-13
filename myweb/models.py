from django.db import models
# Create your models here.
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.
choice=[
    ('Javascript','Javascript'),
    ('Python','Python'),
    ('C++','C++'),
    ('Html','Html'),
    ('Css','Css'),
    ('SQL','SQL'),('Django','Django'),('Flask','Flask'),('Express.js','Express.js'),
    ('Algorithm&DataStructure','Algorithm&DataStructure'),('TimeComplexity','TimeComplexity')]
 
class Upload(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="upload")
    title=models.CharField(max_length=100)
    video=models.URLField()
    language=models.CharField(choices=choice,max_length=100,blank=True,null=True)
    like=models.ManyToManyField(User,related_name="like",blank=True)
    def __str__(self):
        return self.title



class UploadForm(ModelForm):
    class Meta:
        model=Upload
        fields=['title','video','language']
        widgets={
            'title':forms.TextInput(attrs={'placeholder':' Enter Video Title'}),
            'video':forms.TextInput(attrs={'placeholder':'Enter video url from youtube'}),
        }

    def clean_video(self):
        a='https://www.youtube.com/embed/'
        self.cleaned_data['video']=a+self.cleaned_data['video'].split('/')[-1]
        return self.cleaned_data.get('video')

import django_filters

class UploadFilter(django_filters.FilterSet):
    title=django_filters.CharFilter(field_name="title",lookup_expr='icontains',label="Title")
    class Meta:
        model=Upload
        fields=['language','title']