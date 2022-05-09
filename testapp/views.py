from django.shortcuts import render,reverse,get_object_or_404	
from testapp.models import Student
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.


def index_view(request):
	return render(request,'testapp/registration.html')



def insert_view(request):
	rollno=request.POST["srno"]
	name=request.POST["sname"]
	dob=request.POST["sdate"]
	marks=request.POST["smark"]
	email=request.POST["semail"]
	contact=request.POST["scontact"]
	address=request.POST["saddr"]
	students=Student(rollno=rollno,name=name,dob=dob,marks=marks,email=email,phonenumber=contact,address=address)
	students.save()
	return HttpResponseRedirect(reverse('fetch'))
	#return redirect('fetch')
	#return render(request,'testapp/tableshow.html')
	#return 



def fetch_all_view(request):
	students=Student.objects.all()
	return render(request,'testapp/tableshow.html',{'students':students})
	#students=Student.objects.all()
	#students=Student.objects.filter(marks__lt=35)
	#students=Student.objects.filter(name__startswith='R')
	#students=Student.objects.all().order_by('marks')
	#students=Student.objects.all().order_by('-marks')
	#return render(request,'testapp/index.html',{'students':students})

def edit_view(request,pk):
	student=get_object_or_404(Student,pk=pk)
	return render(request,'testapp/edit.html',{'student':student})


def editpage_view(request):
	id=request.POST["sid"]
	rollno=request.POST["srno"]
	name=request.POST["sname"]
	dob=request.POST["sdate"]
	marks=request.POST["smark"]
	email=request.POST["semail"]
	contact=request.POST["scontact"]
	address=request.POST["saddr"]
	students=Student(id=id,rollno=rollno,name=name,dob=dob,marks=marks,email=email,phonenumber=contact,address=address)
	students.save()
	return HttpResponseRedirect(reverse('fetch'))
	
def delete_view(request,pk):
	student=get_object_or_404(Student,pk=pk)
	student.delete()
	return HttpResponseRedirect(reverse('fetch'))