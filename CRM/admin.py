from django.contrib import admin
from .models import Tasks_status,Tasks,Cases
# Register your models here.

@admin.register(Tasks)
class tasks(admin.ModelAdmin):
    pass
    list_display = ('task_id','task_name')

@admin.register(Tasks_status)
class tasks_status(admin.ModelAdmin):
    pass
    list_display = ('task_status_id','task_status')

@admin.register(Cases)
class cases(admin.ModelAdmin):
    pass
    list_display = ('case_id','title','task_id','updated_on','created_on','content','task_status')

