from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.user_login, name='login'),
    path('home/', views.home, name='home'),
    path('create_course/', views.create_course, name='create_course'),
    path('edit_course/<int:pk>/', views.edit_course, name='edit_course'),
    path('delete_course/<int:pk>/', views.delete_course, name='delete_course'),
    path('students/', views.students, name='students'),
    path('student_create/', views.student_create, name='student_create'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student'),
    path('student_info/<int:pk>',views.student_info,name='student_info'),
    path('company/',views.company_details,name='company'),
    path('company_create',views.company_create,name='company_create'),
    path('company_update/<int:pk>/',views.company_update,name='company_update'),
    path('company_delete/<int:pk>/',views.company_delete,name='company_delete'),
  
]

