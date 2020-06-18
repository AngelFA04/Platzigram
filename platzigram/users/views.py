"""Users views"""
#Django
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.views.generic import ListView, FormView


#Exception
from django.db.utils import IntegrityError

#Models
from users.models import Profile
from django.contrib.auth.models import User
from posts.models import Post

#Forms
from users.forms import ProfileForm, SignupForm

#Generic class views
from django.views.generic import DetailView, UpdateView



class UserDetailView(LoginRequiredMixin, DetailView):
    """ User detail view."""
    template_name = 'users/detail.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    queryset = User.objects.all()
    context_object_name = 'user'
    
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class SignupView(FormView):
    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        """ Save from data """
        form.save()
        return super().form_valid(form)

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """ Update profile view """

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']
    

    def get_object(self):
        """" Return user's profile """
        return self.request.user.profile
    
    def get_success_url(self):
        """ Return to user's profile """
        username = self.object.user.username 
        return reverse('users:detail', kwargs={'username': username})

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
            return redirect('posts:feed')
        else:
            return render(request, 'users\login.html', {'error': 'Invalid username and password'})

    return render(request, 'users\login.html')

@login_required
def logout_view(request):        
    logout(request)
    # Redirect to a success page.        
    return redirect('users:login')


#These functions are not longer used. But for didactic purposes they aren't erased.

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')

    else:
        form = SignupForm()

    return render(
    request=request, 
    template_name='users/signup.html',
    context={'form':form})




@login_required
def update_profile(request):
    """ Update a user's profile view. """
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        errs = form.errors
        if form.is_valid():
            data = form.cleaned_data
            print("**********\n",form.cleaned_data)
            profile.biography = data["biography"]
            profile.website = data["website"]
            profile.phone_number = data["phone_number"]
            profile.picture = data["picture"]
            
            profile.save()

            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

    else:
        form = ProfileForm()
   
    
    return render(request=request, 
                  template_name='users/update_profile.html',
                  context={
                      'profile':profile,
                      'user':request.user,
                      'form':form,
                  })
                
