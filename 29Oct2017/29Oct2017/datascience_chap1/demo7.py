from collections import defaultdict
salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
        (48000, 0.7), (76000, 6),
        (69000, 6.5), (76000, 7.5),
        (60000, 2.5), (83000, 10),
        (48000, 1.9), (63000, 4.2),
        (65000, 4.2)
                        ]

salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

print(salary_by_tenure)

# keys are years, each value is average salary for that tenure
average_salary_by_tenure = {
    tenure : sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)