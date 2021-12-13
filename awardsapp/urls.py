from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    url(r'^$',views.home,name='home'),
    url(r'^profile/',views.profile,name = 'profile'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profiles/(\d+)',views.profiles,name='profiles'),
    url(r'^comment/(\d+)',views.comment,name='comment'),
    url(r'^review/(\d+)',views.review,name='review'),
    url(r'^upload/', views.upload, name='upload'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),
    url(r'api/projects/merch-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'api/profile/merch-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)