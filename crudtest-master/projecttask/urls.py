from django.urls import path

from projecttask import views

urlpatterns = [
    path('create_project/', views.create_project, name='createproject'),
    path('project_list/', views.project_list, name='projectlist'),
    path('update_project/', views.update_project, name='updateproject'),
    path('delete_project/', views.delete_project, name='deleteproject'),

]
