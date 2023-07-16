from rest_framework import serializers
from poems.models import Poem
from likes.models import Like
from datetime import datetime


class PoemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    profile_name = serializers.ReadOnlyField(
        source='owner.profile.display_name')
    featured_flag = serializers.ReadOnlyField()
    published_at = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    comments_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, poem=obj
            ).first()
            return like.id if like else None
        return None

    def get_published_at(self, obj):
        if obj.published_at:
            return obj.published_at.strftime("%d %b %Y")
        return obj.published_at

    def validate_image(self, value):
        if value.size > 800 * 1024:
            raise serializers.ValidationError(
                "File larger than 800KB can't be uploaded."
            )
        if value.image.height > 1000:
            raise serializers.ValidationError(
                "Image with height over 1000px can't be uploaded."
            )
        if value.image.width > 1000:
            raise serializers.ValidationError(
                "Image with width over 1000px can't be uploaded."
            )
        return value

    class Meta:
        model = Poem
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'profile_name', 'created_at', 'published_at',
            'updated_at', 'title', 'content', 'category', 'published',
            'featured_flag', 'like_id', 'likes_count', 'comments_count',
        ]
