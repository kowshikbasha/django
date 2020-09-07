from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    dt=datetime.datetime.now()
    h=int(dt.strftime('%H'))
    msg='Hello Guest'
    if h<12:
        msg=msg+' Good Morning'
    elif h<16:
        msg=msg+' Good Afternoon'
    elif h<21:
         msg=msg+' Good Evening'
    else:
         msg=msg+' Good Night'
    return render(request,'website/index.html',{'msg':msg})
    