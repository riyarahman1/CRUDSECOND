from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    # path('edit/<int:id>', views.edit, name='edit'),

    # path('update/<int:id>/', views.update_category, name='update_category'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('projectcategory/<int:projectcategory_id>/toggle-active/', views.toggle_projectcategory_active, name='toggle_projectcategory_active'),
# ----------------------------subcategory-------------------------
    path("create_project",views.create_project,name="create_project"),
    path('create_project/read1/',views.read1, name='read1'),
    path('projectsubcategory/<int:projectsubcategory_id>/toggle-active/', views.toggle_projectsubcategory_active, name='toggle_projectsubcategory_active'),
# ------------------------------project------------------------
  
    path("project",views.project,name="project"),
    path('project/viewproject/',views.viewproject, name='viewproject'),
    path('project/<int:project_id>/toggle-active/', views.toggle_active, name='toggle_active'),

]