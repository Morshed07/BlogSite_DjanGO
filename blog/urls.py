from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogList.as_view(), name='home'),
    # path('<slug:slug>/', views.BlogDetail.as_view(), name='post_detail'),
    path('blog-details/', views.BlogDetails, name='post_detail'),

]