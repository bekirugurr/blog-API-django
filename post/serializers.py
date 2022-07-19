from email.policy import default
from rest_framework import serializers
from .models import Category, Post, Comment, Like, View
from user.serializers import ProfileSerializer
from user.models import Profile
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    commenter_name = serializers.SerializerMethodField()
    def get_commenter_name(self, obj):
        return User.objects.get(id=obj.commenter_id).username
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
    comments = CommentSerializer(many=True, read_only=True, required=False)
    post_detail = serializers.HyperlinkedIdentityField(view_name='post-detail') 
    is_liked = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    views_count = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()
    writer_name = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
     
    def get_is_liked(self, obj):
        current_user = self.context['request'].user
        # liked_list = Like.objects.filter(post=obj) # instead this, below line is written for quick query  
        liked_list = Like.objects.select_related('post').filter(post=obj)
        who_liked_list = [item.who_liked for item in liked_list]
        if current_user in who_liked_list:
            return True
        return False

    def get_is_viewed(self, obj):
        current_user = self.context['request'].user
        # viewed_list = View.objects.filter(post=obj) # instead this, below line is written for quick query
        viewed_list = View.objects.select_related('post').filter(post=obj)
        who_viewed_list = [item.who_viewed for item in viewed_list]
        if current_user in who_viewed_list:
            return True
        return False

    def get_likes_count(self, obj):
        # return Like.objects.filter(post=obj).count() # instead this, below line is written for quick query
        return Like.objects.select_related('post').filter(post=obj).count()

    def get_views_count(self, obj):
        # return View.objects.filter(post=obj).count() # instead this, below line is written for quick query
        return View.objects.select_related('post').filter(post=obj).count()

    def get_profile_pic(self, obj):
        # profile_list = Profile.objects.filter(user=obj.writer)# instead this, below line is written for quick query
        profile_list = Profile.objects.select_related('user').filter(user=obj.writer)
        if profile_list:
            profile = profile_list[0]
            return 'media/' + str(profile.profile_pic)
        return False
    
    def get_writer_name(self, obj):
        # return User.objects.get(id=obj.writer.id).username
        return obj.writer.username
    
    def get_like_id(self, obj):
        if self.context['request'].user.id:
            current_user_id = self.context['request'].user.id
            print(current_user_id)
            like_id_arr = Like.objects.filter(post=obj).filter(who_liked=current_user_id)
            if like_id_arr:
                return like_id_arr[0].id
        return 1 #! bu 1 i hiç kullanmıyor. Ama integer dönmezse hata veriyor

    # def get_like_id(self, obj):
    #     current_user = self.context['request'].user
    #     like_id = Like.objects.select_related('post').filter(post=obj).filter(who_liked=current_user)
    #     if like_id:
    #         return like_id[0].id
    #     return False

    class Meta:
        model = Post
        fields = (
    "id",
    "comments",
    "is_viewed",
    "is_liked",
    "views_count",
    "likes_count",
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
    "category",
    "writer_name",
    'like_id'
    )


