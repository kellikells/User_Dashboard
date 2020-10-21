from django.conf.urls import url
from . import views         

urlpatterns = [
    
    url(r'^$', views.index, name='user_dashboard_index'),

    url(r'^logout/$', views.logout, name="user_dashboard_logout"),

    url(r'^signin/$', views.signin, name='user_dashboard_signin'),
    
    url(r'^signin_process/$', views.signin_process, name='user_dashboard_signin_process'),

    url(r'^register/$', views.register, name='user_dashboard_register'),    

    url(r'^register_process/$', views.register_process, name='user_dashboard_register_process'),

    url(r'^register_success/$', views.register_success, name='user_dashboard_register_success'),    

    url(r'^dashboard_admin/$', views.dashboard_admin, name="user_dashboard_dashboard_admin"),

    url(r'^dashboard/$', views.dashboard, name="user_dashboard_dashboard"),    

    url(r'^users_new/$', views.users_new, name="user_dashboard_users_new"),

    url(r'^remove/$', views.remove, name="user_dashboard_remove"),

    url(r'^users/show/(?P<id>\d+)/$', views.users_show, name="user_dashboard_users_show"),

    # admin 
    url(r'^users/edit/(?P<id>\d+)/$', views.users_edit, name="user_dashboard_users_edit"),

    # normal
    url(r'^users/edit/$', views.normal_users_edit, name="user_dashboard_normal_users_edit"),

    # admin
    url(r'^update/(?P<id>\d+)/$', views.update, name="user_dashboard_update"),

    url(r'^update_password/(?P<id>\d+)/$', views.update_password, name="user_dashboard_update_password"),

    url(r'^update_description/(?P<id>\d+)/$', views.update_description, name="user_dashboard_update_description"),

    url(r'^create_message/(?P<id>\d+)/(?P<receiverID>\d+)/$', views.create_message, name="user_dashboard_create_message"),

    url(r'^create_comment/(?P<userID>\d+)/(?P<messageID>\d+)/(?P<receiverID>\d+)/$', views.create_comment, name="user_dashboard_create_comment"),

    url(r'^search_by_name/$', views.search_by_name, name="user_dashboard_search_by_name"),

    url(r'^users/show/(?P<id>\d+)/messageDel/(?P<messageID>\d+)/$', views.message_delete, name="user_Dashboard_messageDel"),

    url(r'^users/show/(?P<id>\d+)/commentDel/(?P<commentID>\d+)/$', views.comment_delete, name="user_Dashboard_commentDel"),

    url(r'^search_by_header/$', views.search_by_header, name="user_dashboard_search_by_header"),

    url(r'^on_load/$', views.on_load, name="user_dashboard_on_load"),
    
    



]