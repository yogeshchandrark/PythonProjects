from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Length, Substr
import numpy as np

# Create your models here.
class Question(models.Model):
    title = models.TextField(null=True, blank=True)
    status = models.CharField(default='inactive', max_length=20)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete='CASCADE')

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Choice(models.Model):
    question = models.ForeignKey('poll.Question', on_delete='CASCADE')
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

class TestModel(models.Model):

    def create_assetcode():
        string = 'DCC/0000000000'
        Asset = TestModel.pk
        te = Length(Asset)
        if int(te)<=0:
            return string
        else:
            getstring = Substr(string,0, 14-te)
            GenId = getstring+str(Asset)
            return GenId


    AssetId = models.CharField(max_length=14, editable= False, unique= True, null=False, default= create_assetcode)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.AssetId
