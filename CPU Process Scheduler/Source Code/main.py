

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QTableWidgetItem
from PyQt5.QtGui import QBrush, QPen
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("color: rgb(85, 85, 255);\n""font: 25 10pt \"Calibri Light\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(5)
        self.table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        self.gridLayout_2.addWidget(self.table, 7, 0, 1, 1)
        self.label_gantt_chart = QtWidgets.QLabel(self.centralwidget)
        self.label_gantt_chart.setStyleSheet("font: 75 12pt \"Calibri\";\n""color: rgb(0, 85, 127);")
        self.label_gantt_chart.setObjectName("label_gantt_chart")
        self.gridLayout_2.addWidget(self.label_gantt_chart, 11, 0, 1, 2, QtCore.Qt.AlignHCenter)
        self.label_processes_data = QtWidgets.QLabel(self.centralwidget)
        self.label_processes_data.setStyleSheet("font: 75 12pt \"Calibri\";\n""color: rgb(0, 85, 127);")
        self.label_processes_data.setObjectName("label_processes_data")
        self.gridLayout_2.addWidget(self.label_processes_data, 2, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.chart_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.chart_view.setObjectName("chart_view")
        self.gridLayout_2.addWidget(self.chart_view, 15, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_avg_waiting_time = QtWidgets.QLabel(self.centralwidget)
        self.label_avg_waiting_time.setObjectName("label_avg_waiting_time")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_avg_waiting_time)
        self.label_avg_turnaround_time = QtWidgets.QLabel(self.centralwidget)
        self.label_avg_turnaround_time.setObjectName("label_avg_turnaround_time")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_avg_turnaround_time)
        self.avg_waiting_label = QtWidgets.QLabel(self.centralwidget)
        self.avg_waiting_label.setText("")
        self.avg_waiting_label.setObjectName("avg_waiting_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.avg_waiting_label)
        self.avg_turnaround_label = QtWidgets.QLabel(self.centralwidget)
        self.avg_turnaround_label.setText("")
        self.avg_turnaround_label.setObjectName("avg_turnaround_label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.avg_turnaround_label)
        self.gridLayout_2.addLayout(self.formLayout, 6, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_desired_algorithm = QtWidgets.QLabel(self.centralwidget)
        self.label_desired_algorithm.setObjectName("label_desired_algorithm")
        self.horizontalLayout_2.addWidget(self.label_desired_algorithm, 0, QtCore.Qt.AlignRight)
        self.algorithm_dropdown = QtWidgets.QComboBox(self.centralwidget)
        self.algorithm_dropdown.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.algorithm_dropdown.setObjectName("algorithm_dropdown")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.setItemText(0, "")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.addItem("")
        self.algorithm_dropdown.addItem("")
        self.horizontalLayout_2.addWidget(self.algorithm_dropdown)
        self.label_time_quantum = QtWidgets.QLabel(self.centralwidget)
        self.label_time_quantum.setObjectName("label_time_quantum")
        self.horizontalLayout_2.addWidget(self.label_time_quantum, 0, QtCore.Qt.AlignRight)
        self.tq_in = QtWidgets.QLineEdit(self.centralwidget)
        self.tq_in.setObjectName("tq_in")
        self.horizontalLayout_2.addWidget(self.tq_in, 0, QtCore.Qt.AlignLeft)
        self.simulate_b = QtWidgets.QPushButton(self.centralwidget)
        self.simulate_b.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.simulate_b.setObjectName("simulate_b")
        self.horizontalLayout_2.addWidget(self.simulate_b)
        self.clear_b = QtWidgets.QPushButton(self.centralwidget)
        self.clear_b.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.clear_b.setObjectName("clear_b")
        self.horizontalLayout_2.addWidget(self.clear_b)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 13, 0, 2, 2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 8, 0, 1, 2)
        self.label_scheduling_stats = QtWidgets.QLabel(self.centralwidget)
        self.label_scheduling_stats.setStyleSheet("font: 75 12pt \"Calibri\";\n""color: rgb(0, 85, 127);")
        self.label_scheduling_stats.setObjectName("label_scheduling_stats")
        self.gridLayout_2.addWidget(self.label_scheduling_stats, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.add_b = QtWidgets.QPushButton(self.centralwidget)
        self.add_b.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.add_b.setObjectName("add_b")
        self.horizontalLayout_3.addWidget(self.add_b)
        self.remove_b = QtWidgets.QPushButton(self.centralwidget)
        self.remove_b.setStyleSheet("background-color: rgb(247, 248, 255);")
        self.remove_b.setObjectName("remove_b")
        self.horizontalLayout_3.addWidget(self.remove_b)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)
        self.stats_table = QtWidgets.QTableWidget(self.centralwidget)
        self.stats_table.setObjectName("stats_table")
        self.stats_table.setColumnCount(4)
        self.stats_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.stats_table.setHorizontalHeaderItem(3, item)
        self.gridLayout_2.addWidget(self.stats_table, 7, 1, 1, 1)
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setStyleSheet("font: 75 16pt \"Calibri\";\n""text-decoration: underline;\n""color: rgb(0, 85, 127);")
        self.title_label.setObjectName("title_label")
        self.gridLayout_2.addWidget(self.title_label, 0, 0, 1, 2, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 12, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 3, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Attributes
        self.row = 0
        self.processes_list = []
        self.chart = []
        self.clear_flag = False
        self.comboBox = []

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Buttons Connections
        self.add_b.clicked.connect(lambda: self.add_clicked())
        self.remove_b.clicked.connect(lambda: self.remove_clicked())
        self.simulate_b.clicked.connect(lambda: self.simulate_clicked())
        self.clear_b.clicked.connect(lambda: self.clear_clicked())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Color"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Burst Time"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Priority"))
        self.label_gantt_chart.setText(_translate("MainWindow", "GANTT Chart"))
        self.label_processes_data.setText(_translate("MainWindow", "Processes Data"))
        self.label_avg_waiting_time.setText(_translate("MainWindow", "Average Waiting Time:"))
        self.label_avg_turnaround_time.setText(_translate("MainWindow", "Average Turnaround Time:"))
        self.label_desired_algorithm.setText(_translate("MainWindow", "Desired Scheduling Algorithm"))
        self.algorithm_dropdown.setItemText(1, _translate("MainWindow", "First Come, First Served"))
        self.algorithm_dropdown.setItemText(2, _translate("MainWindow", "Shortest Job First                     (Non Preemptive)"))
        self.algorithm_dropdown.setItemText(3, _translate("MainWindow", "Shortest Job First                     (Preemptive)"))
        self.algorithm_dropdown.setItemText(4, _translate("MainWindow", "Priority                                      (Non Preemptive)"))
        self.algorithm_dropdown.setItemText(5, _translate("MainWindow", "Priority                                      (Preemptive)"))
        self.algorithm_dropdown.setItemText(6, _translate("MainWindow", "Round Robin"))
        self.label_time_quantum.setText(_translate("MainWindow", "RR Time Quantum"))
        self.simulate_b.setStatusTip(_translate("MainWindow", "Simulates CPU Scheduling and View GANTT Chart"))
        self.simulate_b.setText(_translate("MainWindow", "Simulate"))
        self.clear_b.setStatusTip(_translate("MainWindow", "Clears Application"))
        self.clear_b.setText(_translate("MainWindow", "Clear"))
        self.label_scheduling_stats.setText(_translate("MainWindow", "Scheduling Statistics"))
        self.add_b.setStatusTip(_translate("MainWindow", "Adds a Process Entry to the Table"))
        self.add_b.setText(_translate("MainWindow", "Add Process"))
        self.remove_b.setStatusTip(_translate("MainWindow", "Removes a Process Entry from the Table"))
        self.remove_b.setText(_translate("MainWindow", "Remove Process"))
        item = self.stats_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.stats_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Finish Time"))
        item = self.stats_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Turnaround Time"))
        item = self.stats_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Waiting Time"))
        self.title_label.setText(_translate("MainWindow", "CPU Scheduler"))

    # UI Functionality
    def get_departure_time(self, pid):
        for index in range(len(self.chart) - 1, -1, -1):
            if self.chart[index] == "Idle":
                continue
            elif self.chart[index].pid == pid:
                return index + 1

    def get_arrival_time(self, pid):
        for process in self.processes_list:
            if process.pid == pid:
                return process.arrival_time

    def get_burst_time(self, pid):
        for index in range(len(self.pids)):
            if self.pids[index] == pid:
                return self.burst_times[index]

    def get_turnaround_time(self, pid):
        return self.get_departure_time(pid) - self.get_arrival_time(pid)

    def get_waiting_time(self, pid):
        return self.get_turnaround_time(pid) - self.get_burst_time(pid)

    # Populate Stats Table
    def display_stats(self):

        # Clear Table
        for r in range(self.stats_table.rowCount()):
            self.stats_table.removeRow(0)

        # Average Waiting/Turnaround Time
        total_waiting_time = 0
        total_turnaround_time = 0

        for process_row in range(len(self.processes_list)):
            self.stats_table.insertRow(process_row)
            pid = self.processes_list[process_row].pid
            finish_time = str(self.get_departure_time(pid))
            waiting_time = str(self.get_waiting_time(pid))
            total_waiting_time += int(waiting_time)
            turnaround_time = str(self.get_turnaround_time(pid))
            total_turnaround_time += int(turnaround_time)

            item = QTableWidgetItem(pid)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stats_table.setItem(process_row, 0, item)

            item = QTableWidgetItem(finish_time)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stats_table.setItem(process_row, 1, item)

            item = QTableWidgetItem(turnaround_time)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stats_table.setItem(process_row, 2, item)

            item = QTableWidgetItem(waiting_time)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.stats_table.setItem(process_row, 3, item)

        self.avg_waiting_label.setText(str(round(total_waiting_time / len(self.processes_list), 3)))
        self.avg_turnaround_label.setText(str(round(total_turnaround_time / len(self.processes_list), 3)))
        self.processes_list = []

    # Draw Gantt Chart
    def draw_chart(self):

        self.clear_flag = True

        # Scene
        pen = QPen(Qt.lightGray)
        red_brush = QBrush(Qt.darkRed, Qt.SolidPattern)
        blue_brush = QBrush(Qt.darkBlue, Qt.SolidPattern)
        pink_brush = QBrush(Qt.darkMagenta, Qt.SolidPattern)
        green_brush = QBrush(Qt.darkGreen, Qt.SolidPattern)
        yellow_brush = QBrush(Qt.darkYellow, Qt.SolidPattern)
        cyan_brush = QBrush(Qt.darkCyan, Qt.SolidPattern)
        grey_brush = QBrush(Qt.darkGray, Qt.SolidPattern)
        black_brush = QBrush(Qt.black, Qt.SolidPattern)
        white_brush = QBrush(Qt.white, Qt.SolidPattern)

        self.scene = QGraphicsScene()

        rect_x = 0
        for process in self.chart:
            if process == "Idle":
                self.scene.addRect(rect_x, -50, 20, 100, pen, white_brush)
            elif process.color == "red":
                self.scene.addRect(rect_x, -50, 20, 100, pen, red_brush)
            elif process.color == "blue":
                self.scene.addRect(rect_x, -50, 20, 100, pen, blue_brush)
            elif process.color == "pink":
                self.scene.addRect(rect_x, -50, 20, 100, pen, pink_brush)
            elif process.color == "green":
                self.scene.addRect(rect_x, -50, 20, 100, pen, green_brush)
            elif process.color == "yellow":
                self.scene.addRect(rect_x, -50, 20, 100, pen, yellow_brush)
            elif process.color == "cyan":
                self.scene.addRect(rect_x, -50, 20, 100, pen, cyan_brush)
            elif process.color == "grey":
                self.scene.addRect(rect_x, -50, 20, 100, pen, grey_brush)
            elif process.color == "black":
                self.scene.addRect(rect_x, -50, 20, 100, pen, black_brush)

            # Time axis labels
            text_item = QtWidgets.QGraphicsTextItem(str(int((rect_x + 20) / 20)))
            text_item.setPos(rect_x + 12, 50)
            self.scene.addItem(text_item)

            rect_x += 20

        # Show Scene
        self.chart_view = QGraphicsView(self.scene, self.chart_view)
        self.gridLayout_2.addWidget(self.chart_view, 15, 0, 1, 2)
        #self.chart_view.setGeometry(QtCore.QRect(0, 0, 1000, 700))
        self.chart_view.show()

    # Show Error Message Popup
    def popup(self, title, text):

        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)

        show_msg = msg.exec_()

    # Clear Button is Clicked
    def clear_clicked(self):

        self.stats_table.setRowCount(0)
        self.avg_turnaround_label.clear()
        self.avg_waiting_label.clear()

        if self.clear_flag:
            self.scene.clear()
            self.clear_flag = False

    # Add Button is Clicked
    def add_clicked(self):
        # Add table row
        self.table.insertRow(self.row)

        # Center Alignment
        for col in range(5):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.table.setItem(self.row, col, item)

        # Create Drop-down menu for colors
        self.comboBox.append(QtWidgets.QComboBox())
        self.comboBox[self.row].addItem("")
        self.comboBox[self.row].addItem("black")
        self.comboBox[self.row].addItem("grey")
        self.comboBox[self.row].addItem("blue")
        self.comboBox[self.row].addItem("cyan")
        self.comboBox[self.row].addItem("red")
        self.comboBox[self.row].addItem("pink")
        self.comboBox[self.row].addItem("green")
        self.comboBox[self.row].addItem("yellow")
        self.table.setCellWidget(self.row, 1, self.comboBox[self.row])

        self.row += 1

    # Remove Button is Clicked
    def remove_clicked(self):
        # Remove table row
        if self.row > 0:
            self.row -= 1
            self.table.removeRow(self.row)
            self.comboBox.pop(self.row)

    # Simulate Button is Clicked
    def simulate_clicked(self):

        # Error Checking
        # Check if at least 1 process is provided
        if self.row == 0:
            self.popup("Process Selection", "Please Provide at least one Process.")
            return

        # Check that all mandatory table cells are provided
        # Also checks for data validation
        for row in range(self.table.rowCount()):
            for col in range(4):
                # Check if color cell
                if col == 1:
                    if self.comboBox[row].currentText() != "":
                        continue
                    else:
                        # Error Message
                        self.popup("Invalid Input", "Please Fill All Essential Table Entries.")
                        return

                # Empty Cells
                elif self.table.item(row, col).text() == "":
                    # Error Message
                    self.popup("Invalid Input", "Please Fill All Essential Table Entries.")
                    return

                # Invalid Input
                elif not self.table.item(row, col).text().isdigit():
                    # Error Message
                    self.popup("Invalid Input", "Table cells only accept numeric values.")
                    return

            if not self.table.item(row, 4).text().isdigit() and self.table.item(row, 4).text() != "":
                # Error Message
                self.popup("Invalid Input", "Table cells only accept numeric values.")
                return

        # Take data from table
        self.processes_list = []
        for row in range(self.table.rowCount()):
            pid = self.table.item(row, 0).text()
            color = self.comboBox[row].currentText()
            arrival = int(self.table.item(row, 2).text())
            burst = int(self.table.item(row, 3).text())
            if self.table.item(row, 4).text() != "":
                priority = int(self.table.item(row, 4).text())
            else:
                priority = 0
            self.processes_list.append(Process(pid, color, arrival, burst, priority))

        # Get the desired algorithm
        selected_algorithm = self.algorithm_dropdown.currentText()

        # Populate one list with pids and another with corresponding burst times
        self.pids = []
        self.burst_times = []
        for process in self.processes_list:
            self.pids.append(process.pid)
            self.burst_times.append(process.burst_time)

        # First Come, First Served
        if selected_algorithm == "First Come, First Served":
            self.chart = CPU_SCHEDULER.first_come_first_served(self.processes_list)

        # Shortest Job First (Non)
        elif selected_algorithm == "Shortest Job First                     (Non Preemptive)":
            self.chart = CPU_SCHEDULER.shortest_job_first(self.processes_list, preemptive=0)

        # Shortest Job First (Pre)
        elif selected_algorithm == "Shortest Job First                     (Preemptive)":
            self.chart = CPU_SCHEDULER.shortest_job_first(self.processes_list, preemptive=1)

        # Priority (Non)
        elif selected_algorithm == "Priority                                      (Non Preemptive)":
            # Priority fields check
            for row in range(self.table.rowCount()):
                if self.table.item(row, 4).text() == "":
                    # Error Message
                    self.popup("Invalid Input", "Please Fill Priority Cells.")
                    return

            self.chart = CPU_SCHEDULER.priority(self.processes_list, preemptive=0)

        # Priority (Pre)
        elif selected_algorithm == "Priority                                      (Preemptive)":
            # Priority fields check
            for row in range(self.table.rowCount()):
                if self.table.item(row, 4).text() == "":
                    # Error Message
                    self.popup("Invalid Input", "Please Fill Priority Cells.")
                    return

            self.chart = CPU_SCHEDULER.priority(self.processes_list, preemptive=1)

        # Round Robin
        elif selected_algorithm == "Round Robin":
            if self.tq_in.text() == "":
                self.popup("Time Quantum Selection", "Please Specify the Desired Time Quantum.")
                return
            else:
                self.chart = CPU_SCHEDULER.round_robin(int(self.tq_in.text()), self.processes_list)

        # No Algorithm is checked
        else:
            self.popup("Algorithm Selection", "Please Select the Desired Algorithm.")
            return

        self.display_stats()
        self.draw_chart()


###################################################################################################


class Process(object):
    def __init__(self, pid, color, arrival_time, burst_time, priority=0):
        self.pid = pid
        self.color = color
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority


class Scheduler(object):
    def __init__(self):
        self.chart = []

    def circular_shift_left(self, queue):
        temp = queue[0]
        for i in range(len(queue) - 1):
            queue[i] = queue[i + 1]
        queue[len(queue) - 1] = temp
        return queue

    def first_come_first_served(self, processes_list):

        # Sort processes_list by arrival time
        processes_list.sort(key=lambda x: (x.arrival_time, x.priority, x.burst_time))

        # Gantt Chart to return
        self.chart = []

        # Time variable
        time = 0

        # Waiting Queue
        queue = []

        total_processes_num = len(processes_list)
        arrived_processes_num = 0
        ready_processes_num = 0
        finished_processes_num = 0

        while finished_processes_num < total_processes_num:
            for i in range(arrived_processes_num, total_processes_num):

                # If process arrived, append it to the waiting/ready queue
                if time >= processes_list[i].arrival_time:
                    queue.append(processes_list[i])
                    arrived_processes_num += 1
                    ready_processes_num += 1

            # If no processes arrived
            if ready_processes_num < 1:
                time += 1
                self.chart.append("Idle")
                continue

            # Run process till it's finished
            if queue[0].burst_time > 0:
                for g in range(queue[0].burst_time):
                    self.chart.append(queue[0])

                time += queue[0].burst_time
                queue.pop(0)
                finished_processes_num += 1
                ready_processes_num -= 1
        return self.chart

    def round_robin(self, time_quantum, processes_list):

        # Sort processes_list by arrival time
        processes_list.sort(key=lambda x: (x.arrival_time, x.priority, x.burst_time))

        # Gantt Chart to return
        self.chart = []

        # Time variable
        time = 0

        # Waiting Queue
        queue = []

        # Total number of processes
        total_processes_num = len(processes_list)

        # Number of arrived processes
        arrived_processes_num = 0

        # Number of ready processes
        ready_processes_num = 0

        # Number of finished processes
        done_processes_num = 0

        # Initial flag
        start_flag = 1

        while done_processes_num < total_processes_num:

            # Check processes_list for arrived processes
            for i in range(arrived_processes_num, total_processes_num):
                if time >= processes_list[i].arrival_time:
                    queue.append(processes_list[i])
                    arrived_processes_num += 1
                    ready_processes_num += 1

            # Check if Queue is Empty
            if ready_processes_num < 1:
                self.chart.append("Idle")
                time += 1
                continue

            # Circular Shift
            if not start_flag:
                queue = self.circular_shift_left(queue)

            # Check if first process is not finished
            if queue[0].burst_time > 0:

                # Process needs the full time quantum
                if queue[0].burst_time > time_quantum:
                    for g in range(time, time + time_quantum):
                        self.chart.append(queue[0])
                    time += time_quantum
                    queue[0].burst_time -= time_quantum

                # Process won't need the full time quantum to finish
                else:
                    for g in range(time, time + queue[0].burst_time):
                        self.chart.append(queue[0])
                    time += queue[0].burst_time
                    queue[0].burst_time = 0

                    done_processes_num += 1
                    ready_processes_num -= 1

                start_flag = 0

        return self.chart

    def shortest_job_first(self, processes_list, preemptive=0):

        # Sort processes_list by arrival time
        processes_list.sort(key=lambda x: (x.arrival_time, x.priority, x.burst_time))

        # Gantt Chart to return
        self.chart = []

        # Time variable
        time = 0

        # Waiting Queue
        queue = []

        total_processes_num = len(processes_list)
        arrived_processes_num = 0
        ready_processes_num = 0
        finished_processes_num = 0

        # Non-preemptive Algorithm
        if not preemptive:
            while finished_processes_num < total_processes_num:
                for i in range(arrived_processes_num, total_processes_num):

                    # If process arrived, append it to the waiting/ready queue
                    if time >= processes_list[i].arrival_time:
                        queue.append(processes_list[i])
                        arrived_processes_num += 1
                        ready_processes_num += 1

                # If no processes arrived
                if ready_processes_num < 1:
                    time += 1
                    self.chart.append("Idle")
                    continue

                # Sort queue by burst time
                queue.sort(key=lambda x: (x.burst_time, x.arrival_time))

                # Run process till it's finished
                if queue[0].burst_time > 0:
                    for g in range(queue[0].burst_time):
                        self.chart.append(queue[0])

                    time += queue[0].burst_time
                    queue.pop(0)
                    finished_processes_num += 1
                    ready_processes_num -= 1
            return self.chart

        # Preemptive Algorithm
        else:
            while finished_processes_num < total_processes_num:
                for i in range(arrived_processes_num, total_processes_num):

                    # If process arrived, append it to the waiting/ready queue
                    if time >= processes_list[i].arrival_time:
                        queue.append(processes_list[i])
                        arrived_processes_num += 1
                        ready_processes_num += 1

                # If no processes arrived
                if ready_processes_num < 1:
                    time += 1
                    self.chart.append("Idle")
                    continue

                # Sort queue by burst time
                queue.sort(key=lambda x: (x.burst_time, x.arrival_time))

                # Run process till it's finished
                if queue[0].burst_time > 0:
                    self.chart.append(queue[0])
                    time += 1
                    queue[0].burst_time -= 1
                    if queue[0].burst_time < 1:
                        queue.pop(0)
                        finished_processes_num += 1
                        ready_processes_num -= 1
            return self.chart

    def priority(self, processes_list, preemptive=0):

        # Sort processes_list by arrival time
        processes_list.sort(key=lambda x: (x.arrival_time, x.priority, x.burst_time))

        # Gantt Chart to return
        self.chart = []

        # Time variable
        time = 0

        # Waiting Queue
        queue = []

        total_processes_num = len(processes_list)
        arrived_processes_num = 0
        ready_processes_num = 0
        finished_processes_num = 0

        # Non-preemptive Algorithm
        if not preemptive:
            while finished_processes_num < total_processes_num:
                for i in range(arrived_processes_num, total_processes_num):

                    # If process arrived, append it to the waiting/ready queue
                    if time >= processes_list[i].arrival_time:
                        queue.append(processes_list[i])
                        arrived_processes_num += 1
                        ready_processes_num += 1

                # If no processes arrived
                if ready_processes_num < 1:
                    time += 1
                    self.chart.append("Idle")
                    continue

                # Sort queue by burst time
                queue.sort(key=lambda x: (x.priority, x.arrival_time))

                # Run process till it's finished
                if queue[0].burst_time > 0:
                    for g in range(queue[0].burst_time):
                        self.chart.append(queue[0])

                    time += queue[0].burst_time
                    queue.pop(0)
                    finished_processes_num += 1
                    ready_processes_num -= 1
            return self.chart

        # Preemptive Algorithm
        else:
            while finished_processes_num < total_processes_num:
                for i in range(arrived_processes_num, total_processes_num):

                    # If process arrived, append it to the waiting/ready queue
                    if time >= processes_list[i].arrival_time:
                        queue.append(processes_list[i])
                        arrived_processes_num += 1
                        ready_processes_num += 1

                # If no processes arrived
                if ready_processes_num < 1:
                    time += 1
                    self.chart.append("Idle")
                    continue

                # Sort queue by burst time
                queue.sort(key=lambda x: (x.priority, x.arrival_time))

                # Run process till it's finished
                if queue[0].burst_time > 0:
                    self.chart.append(queue[0])
                    time += 1
                    queue[0].burst_time -= 1
                    if queue[0].burst_time < 1:
                        queue.pop(0)
                        finished_processes_num += 1
                        ready_processes_num -= 1
            return self.chart


##################################################################################################


CPU_SCHEDULER = Scheduler()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
