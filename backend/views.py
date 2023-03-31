from rest_framework import viewsets,generics,permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from .models import *
from .serializers import *
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from .pagination import *
# --------------  view creat user ------------------------
class UserViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'get_current_user':
            return [permissions.IsAuthenticated()]   
        return [permissions.AllowAny()]
    
    # ----------------------- get get_current_user ---------------------
    @action(methods=['get'],detail=False,url_path='current-user')
    def get_current_user(self,request):
        serializer =UserGetSerializer(request.user,context={"request": request})
        return Response(serializer.data,status=status.HTTP_200_OK)


# ------------------------- get comment --------------------------------
class CommentViewSet(viewsets.ViewSet,generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video_id']
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    pagination_class = PaginationClass
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.IsAuthenticated()]   
        return [permissions.AllowAny()]
    
    # ---------------------- create comment --------------------
    def create(self, request, *args, **kwargs):
        serializer = CommentPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ------------------------------ reply comment ------------------
class ReplyCommentViewSet(viewsets.ViewSet,generics.CreateAPIView):
    queryset = ReplyComment.objects.all()
    serializer_class = ReplyPostCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

