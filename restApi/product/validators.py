from .models import Category, Product
from rest_framework import serializers


def validate_category_name(value):
    qs = Category.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"La catégorie {value} existe déjà")
    return value



def validate_product_name(value):
    qs = Product.objects.filter(name__iexact=value)
    if qs.exists():
        raise serializers.ValidationError(f"Le produit {value} existe déjà")
    return value


def validate_product_price(value):
    if value <= 0:
        raise serializers.ValidationError("Le prix doit être supérieur à 0")
    return value

