from django.urls import path
from lms.views import index,about,blog,contact,event,cart,checkout,detail,onended,allcourses,mycourses,CourseDetail,enrol
from authentication.views import profile

app_name = 'lms'

urlpatterns = [
    path('',index,name = 'index'),
    path('about/',about,name = 'about'),
    path('course/<slug:slug>/',CourseDetail.as_view(),name = 'coursedetail'),
    path('allcourses/',allcourses,name = 'allcourses'),
    path('mycourses/',mycourses,name = 'mycourses'),
    path('blog/',blog,name = 'blog'),
    path('contact/',contact,name = 'contact'),
    path('event/',event,name = 'event'),
    path('cart/',cart,name = 'cart'),
    path('checkout/<slug:slug>/',checkout,name = 'checkout'),
    path('detail/<slug:slug>/',detail.as_view(),name = 'detail'),
    path('ajax/onended/',onended,name = 'onended'),
    path('ajax/staus/',enrol,name = 'status'),
]