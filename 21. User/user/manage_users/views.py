from django.shortcuts import render
from .models import Users
from django.http import HttpResponse


# Create your views here.

def Main_Page(request):
    return render(request, 'main.html')

def List_Users(request):
    all_users = Users.objects.all().values()
    context = {'all_users':all_users}

    return render(request, 'list_users.html', context=context)

def Create_User(request):
    return render(request, 'create_user.html')

def Update_User(request):
    return render(request, 'update_user.html')

def Delete_User(request):
    return render(request, 'delete_user.html')

"""def reader(request):
    if request.method == 'POST':
        form = Readers_Data(request.POST)
        if form.is_valid():
            return render(request, 'book.html')


    return render(request, 'reader.html', {"form" : Readers_Data})"""