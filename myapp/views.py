from django.shortcuts import render,redirect,get_object_or_404

from .models import Student
from .forms import studentform,RegisterForm

from django.contrib import messages


# Create your views here.

def home(request):
	return render(request,'index.html')

def Home(request):
	return render(request,'home.html')

#read
def student_list(request):
	stud = Student.objects.all()

	return render(request,'studentlist.html',{'students':stud}) 

#create
def add_student(request):
	form = studentform(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('studlist')
	return render(request,'add_student.html',{'form':form})

#update
def edit_student(request,pk):
	student = get_object_or_404(Student,pk=pk)
	form = studentform(request.POST or None,instance=student)
	if form.is_valid():
		form.save()
		return redirect('studlist')
	return render(request,'edit_student.html',{'form':form})

#delete
def delete_student(request,pk):
	student = get_object_or_404(Student,pk=pk)
	if request.method == 'POST':
		student.delete()
		return redirect('studlist') 
	return render(request,'delete_student.html',{'student':student})



def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request,"successfully")

			return redirect('login')

	else:
		form = RegisterForm()
	return render(request,'register.html',{'form':form})                                                                                                                           


def reshome(request):
	return render(request,'reshome.html')