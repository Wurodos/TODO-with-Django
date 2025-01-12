from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Task

from django.http import HttpResponseRedirect
from .forms import TaskForm

# Create your views here.

@csrf_exempt
def home_view(request, id=None, is_form = ""):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = TaskForm(request.POST)
        # check whether it's valid:
        print(form.is_valid())
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print(form.cleaned_data)
            
            new_task = Task(
                title = form.cleaned_data["title_field"],
                description = form.cleaned_data["desc_field"],
                color = form.cleaned_data["color_picker"]
            )
            
            print(new_task.title)
            
            new_task.save()
            
        # redirect to a new URL:
        return HttpResponseRedirect("")
    
    # DELETE request handling
    if request.method == "DELETE":
        task_obj = Task.objects.get(pk=id)
        if task_obj:
            task_obj.delete()
        return HttpResponseRedirect("")
    context = {
        "task_list": Task.objects.all(),
    }
    
    if is_form == "true": context["is_form"] = True
    else: context["is_form"] = False
    
    return render(request, "index.html", context)
