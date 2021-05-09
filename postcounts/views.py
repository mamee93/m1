from django.shortcuts import render, redirect
from .models import PostCount, AllCounts
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.db.models import Count
from django.contrib.auth.models import User
from django.db.models import Sum

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


class CoustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('count-List')


class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('count-List')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

        def get(self, *args, **kwargs):
            if self.request.user.is_authenticated:
                return redirect('count-List')
            return super(RegisterPage, self).get(*args, **kwargs)


class countList(LoginRequiredMixin, ListView):
    model = PostCount
    template_name = 'list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['count'] = PostCount.objects.all().aggregate(total_sum=Sum('count'))
         

        return context


# class Counts(LoginRequiredMixin, DetailView):
#     model = PostCount
#     context_object_name = 'counts'
#     template_name = 'counts.html'


class InsertCount(LoginRequiredMixin, CreateView):
    model = PostCount
    fields = ['count']
    template_name = 'insert-count.html'
    success_url = reverse_lazy('count-List')
