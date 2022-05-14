from django.urls import path
from .views import ProductViewSet, RecommendationsViewSet, CategoryViewSet, OrderingViewSet, ReviewViewSet


urlpatterns = [
    path('prod-list/', ProductViewSet.as_view({'get': 'list'})),
    #path('prod-change/<int:pk>/', ProductViewSet.as_view({'patch': 'update'})),
    path('prod-detail/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve'})),
    #path('prod-delete/<int:pk>/', ProductViewSet.as_view({'delete': 'destroy'})),

    path('rec-list/', RecommendationsViewSet.as_view({'get': 'list'})),
    #path('rec-change/<int:pk>/', RecommendationsViewSet.as_view({'patch': 'update'})),
    path('rec-detail/<int:pk>/', RecommendationsViewSet.as_view({'get': 'retrieve'})),
    #path('rec-delete/<int:pk>/', RecommendationsViewSet.as_view({'delete': 'destroy'})),

    path('category-list/', CategoryViewSet.as_view({'get': 'list'})),
    #path('category-change/<int:pk>/', CategoryViewSet.as_view({'patch': 'update'})),
    path('category-detail/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve'})),
    #path('category-delete/<int:pk>/', CategoryViewSet.as_view({'delete': 'destroy'})),

    path('ordering-create/', OrderingViewSet.as_view({'post': 'create'})),
    path('ordering-list/', OrderingViewSet.as_view({'get': 'list'})),
    path('ordering-change/<int:pk>/', OrderingViewSet.as_view({'patch': 'update'})),
    path('ordering-detail/<int:pk>/', OrderingViewSet.as_view({'get': 'retrieve'})),
    path('ordering-delete/<int:pk>/', OrderingViewSet.as_view({'delete': 'destroy'})),

    path('review-create/', ReviewViewSet.as_view({'post': 'create'})),
    path('review-list/', ReviewViewSet.as_view({'get': 'list'})),
    path('review-change/<int:pk>/', ReviewViewSet.as_view({'patch': 'update'})),
    path('review-detail/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'})),
    path('review_delete/<int:pk>/', ReviewViewSet.as_view({'delete': 'destroy'}))
]
