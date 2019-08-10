--Data Analysis Questions:

-- QUESTION 1. List the following details of each employee: employee number, last name, first name, gender, and salary.
	
SELECT employees.emp_no, employees.last_name, employees.first_name, employees.gender, salaries.salary
	FROM employees
	JOIN salaries ON employees.emp_no=salaries.emp_no;

-- QUESTION 2. List employees who were hired in 1986.

SELECT * FROM employees
	WHERE hire_date >= '1986-01-01' AND <= '1986-01-01'; 

-- QUESTION 3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT departments.dept_no, departments.dept_name, dept_manager.emp_no, employees.last_name, employees.first_name, dept_manager.from_date, dept_manager.to_date
	FROM departments
	JOIN dept_manager ON departments.dept_no=dept_manager.dept_no
	INNER JOIN employees ON dept_manager.emp_no=employees.emp_no;

-- QUESTION 4. List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
	FROM dept_emp
	JOIN employees ON dept_emp.emp_no=employees.emp_no
	JOIN departments ON dept_emp.dept_no=departments.dept_no;

-- QUESTION 5. List all employees whose first name is "Hercules" and last names begin with "B."

SELECT first_name, last_name
	FROM employees
	WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

-- QUESTION 6. List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
	FROM dept_emp
	JOIN employees ON dept_emp.emp_no=employees.emp_no
	JOIN departments ON dept_emp.dept_no=departments.dept_no
	WHERE dept_name LIKE 'Sales';

-- QUESTION 7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT employees.emp_no, employees.last_name, employees.first_name, departments.dept_name
	FROM dept_emp
	JOIN employees ON dept_emp.emp_no=employees.emp_no
	JOIN departments ON dept_emp.dept_no=departments.dept_no
	WHERE dept_name LIKE 'Sales' OR dept_name LIKE 'Development'

-- QUESTION 8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.

SELECT last_name, COUNT(*)
	FROM employees 
	GROUP BY last_name
	ORDER BY COUNT DESC;

