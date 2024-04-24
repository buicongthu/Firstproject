from django.urls import path
from .views import ProductViewSet
urlpatterns = [
    path('product/',ProductViewSet.as_view({
        'post':'create'
    })),
    path('product/<str:pk>',ProductViewSet.as_view({
        'put':'update',
        'delete':'destroy'
    }))
]
