from django.conf.urls import url, include


urlpatterns = [

    url(r'^user_dashboard/', include('apps.user_dashboard.urls', namespace='user_dashboard'))
    
]
