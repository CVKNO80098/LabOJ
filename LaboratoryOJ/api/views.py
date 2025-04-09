from django.db.models import Sum
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from .models import Problem, Submission, User
from .serializers import UserSerializer, ProblemSerializer, SubmissionSerializer

# 用户注册视图
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 用户登录视图
class LoginView(APIView):
    def post(self, request):
        # 获取用户名和密码
        username = request.data.get('username')
        password = request.data.get('password')
        # 验证用户
        user = authenticate(username=username, password=password)
        if user:
            # 获取或创建用户的 Token
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid Credentials'}, status=400)

# 用户注销视图
class LogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # 删除用户的 Token，实现注销
        request.user.auth_token.delete()
        return Response({'message': 'Successfully logged out.'})

# 获取题目列表视图
class ProblemListView(generics.ListAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.AllowAny]  # 允许任何人访问

# 获取题目详情视图
class ProblemDetailView(generics.RetrieveAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    permission_classes = [permissions.IsAuthenticated]  # 需要认证

# 提交代码视图
class SubmissionCreateView(generics.CreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]  # 需要认证

    def perform_create(self, serializer):
        # 保存提交记录，并设置提交者为当前用户
        serializer.save(user=self.request.user, status='Pending')
        # TODO: 调用评测系统处理提交的代码

# 获取提交结果视图
class SubmissionDetailView(generics.RetrieveAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]  # 需要认证

# 获取排行榜视图
class LeaderboardView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]  # 需要认证

    def get_queryset(self):
        # 根据用户的总得分进行排序，生成排行榜
        return User.objects.annotate(total_score=Sum('submission__score')).order_by('-total_score')
