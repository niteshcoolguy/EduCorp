from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from .models import *


def register(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']
        email = request.POST['email']
        
        # Check if username already exists
        if createuser.objects.filter(username=Username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        createuser.objects.create(username=Username, password=password, email=email)
        messages.info(request, 'Account created!')
        return redirect('/')
    else:
        return render(request, 'login_registration/registration.html', {})

def user_login(request):
    if request.method == 'POST':
        Username = request.POST['Username']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=Username, password=password)
        
        if user is not None:
            # Log in the user
            login(request, user)
            request.session['type_id'] = 'User'
            request.session['username'] = Username
            request.session['login'] = 'Yes'
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('/')
    else:
        return render(request, 'login_registration/user_login.html', {})

def user_logout(request):
    auth_logout(request)
    return redirect('/')


@login_required(login_url='/')
def home(request):
    query = request.GET.get('q', '')

    # Filter courses based on the search query
    users = course.objects.filter(
        Q(course_name__icontains=query) | Q(course_description__icontains=query)
    ).order_by('-created_date')

    # Set up pagination
    paginator = Paginator(users, 6)  # Show 6 courses per page
    page = request.GET.get('page')
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users, 'query': query}
    return render(request, 'login_registration/home.html', context)

@login_required(login_url='/')
def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        task_content = request.POST.get('task_content', '')

        if course.objects.filter(course_name=title).exists():
            messages.error(request, 'Course already exists.')
            return redirect('home')

        # Create the course object
        course.objects.create(
            course_name=title,
            course_description=task_content
        )
        messages.success(request, 'Your Course is created!')
        return redirect('home')  # Redirect to 'home' after successful creation

    return render(request, 'login_registration/home.html')


@login_required(login_url='/')
def edit_course(request, pk):
    course_instance = course.objects.get(id=pk)
    
    if request.method == 'POST':
        course_instance.course_name = request.POST.get('title')
        course_instance.course_description = request.POST.get('task_content')
        course_instance.save()

        messages.success(request, 'Your Course is Updated Successfully!')
        return redirect('home')
   
    return render(request, 'login_registration/home.html', {'course_instance': course_instance})


@login_required(login_url='/')
def delete_course(request, pk):
    todo = course.objects.get(id=pk)
    if todo:
        todo.delete()
        return redirect('home')
    return render(request, 'login_registration/home.html', {})



@login_required(login_url='/')
def students(request):
    query = request.GET.get('q', '')

    users = student.objects.filter(
        Q(username__icontains=query)
    ).order_by('-created_date')

    courses = course.objects.all()
    
    paginator = Paginator(users, 6) 
    page = request.GET.get('page')
    
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    context = {'users': users, 'query': query, 'courses': courses}
    return render(request, 'login_registration/students.html', context)



@login_required(login_url='/')
def student_create(request):
    if request.method == 'POST':
        usernames = request.POST.get('username')
        surname = request.POST.get('surname')
        emails = request.POST.get('email')
        phone_numbers = request.POST.get('phone_number')
        student_courses = request.POST.get('course')

        student.objects.create(
            username=usernames,
            surname=surname,
            email=emails,
            phone_number=phone_numbers,
            student_course_id=student_courses
        )
        messages.success(request, 'Student is created!')
        return redirect('students')

    courses = course.objects.all()
    return render(request, 'login_registration/students.html', {'courses': courses})


@login_required(login_url='/') 
def update_student(request, pk):
    student_instance = student.objects.get(id=pk)
    
    if request.method == 'POST':
        student_instance.username = request.POST.get('username')
        student_instance.surname = request.POST.get('surname')
        student_instance.email = request.POST.get('email')
        student_instance.phone_number = request.POST.get('phone_number')
        student_instance.student_course_id = request.POST.get('course')
        student_instance.save()
        
        messages.success(request, 'Student is updated!')
        return redirect('students')
    
    courses = course.objects.all()
    return render(request, 'login_registration/students.html', {'student_instance': student_instance, 'courses': courses})


@login_required(login_url='/')
def delete_student(request,pk):
    student_instance = student.objects.get(id=pk)
    if student_instance:
        student_instance.delete()
        messages.success(request, 'Student is deleted!')
        return redirect('students')
    return render(request,'login_registration/students.html')

@login_required(login_url='/')
def student_info(request,pk):
    student_instance = student.objects.get(id=pk)
    # print(student_instance)
    
    return render(request, 'login_registration/student_info.html', {'student_instance': student_instance})


@login_required(login_url='/')
def company_details(request):
    query = request.GET.get('q', '')

    companies = Company.objects.filter(
        Q(company_name__icontains=query)
    ).order_by('-company_created')
    
    paginator = Paginator(companies, 6)
    page = request.GET.get('page')
    
    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        companies = paginator.page(1)
    except EmptyPage:
        companies = paginator.page(paginator.num_pages)

    context = {'companies': companies, 'query': query}
    return render(request, 'login_registration/company.html', context)

@login_required(login_url='/')
def company_create(request):
    if request.method == 'POST':
        company_names = request.POST.get('company_name')
        company_locations = request.POST.get('company_location')
        company_websites = request.POST.get('company_website')
        company_create = request.POST.get('company_create')
        print(f"username: {company_names}, email: {company_locations}, phone_number: {company_websites}, course: {company_create}")

        # if all([usernames, emails, phone_numbers, student_courses]):
        Company.objects.create(
            company_name=company_names,
            company_location=company_locations,
            company_website=company_websites,
            company_created=company_create
        )
        messages.success(request, 'Student is created!')
        return redirect('company')
        # else:
        #     messages.error(request, 'All fields are required.')

    courses = Company.objects.all()
    return render(request, 'login_registration/company.html', {'courses': courses})


@login_required(login_url='/')
def company_update(request, pk):
    # company = get_object_or_404(Company, pk=pk)
    company = Company.objects.get(id=pk)
    
    if request.method == 'POST':
        company.company_name = request.POST.get('company_name')
        company.company_location = request.POST.get('company_location')
        company.company_website = request.POST.get('company_website')
        company.company_created = request.POST.get('company_create')

        company.save()
        messages.success(request, 'Company updated successfully!')
        return redirect('company')
    
    context = {'company': company}
    return render(request, 'login_registration/company.html', context)


@login_required(login_url='/')
def company_delete(request,pk):
    company_remove = Company.objects.get(id=pk)
    if company_remove:
        company_remove.delete()
        messages.success(request,"Compnay is delete")
        return redirect('company')
    
    return render(request,'login_registration/company.html')
    
