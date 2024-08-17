from django.urls import path
from .Views import list_books, LibraryDetailView
from .views import list_books

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
]


# relationship_app
from django.urls import path
from .views import admin_view, librarian_view, member_view

urlpatterns = [
    path('admin-view/', views.admin_view, name='admin_view'),
    # other URLs
]

# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]