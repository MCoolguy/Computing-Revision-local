import flask
from flask import request, render_template
import sqlite3

def departments():
    conn = sqlite3.connect("schools.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Department FROM staff ORDER BY Department ASC")
    rows = cur.fetchall()
    department = []
    for row in rows:
        department.append(row[0])
    conn.close()
    return department

def schools():
    conn = sqlite3.connect("schools.db")
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT Name FROM schools ORDER BY Name ASC")
    rows = cur.fetchall()
    schools = []
    for row in rows:
        schools.append(row[0])
    conn.close()
    return schools

def search_html(school, department):
    connection = sqlite3.connect("schools.db")
    sql_statement = """
                    SELECT schools.Name, staff.Name, staff.Department, staff.Contact, schools.Address
                    FROM schools, staff
                    WHERE staff.SchoolCode = schools.SchoolCode AND schools.Name LIKE ? AND staff.Department LIKE ?
                    """

    cur = connection.cursor()
    cur.execute(sql_statement,('%'+school+'%',department))
    rows = cur.fetchall()
    results = []
    for row in rows:
        results.append(row)
    print(results)
    return results
    
school = schools()
department = departments()
print(department)
