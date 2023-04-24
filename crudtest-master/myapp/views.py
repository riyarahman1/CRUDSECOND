from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_http_methods
from myapp.models import Project_Category, Project_Subcategory,Project
from django.db import IntegrityError


def index(request):
    return render(request, 'index.html')


def create(request):
    data = Project_Category(name=request.POST['name'] )
    data.is_active = False
    data.save()
    return redirect('/')

def read(request):
    read = Project_Category.objects.order_by('-id')
    context = {'read':read}
    return render(request, 'result.html', context)


def delete(request, id):
    obj = Project_Category.objects.get(id=id)
    obj.delete()
    return redirect('/')

def update(request,id):
    data = Project_Category.objects.get(id=id)
    data.name = request.POST['name']
    data.is_active = False
    data.save()
    return redirect('read')

@csrf_exempt
def toggle_projectcategory_active(request, projectcategory_id):
    try:
        projectsubcategory = Project_Category.objects.get(id=projectcategory_id)
    except Project_Category.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'projectsubcategory not found'})
    
    projectsubcategory.is_active = not projectsubcategory.is_active
    projectsubcategory.save()
    
    return JsonResponse({'status': 'success', 'is_active': projectsubcategory.is_active})






# --------------------------subcategory-----------------------

@csrf_exempt
def create_project(request):
    values=Project_Category.objects.all()

    if request.method == 'POST':
     
        
        category = request.POST.get('category')
        print(category)
        print("k")
        project_name = request.POST.get('project_name')
        print("product")
        print(project_name)
        # # Create a new project instance
        project = Project_Subcategory(category_id=category, project_name=project_name,is_active = True)
        project.save()

        response_data = {'status': 'success', 'message': 'Project type created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'subcategory/subindex.html',{'values':values})


def read1(request):
    readd = Project_Subcategory.objects.order_by('-id')
    context = {'readd':readd}
    return render(request, 'subcategory/res.html', context)




def update2(request, id):
    data = Project_Subcategory.objects.get(id=id)
    category = request.POST['category']
    project_name = request.POST['project_name']
    obj = Project_Subcategory.objects.get(id=id)
    obj.category = category
    obj.project_name = project_name
    obj.save()
    data.is_active = False
    return redirect('read',{'data':data})




@csrf_exempt
def toggle_projectsubcategory_active(request, projectsubcategory_id):
    try:
        projectsubcategory = Project_Subcategory.objects.get(id=projectsubcategory_id)
    except Project_Subcategory.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'projectsubcategory not found'})
    
    projectsubcategory.is_active = not projectsubcategory.is_active
    projectsubcategory.save()
    
    return JsonResponse({'status': 'success', 'is_active': projectsubcategory.is_active})



# -------------------------Project------------------------------

def project(request):
    data=Project_Subcategory.objects.all()
 

    if request.method == 'POST':
     
        
        subcategory = request.POST.get('subcategory')
        print(subcategory)
    
    
        title = request.POST.get('title')
        print(title)

        description = request.POST.get('description')
        print(description)

        # # Create a new project instance
        project = Project(subcategory=subcategory, title=title,description = description,is_active= True)
        project.save()

        response_data = {'status': 'success', 'message': 'Product created successfully'}
    # else:
    #     response_data = {'status': 'error', 'message': 'Invalid request'}
        
        return JsonResponse(response_data)
    return render(request,'projecttask/home.html',{'data':data})



def viewproject(request):
    object = Project.objects.all()
    print(object)
    context = {'object':object}
    return render(request, 'projecttask/table.html', context)
    

@csrf_exempt
def toggle_project_active(request,project_id):
    try:
        create = Project.objects.get(id=project_id)
        
    except create.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'})
    
    create.is_active = not create.is_active
    create.save()
    
    return JsonResponse({'status': 'success', 'is_active': create.is_active})