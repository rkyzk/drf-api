from rest_framework import serializers
from .models import Profile
from followers.models import Follower


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    followers_count = serializers.ReadOnlyField()
    poems_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            return following.id if following else None
        return None

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
        model = Profile
        fields = [
            'id', 'owner', 'display_name', 'created_at', 'updated_at',
            'about_me', 'favorites', 'image', 'is_owner', 'following_id',
            'followers_count', 'poems_count'
        ]
