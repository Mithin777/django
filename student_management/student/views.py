

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def home(request):
    return render(request, 'student/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        Student.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            roll_no=request.POST['roll_no'],
            course=request.POST['course']
        )
        return redirect('student_list')
    return render(request, 'student/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.email = request.POST['email']
        student.roll_no = request.POST['roll_no']
        student.course = request.POST['course']
        student.save()
        return redirect('student_list')
    return render(request, 'student/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('student_list')