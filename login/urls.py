from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path("", views.home, name="home"),
    path('login/', views.login_view, name='login'),
    path("auth_home/", views.auth_home, name="auth_home"),
    path("admin_home/", views.admin_home, name="admin_home"),
    path("logout/", views.logout_view, name="logout"),
    path("upload/", views.upload_file, name="upload_file"),
    path("list_files/", views.list_files, name="list_files"),
    path("list_files_new/", views.list_files_new, name="list_files_new"),
    path("list_files_ip/", views.list_files_ip, name="list_files_ip"),
    path("list_files_resolved/", views.list_files_resolved, name="list_files_resolved"),
    path("user_reports/", views.list_specific_user_files, name="user_reports"),
    path("user_list_files_new/", views.user_list_files_new, name="user_list_files_new"),
    path("user_list_files_ip/", views.user_list_files_ip, name="user_list_files_ip"),
    path("user_list_files_resolved/", views.user_list_files_resolved, name="user_list_files_resolved"),
    path("user_file_view/<int:report_id>/", views.user_file_view, name="user_file_view"),
    path("individual_file_view/<int:report_id>/", views.individual_file_view, name="individual_file_view"),
    path("individual_file_view_new/<int:report_id>/", views.individual_file_view_new, name="individual_file_view_new"),
    path("individual_file_view_ip/<int:report_id>/", views.individual_file_view_ip, name="individual_file_view_ip"),
    path("individual_file_view_resolved/<int:report_id>/", views.individual_file_view_resolved,
         name="individual_file_view_resolved"),
    path("detail/<str:file_name>/", views.file_detail, name="file_detail"),
    path(
        "resolve_report_submit/<int:report_id>/",
        views.resolve_report_submit,
        name="resolve_report_submit",
    ),
    path("delete_report/<int:report_id>/", views.delete_report, name="delete_report"),
]
