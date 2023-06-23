from django.shortcuts import render
from app.models import *

from django.db.models.functions import Length

# Create your views here.

def display_topics(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    LWO=Webpage.objects.all()          ## it will give all the data inside the table
    LWO=Webpage.objects.filter(id=7)    ## it will give data based on condition (cond_ex;- topic_name='Cricket')
    LWO=Webpage.objects.exclude(id=5)   ## it will give data except given conditon
    LWO=Webpage.objects.all().order_by('name')   ## it will arrange name column data in order based on asci values
    LWO=Webpage.objects.all().order_by('-name')   ## it will arrange name column_data in reverse_order based on asci values
    LWO=Webpage.objects.all().order_by(Length('name'))    ## it will arrange name column_data in order based on length 
    LWO=Webpage.objects.all().order_by(Length('name').desc())  ## it will arrange name column_data in reverse_order based on length 
    d={'LWO':LWO}
    return render(request,'display_webpages.html',d)

def display_accessrecord(request):
    ACO=AccessRecord.objects.all()
    d={'ACO':ACO}
    return render(request,'display_accessrecord.html',d)

def display_alltables(request):
    LTO=Topic.objects.all()
    LWO=Webpage.objects.all()
    LAO=AccessRecord.objects.all()
    d={'LTO':LTO,'LWO':LWO,'LAO':LAO}
    return render(request,'display_alltables.html',d)