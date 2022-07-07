from django.urls import path, include
from rest_framework import routers
from .views import CategoryView, PostView, CommentView, LikeView, ViewListView


router = routers.DefaultRouter()
router.register('category', CategoryView) 
router.register('post', PostView) 
router.register('comment', CommentView) 
router.register('like', LikeView) 
router.register('view', ViewListView) 

urlpatterns = [

]

urlpatterns += router.urls

