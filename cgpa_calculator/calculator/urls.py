from django.urls import path
from . import views

urlpatterns = [
    path("",views.loginform,name='home1'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('home/', views.home, name='home'),
    path('enter_grades/<int:semester_number>/', views.enter_grades, name='enter_grades'),
]