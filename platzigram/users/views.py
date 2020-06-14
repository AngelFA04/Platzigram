"""Users views"""
#Django
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
 
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
#Models
from users.models import Profile

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

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users\signup.html', {'error': 'Password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=passwd, email=email)
        except IntegrityError:
            return render(request, 'users\signup.html', {'error': 'This user already exists'})
        
        
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.save()
        profile =  Profile(user=user)
        profile.save()

        return redirect('login')


    return render(request, 'users/signup.html')

def update_profile(request):
    return render(request, 'users/update_profile.html')