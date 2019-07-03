from django.conf.urls import url
from . views import Info_ListView, Info_DetailView, Info_DeleteView, Info_FormView, Marks_MarksView, Marks_ListView, Marks_DisplayView, Marks_UpdateView, Info_UpdateView,Home
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^student/$', Info_ListView.as_view(), name='index'),
    url(r'^student/detail/(?P<pk>[-\w]+)/$', Info_DetailView.as_view(), name='student-detail'),
    url(r'^student/delete/(?P<pk>[-\w]+)/$', Info_DeleteView.as_view(), name='delete'),
    url(r'^student/add/$', Info_FormView.as_view(), name='add'),
    url(r'^student/(?P<student_id>[-\w]+)/marks/$', Marks_MarksView.as_view(), name='marks'),
    url(r'^student/markslist/$', Marks_ListView.as_view(), name='markslist'),
    url(r'^student/displaymarks/(?P<pk>[-\w]+)/$', Marks_DisplayView.as_view(), name='display-marks'),
    url(r'^student/update/(?P<pk>[-\w]+)/$', Marks_UpdateView.as_view(), name='updatemarks'),
    url(r'^student/updatestudent/(?P<pk>[-\w]+)/$', Info_UpdateView.as_view(), name='updatestudent'),
    url (r'contact/$', Home.as_view(),name='home'),
]