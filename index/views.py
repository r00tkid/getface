from django.shortcuts import render
from rest_framework.views import View


class Index(View):
    @staticmethod
    def get(request):
        return render(request, 'index.html')
