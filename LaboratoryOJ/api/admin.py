from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from api.models import User, Problem, Submission
from api.resources import ProblemResource, UserResource


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ('username', 'email', 'date_joined')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    # 感觉没必要批量导入，用不上
    list_display = ('user', 'problem', 'status')

@admin.register(Problem)
class ProblemAdmin(ImportExportModelAdmin):
    resource_class = ProblemResource
    list_display = ('title', 'description', 'input_format', 'output_format', 'difficulty')  # 根据你的模型字段调整