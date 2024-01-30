from django.urls import path
from founders.views import founders
#from founders.views import details

urlpatterns = [
    path('home/', founders),
    #path('fd/', details),

]
