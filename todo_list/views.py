from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from todo_list.models import Todo


def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, 'todo_list/index.html', {"todo_items": todo_items})


@csrf_exempt
def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    # TODO: Improve form validation
    if content == "":
        return HttpResponseRedirect("/")
    else:
        Todo.objects.create(added_date=current_date, text=content)
        return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
