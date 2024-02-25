from django.contrib import admin

from TodoApp.models import TodoTable


#Register Todo Table in Admin Portal

admin.site.models(TodoTable)