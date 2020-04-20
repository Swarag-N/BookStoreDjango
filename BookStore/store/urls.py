from django.urls import path
from .views import SignUpView,HomeView,ShowBooks,OrderBooks,DetailBookView,DeleteOrderView

urlpatterns = [
   path('',HomeView.as_view(),name='home'),
   path('signup/',SignUpView.as_view(),name='signup'),
   path('books/',ShowBooks.as_view(),name='books'),
   path('orders/',OrderBooks.as_view(),name='orders'),
   path('<slug:slug>/',DetailBookView.as_view(),name='book-detail'),
   path('order/del/<int:pk>/',DeleteOrderView.as_view(), name='order-del')
]