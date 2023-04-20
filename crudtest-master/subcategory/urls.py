from django.urls import path

from subcategory import views

urlpatterns = [
    # other URL patterns
  
    path('create_project_subcategory/', views.create_project_subcategory, name='createsubcategory'),
    path('view_project_subcategory/', views.view_project_subcategory, name='viewsubcategory'),
    path('update_project_subcategory/<int:category_id>', views.update_project_subcategory, name='updatesubcategory'),
    path('delete_project_subcategory/<int:category_id>', views.delete_project_subcategory, name='deletesubcategory'),


]
