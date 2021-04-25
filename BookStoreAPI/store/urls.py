from django.urls import path, include

from store import views

urlpatterns = [
    path('latest-products/', views.LatestBooksList.as_view()),
    # path('products/search/', views.search),
    # path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetail.as_view()),
    # path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]