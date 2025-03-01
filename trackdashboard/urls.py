from django.urls import path
from . import views

from .views import signup_view, login_view, logout_view,index

urlpatterns = [
    path('activity_list', views.activity_list, name='activity_list'),
    path('', views.index, name='index'),
    path('create/', views.create_activity, name='create_activity'),
    path('view_activity/<int:pk>', views.view_activity, name='view_activity'),
    path('update_activity/<int:pk>', views.update_activity, name='update_activity'),
    path('delete_activty/<int:pk>', views.delete_activity, name='delete_activity'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
  
]


