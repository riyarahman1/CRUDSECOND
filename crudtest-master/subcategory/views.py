from django.http import JsonResponse
from django.shortcuts import redirect, render 
from requests import request
from django.views.decorators.csrf import csrf_exempt
from myapp.models import Project_Category,Project_Subcategory



 


@csrf_exempt
def create_project_subcategory(request):
    values=projectcategory.objects.all()
    print(values)
    if request.method == 'POST':
        projectcategory = request.POST.get('projectcategory')
        print(projectcategory)
        projectsubcategory = request.POST.get('subcategory')
        is_active = request.POST.get('is_active')

        # Create a new project instance
        project = Project_Subcategory(projectcategory=projectcategory, projectsubcategory=projectsubcategory, is_active=is_active)
        project.save()

        response_data = {'status': 'success', 'message': 'Project type created successfully'}
    else:
        response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'subcategory/project.html',values)


def view_project_subcategory(request):
    projectsubcategory = Project_Subcategory.objects.all().order_by("-id")
    projectcategory = Project_Category.objects.all()
    print(projectcategory)
    context = {
        'projectcategory': projectcategory,
        'projectsubcategory': projectsubcategory,
    }
    return render(request, "subcategory/project.html", context)




def update_project_subcategory(request, category_id):
    subcategory = Project_Category.objects.get(id=category_id)
    if request.method == 'POST':
        subcategory.category = request.POST.get('category')
        subcategory.project_name = request.POST.get('project_name')
        subcategory.save()

        return redirect('project')
    context = {
        'subcategory': subcategory,
    }
    return render(request, 'subcategory/update_project_category.html', context)


def delete_project_subcategory(request, category_id):
    category = Project_Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()

        return redirect('project')
    context = {
        'category': category,
    }
    return render(request, 'subcategory/delete_project_category.html', context)
