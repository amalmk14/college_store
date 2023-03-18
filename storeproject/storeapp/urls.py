from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('base',views.base,name='base'),
    path('add/',views.add,name='add'),
    # path('<int:pk>/', views.task_update_view, name='task_change'),
    path('ajax/load-course/', views.load_course, name='ajax_load_course'), # AJAX

]