from django.db import models

# Create your models here.


class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    joining_year = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    bonus_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return f"{self.name} ({self.employee_id})"
    
    def calculate_total_annual_salary(self):
        base_salary = self.salary * 12
        bonus_amount = (self.salary * self.bonus_percentage / 100) * 12
        return base_salary + bonus_amount
    
    def get_grade(self):
        total_salary = self.calculate_total_annual_salary()
        
        if total_salary >= 1000000:
            return "Grade A"
        elif total_salary >= 700000:
            return "Grade B"
        elif total_salary >= 500000:
            return "Grade C"
        elif total_salary >= 300000:
            return "Grade D"
        else:
            return "Needs Improvement"