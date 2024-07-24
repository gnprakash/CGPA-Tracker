from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import User1,Semester1,Semester2,Semester3

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            # Return an error message or handle the case where the username is already taken
            return render(request, 'signup.html', {'error': 'RegisterNo already exists'})

        # Create a new user
        new_user = User.objects.create(username=username, password=make_password(password))
        new_user1 = User1.objects.create(username=username, password=make_password(password))
        # You can set additional attributes of the user here if needed

        # Redirect to a success page or login page
        return redirect('login')  # Assuming you have a URL named 'login'

    return render(request, 'signup.html')


def loginform(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                # Handle invalid credentials with a specific error message
                error_message = 'Invalid Username or Password. Please try again.'
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    user_name = request.user  
    user = User1.objects.get(username=str(request.user))
    semesters = [
        {'number': 1},
        {'number': 2},
        {'number': 3},
        {'number': 4},
        {'number': 5},
        {'number': 6},
        {'number': 7},
        {'number': 8},
    ]
    semester1_data = None
    try:
        semester1_data = Semester1.objects.get(user=user)
    except Semester1.DoesNotExist:
        pass 

    semester2_data = None
    try:
        semester2_data = Semester2.objects.get(user=user)
    except Semester2.DoesNotExist:
        pass 

    semester3_data = None
    try:
        semester3_data = Semester3.objects.get(user=user)
    except Semester3.DoesNotExist:
        pass 

    context = {
        'user_name': user_name,  # Replace with actual user name
        'semesters': semesters,
        "semester1_data":{"semester1_data":semester1_data,"number":1},
        "semester2_data":{"semester2_data":semester2_data,"number":2},
        "semester3_data":{"semester3_data":semester3_data,"number":3},
    }
        # User is logged in, display full home page content
    return render(request, 'index.html', context)


def log_out(request):
    logout(request)
    return redirect('home')

def enter_grades(request, semester_number):
    gpa = None

    s = {1:['Mathamethics-1',"Physics",'Chemistry',"Thermodynamics",'EEE/ECE','Computer Programming','Engineering Graphics ','CP-LAB',"Basic Electrical & Electronics Lab"],
         2:['Mathemathics-2','Material Science','Environmental Science',"Basic Civil/Mechanical Engineering","Engineering Mechanics","Communicative English","Physics lab","Chemistry lab","Workshop Practice"],
        3:["Mathematics-3","Electronics Devices and Circuits","Digital System Design","Data Structures","OOPD","Computer Organization&Architecture","Electrical and Electronics Laboratory ","Digital Laboratory","Data Structures Laboratory"],
         4:["Mathematics-4","OOPS","Microprocessor/Microcontroller","Graphical Image Processing","Design Analysis/Algorithm","Automata Language&Computation","OOPS-Lab","MPMC-Lab","DAA-Lab"],
         5:["Operating System","Computer Networks","DBMS","Language Translator","Software Engineering","OS-Lab","DBMS-Lab","CN-Lab"],
         6:["OOAD","Embedded System","Enterprise Solution","E-Business","Web Technology","WT-Lab","ES-Lab","ERP-Lab"]}
    
    subjects = s.get(semester_number, [])
    user = User1.objects.get(username=str(request.user))

    if request.method == 'POST':
        grades = [float(request.POST.get(f'grade{i}', 0)) for i in range(len(request.POST))]
        credit_hours = [float(request.POST.get(f'creditHour{i}', 0)) for i in range(len(request.POST))]
        
        total_credit_hours = sum(credit_hours)
        weighted_grade_points = sum(grades[i] * credit_hours[i] for i in range(len(grades)))
        
        if total_credit_hours > 0:
            gpa = weighted_grade_points / total_credit_hours
            gpa = round(gpa,2)
            if semester_number == 1:
                semester1, created = Semester1.objects.get_or_create(user=user)
                semester1.subject1 = grades[0]
                semester1.subject2 = grades[1]
                semester1.subject3 = grades[2]
                semester1.subject4 = grades[3]
                semester1.subject5 = grades[4]
                semester1.subject6 = grades[5]
                semester1.subject7 = grades[6]
                semester1.subject8 = grades[7]
                semester1.subject9 = grades[8]
                semester1.gpa = gpa
                semester1.save()
            elif semester_number == 2:
                semester2, created = Semester2.objects.get_or_create(user=user)
                semester2.subject1 = grades[0]
                semester2.subject2 = grades[1]
                semester2.subject3 = grades[2]
                semester2.subject4 = grades[3]
                semester2.subject5 = grades[4]
                semester2.subject6 = grades[5]
                semester2.subject7 = grades[6]
                semester2.subject8 = grades[7]
                semester2.subject9 = grades[8]
                semester2.gpa = gpa
                semester2.save()
            elif semester_number == 3:
                semester3, created = Semester3.objects.get_or_create(user=user)
                semester3.subject1 = grades[0]
                semester3.subject2 = grades[1]
                semester3.subject3 = grades[2]
                semester3.subject4 = grades[3]
                semester3.subject5 = grades[4]
                semester3.subject6 = grades[5]
                semester3.subject7 = grades[6]
                semester3.subject8 = grades[7]
                semester3.subject9 = grades[8]
                semester3.gpa = gpa
                semester3.save()
        else:
            gpa = 0
        
        # Pass GPA and other necessary data to the template
        return render(request, 'gpacal.html', {'gpa': gpa,'subjects':subjects})
    return render(request, 'gpacal.html', {'subjects': subjects,'gpa':gpa})

def fetch_results(request,semester_number):
    user = User1.objects.get(username=str(request.user))
    if semester_number == 1:
        semester1_data = None
        try:
            semester1_data = Semester1.objects.get(user=user)
        except Semester1.DoesNotExist:
            pass 
        return render(request,'index.html',{'semester1_data':semester1_data})
    return render(request,'index.html',{'semester1_data':semester1_data,'number':semester_number})
