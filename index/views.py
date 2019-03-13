from django.shortcuts import render
from django.views.generic import View


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')
