from os import name
from django.urls import path
from . import views


app_name = 'crime'  # here for namespacing of urls.

urlpatterns = [
    path("", views.Run_Here, name="Run_Here"),
    path("Run_Here", views.Run_Here, name="Run_Here"),
    path("contact", views.contact, name="contact"),
    path("finishh", views.finishh, name="finishh"),
    path("crimemissing", views.crimemissing, name="crimemissing"),
    path("publiccomplaint", views.publiccomplaint, name="publiccomplaint"),
    path("publiccomp", views.publiccomp, name="publiccomp"),
    path("logincheck", views.logincheck, name="logincheck"),
    path("branchlogin", views.branchlogin, name="branchlogin"),
    path("branch", views.branch, name="branch"),
    path("admincheck", views.admincheck, name="admincheck"),
    path("register", views.register, name="register"),
    path("areareg", views.areareg, name="areareg"),
    path("areas", views.areas, name="areas"),
    path("index", views.index, name="index"),
    path("Add_Complaint", views.Add_Complaint, name="Add_Complaint"),
    path("Add_Complaint_public", views.add_complaint_public, name="Add_Complaint_public"),
    path("add_police", views.add_police, name="add_police"),
    path("Complaintstatus", views.Complaintstatus, name="Complaintstatus"),
    path("AddMissing", views.AddMissing, name="AddMissing"),
    path("missingstatus", views.missingstatus, name="missingstatus"),

    path("AddMissing_public", views.AddMissing_public, name="addmissingpublic"),
    path("Addcriminal_public", views. Addcriminal_public, name="addcriminalpublic"),
    


    path("policehome", views.policehome, name="policehome"),
    path("complaint", views.ccomplaint, name="complaint"),
    path("Missing_details", views.Missing_details, name="Missing_details"),
    path("criminalview", views.criminalview, name="criminalview"),
    path("content", views.content, name="content"),
    path("chatpolice", views.chatpolice, name="chatpolice"),
    path("addcriminals", views.addcriminals, name="addcriminals"),
    path("viewcomp", views.viewcomp, name="viewcomp"),
    path("viewcomp2", views.viewcomp2, name="viewcomp2"),
    path("addcrime", views.addcrime, name="addcrime"),
    path("publiccompl", views.publiccompl, name="publiccompl"),
    path("reqdoc", views.reqdoc, name="reqdoc"),
    path("reqdoc2", views.reqdoc2, name="reqdoc2"),
    path("acceptdoc", views.acceptdoc, name="acceptdoc"),
    path("chatpolice2", views.chatpolice2, name="chatpolice2"),
    path("chatreg", views.chatreg, name="chatreg"),
    path("upload", views.upload, name="upload"),
    path("finish", views.finish, name="finish"),


    path('add_complaint',views.add_complaint,name='add_complaint'),

    path('view_my_complaints',views.view_my_complaints,name='view_my_complaints'),
    path('complaint_reply/<int:id>',views.complaint_reply,name='complaint_reply'),

    path('view_all_complaint',views.view_all_complaint,name='view_all_complaint'),

    path('add_feedback',views.add_feedback,name='add_feedback'),
    path('view_feedback',views.view_feedback,name='view_feedback'),

    path('add_news',views.add_news,name='add_news'),
    path('view_news',views.view_news,name='view_news'),
    path('view_news2',views.view_news2,name='view_news2'),
    path('add_fir/<int:id>',views.add_fir,name='add_fir'),

    path('view_fir',views.view_fir,name='view_fir'),

    path('edit_complaint/<int:id>',views.edit_complaint,name='edit_complaint'),



  
]