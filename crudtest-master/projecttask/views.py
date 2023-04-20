# import required models
from django.shortcuts import render, redirect
from myapp.models import Project_Subcategory, Project

# CREATE operation


def create_project(request):
    # check if the request method is POST
    if request.method == 'POST':
        # get the project data from the request.POST object
        title = request.POST['title']
        description = request.POST['description']
        subcategory_id = request.POST['subcategory_id']
        is_active = True if request.POST.get('is_active') else False

        # create a new project object with the data
        project = Project(title=title, description=description,
                          subcategory_id=subcategory_id, is_active=is_active)
        # save the project object
        project.save()

        # redirect to the project list page
        return redirect('project_list')

    # if the request method is GET, render the create project form
    subcategories = Project_Subcategory.objects.all()
    context = {'subcategories': subcategories}
    return render(request, 'projecttask/createproject.html', context)


# READ operation
def project_list(request):
    # get all the projects
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projecttask/projectlist.html', context)


# UPDATE operation
def update_project(request, project_id):
    # get the project object with the given id
    project = Project.objects.get(id=project_id)

    # check if the request method is POST
    if request.method == 'POST':
        # update the project object with the data from the request.POST object
        project.title = request.POST['title']
        project.description = request.POST['description']
        project.subcategory_id = request.POST['subcategory_id']
        project.is_active = True if request.POST.get('is_active') else False
        # save the updated project object
        project.save()

        # redirect to the project list page
        return redirect('project_list')

    # if the request method is GET, render the update project form
    subcategories = Project_Subcategory.objects.all()
    context = {'project': project, 'subcategories': subcategories}
    return render(request, 'projecttask/updateproject.html', context)


# DELETE operation
def delete_project(request, project_id):
    # get the project object with the given id
    project = Project.objects.get(id=project_id)

    # delete the project object
    project.delete()

    # redirect to the project list page
    return redirect('project_list')
