from django.urls import path
from User.views import SignUp, Login, Inicio, cerrar
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

urlpatterns = [
    path('', Inicio, name='inicio'),
    path('cerrar/', cerrar, name='cerrar'),
    path('signup/', SignUp, name='signup'),
    path('login/', Login, name='login'),
    path(r'^reset/password_reset/$', PasswordResetView.as_view(), name='reset_password_reset1'),
    path(r'^reset/password_reset/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]