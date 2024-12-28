from django.urls import path
from . import views 

urlpatterns = [
    path('create-performance-review/', views.create_performance_review, name='create_performance_review'),
    path('api/performance-review/list/', views.performance_review_list, name='performance_review_list'),
    path('api/goal/create/', views.create_goal, name='create_goal'),
    path('api/goal/list/', views.goal_list, name='goal_list'),
    path('api/feedback/create/', views.create_feedback, name='create_feedback'),
    path('api/feedback/list/', views.feedback_list, name='feedback_list'),
    path('api/kpi_dashboard/', views.kpi_dashboard, name='kpi_dashboard'),
    path('api/kpi_dashboard_employee/<int:employee_id>/', views.kpi_dashboard_employee, name='kpi_dashboard_employee'),
    path('api/kpi_dashboard_admin/', views.kpi_dashboard_admin, name='kpi_dashboard_admin'),
    path('performance_review_list_employee/<str:employee_name>/', views.performance_review_list_employee, name='performance_review_list_employee'),
    path('view_goal_employee/<str:employee_name>/', views.view_goal_employee, name='view_goal_employee'),
    path('view_feedback_employee/<str:employee_name>/', views.view_feedback_employee, name='view_feedback_employee'),
    path('create_performance_review_manager/', views.create_performance_review_manager, name='create_performance_review_manager'),
    path('api/create_goal_manager/', views.create_goal_manager, name='create_goal_manager'),
    path('api/create_feedback_manager/', views.create_feedback_manager, name='create_feedback_manager'),
    path('api/view_manager_reviews/', views.view_manager_reviews, name='view_manager_reviews'),
    path('api/view_manager_goals/', views.view_manager_goals, name='view_manager_goals'),
    path('api/view_manager_feedbacks/', views.view_manager_feedbacks, name='view_manager_feedbacks'),
    path('api/view_create_performance_review_manager/<str:manager_name>/', views.view_create_performance_review_manager, name='view_create_performance_review_manager'),
    path('api/view_create_goal_manager/<str:manager_name>/', views.view_create_goal_manager, name='view_create_goal_manager'),
    path('api/view_create_feedback_manager/<str:manager_name>/', views.view_create_feedback_manager, name='view_create_feedback_manager'),
    path('api/feedback_form/', views.feedback_form, name='feedback_form'),
    path('api/submit_feedback/', views.submit_feedback, name='submit_feedback'),
    path('api/admin_feedback_dashboard/', views.admin_feedback_dashboard, name='admin_feedback_dashboard'),
    path('api/update_feedback_status/<int:feedback_id>/', views.update_feedback_status, name='update_feedback_status'),
    path('api/update_goal/<int:goal_id>/', views.update_employee_goal, name='update_employee_goal'),
    path('api/update_manager_goal/<int:goal_id>/', views.update_manager_goal, name='update_manager_goal'),
    path('api/check_if_manager/', views.check_if_manager, name='check_if_manager'),
    ]