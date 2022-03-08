from django.contrib import admin
from django.urls import path, include
from books.urls import router as BooksRouter

urlpatterns = [
    path('', include(BooksRouter.urls)),
    path('admin/', admin.site.urls),
]
