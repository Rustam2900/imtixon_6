from django.shortcuts import render,redirect,get_object_or_404,render,HttpResponseRedirect
from django.contrib import  messages

from Todo.forms import TodoForm
from Todo.models import Todo


def index(request):

    itim_list =Todo.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Todo Added Successfully')
            return redirect('todo')
    form = TodoForm()
    page ={
        'form':form,
        'itim_list':itim_list,
        'title':'TODO LIST',
    }
    return render(request, 'todo/index.html', page)


from django.shortcuts import render

# relative import of forms



def create_view(request):
    form = TodoForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, "todo/create_view.html", context)


def detail_view(request, id):
    context = {}
    context["data"] = Todo.objects.get(id=id)

    return render(request, "todo/detail_view.html", context)

def update_view(request, id):
    context = {}
    obj = get_object_or_404(Todo, id=id)
    form = TodoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + id)
    context = {
        'form': form,
    }
    return render(request, "todo/update_view.html", context)


def delete_view(request, id):
    context = {}
    obj = get_object_or_404(Todo, id=id)

    if request.method == "POST":
        return HttpResponseRedirect("/")

    return render(request, "todo/delete_view.html", context)







