from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.custom, name="index"),
    path('usertask/', views.user_task, name="task.create"),
    path('usertask/usertaskpost/', views.user_task_post, name="task.post"),
    path('assignedtaskdesc/', views.assigned_task_desc, name="task.assign"),
    path('personaltask/post/', views.personal_task_post, name="task.personal"),
    path('personaltask/', views.personal_task, name="task.personal.post"),
    path('usernote/', views.user_note, name="user.note"),
    path('usernote-add/', views.user_note_add, name="user.note.add")
]
