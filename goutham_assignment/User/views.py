from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .models import Post


def register(request):
    if request.user.is_authenticated:
        return redirect('logout')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"{username} has successfully registered.")
            return redirect('login')
        else:
            messages.error(request, 'Please check the info')
            return render(request, 'user/register.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request, 'User/register.html', {'form': form})


def home(request):
    return render(request, 'User/home.html')


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['text']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Your post has been created.')
        return super().form_valid(form)
