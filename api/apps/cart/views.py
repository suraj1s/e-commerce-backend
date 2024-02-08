from django.shortcuts import render
from rest_framework import generics
from .models import Cart
from .serializers import CartSerializer

class CartListAPIView(generics.ListAPIView):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class CartCreateAPIView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CartRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartUpdateAPIView(generics.UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartDeleteAPIView(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer