from django.shortcuts import render
from django.http import HttpResponse


def donations(req):
    #return HttpResponse("<h1>Donations</h1>")
    return render(req,'donations/don.html')
'''def donationsdetails(req):
    return HttpResponse("Recent Donations")'''
