from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("signup",views.signup,name="signup"),
    path("login",views.loginuser,name="login"),
    path("logout",views.logoutuser,name="logout"),
    path("auth",views.auth,name="auth"),
    path("",views.home,name=""),
    path("app",views.app,name="app"),
    path("event_info",views.event_info,name="event_info"),
    path("create_form/<int:pk>",views.create_form,name="create_form"),
    path("form/<int:pk>",views.form_render,name="form_render"),
    path("api/form/<int:pk>",views.formapi,name="api/form"),
    path("submit-form/<int:pk>",views.submit_form,name="submit-form"),
    path("api/user/data-integration/end-point/",views.dataItegration,name="api/user/data-integration/end-point/'"),
    path("answer/api/<int:id>",views.AnswerAPI,name="answer/api"),
    path("answer/<int:id>",views.Answer,name="answer"),
    path("answer/api/v2/<int:id>",views.AnswerRender,name="answer/api/v2"),
    path("responses/<int:id>",views.Responses,name="responses"),
    # '''
    # editing is paused:
    # path('api/draft/',views.Draft,name='api/draft'),
    # path('api/get/draft/<int:pk>',views.GetDraft,name='api/get/draft')
    # '''


]
