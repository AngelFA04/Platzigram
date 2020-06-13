"""Users views"""
#Django
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 


def login_view(request):
    """ Login view. """
    print("*"*20)
    print("TODO BIEN TODO CORRECTO")
    print("*"*20)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Implementación de login de documentación
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('feed')
        else:
            return render(request, 'users\login.html', {'error': 'Invalid username and password'})

    return render(request, 'users\login.html')

@login_required
def logout_view(request):        
    logout(request)
    # Redirect to a success page.        
    return redirect('login')