from django.urls import path
from .views import PeopleView, CategoriesView, MassageView, OrdersView


urlpatterns = [
    path('user/<int:uuid>', PeopleView.as_view()),
    path('user', PeopleView.as_view()),
    path('catalog', CategoriesView.as_view()),
    path('catalog/<int:uuid>', CategoriesView.as_view()),
    path('massage', MassageView.as_view()),
    path('massage/<int:uuid>', MassageView.as_view()),
    path('orders', OrdersView.as_view()),
    path('orders/<int:uuid>', OrdersView.as_view()),
]