from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
     path(
        route='profile/<int:pk>',
        view=views.UserDetail.as_view(),
        name='member_profile'
    ),
    path(
        route='update/<int:pk>',
        view=views.UserUpdateView.as_view(),
        name='user_update'
    ),
    # Login and Password reset
    path(
        route='login',
        view=views.UserLoginView.as_view(),
        name='login'
    ),
    path(
        route='reset-password',
        view=views.PasswordResetView.as_view(),
        name='password_reset'
    ),
    path('password-reset/done/', views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset_complete/done/', views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
    path('password-change', views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password-change/done/', views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),

    path('activate/<uidb64>/<token>/',
         views.activate, name='activate'),

]
