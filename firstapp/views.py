import calendar
from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from calendar import HTMLCalendar
from firstapp.form import AssignedTaskDescForm, UserTaskForm, PersonalTaskForm, UserNoteForm
from firstapp.models import UserNote

# Create your views here.
def index(request, year = date.today().year, month=date.today().month):
    title = "Dynamic Title Sent From Code"
    year = int(year)
    month = int(month)

    if(year < 1999 or year > 2099):
        year = date.today().year

    month_name = calendar.month_name[month]
    cal = HTMLCalendar().formatmonth(year, month)

    data = {'title':title, 'year':year, 'month':month, 'cal':cal, 'monthname':month_name}
    #{'demo':title, 'year':year, 'n':range(10), 'cal':cal, 'monthname':month_name}
    return render(request, "home.html", data)

def user_task(request):
    userTask = UserTaskForm()
    return render(request, "base.html", {'form': userTask})

def user_task_post(request):
    task_title = request.POST['task_title']
    task_description = request.POST['task_description']
    task_assigned_at = request.POST['task_assigned_at']
    data = {
        'task_title':task_title,
        'task_description':task_description,
        'task_assigned_at':task_assigned_at
    }
    return render(request, "home.html", {'data': data})

def assigned_task_desc(request):
    assignedTask = AssignedTaskDescForm()
    return render(request, "home.html", {'form': assignedTask})

def personal_task(request):
    personalTask = PersonalTaskForm()
    return render(request, "home.html", {'form': personalTask})

def personal_task_post(request):
    personalTask = PersonalTaskForm()
    task_title: request.GET['task_title']
    data = {
        'form': personalTask,
        'task_title': request.GET['task_title'],
        'task_description': request.GET['task_description'],
        'task_assigned_at': request.GET['task_assigned_at']
    }
    return render(request, "personaltask.html", {'data': data})

def user_note(request):
    userNote = UserNoteForm()
    return render(request, "usernote.html", {'form': userNote})

def custom(request):
    return HttpResponse("Custom Page")

def user_note_add(request):
    userNote = UserNoteForm()
    template = 'usernote.html'
    if request.method == "POST":
        title = request.POST.get('note_title')
        description = request.POST.get('note_description')
        addedAt = request.POST.get('note_added_at')
        un = UserNote(note_title= title, note_description = description, note_added_at = addedAt)
        # context = {
        #     'note_title': title,
        #     'note_description': description,
        #     'note_added_at': addedAt
        # }
        #msg = "Success"
        return render(request, template , {'form': userNote, 'un': un})
    else:
        msg = "Fail"
        return render(request, template , {'form': userNote, 'msg': msg})

    