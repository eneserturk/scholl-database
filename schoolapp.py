from dbmanager import DbManager
import datetime
from student import Student

class App:
    def __init__(self):
        self.db = DbManager() # () koymazsak self parametresi eksik hatası veriyor ve çalışmıyor UNUTMA!!!!!! ()

    def initApp(self):
        msg="*******\n1-Öğrenci Listesi\n2-Öğrenci Ekle\n3-Öğrenci Güncelle\n4-Öğrenci Sil\n5-Öğretmen Ekle\n6-Sınıflara Göre Dersler\n7-Çıkış(E/Ç)"
        while True:
            print(msg)
            islem = input("Seçiminiz Nedir: ")

            if islem == "1":
                self.displayStudents()
            elif islem == "2":
                self.addStudent()
            elif islem == "3":
                self.editStudent()
            elif islem == "4":
                self.deleteStudent()
            elif islem == "5":
                pass
            elif islem == "6":
                pass
            elif islem == "E" or islem == "Ç" :
                break
            else:
                print("Yanlış Seçim...")

    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id: "))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input("Öğrenci Id: "))

        student = self.db.getStudentById(studentid)

        student[0].name = input("Adı: ") or student[0].name # giriş yapmazsa önceki kayılı olan değer yüklensin diye bu şekilde yazdık
        student[0].surname = input("Soyadı: ") or student[0].surname
        student[0].gender = input("Cinsiyet (E/K) : ") or student[0].gender
        student[0].classid = int(input("Sınıf Id : ")) or student[0].classid

        year = input("Yıl : ") or student[0].birthdate.year
        month = input("Ay : ") or student[0].birthdate.month
        day = input("Gün : ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)

        self.db.editStudent(student[0])

    def addStudent(self):
        self.displayClasses()
        classid = int(input("hangi sınıf: "))
        number = int(input("Öğrenci Numarası: "))
        name = input("Öğrenci Adı: ")
        surname = input("Öğrenci Soyadı: ")
        year = int(input("Doğum yılı: "))
        month = int(input("Ay: "))
        day = int(input("Gün: "))
        birthdate = datetime.date(year=year,month=month,day=day)
        gender = input("Cinsiyet(E/K): ")
        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)


    def displayClasses(self):
        clss = self.db.getClasses() # sınıflar bununla gelecek
        for i in clss:
            print(f"{i.id} : {i.name}")

    def displayStudents(self):
        self.displayClasses()
        classid = int(input("hangi sınıf: ")) # tüm sınıfların listesini gösterip oradan seçmesini isteyeceğiz
        students = self.db.getStudentByClassId(classid)
        print("Öğrenci Listesi")
        for std in students: # öğrencileri sıralı biçimde göstermek için index numaralarını da aldık bu şekilde
            print(f"{std.id}--{std.name} {std.surname}")
        return classid


app = App()
app.initApp()




