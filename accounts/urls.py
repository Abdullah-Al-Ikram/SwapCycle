from django.urls import path

from accounts import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('signup/user/', views.signup_user, name='signup-user'),
    path('signup/seller/', views.signup_seller, name='signup-seller'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)