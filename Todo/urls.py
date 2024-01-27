from django.urls import path

from .views import index, create_view, detail_view, update_view, delete_view

urlpatterns = [
    path('', index, name='todo'),
    path('create_view/',create_view, name='create_view'),
    path('detail_view/<int:id>/',detail_view, name='detail_view'),
    path('update_view/<int:id>/',update_view, name='update_view'),
    path('<id>/delete', delete_view )
]
