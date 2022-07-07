from email.policy import default
from rest_framework import serializers
from .models import Category, Post, Comment, Like, View
from user.serializers import ProfileSerializer
from user.models import Profile
from pprint import pprint

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    comments = CommentSerializer(many=True, read_only=True, required=False)
    post_detail = serializers.HyperlinkedIdentityField(view_name='post-detail') 
    is_liked = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        current_user = self.context['request'].user
        liked_list = Like.objects.filter(post=obj)
        who_liked_list = [item.who_liked for item in liked_list]
        if current_user in who_liked_list:
            return True
        return False

    def get_is_viewed(self, obj):
        current_user = self.context['request'].user
        viewed_list = View.objects.filter(post=obj)
        who_viewed_list = [item.who_viewed for item in viewed_list]
        if current_user in who_viewed_list:
            return True
        return False
    
    def get_profile_pic(self, obj):
        profile_list = Profile.objects.filter(user=obj.writer)
        if profile_list:
            profile = profile_list[0]
            return 'media/' + str(profile.profile_pic)
        return False

    class Meta:
        model = Post
        fields = (
    "id",
    "comments",
    "is_viewed",
    "is_liked",
    "profile_pic",
    "post_detail",
    "title",
    "content",
    "post_pic",
    "publish_date",
    "update_date",
    "status",
    "slug",
    "writer",
    "category"
    )
    








