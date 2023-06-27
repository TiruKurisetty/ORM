from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q


# Create your views here.
def insert_topic(request):
    tn=input(' Enter Topic name')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    return HttpResponse(' Data inserted succfully')
def insert_Webpage(request):
    tn= input(' Enter TopicName : ')
    TO=Topic.objects.get_or_create(Topic_name=tn)[0]
    TO.save()
    name=input('Enter name :')
    url=input('Enter url name :')
    WO=Webpage.objects.get_or_create(Topic_name=TO,Name=name,Url=url)[0]
    WO.save()
    return HttpResponse(' Data inserted succfully')

def display_topic(request):
    topic=Topic.objects.all()
    d={'topic':topic}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    # web=Webpage.objects.all()
    # web=Webpage.objects.filter(Topic_name='Cricket')
    # web=Webpage.objects.exclude(Topic_name='Cricket')
    # web=Webpage.objects.all()[:3]
    # web=Webpage.objects.all()[::-1]
    # web=Webpage.objects.all().order_by('Name')
    # web=Webpage.objects.all().order_by('-Name')
    # web=Webpage.objects.all().order_by(Length('Name'))
    web=Webpage.objects.all()
    d={'web':web}
    return render(request,'display_webpage.html',d)
def display_accessmode(request):
    TAO=AccessMode.objects.all()
    TAO=AccessMode.objects.filter(id=1)
    TAO=AccessMode.objects.filter(Date='2000-06-26')
    TAO=AccessMode.objects.filter(Date__gt='2000-06-26')
    TAO=AccessMode.objects.filter(Date__gte='2000-06-26')
    TAO=AccessMode.objects.filter(Date__lt='2002-06-26')
    TAO=AccessMode.objects.filter(Date__lte='2000-06-26')
    # TAO=AccessMode.objects.filter(Date__ne='2000-06-26')
    TAO=AccessMode.objects.filter(Date__year='2000')
    TAO=AccessMode.objects.filter(Date__month='06')
    TAO=AccessMode.objects.filter(Date__day='26')
    TAO=AccessMode.objects.filter(Date__month__gte='06')
    TAO=AccessMode.objects.filter(Q(id=3) | Q(Date='2000-06-26'))
    d={'TAO':TAO}
    return render(request,'display_accessmode.html',d)

def update_webpage(request):
    Webpage.objects.filter(Name='Tiru').update(Url='http://.ktm.in')
    Webpage.objects.filter(Name='Kinger').update(Url='https//King.com')
    Webpage.objects.filter(Name='Kinger').update(Topic_name='Cricket')
    topic_name=Topic.objects.get(Topic_name='Cricket')
    Webpage.objects.update_or_create(Name='Gopi',defaults={'Topic_name':topic_name})
    web=Webpage.objects.all()
    d={'web':web}
    return render(request,'display_webpage.html',d)