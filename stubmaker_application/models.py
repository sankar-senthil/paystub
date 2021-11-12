from django.db import models
import os
from stubmaker_application.utils import additional as AD

# Create your models here.


def path_and_rename(instance, filename):
    upload_to = 'photos'
    ext = filename.split('.')[-1]

        # set filename as random string
    filename = '{}.{}'.format(AD.file_name, ext)
    print('filename',filename)
    print('os.path.join(upload_to, filename)',os.path.join(upload_to, filename))
    # return the whole path to the file
    return os.path.join(upload_to, filename)



class StubData(models.Model):
    id = models.AutoField(primary_key=True)
    EMSE = models.CharField(max_length = 264,null=True)
    ST = models.CharField(max_length = 264,null=True)
    MS = models.CharField(max_length = 264,null=True)
    HRUP = models.CharField(max_length = 264,null=True)
    HR = models.CharField(max_length = 264,null=True)
    TH = models.CharField(max_length = 264,null=True)
    CPY = models.CharField(max_length = 264,null=True)
    ET = models.CharField(max_length = 264,null=True)
    LYD = models.CharField(max_length = 264,null=True)
    LFM = models.CharField(max_length = 264,null=True)
    LFSS = models.CharField(max_length = 264,null=True)
    LFT = models.CharField(max_length = 264,null=True)
    LST = models.CharField(max_length = 264,null=True)
    EN = models.CharField(max_length = 264,null=True)
    EA = models.CharField(max_length = 264,null=True)
    CN = models.CharField(max_length = 264,null=True)
    CA = models.CharField(max_length = 264,null=True)
    SSN = models.CharField(max_length = 264,null=True)
    RP = models.CharField(max_length = 264,null=True)
    PD = models.CharField(max_length = 264,null=True)
    CK = models.CharField(max_length = 264,null=True)
    FMT = models.CharField(max_length = 264,null=True)
    FMY = models.CharField(max_length = 264,null=True)
    FSST = models.CharField(max_length = 264,null=True)
    FSSY = models.CharField(max_length = 264,null=True)
    FtT = models.CharField(max_length = 264,null=True)
    FtY = models.CharField(max_length = 264,null=True)
    StT = models.CharField(max_length = 264,null=True)
    StY = models.CharField(max_length = 264,null=True)
    YTDG = models.CharField(max_length = 264,null=True)
    YTDD = models.CharField(max_length = 264,null=True)
    YTDN = models.CharField(max_length = 264,null=True)
    TTL = models.CharField(max_length = 264,null=True)
    DED = models.CharField(max_length = 264,null=True)
    NP = models.CharField(max_length = 264,null=True)
    CL = models.ImageField(upload_to=path_and_rename,null=True)
