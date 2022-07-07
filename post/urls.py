from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, PostView


router = routers.DefaultRouter()
router.register('category', CategoryView) 
router.register('post', PostView) 

urlpatterns = [

]

urlpatterns += router.urls

