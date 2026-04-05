import pandas as pd
import numpy as np
# Random employee data  for example:
employees = pd.DataFrame({
    'Name': ['ALi', 'Sarah', 'Malik', 'Laiba', 'Talha'],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR'],
    'Salary': [75000, 65000, 80000, 70000, 68000],
    'Experience': [5, 3, 8, 4, 6]
})

# Filtering IT department form employees
it_employees = employees[employees['Department'] == 'IT']
print("IT Department:")
print(it_employees)

# Filtering high salary which is greater than 70000
high_earners = employees[employees['Salary'] > 70000]
print("\nHigh earners:")
print(high_earners)

# Sorted by salary
sorted_by_salary = employees.sort_values('Salary', ascending=False)
print("\nSorted by salary (highest first):")
print(sorted_by_salary)

# Multiple conditions (IT and salary > 70000)
it_high_earners = employees[(employees['Department'] == 'IT') & (employees['Salary'] > 70000)]
print("\nIT employees with salary > 70000:")
print(it_high_earners)