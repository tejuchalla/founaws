from django.urls import path
from donations.views import donations
#from donations.views import donationsdetails

urlpatterns = [
    path('dp/', donations),
    #path('rd/', donationsdetails),

]
