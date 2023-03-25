from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,CommentViewSet,ReplyCommentViewSet




router=DefaultRouter()
router.register('register',UserViewSet)
router.register('comment',CommentViewSet)
router.register('reply-comment',ReplyCommentViewSet)



urlpatterns = [
    path('', include(router.urls)),
]