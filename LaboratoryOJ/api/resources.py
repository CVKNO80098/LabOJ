from import_export import resources
from .models import Problem, Submission, User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        import_id_fields = ['id']

class ProblemResource(resources.ModelResource):
    class Meta:
        model = Problem
        import_id_fields = ['id']