from django.urls import path
from django.views.decorators.cache import cache_page

from . import views

app_name = 'connection'

urlpatterns = [
    path('', views.index, name='index'),
    path('book/', cache_page(60)(views.BookListView.as_view()), name='book'),
    path('quote/', views.QuoteListView.as_view(), name='quotes'),
    path('creator/', views.CreatorListView.as_view(), name='creator'),
    path('creator/create/',
         views.CreatorCreate.as_view(),
         name='creator-create'),

    path('creator/<int:pk>/update/',
         views.CreatorUpdate.as_view(),
         name='creator-update'),

    path('creator/<int:pk>/delete/',
         views.CreatorDelete.as_view(),
         name='creator-delete'),

    path('creator/<int:pk>/',
         views.CreatorDetailView.as_view(),
         name='creator-detail'),
    path('creator/success/', views.success, name='success'),
]
