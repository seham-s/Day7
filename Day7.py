import pandas as pd

df = pd.read_csv('C:\Users\seafaneh\OneDrive - Cisco\Desktop\python\Employee_Salaries(1).csv')

# To calculate the average salary of all employees
average_salary = df['Base_Salary'].mean()
print(f"The average salary of all employees is: ${average_salary:.2f}")

# To find the department with the highest average salary
department_avg_salary = df.groupby('Department')['Base_Salary'].mean()
highest_avg_salary_dept = department_avg_salary.idxmax()
highest_avg_salary = department_avg_salary.max()
print(f"The department with the highest average salary is: {highest_avg_salary_dept} with an average salary of: ${highest_avg_salary:.2f}")

# To calculate the average salary of employees based on gender
gender_avg_salary = df.groupby('Gender')['Base_Salary'].mean()
print("The average salary of employees based on gender:")
for gender, avg_salary in gender_avg_salary.items():
    print(f"{gender}: ${avg_salary:.2f}")
