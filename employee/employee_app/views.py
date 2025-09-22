from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def index(request):
    return render(request,'index.html')

def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_app:employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'create_employee.html', {'form': form})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    total_annual_salary = employee.calculate_total_annual_salary()
    grade = employee.get_grade()
    
    context = {
        'employee': employee,
        'total_annual_salary': total_annual_salary,
        'grade': grade,
    }
    return render(request, 'employee_detail.html', context)

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employee_app:employee_detail', employee_id=employee.employee_id)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update_employee.html', {'form': form, 'employee': employee})

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, employee_id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_app:employee_list')
    return render(request, 'delete_employee.html', {'employee': employee})

def search_employee(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        try:
            employee = Employee.objects.get(employee_id=employee_id)
            return redirect('employee_app:employee_detail', employee_id=employee.employee_id)
        except Employee.DoesNotExist:
            return render(request, 'search_employee.html', {'error': 'Employee not found'})
    return render(request, 'search_employee.html')

def debug_urls(request):
    from django.urls import get_resolver
    url_conf = get_resolver()
    patterns = []
    
    for pattern in url_conf.url_patterns:
        patterns.append(str(pattern))
    
    return render(request, 'debug_urls.html', {'patterns': patterns})