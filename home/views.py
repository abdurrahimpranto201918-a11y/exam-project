
from django.shortcuts import render, redirect
from .models import Student, Teacher


def home(request):
    return render(request, 'home/index.html')


def student_form(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        roll = request.POST.get('roll', '').strip()
        registration = request.POST.get('registration', '').strip()
        image = request.FILES.get('image')

        errors = []
        if not name:
            errors.append('Name is required.')
        if not email:
            errors.append('Email is required.')
        if not roll:
            errors.append('Roll is required.')
        if not registration:
            errors.append('Registration is required.')

        if errors:
            return render(request, 'home/student_form.html', {'errors': errors})

        Student.objects.create(
            name=name,
            email=email,
            roll=roll,
            registration=registration,
            image=image
        )
        return redirect('student_form')

    return render(request, 'home/student_form.html')


def teacher_form(request):
    if request.method == 'POST':
        name = request.POST.get('name') or None
        email = request.POST.get('email') or None
        image = request.FILES.get('image')

        Teacher.objects.create(
            name=name,
            email=email,
            image=image
        )

        return redirect('teacher_form')

    return render(request, 'home/teacher_form.html')
