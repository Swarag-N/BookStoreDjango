from django.urls import path, include

from store import views

urlpatterns = [
    path('latest-products/', views.LatestBooksList.as_view()),
    path('genre/<slug:genre_slug>/', views.GenreDetail.as_view()),
    path('<slug:genre_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
    # path('products/search/', views.search),
]