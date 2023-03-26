from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import *



# ------------------- user create ----------------------------
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =['id','username','email','password','avatar']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
         
# --------------------- user get -----------------------------
class UserGetSerializer(ModelSerializer):
    avatar = SerializerMethodField()
    def get_avatar(self,user):
        request = self.context['request']
        name = user.avatar.name
        if name.startswith('static/'):
            path = '/%s' %name
        else:
            path = '/static/%s'%name
        return request.build_absolute_uri(path)
    class Meta:
        model = User
        fields =['id','username','avatar']
        
    

# -------------------------- get reply comment ------------------
class ReplyCommentSerializer(ModelSerializer):
    user = UserGetSerializer(read_only=True)
    class Meta:
        model = ReplyComment
        fields =['user','content','comment','created_at']


# ---------------------------- post reply comment ---------------
class ReplyPostCommentSerializer(ModelSerializer):
    class Meta:
        model = ReplyComment
        fields =['user','content','comment','created_at']



# --------------------------- get comment -----------------------
class CommentSerializer(ModelSerializer):
    replies = ReplyCommentSerializer(many=True, read_only=True)
    user = UserGetSerializer(read_only=True) 
    class Meta:
        model = Comment
        fields =('id','user','video_id','content','created_at','replies')
        

# ---------------------------- post comment -----------------------
class CommentPostSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields =('user','video_id','content','created_at')
        
    