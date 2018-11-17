import cv2
from django.shortcuts import render
from .models import *
# from django.contrib.staticfiles.templatetags.staticfiles import static
from django.core.files import File
from .core import CoreAttendanceData
from django.http import HttpResponse
import datetime as dt


from .detectface import detect

# Create your views here.
def home(request):
    return render(request, 'attendance/homepage.html')

def traindata(request):
    return render(request, 'attendance/traindata.html')


def doattendance(request):

    #read recognition file
    url = 'attendance/temporarydata.txt'

    f = open(url, 'r')

    now = dt.datetime.now()

    listData = []

    #loop per row
    for i in f:
        try:
            data = i.split('#')
            id = data[0]
            # name = data[1]
            date = data[2]
            time = data[3].replace('\n','')

            dateObj = dt.datetime.strptime(date+ ' ' + time, '%Y-%m-%d %H:%M:%S')

            # get current schedule data
            student = Student.objects.get(binusianID=id)

            #check if today the current recognized student has a class schedule or not
            q = ClassSchedule.objects.filter(studentID = student).filter(date = now.date())

            if(q.count() != 0):
                for i in q:
                    if(dateObj >= dt.datetime.combine(i.getDate(),i.getStartTime()) and dateObj <= dt.datetime.combine(i.getDate(),i.getEndTime())):

                        check = AttendanceData.objects.filter(classScheduleID = i)
                        # print("Check : " + str(check))
                        # print("Data : ")
                        # print(data)
                        # print("------------")
                        if(check.count() == 0):
                            obj = AttendanceData.objects.create(studentID = student, classScheduleID = i, loginDate = date, loginTime = time)
                            listData.append(obj)
                        else:
                            if(check[0] not in listData):
                                listData.append(check[0])
            else:
                print("cannot do attendant")
        except:
            print("empty line founded")
            continue

        # obj = CoreAttendanceData(data[0], data[1], data[2])

    # listData.sort(key = lambda x:x.loginDate,reverse = True)
    # data = AttendanceData.objects.all()

    f.close()

    context = {
        'title' : 'hello',
        'data' : listData
    }

    print(context)

    return render(request, 'attendance/doattendance.html', context)

def submit(request):
    binusianId = request.POST['binusianid']
    name = request.POST['name']

    response = detect(binusianId, name)


    # insert new student data to database
    Student.objects.create(name=name, binusianID = binusianId)

    print("Response : " + str(response))

    return render(request, 'attendance/response.html')


def response(request):
    return render(request, 'attendance/response.html')


def dataset(request):

    obj = Student.objects.all()


    context = {
        'data' : obj
    }

    return render(request, 'attendance/dataset.html', context)