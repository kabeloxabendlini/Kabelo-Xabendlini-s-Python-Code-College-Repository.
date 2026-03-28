# app - views.py file
# app - views.py file

from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.http import HttpResponse

def debug_photos(request):
    users = User.objects.all()
    output = "<br>".join([f"{u.name} | {u.photo}" for u in users])
    return HttpResponse(output)

def user_list(request):
    records = User.objects.all()
    mydict = {'records': records}
    return render(request, 'Listingpage.html', context=mydict)

def AddUser(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('user-list')
    return render(request, 'Add.html', {'form': form})

def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('user-list')
    return render(request, 'Edit.html', {'form': form})

def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('user-list')
    return render(request, 'Delete.html', {'user': one_rec})

def ViewUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    return render(request, 'View.html', {'user': one_rec})