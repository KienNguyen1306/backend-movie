from rest_framework.serializers import ModelSerializer
from .models import *



class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields =['username','email','password','avatar']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
         
class ReplyCommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ReplyComment
        fields =['user','content','comment','created_at']


class ReplyPostCommentSerializer(ModelSerializer):
    class Meta:
        model = ReplyComment
        fields =['user','content','comment','created_at']



class CommentSerializer(ModelSerializer):
    replies = ReplyCommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True) 
    class Meta:
        model = Comment
        fields =('id','user','video_id','content','created_at','replies')
        
    
class CommentPostSerializer(ModelSerializer):
     
    class Meta:
        model = Comment
        fields =('user','video_id','content','created_at')
        
    