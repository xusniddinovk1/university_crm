from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TeacherHomeworkViewSet, StudentHomeworkView, ChangePasswordView
from .views.attendance_view import GroupAttendanceView
from .views.group_view import DepartmentsViewSet, CourseViewSet, TeacherGroupViewSet, StudentGroupViewSet, \
    GroupStudentViewSet
from .views.login import *
from .views.payment_view import PaymentViewSet
from .views.register_view import RegisterUserApi
from .views.statistics_view import StudentStatisticsView
from .views.student_view import *
from .views.teacher_view import TeacherListCreateView, TeacherDetailView

router = DefaultRouter()
router.register(r'payment', PaymentViewSet, basename='payment')
router.register(r'department', DepartmentsViewSet, basename='department')
router.register(r'course', CourseViewSet, basename='course')
router.register(r'teacher-homeworks', TeacherHomeworkViewSet, basename='teacher-homework')
router.register(r'groups', GroupStudentViewSet, basename='groups')
router.register(r'teacher-groups', TeacherGroupViewSet, basename='teacher-groups')
router.register(r'student-groups', StudentGroupViewSet, basename='student-groups')

urlpatterns = [
    path('', include(router.urls)),

    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('register/', RegisterUserApi.as_view(), name='register'),
    path('teachers/', TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),

    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/create/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/statistics/', StudentStatisticsView.as_view(), name='student-statistics'),
    path('student/homework/', StudentHomeworkView.as_view(), name='student-homework'),

    path('attendance/', GroupAttendanceView.as_view(), name='attendance'),

    path('change-password/', ChangePasswordView.as_view(), name='change-password'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
