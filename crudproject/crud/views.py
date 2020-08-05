from django.shortcuts import render,redirect
from .forms import MyUserForms
from .models import MyUser

def create_user(request):
    form= MyUserForms(request.POST or None)
    users= MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'index.html',{'form':form,'users':users})

def update_user(request,id):
    id=MyUser.objects.get(id=id)
    form= MyUserForms(request.POST or None,instance=id)
    users= MyUser.objects.all()
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'index.html',{'form':form,'users':users})


def delete_user(request,id):
    user=MyUser.objects.get(id=id)
    user.delete()
    return redirect('/')
