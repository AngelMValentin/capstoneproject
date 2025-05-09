from . import views
from django.urls import path

urlpatterns = [
    path('login/', views.UserLogin.as_view(), name="login"),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('update_profile/', views.ProfileUpdate.as_view(), name="update_profile"),
    path('view_profile/<int:pk>/', views.ProfileView.as_view() ,name='user_profile'),
]