from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def cal_view(request):
    #resp=HttpResponse("<h1>heyyy world.........</h1>")
    #return resp
    #a=int(request.GET.get('t1',0))
    #b=int(request.GET.get('t2',0))
    #res=a+b
    #print('a=',a,'b=',b)
    #d1={'t1':a,'t2':b,'t3':a+b}
    if request.method=="GET":
        res=render(request,'cms/home.html')
        return res
    elif request.method=="POST":
        if 'btn_add' in request.POST:
            a=int(request.POST.get('t1',0))
            b=int(request.POST.get('t2',0))
            res=a+b
            d1={'t1':a,'t2':b,'t3':res}
            resp=render(request,"cms/home.html",context=d1)
            return resp
        elif "btn_subtract" in request.POST:
            a=int(request.POST.get('t1',0))
            b=int(request.POST.get('t2',0))
            res=a-b
            d1={'t1':a,'t2':b,"t3":res}
            resp=render(request,"cms/home.html",context=d1)
            return resp
        elif "btn_multiply" in request.POST:
            a=int(request.POST.get('t1',0))
            b=int(request.POST.get('t2',0))
            res=a*b
            d1={'t1':a,"t2":b,"t3":res}
            resp=render(request,"cms/home.html",context=d1)
            return resp
        elif "btn_devide" in request.POST:
            a=int(request.POST.get("t1",0))
            b=int(request.POST.get("t2",0))
            res=a/b
            d1={'t1':a,'t2':b,'t3':res}
            resp=render(request,"cms/home.html",context=d1)
            return resp 