from django.db import models

# Create your models here.

class Student(models.Model):
    binusianID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.binusianID + " ( "+ self.name +" )"

    def getBinusianID(self):
        return self.binusianID

    def getName(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=100)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Class(models.Model):
    name = models.CharField(max_length=100)
    roomNumber = models.CharField(max_length=100)
    courseID = models.ForeignKey(Course, on_delete=models.CASCADE)

    def getName(self):
        return self.name

    def getRoomNumber(self):
        return self.roomNumber

    def getCourse(self):
        return self.courseID

    def __str__(self):
        return self.name + '-' + self.roomNumber + '-' + self.courseID.name

    class Meta:
        verbose_name_plural = "Classes"

class ClassSchedule(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    classID = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    startTime = models.TimeField()
    endTime = models.TimeField()

    def __str__(self):
        return self.studentID.name + ' # ' + self.classID.name + ' # ' + str(self.date) + ' # ' + str(self.startTime) + ' - ' + str(self.endTime)

    def getStudentID(self):
        return self.studentID

    def getClassID(self):
        return self.classID

    def getDate(self):
        return self.date

    def getStartTime(self):
        return self.startTime

    def getEndTime(self):
        return self.endTime


class AttendanceData(models.Model):
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    classScheduleID = models.ForeignKey(ClassSchedule, on_delete=models.CASCADE)
    loginDate = models.DateField()
    loginTime = models.TimeField()

    def __str__(self):
        return self.classScheduleID.__str__() + '# Login Date : ' + str(self.loginDate) + ' # Login Time : ' + str(self.loginTime)

    def getStudentID(self):
        return self.studentID

    def getClassScheduleID(self):
        return self.classScheduleID

    def getLoginDate(self):
        return self.loginDate

    def getLoginTime(self):
        return self.loginTime