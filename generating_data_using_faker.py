import mysql.connector
from faker import Faker


fake = Faker("EN_IN")


db = mysql.connector.connect(
    host='localhost',  
    user="root",  
    password="MrKhan123!",  
    database="Mark",
    auth_plugin='mysql_native_password'
   
)


cursor = db.cursor()
def College_Table():
    for _ in range(1):
        Name ="Maharaja Ranjit Singh College of Professional Sciences"
        Email = "info@mrscps.edu"
        Contact = 9876543210
        Address = "Indore, Madhya Pradesh, India"

        query = "INSERT INTO College (Name,Email,Contact,Address) VALUES (%s, %s, %s, %s)"
        values = (Name, Email, Contact, Address)

        cursor.execute(query, values)
def Department_Table():
    for _ in range(10):  
        ID  = fake.unique.random_int(100,200)
        Name = fake.word().title() + " Department"
        Head = fake.name()
        Email = fake.email()
        Contact = fake.phone_number()
        College_Name = "Maharaja Ranjit Singh College of Professional Sciences"

        query = "INSERT INTO Department (ID,Name,Head,Email,Contact,College_Name) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ID,Name,Head,Email,Contact,College_Name)

        cursor.execute(query, values)
        return ID
def Program_Table():
    for _ in range(10): 
        ID =fake.unique.random_int(201,300)
        Name = fake.word().title()+"Program"
        Degree_Level =fake.random_element(["Bachelor", "Master", "Doctorate"])
        Duration = fake.random_int(min=1,max=6)
        Program_Type = fake.random_element(["Full-Time","Part-Time"])
        Department_ID =Department_Table()

        query = "INSERT INTO Program (ID,Name,Degree_Level,Duration,Program_Type,Department_ID) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (ID,Name,Degree_Level,Duration,Program_Type,Department_ID)

        cursor.execute(query, values)
        return ID
def Faculty_Table():
    for _ in range(10):
        ID = fake.unique.random_int(301,400)
        Name = fake.word().title()+"Faculty"
        Email = fake.email()
        Contact = fake.phone_number()
        Department_ID = Department_Table()
        Address = fake.address()
        Title_Position = fake.random_element(["Professor", "Assistant Professor", "Lecturer", "Associate Professor"])
        Date_Join  = fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
        Experience = fake.random_int(min=1,max=10)
        Qualification = fake.random_element(["Bachelor's", "Master's", "Ph.D.", "M.Tech", "MBA", "MSc", "BSc"])

        query = "INSERT INTO Faculty (ID,Name,Email,Contact,Department_ID,Address, Title_Position,Date_Join,Experience,Qualification) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values = (ID,Name,Email,Contact,Department_ID,Address, Title_Position,Date_Join,Experience,Qualification)

        cursor.execute(query,values)
        return ID
def Semester_Table():
    for _ in range(10):
        ID = fake.unique.random_int(401,500)
        Name = fake.random_element(["Semester 1","Semester 2","Semester 3","Semester 4","Semester 5","Semester 6",])
        Program_ID = Program_Table()
        Start_Date = fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
        End_Date = fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
        query = "INSERT INTO Semester (ID,Name,Program_ID,Start_Date,End_Date) VALUES (%s,%s,%s,%s,%s)"
        values =(ID,Name,Program_ID,Start_Date,End_Date)
        cursor.execute(query,values)
        return ID 
def Course_Table():
    for _ in range(10):
        ID = fake.unique.random_int(501,600)
        Name = fake.random_element(["CS", "MATH", "BIO", "CHEM", "ENG", "PHY", "ECON", "PSY"])
        Course_code = fake.random_element(["QFR623","SXY325","DHK708","TPL132","UVJ942","NYO591","MBG845","KFD329","BRM661","XQJ110"])
        Assessment_Method =fake.random_element([
            "Written Exam", 
            "Practical Exam", 
            "Project", 
            "Assignment", 
            "Group Discussion", 
            "Presentation", 
            "Lab Work", 
            "Quiz", 
            "Research Paper", 
            "Oral Exam"
        ])
        Faculty_ID =Faculty_Table()
        Semester_ID =Semester_Table()

        query = "INSERT INTO Course (ID,Name,Course_code,Assessment_Method,Faculty_ID,Semester_ID ) VALUES (%s,%s,%s,%s,%s,%s)"
        values =(ID,Name,Course_code,Assessment_Method,Faculty_ID,Semester_ID )
        cursor.execute(query,values)
        return ID
def Internal_Table():
    for _ in range(10):
        ID =fake.unique.random_int(601,700)
        Name =fake.random_element([
            "Written Exam", 
            "Practical Exam", 
            "Project", 
            "Assignment", 
            "Group Discussion", 
            "Presentation", 
            "Lab Work", 
            "Quiz", 
            "Research Paper", 
            "Oral Exam"
        ])
        Course_ID = Course_Table()
        Faculty_ID =Faculty_Table()
        Submission_Status = fake.random_element([
            "Submitted",
            "Late",
            "Rejected",
            "Not Submitted",
        ])
        Marks =fake.random_int(1,100)
        Grade =fake.random_element(["A+","A","B","C","Fail"])
        Total_Number =fake.random_int(1,300)
        Assessment_Date =fake.date_between(start_date='-2y', end_date='today').strftime('%Y-%m-%d')
        Assessment_Type =fake.random_element([
            "Midterm Exam",
            "Final Exam",
            "Quiz",
            "Assignment",
            "Project",
            "Presentation",
            "Lab Exam",
            "Research Paper",
            "Oral Exam",
            "Case Study"
        ])
        query = "INSERT INTO Internal (ID,Name,Course_ID,Faculty_ID ,Submission_Status,Marks,Grade,Total_Number,Assessment_Date,Assessment_Type ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        values =(ID,Name,Course_ID,Faculty_ID ,Submission_Status,Marks,Grade,Total_Number,Assessment_Date,Assessment_Type )
        cursor.execute(query,values)
        return ID
def Student_Table():
    for _ in range(10):  
        ID  = fake.unique.random_int(1, 100)
        Name = fake.name()
        DOB = fake.date_of_birth().strftime('%Y-%m-%d')  
        Gender = fake.profile()['sex'] 
        Email = fake.email()
        Contact = fake.phone_number()
        Address = fake.address().replace("\n", ", ")  
        Enroll_Date = fake.date_this_decade().strftime('%Y-%m-%d')  
        Internal_ID = Internal_Table()  
        query = """
        INSERT INTO Student (ID, Name, DOB, Gender, Email, Contact, Address, Enroll_Date, Internal_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (ID, Name, DOB, Gender, Email, Contact, Address, Enroll_Date, Internal_ID)

        cursor.execute(query, values)


College_Table()
Department_Table()
Program_Table()
Semester_Table()
Faculty_Table()
Course_Table()
Internal_Table()
Student_Table()
db.commit()

cursor.close()
db.close()

print("Fake data inserted successfully!")

