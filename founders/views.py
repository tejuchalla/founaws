from django.shortcuts import render
from django.http import HttpResponse
from founders.models import account
from founders.models import Bankdetails

# Create your views here.
def homepage(req):
    founderdetails={"name":"Somnath","cf1":"Prathyusha","cf2":"Charitha","cf3":"Teja"}
    return render(req,'founders/index.html',founderdetails)

def founders(req):
    #return HttpResponse("\n<h1>Amma SERV Foundation</h1>\n<h3>Founders</h3>")
    founderdetails={"name":"Somnath","age":25}
    return render(req,'founders/home.html',founderdetails)

def accdetails(req):
    res=account.objects.all()
    ad={'det':res}
    return render(req,'founders/index.html',ad)

def bankdet(req):
    result=Bankdetails.objects.all()
    #asfb={'asf':result}
    return render(req,'founders/index.html',{'asf':result})
