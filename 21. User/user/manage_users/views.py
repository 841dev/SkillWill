from django.shortcuts import render, redirect, get_object_or_404
from .models import Users
from .forms import UsersForm, UpdateForm, DeleteForm


# Create your views here.

def Main_Page(request):
    return render(request, 'main.html')

def List_Users(request):
    all_users = Users.objects.all().values()
    context = {'all_users':all_users}

    return render(request, 'list_users.html', context=context)

def Create_User(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/list/')
        else:
            print(form.errors)
    else:
        form = UsersForm()


    context = {'form':form}
    return render(request, 'create_user.html', context=context)

def Update_User(request, user_id):
    user = get_object_or_404(Users, id=user_id)

    if request.method == 'POST':
        form = UpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/list/')
    else:
        form = UpdateForm(instance=user)

    context = {'form':form}
    return render(request, 'update_user.html', context=context)


def Delete_User(request):
    if request.method == 'POST':
        form = DeleteForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            user = get_object_or_404(Users, pk=user_id)
            user.delete()
            return redirect('/list/')
    else:
        form = DeleteForm()

    context = {'form':form}
    return render(request, 'delete_user.html', context=context)