from rest_framework import serializers
from .models import Product, Category
from .validators import validate_category_name, validate_product_name, validate_product_price


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail', lookup_field='pk')
    name = serializers.CharField(validators=[validate_category_name])
    description = serializers.CharField(required=False, allow_blank=True)
    
    class Meta:
        model = Category
        fields = ["url", "name", "description"]
        
        
class ProductSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    name = serializers.CharField(validators=[validate_product_name])
    description = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = Product
        fields = ['url', 'name', 'description', 'price', 'stock', 'category']