from django.shortcuts import render
from django.views import View
import requests


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', )


class ServiceView(View):
    def get(self, request):
        services = requests.get("http://127.0.0.1:8000/Servises/").json()
        context = {
            'services': services
        }
        return render(request, 'service.html', context)


class ServiceDetailView(View):
    def get(self, request):
        services = requests.get("http://127.0.0.1:8000/Servises/").json()
        context = {
            'services': services
        }
        return render(request, 'services-detail.html', context)


class AdvisersView(View):
    def get(self, request):
        advisers = requests.get("http://127.0.0.1:8000/Advisers/").json()
        context = {
            'advisers': advisers
        }

        return render(request, 'advisers.html', context)


class AdvisersDetailView(View):
    def get(self, request):
        return render(request, 'advisers-detail.html')


class ClientsView(View):
    def get(self, request):
        return render(request, 'client.html')


class CommentView(View):
    def get(self, request):
        return render(request, 'comment.html')


class FeatureView(View):
    def get(self, request):
        return render(request, 'feature.html')


class FAQView(View):
    def get(self, request):
        return render(request, 'FAQ.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')
