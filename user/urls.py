from django.urls import path, include
from .views import RegisterView, GetUpdateUserView, ProfileView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', ProfileView) # all crud opps for profile

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()), # for user create
    path('user/<int:id>/', GetUpdateUserView.as_view()), # for get and update user
]

urlpatterns += router.urls

