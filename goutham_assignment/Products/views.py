from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Product
from django.contrib import messages


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ['name', 'weight', 'price']

    def form_valid(self, form):
        messages.success(self.request, 'Your product has been created.')
        return super().form_valid(form)
