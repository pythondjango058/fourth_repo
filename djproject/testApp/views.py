from django.shortcuts import render
from testApp.models import *
# Create your views here.
def home(request):
    return render(request,'testApp/home.html')
def hydjobs1(request):
    hydjobs_list=hydjobs.objects.order_by('date')
    my_dict={'hydjobs_list':hydjobs_list}
    return render(request,'testApp/hydjobs.html', context=my_dict)

def banglorejobs1(request):
    banglorejobs_list=banglorejobs.objects.order_by('date')
    my_dict={'banglorejobs_list':banglorejobs_list}
    return render(request,'testApp/banglorejobs.html',context=my_dict)

def chennaijobs1(request):
    chennaijobs_list=chennaijobs.objects.order_by('date')
    my_dict={'chennaijobs_list':chennaijobs_list}
    return render(request,'testApp/chennaijobs.html',context=my_dict)

def punejobs1(request):
    punejobs_list=punejobs.objects.order_by('date')
    my_dict={'punejobs_list':punejobs_list}
    return render(request,'testApp/punejobs.html',context=my_dict)
