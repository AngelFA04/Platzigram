#Django
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, FormView   
from django.urls import reverse_lazy

#Utilities
from datetime import datetime

#Forms
from posts.forms import PostForm
from users.forms import SignupForm

#Models
from posts.models import Post


class PostsFeedView(LoginRequiredMixin, ListView):
    """" Return all published posts. """
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 2
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """ Post detail view."""
    #Necesary attributes
    template_name = 'posts/detail.html'
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post'

    pk_url_kwarg = 'pk'
    slug_field = 'id'
    slug_url_kwarg = 'post_id'

class CreatePostView(LoginRequiredMixin, CreateView):
    """ Create a post view """
    #This is a better implemenation compared with create_post function 

    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')
    
    def get_context_data(self, **kwargs):
        """ Add user and profile to context. """
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context



# Create your views here.
#These funcitions are not longer used. But for didactic purposes they aren't erased.
@login_required
def list_posts(request):
    """List existing posts"""
    posts = Post.objects.all().order_by('-created')

    return render(request, 'posts/feed.html', {'posts': posts})



@login_required
def create_post(request):
    """"Create new post view"""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')
    else:
        form = PostForm()
    
    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form':form,
            'user': request.user,
            'profile': request.user.profile,
        }
    )