from django.urls import path
from .views import SignUpView,HomeView,ShowBooks,OrderBooks


urlpatterns = [
   path('',HomeView.as_view(),name='home'),
   path('signup/',SignUpView.as_view(),name='signup'),
   path('books/',ShowBooks.as_view(),name='books'),
   path('orders/',OrderBooks.as_view(),name='orders')
]