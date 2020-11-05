from django.shortcuts import render, redirect
from django.contrib.auth import authenticate

# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]        
        user = authenticate(username="admin1", password="issi123")
        print(user)
        if user is not None :
            return redirect('index')
        else :
            context = {
                'error' : 'Enter valid credentials!'
            }
            return render(request, 'Login.html',context)    
    else:
        return render(request, 'Login.html')
