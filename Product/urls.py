from django.urls import path
from .views import ProductViewSet,CompanyViewSet
urlpatterns = [
    path('product/',ProductViewSet.as_view({
        'post':'create'
    })),
    path('product/<str:pk>',ProductViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    })),
    path('product/add/',ProductViewSet.as_view({'post':'add'})),
    path('company/add/',CompanyViewSet.as_view({'post':'add'}))

]
