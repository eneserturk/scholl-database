import mysql.connector
from datetime import datetime
from connection import connection
from student import Student
from teacher import Teacher
from clss import Class


class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        sql = "SELECT * FROM student where id = %s"
        value = (id,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchone()
            print(obj)
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def deleteStudent(self,studentid):
        sql = "DELETE FROM student where id = %s"
        value = (studentid,)
        self.cursor.execute(sql,value)
        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt silindi")
        except mysql.connector.Error as err:
            print("Error: ", err)



    def getClasses(self):
        sql = "SELECT * FROM class"
        self.cursor.execute(sql)
        try:
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj) # yeni tanımlanacak
        except mysql.connector.Error as err:
            print("Error: ", err)


    def getStudentByClassId(self,classid):
        sql = "SELECT * FROM student where classid = %s"
        value = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print("Error: ", err)

    def addorEditStudent(self):
        pass
        # addStudent ile editStudent nurada tek foksiyonda yapaibliriz
        # id bilgisine göre filtreleme yaparak kodları yazabiliriz

    def addStudent(self, student: Student): # student bilgisinin tipini belirtmiş olduk
        sql = "INSERT INTO student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender,student.classid)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt eklendi.")
            print(f"son eklenen kaydın Id Numarası:{self.cursor.lastrowid}")
        except self.cursor.connector.Error as err:
            print("hata: ", err)

    def editStudent(self, student: Student):
        sql = "update student set studentnumber=%s, name=%s,surname=%s,birthdate=%s, gender=%s, classid=%s where id=%s"
        value = (student.studentnumber, student.name, student.surname, student.birthdate, student.gender, student.classid, student.id)
        self.cursor.execute(sql, value)

        try:
            self.connection.commit()
            print(f"{self.cursor.rowcount} tane kayıt güncellendi.")
            print(f"son eklenen kaydın Id Numarası:{self.cursor.lastrowid}")
        except self.cursor.connector.Error as err:
            print("hata: ", err)

    def addTeacher(self, teacher: Teacher):
        pass

    def editTeacher(self, teacher: Teacher):
        pass

    def __del__(self):
        self.connection.close()
        print("db silindi")




# student id ye göre bilgi alınması
# db = DbManager()
# student = db.getStudentById(2)

#classid ye göre bilgi alınması
# db = DbManager()
# student = db.getStudentByClassId(1)
# print(student[0].name) #gelen student bilgieri listede olduğu için ilk index bilgisinin adını aldık
# print(student[1].surname)# ikinci index in soyadını aldık

# öğrenci kaydı ekleme
# db = DbManager()
# birinci yöntem kayıtlardaki öğrenciyi alıp onun üzerinden değişiklik yaparak eklemek
# student = db.getStudentById(2)
# student[0].name = "Salih Asaf"
# student[0].surname="ERTÜRK"
# student[0].studentnumber = "390"
# student[0].gender = "E"
# db.addStudent(student[0])

#öğrenci bilgilerini girerek kayıt yapmak
# ogrenci = Student(None, 391,"Metehan", "....",datetime(year=2018,month=10,day=20),"E",1)# Student class ında id yazdığımız için burada onu belirtmemiz gerekti
# db.addStudent(ogrenci)

#öğrenci id sine göre öğrencinin bilgilerini güncellemek

#diğer id fonksiyonu ile getirdiğimiz bilgileri güncelleme
# db = DbManager()
# student = db.getStudentById(7)
# student[0].surname = "KÖSE"
# db.editStudent(student[0])

# editStudent i kullanarak
# db=DbManager()
# guncelle = (391,"Metehan Emrah", "KOSE",datetime(year=2018,month=10,day=25),"E",2,7 )
# db.editStudent(guncelle)
