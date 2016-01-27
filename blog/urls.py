from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
     url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
"""
it starts with ^ again -- "the beginning"

post/ only means that after the beginning, the URL should contain the word post and /. So far so good.

(?P<pk>[0-9]+) - this part is trickier. It means that Django will take everything that you place here and transfer it to a view as a variable called pk. [0-9] also tells us that it can only be a number, not a letter (so everything between 0 and 9). + means that there needs to be one or more digits there. So something like http://127.0.0.1:8000/post// is not valid, but http://127.0.0.1:8000/post/1234567890/ is perfectly ok!

/ - then we need / again

$ - "the end"!
"""