from django.views.generic import View
from django.shortcuts import render


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')
