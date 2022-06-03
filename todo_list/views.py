from django.contrib import messages
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
    if content == "":
        messages.error(request, "Todo item is empty!")
        return HttpResponseRedirect("/")
    else:
        messages.success(request, "Todo added!")
        Todo.objects.create(added_date=current_date, text=content)
        return HttpResponseRedirect("/")


@csrf_exempt
def delete_todo(request, todo_id):
    messages.success(request, "Todo deleted!")
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/")
