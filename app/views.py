from django.shortcuts import render
from app.models import *
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.


def topic(request):
    topics=Topic.objects.all()
    #topics=Topic.objects.filter(topic_name='Music')
    return render(request,'displaytopic.html',context={'topics':topics})


def webpage(request):
    webpages=Webpage.objects.all()
    #webpages=Webpage.objects.filter(name='ronaldo')
    #webpages=Webpage.objects.order_by('url')
    #webpages=Webpage.objects.all()[0:5]
    #webpages=Webpage.objects.exclude(name='ronaldo')
    #webpages=Webpage.objects.filter(url__startswith='https')
    #webpages=Webpage.objects.filter(url__endswith='.com/')
    #webpages=Webpage.objects.filter(name__contains='Ro')
    #webpages=Webpage.objects.filter(Q(url__startswith='https'))
    #webpages=Webpage.objects.filter(Q(url__startswith='https') & Q(name__startswith='K'))
    #webpages=Webpage.objects.filter(Q(url__startswith='https') | Q(name__startswith='S'))
    #webpages=Webpage.objects.filter(Q(url__endswith='.com/') & Q(name__startswith='M'))


    return render(request,'displaywebpage.html',context={'webpages':webpages})



def access(request):
    #access=Access_Records.objects.all()
    access=Access_Records.objects.filter(date__gt='2011-03-12')
    #access=Access_Records.objects.filter(date__gte='2011-03-12')
    #access=Access_Records.objects.filter(date__lt='2011-03-12')
    #access=Access_Records.objects.filter(date__lte='2011-03-12')
    #access=Access_Records.objects.exclude(date__lte='2011-03-12')
    #access=Access_Records.objects.filter(date__year='2011')
    #access=Access_Records.objects.filter(date__month='03')
    #access=Access_Records.objects.filter(date__day='11')


    return render(request,'displayaccess.html',context={'access':access})

def deleteweb(request):
    #Webpage.objects.filter(name='Robert').delete()
    Webpage.objects.all().delete()

    webpages=Webpage.objects.all()

    #return HttpResponse('one record has been deleted successfully')
    return render(request,'displaywebpage.html',context={'webpages':webpages})


def updateweb(request):
    #Webpage.objects.filter(name='Dean').update(url='https://www.jones-garcia.biz/')
    #Webpage.objects.filter(name='Dean').update(name='Dhoni')
    Webpage.objects.filter(name='Dhoni').update(topic_name='Cricket')
    webpages=Webpage.objects.all()


    #return HttpResponse('one record as been updated')
    return render(request,'displaywebpage.html',context={'webpages':webpages})














