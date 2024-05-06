
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=False)
    def by_category(self, request):
        category = self.request.query_params.get('category', None)
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer