from django.urls import path
from . import views
urlpatterns = [
    path('', views.add_book),
    path('authors', views.add_author),
    path('authors/<int:id>', views.see_author),
    path('books/<int:id>', views.see_book)
]
