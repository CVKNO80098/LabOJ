from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    # 可以在此处添加其他自定义字段
    first_name = None
    last_name = None
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # 使用不同的 related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # 使用不同的 related_name
        blank=True,
    )


# 题目模型
class Problem(models.Model):
    title = models.CharField(max_length=255)  # 题目标题
    description = models.TextField()          # 题目描述
    input_format = models.TextField()         # 输入格式
    output_format = models.TextField()        # 输出格式
    difficulty = models.CharField(max_length=50)  # 难度等级

# 代码提交记录模型
class Submission(models.Model):
    STATUS_CHOICES = [
        ('Pending', '待评测'),
        ('Judging', '评测中'),
        ('Accepted', '通过'),
        ('Rejected', '未通过'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 提交者
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)  # 对应的题目
    code = models.TextField()             # 提交的代码
    language = models.CharField(max_length=50)  # 编程语言
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')    # 评测状态，如 'Pending', 'Accepted', 'Wrong Answer'
    execution_time = models.IntegerField(null=True, blank=True)  # 执行时间（毫秒）
    memory_used = models.IntegerField(null=True, blank=True)     # 使用内存（KB）
    score = models.IntegerField(null=True, blank=True)           # 得分
    submitted_at = models.DateTimeField(auto_now_add=True)       # 提交时间
