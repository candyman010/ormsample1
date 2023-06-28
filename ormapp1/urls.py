from django.urls import path

from ormapp1 import views

urlpatterns = [
    path('', views.index_fun),
    path('insert', views.insert_fun),
    path('display', views.display_fun, name='display'),
    path('update/<int:id>', views.update_fun, name='update'),
    path('del/<int:id>', views.delete_fun, name='del'),
]