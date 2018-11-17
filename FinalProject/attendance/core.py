class CoreAttendanceData():

    def __init__(self, binusianID, name, login):
        self.binusianID =binusianID
        self.name = name
        self.login = login

    def getBinusianID(self):
        return self.binusianID

    def getName(self):
        return self.name

    def getLogin(self):
        return self.login
