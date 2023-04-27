from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('Topic is Inserted')
        else:
            return HttpResponse('data is not valid')

    return render(request,'insert_topic.html',d)