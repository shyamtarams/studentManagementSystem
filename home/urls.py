from django.urls import path,include
from .views import *

urlpatterns = [
    # path('student/', student),
    # path('signup/', signup),
    path('login/', login),
    path('logout/', logout),
    path('adminsite/', adminsite,name="admin site"),
    path('addstudent/', studentRegister,name="studentRegister"),
    path('active/', activeStudent,name="activeStudent"),
    path('inactive/', inactiveStudent,name="inactiveStudent"),
    path('status/<int:id>', studentStatus,name="studentStatus"),
    path('studentDetails/', studentDetails,name="studentDetails"),
    path('updatedetails/', updateStudent,name="updateStudent"),
]