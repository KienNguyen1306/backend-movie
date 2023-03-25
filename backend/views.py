from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

class UserViewSet(viewsets.ViewSet,generics.CreateAPIView,generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CommentViewSet(viewsets.ViewSet,generics.ListAPIView,APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video_id']
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    
    def create(self, request, *args, **kwargs):
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ReplyCommentViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyPostCommentSerializer

