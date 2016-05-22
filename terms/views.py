# -*- coding: utf-8 -*-
from django.views.generic import ListView, DetailView
from rest_framework import viewsets

from .models import Term, Category
from .serializers import TermSerializer, CategorySerializer


class TermViewDetail(DetailView):
    model = Term

    def get_context_data(self, **kwargs):
        context = super(TermViewDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter().distinct()
        return context


class TermViewList(ListView):
    model = Term
    paginate_by = 10

    def get_queryset(self):
        if self.request.GET.get('q'):
            return self.model.objects.filter(
                active=True,
                title__icontains=self.request.GET['q']).distinct()
        else:
            return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super(TermViewList, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.filter().distinct()
        return context


class CategoryViewDetail(DetailView):
    model = Category


class CategoryViewList(ListView):
    model = Category


class TermAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Term.objects.all().order_by('-rank')
    serializer_class = TermSerializer


class CategoryAPIViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to b
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
