from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from apps.core.views import *
from apps.job.views import *
from apps.userprofile.views import dashboard

urlpatterns = [
    path('', front_page, name = 'front_page'),
    path('signup/', signup, name = 'signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name="dashboard"),

    path('jobs/<int:job_id>/', job_deatil, name='job_detail')
]
