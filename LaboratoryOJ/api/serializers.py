from django.db import IntegrityError
from rest_framework import serializers
from .models import Problem, Submission, User

# 序列化工具似乎应该理解为服务器与客户端之间传递的数据的处理工具？，因为似乎只理解为JSON转格式的话似乎很多数据转化功能都不应该在这里

# 用户注册序列化器
class UserSerializer(serializers.ModelSerializer):
    # Meta定义数据来源
    class Meta:
        model = User # 选择模型
        fields = ['id', 'username', 'password', 'email'] # 选择哪些字段需要序列化
        extra_kwargs = {'password': {'write_only': True}} # 设置字段行为

    def create(self, validated_data): #如果序列化器用于创建对象，需要重写 create() 方法
        # 创建新用户并加密密码
        try:
            # 显式传递字段，避免**解包问题
            user = User.objects.create_user( # create_user() 方法会自动加密密码，确保安全性
                username=validated_data['username'],
                password=validated_data['password'],
                email=validated_data.get('email', '')  # 提供默认值
            )
            if user is None:  # 额外检查
                raise serializers.ValidationError("用户创建失败，返回None")
            return user
        except IntegrityError as e:
            raise serializers.ValidationError("用户名或邮箱已存在")
        except Exception as e:
            raise serializers.ValidationError(f"创建用户时出错: {str(e)}")

# 题目列表和详情序列化器
class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem # 当继承serializers.ModelSerializer时，create和update等如非特殊情况无需重写，有默认
        fields = '__all__'

# 代码提交序列化器
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = '__all__'
        read_only_fields = ['user', 'status', 'execution_time', 'memory_used', 'score', 'submitted_at']
