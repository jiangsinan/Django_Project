from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from mainapp.models import UserEntity

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