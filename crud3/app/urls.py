from django.urls import path
from . import views

urlpatterns = [
    path('form/', views.form, name="form"),
    path('lists/', views.lists, name="lists"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('form/<int:id>', views.form, name="update"),
]
