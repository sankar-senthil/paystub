from django.shortcuts import render
# Create your views here.
from .models import StubData
from datetime import datetime
from stubmaker_application.utils import additional as AD
import os

class Stub():
    file_name = ''
    def __init__(self) -> None:
        self.stub_ins = StubData()
        # self.week_calc = {'Weekly':7,'Bi-Weekly':,''}

    def home(self,request):
        state_list = open(r'G:\Daemon Web Scrab\paystub\NEW-Stub\stub_maker\static\files\state.txt','r').readlines()
        if request.POST.get('EMSE'):
            pass
        else:
            if request.POST.get('EN'):
                content = self.calculations(request)
                for i in content:
                    try:
                        print(f"self.stub_ins.{i} = {content[i]}")
                        if i == 'CL':
                            self.stub_ins.CL = request.FILES.get('CL')
                        else:
                            exec(f"self.stub_ins.{i} = {content[i]}")
                    except:pass
                self.stub_ins.save()
                return render(request, "printpage.html",{'content':content})
            else:
                return render(request, "home.html",{'state_list':state_list})


    def preview(self,request):
        return render(request, "printpage.html")


    def calculations(self,request):
        content = {}
        for field in StubData._meta.fields:
            try:
                content[field.name] = request.POST.get(f'{field.name}').strip()
            except:
                pass

        start_date = datetime.strptime(request.POST.get('RP1'),'%Y-%m-%d').date()
        end_date = datetime.strptime(request.POST.get('RP2'),'%Y-%m-%d').date()
        content['RP'] = f"{start_date} - {end_date}"
        HRUP_OP = 1

        content['CL'] = request.FILES.get('CL')
        Name = content['CN'][:6]+'-img'
        print('Name',Name)

        content['CLDY'] = '/media/photos/'+Name+'.'+str(content['CL']).split('.')[-1]
        for i in os.listdir("media/photos/"):
            print(i)
            if Name in os.path.splitext(i)[0]:
                try:
                    os.remove(f"media/photos/{i}")
                except:pass

        AD.file_name = Name
        if content['HRUP'] == 'Monthly':
            HRUP_OP = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)

        elif content['HRUP'] == 'Bi-Weekly':
            pass

        elif content['HRUP'] == 'Weekly':
            days = abs(end_date-start_date).days
            HRUP_OP = days//7
        else:
            pass

        HRUP_OP = HRUP_OP if HRUP_OP>=1 else 1
        if content['LYD']:
            content['FMY'], content['FSSY'], content['FtY'], content['StY'] = content['LFM'], content['LFSS'], content['LFT'], content['LST']
        else:pass

        content['CPY'] = round(float(content['HR'])*float(content['TH'])*HRUP_OP,2)
        content['DED'] = float(content['FMT'])+float(content['FSST'])+float(content['FtT'])+float(content['StT'])

        content['YTDD'] = float(content['FMY'])+float(content['FSSY'])+float(content['FtY'])+float(content['StY'])
        content['YTDG'] = content['LYD'] if content['LYD'] else content['CPY']*45
        content['YTDN'] = round(float(content['YTDG']) - float(content['YTDD']),2)

        content['TTL'] = content['CPY']
        content['NP'] = round(float(content['TTL']) - float(content['DED']),2)

        print(content)

        content['EN'] = content['EN']+' '+content['EA']
        return content
