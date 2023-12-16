from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/privacy_settings',
         views.privacy_settings, name='privacy_settings'),
    path('profile/edit_privacy_settings/',
         views.edit_privacy_settings, name='edit_privacy_settings'),
    #     path('signup/', views.signup, name='signup'),
    path('signup/', views.UserSignUpView.as_view(), name='signup'),
    #     path('login/', views.user_login, name='login'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    #     path('logout/', views.user_logout, name='logout'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/password_change/', views.password_change, name='password_change'),
    path('profile/password_change_without_old_password/', views.password_change_without_old_password,
         name='password_change_without_old_password'),
]
