from django.db.models import Count,Max,Min,Avg,Sum
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from mainapp.models import *


# Create your views here.

def user_list(request: HttpRequest):
    datas = [
        {'id': 101, 'name': 'jsn'},
        {'id': 102, 'name': 'jack'},
        {'id': 103, 'name': 'tom'},
    ]
    return render(request, 'user/list.html', {'users': datas, 'msg': '最优秀的学员'})

def user_list3(request: HttpRequest):
    users = UserEntity.objects.all()
    msg =  '最优秀的学员'
    return render(request, 'user/list.html', locals())

def add_user(request):
    name = request.GET.get('name',None)
    age = request.GET.get('age',0)
    phone = request.GET.get('phone',None)

    if not all((name,age,phone)):
        return HttpResponse('请求参数不完整！',status=400)

    u1 = UserEntity()
    u1.name = name
    u1.age = age
    u1.phone = phone
    u1.save()
    return redirect('/user/list')

def update_user(request):
    id = request.GET.get('id',None)
    if not id:
        return HttpResponse('请输入正确的id', status=400)
    name = request.GET.get('name',None)
    phone = request.GET.get('phone',None)
    try:
        u = UserEntity.objects.get(pk=int(id))
        if name:
            u.name = name
        if phone:
            u.phone = phone
        u.save()
        return redirect('/user/list')
    except:
        return HttpResponse('此用户不存在', status=400)

def delete_user(request):
    id = request.GET.get('id')
    if not id:
        return HttpResponse('请输入正确的id', status=400)
    try:
        u = UserEntity.objects.get(pk=id)
        u.delete()
        return redirect('/user/list')
    except:
        return HttpResponse('此用户不存在', status=400)

def find_fruit(request):
    price1 = request.GET.get('price1',0)
    price2 = request.GET.get('price2',1000)
    fruits = FruitEntity.objects.filter(price__gte = price1,price__lte = price2).all()
    return render(request,'fruit/list.html',locals())

def find_store(request):
    stores = StoreEntity.objects.filter(create_time__year=2021)
    return render(request,'store/list.html',locals())

def count_fruit(request):
    result = FruitEntity.objects.aggregate(cnt = Count('name'),max=Max('price'),min = Min('price'),avg = Avg('price'),total=Sum('price'))
    return JsonResponse(result)