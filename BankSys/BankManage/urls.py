from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('client/', views.client, name='client'),
    path('account/', views.account, name='account'),
    path('loan_manage/', views.loan_manage, name='loan_manage'),
    path('loan_issue/', views.loan_issue, name='loan_issue'),
    path('statistics/', views.statistics, name='statistics'),
]