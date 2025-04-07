from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProblemListView, ProblemDetailView, SubmissionCreateView, SubmissionDetailView, LeaderboardView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('problems/', ProblemListView.as_view(), name='problem_list'),
    path('problems/<int:pk>/', ProblemDetailView.as_view(), name='problem_detail'),
    path('submissions/', SubmissionCreateView.as_view(), name='submission_create'),
    path('submissions/<int:pk>/', SubmissionDetailView.as_view(), name='submission_detail'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
]
