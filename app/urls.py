from django.urls import path
from app import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('',views.home),
    path('add/',views.add,name='add'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete_all/',views.delete_all,name="delete_all"),
    path('mark-complete/<int:id>/',views.mark_completed,name='Mark-complete')
]
