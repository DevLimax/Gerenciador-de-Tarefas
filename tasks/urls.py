from django.urls import path
from.views import home_view,add_task_view,edit_task,remove_task


urlpatterns = [
    path('', view=home_view, name='home'),
    path("new_task/", add_task_view, name="new_task"),
    path("edit_task/<int:id>", edit_task, name="edit_task"),
    path("remove_task/<int:id>", remove_task, name='remove_task')
]

