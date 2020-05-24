from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from multiprocessing import Process
import time
import sys

hour_conversion_ratio = 1
run = True

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()

        self.createTopGroupBox()
        self.createLeftGroupBox()
        self.createRightGroupBox()
        self.createBottomGroupBox()
        self.createDetailsGroupBox()

        mainLayout = QGridLayout()
        mainLayout.addWidget(self.TopGroupBox, 1, 0, 1, 2)
        mainLayout.addWidget(self.LeftGroupBox, 2, 0, 1, 1)
        mainLayout.addWidget(self.RightGroupBox, 2, 1, 1, 1)
        mainLayout.addWidget(self.BottomGroupBox, 3, 0, 1, 2)
        mainLayout.addWidget(self.DetailsGroupBox, 1, 2, 3, 1)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("The Future of Traffic Control")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()

    def changePalette(self):
        QApplication.setPalette(QApplication.style().standardPalette())

    def createTopGroupBox(self):
        self.TopGroupBox = QGroupBox("North Traffic Signal (Road 1)")

        densitytext = QLabel('Traffic Density: ')

        self.slider = QSlider(Qt.Horizontal, self.TopGroupBox)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(50)
        self.slider.sliderReleased.connect(self.valuechange)

        heightLabel = QLabel()

        holidayComboBox = QComboBox()
        holidayComboBox.addItems(["No Holiday", "Increases Traffic", "Decreases Traffic"])

        holidayLabel = QLabel("Holiday Type: ")
        holidayLabel.setBuddy(holidayComboBox)

        emergencyComboBox = QComboBox()
        emergencyComboBox.addItems(["No", "Yes"])

        emergencyLabel = QLabel("Emergency Vehicle at Nearest Signal: ")
        emergencyLabel.setBuddy(emergencyComboBox)

        signalLabel = QLabel("Signal Color: ")
        colorLabel = QLabel("Red")
        colorLabel.setStyleSheet("color: red")
        signalLabel.setBuddy(colorLabel)

        layout = QGridLayout()
        layout.addWidget(densitytext, 0, 0)
        layout.addWidget(self.slider, 0, 1)
        layout.addWidget(heightLabel, 1, 0)
        layout.addWidget(holidayLabel, 2, 0)
        layout.addWidget(holidayComboBox, 2, 1)
        layout.addWidget(heightLabel, 1, 1)
        layout.addWidget(heightLabel, 1, 2)
        layout.addWidget(emergencyLabel, 0, 3)
        layout.addWidget(emergencyComboBox, 0, 4)
        layout.addWidget(signalLabel, 2, 3)
        layout.addWidget(colorLabel, 2, 4)
        self.TopGroupBox.setLayout(layout)

    def createLeftGroupBox(self):
        self.LeftGroupBox = QGroupBox("West Traffic Signal (Road 4)")

        densitytext = QLabel('Traffic Density: ')

        self.slider = QSlider(Qt.Horizontal, self.LeftGroupBox)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(50)
        self.slider.sliderReleased.connect(self.valuechange)

        heightLabel = QLabel()

        holidayComboBox = QComboBox()
        holidayComboBox.addItems(["No Holiday", "Increases Traffic", "Decreases Traffic"])

        holidayLabel = QLabel("Holiday Type: ")
        holidayLabel.setBuddy(holidayComboBox)

        emergencyComboBox = QComboBox()
        emergencyComboBox.addItems(["No", "Yes"])

        emergencyLabel = QLabel("Emergency Vehicle at Nearest Signal: ")
        emergencyLabel.setBuddy(emergencyComboBox)

        signalLabel = QLabel("Signal Color: ")
        colorLabel = QLabel("Red")
        colorLabel.setStyleSheet("color: red")
        signalLabel.setBuddy(colorLabel)

        layout = QGridLayout()
        layout.addWidget(densitytext, 0, 0)
        layout.addWidget(self.slider, 0, 1)
        layout.addWidget(heightLabel, 1, 0)
        layout.addWidget(holidayLabel, 2, 0)
        layout.addWidget(holidayComboBox, 2, 1)
        layout.addWidget(heightLabel, 3, 0)
        layout.addWidget(emergencyLabel, 4, 0)
        layout.addWidget(emergencyComboBox, 4, 1)
        layout.addWidget(signalLabel, 5, 0)
        layout.addWidget(colorLabel, 5, 1)
        self.LeftGroupBox.setLayout(layout)

    def createRightGroupBox(self):
        self.RightGroupBox = QGroupBox("East Traffic Signal (Road 2)")

        densitytext = QLabel('Traffic Density: ')

        self.slider = QSlider(Qt.Horizontal, self.RightGroupBox)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(50)
        self.slider.sliderReleased.connect(self.valuechange)

        heightLabel = QLabel()

        holidayComboBox = QComboBox()
        holidayComboBox.addItems(["No Holiday", "Increases Traffic", "Decreases Traffic"])

        holidayLabel = QLabel("Holiday Type: ")
        holidayLabel.setBuddy(holidayComboBox)

        emergencyComboBox = QComboBox()
        emergencyComboBox.addItems(["No", "Yes"])

        emergencyLabel = QLabel("Emergency Vehicle at Nearest Signal: ")
        emergencyLabel.setBuddy(emergencyComboBox)

        signalLabel = QLabel("Signal Color: ")
        colorLabel = QLabel("Red")
        colorLabel.setStyleSheet("color: red")
        signalLabel.setBuddy(colorLabel)

        layout = QGridLayout()
        layout.addWidget(densitytext, 0, 0)
        layout.addWidget(self.slider, 0, 1)
        layout.addWidget(heightLabel, 1, 0)
        layout.addWidget(holidayLabel, 2, 0)
        layout.addWidget(holidayComboBox, 2, 1)
        layout.addWidget(heightLabel, 3, 0)
        layout.addWidget(emergencyLabel, 4, 0)
        layout.addWidget(emergencyComboBox, 4, 1)
        layout.addWidget(signalLabel, 5, 0)
        layout.addWidget(colorLabel, 5, 1)
        self.RightGroupBox.setLayout(layout)

    def createBottomGroupBox(self):
        self.BottomGroupBox = QGroupBox("South Traffic Signal (Road 3)")

        densitytext = QLabel('Traffic Density: ')

        self.slider = QSlider(Qt.Horizontal, self.BottomGroupBox)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setValue(50)
        self.slider.sliderReleased.connect(self.valuechange)

        heightLabel = QLabel()

        holidayComboBox = QComboBox()
        holidayComboBox.addItems(["No Holiday", "Increases Traffic", "Decreases Traffic"])

        holidayLabel = QLabel("Holiday Type: ")
        holidayLabel.setBuddy(holidayComboBox)

        emergencyComboBox = QComboBox()
        emergencyComboBox.addItems(["No", "Yes"])

        emergencyLabel = QLabel("Emergency Vehicle at Nearest Signal: ")
        emergencyLabel.setBuddy(emergencyComboBox)

        signalLabel = QLabel("Signal Color: ")
        colorLabel = QLabel("Red")
        colorLabel.setStyleSheet("color: red")
        signalLabel.setBuddy(colorLabel)

        layout = QGridLayout()
        layout.addWidget(densitytext, 0, 0)
        layout.addWidget(self.slider, 0, 1)
        layout.addWidget(heightLabel, 1, 0)
        layout.addWidget(holidayLabel, 2, 0)
        layout.addWidget(holidayComboBox, 2, 1)
        layout.addWidget(heightLabel, 1, 1)
        layout.addWidget(heightLabel, 1, 2)
        layout.addWidget(emergencyLabel, 0, 3)
        layout.addWidget(emergencyComboBox, 0, 4)
        layout.addWidget(signalLabel, 2, 3)
        layout.addWidget(colorLabel, 2, 4)
        self.BottomGroupBox.setLayout(layout)
    
    def createDetailsGroupBox(self):
        self.DetailsGroupBox = QGroupBox()

        timetext = QLabel('Time: ')
        self.timebox = QLineEdit('')

        datetext = QLabel('Date: ')
        self.datebox = QLineEdit('')

        daytext = QLabel('Day: ')
        self.daybox = QLineEdit('')

        monthtext = QLabel('Month: ')
        self.monthbox = QLineEdit('')

        log = QLabel("Logs")
        textEdit = QTextEdit()
        log.setBuddy(textEdit)
        systemtext = "System Logs"
        textEdit.setText(systemtext) 

        heightLabel = QLabel()

        layout = QGridLayout()
        layout.addWidget(timetext, 1, 0)
        layout.addWidget(self.timebox, 1, 1)
        layout.addWidget(datetext, 2, 0)
        layout.addWidget(self.datebox, 2, 1)
        layout.addWidget(daytext, 3, 0)
        layout.addWidget(self.daybox, 3, 1)
        layout.addWidget(monthtext, 4, 0)
        layout.addWidget(self.monthbox, 4, 1)
        layout.addWidget(heightLabel, 5, 0)
        layout.addWidget(log, 6, 0)
        layout.addWidget(textEdit, 7, 0, 1, 2)
        self.DetailsGroupBox.setLayout(layout)

    def valuechange(self):
        print("Slider Value Changed to ")
        print(self.slider.value())
        #pwm.start(self.slider.value())

    def update_hour(self, hour, date, day, month):
        if (hour == 23):
            hour = 0
            day = self.update_day(day)
            date, month = self.update_date(date, month)
        else:
            hour += 1
        return hour, date, day, month

    def update_date(self, date, month):
        if (date == 30)and(month in [4,6,9,11]):
            date = 1
            month = self.update_month(month)
        elif (date == 31)and(month in [1,3,5,7,8,10,12]):
            date = 1
            month = self.update_month(month)
        elif (date == 28)and(month == 2):
            date = 1
            month = self.update_month(month)
        else:
            date += 1
        return date, month

    def update_day(self, day):
        if (day == 7):
            day = 1
        else:
            day += 1
        return day

    def update_month(self, month):
        if (month == 12):
            month = 1
        else:
            month += 1
        return month

    def mean_hour(self, x1, x2, x3, x4, hour_list):
        x1 = (x1 + hour_list[0]*hour_list[4])/(1+hour_list[4])
        x2 = (x2 + hour_list[1]*hour_list[4])/(1+hour_list[4])
        x3 = (x3 + hour_list[2]*hour_list[4])/(1+hour_list[4])
        x4 = (x4 + hour_list[3]*hour_list[4])/(1+hour_list[4])
        return x1, x2, x3, x4, (hour_list[4]+1)

    def mean_date(self, x1, x2, x3, x4, date_list):
        x1 = (x1 + date_list[0]*date_list[4])/(1+date_list[4])
        x2 = (x2 + date_list[1]*date_list[4])/(1+date_list[4])
        x3 = (x3 + date_list[2]*date_list[4])/(1+date_list[4])
        x4 = (x4 + date_list[3]*date_list[4])/(1+date_list[4])
        return x1, x2, x3, x4, (date_list[4]+1)

    def mean_day(self, x1, x2, x3, x4, day_list):
        x1 = (x1 + day_list[0]*day_list[4])/(1+day_list[4])
        x2 = (x2 + day_list[1]*day_list[4])/(1+day_list[4])
        x3 = (x3 + day_list[2]*day_list[4])/(1+day_list[4])
        x4 = (x4 + day_list[3]*day_list[4])/(1+day_list[4])
        return x1, x2, x3, x4, (day_list[4]+1)

    def mean_month(self, x1, x2, x3, x4, month_list):
        x1 = (x1 + month_list[0]*month_list[4])/(1+month_list[4])
        x2 = (x2 + month_list[1]*month_list[4])/(1+month_list[4])
        x3 = (x3 + month_list[2]*month_list[4])/(1+month_list[4])
        x4 = (x4 + month_list[3]*month_list[4])/(1+month_list[4])
        return x1, x2, x3, x4, (month_list[4]+1)

    def print_time(self, hour, date, day, month):
        #print(f"hour:{hour} date:{date} day:{day} month:{month}")
        hour = str(hour)+":00"
        if(day==1):
            day = "Monday"
        elif(day==2):
            day = "Tuesday"
        elif(day==3):
            day = "Wednesday"
        elif(day==4):
            day = "Thrusday"
        elif(day==5):
            day = "Friday"
        elif(day==6):
            day = "Saturday"
        else:
            day = "Sunday"

        if(month==1):
            month = "January"
        elif(month==2):
            month = "February"
        elif(month==3):
            month = "March"
        elif(month==4):
            month = "April"
        elif(month==5):
            month = "May"
        elif(month==6):
            month = "June"
        elif(month==7):
            month = "July"
        elif(month==8):
            month = "August"
        elif(month==9):
            month = "September"
        elif(month==10):
            month = "October"
        elif(month==11):
            month = "November"
        else:
            month = "December"
        self.timebox.setText(str(hour))
        self.datebox.setText(str(date))
        self.daybox.setText(str(day))
        self.monthbox.setText(str(month))

    def main_working(self):
        global run
        hour = 0
        date = 1
        day = 1
        month = 1
        df_hour = {}
        df_date = {}
        df_day = {}
        df_month = {}
        time.sleep(5)
        while run:
            #if start:
            time.sleep(hour_conversion_ratio)
            self.print_time(hour, date, day, month)
            x1, x2, x3, x4 = 50, 50, 50, 50 #input()
            X = x1 + x2 + x3 + x4
            x1 /= X; x2 /= X; x3 /= X; x4 /= X
            try:
                hour_list = df_hour[hour]
                x1, x2, x3, x4, n = self.mean_hour(x1, x2, x3, x4, hour_list)
                df_hour[hour] = [x1, x2, x3, x4, n]
            except KeyError:
                df_hour[hour] = [x1, x2, x3, x4, 1]

            try:
                date_list = df_date[date]
                x1, x2, x3, x4, n = self.mean_date(x1, x2, x3, x4, date_list)
                df_date[date] = [x1, x2, x3, x4, n]
            except KeyError:
                df_date[date] = [x1, x2, x3, x4, 1]

            try:
                day_list = df_day[day]
                x1, x2, x3, x4, n = self.mean_day(x1, x2, x3, x4, day_list)
                df_day[day] = [x1, x2, x3, x4, n]
            except KeyError:
                df_day[day] = [x1, x2, x3, x4, 1]

            try:
                month_list = df_month[month]
                x1, x2, x3, x4, n = self.mean_month(x1, x2, x3, x4, month_list)
                df_month[month] = [x1, x2, x3, x4, n]
            except KeyError:
                df_month[month] = [x1, x2, x3, x4, 1]
            
            hour, date, day, month = self.update_hour(hour, date, day, month)
            #print(df_day)
            QApplication.processEvents()

def startsimulation():
    global start
    start = True

if __name__ == '__main__':
    appctxt = QApplication([])       # 1. Instantiate ApplicationContext
    #window.setWindowIcon(QIcon('Icon.ico'))
    gallery = WidgetGallery()
    gallery.show()
    gallery.main_working()
    exit_code = appctxt.exec_()      # 2. Invoke appctxt.exec_()
    sys.exit(exit_code)