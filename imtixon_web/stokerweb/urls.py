from django.contrib import admin
from django.urls import path, include
from .views import IndexView, ServiceDetailView, ServiceView, AdvisersDetailView, AdvisersView, CommentView, FAQView, \
    ClientsView, ContactView, FeatureView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('advisers/', AdvisersView.as_view(), name='advisers'),
    path('advisers-detail/', AdvisersDetailView.as_view(), name='advisers-detail'),
    path('services/', ServiceView.as_view(), name='service'),
    path('services/', ServiceDetailView.as_view(), name='services-detail'),
    path('client/', ClientsView.as_view(), name='client'),
    path('comment/', CommentView.as_view(), name='comment'),
    path('faq/', FAQView.as_view(), name='faq'),
    path('feature/', FeatureView.as_view(), name='feature'),
    path('contact/', ContactView.as_view(), name='contact'),

]
