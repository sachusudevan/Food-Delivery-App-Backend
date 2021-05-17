from rest_framework import serializers

from apps.products.models import Category




class CategorySerializer(serializers.ModelSerializer):
    # unique_id = serializers.SlugField(max_length=65, min_length=8, write_only=True)
    # name = serializers.CharField(max_length=300, min_length=4),
    # description = serializers.CharField()
    # is_publish = serializers.BooleanField()
    # image = serializers.ImageField()

    class Meta:
        model = Category
        fields = ['id','name', 'is_publish', 'image']

    # def validate(self, attrs):
    #     email = attrs.get('email', '')
    #     if Category.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email': ('Email is already in use')})
    #     return super().validate(attrs)

    # def create(self, validated_data):
    #     return Category.objects.create_user(**validated_data)