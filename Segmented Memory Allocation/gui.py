
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from model import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1064, 799)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/Mike/Documents/My Memory Allocation Using Segmentation\\ram.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("font: 12pt \"Cambria\";\n""color: rgb(50, 50, 50);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.mem_init = QtWidgets.QWidget()
        self.mem_init.setObjectName("mem_init")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.mem_init)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem, 2, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.mem_init)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_mem_size = QtWidgets.QLabel(self.mem_init)
        self.label_mem_size.setObjectName("label_mem_size")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_mem_size)
        self.in_mem_size = QtWidgets.QLineEdit(self.mem_init)
        self.in_mem_size.setObjectName("in_mem_size")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.in_mem_size)
        self.label_num_holes = QtWidgets.QLabel(self.mem_init)
        self.label_num_holes.setObjectName("label_num_holes")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_num_holes)
        self.in_num_holes = QtWidgets.QSpinBox(self.mem_init)
        self.in_num_holes.setObjectName("in_num_holes")
        self.in_num_holes.setAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.in_num_holes)
        self.verticalLayout.addLayout(self.formLayout)
        self.b_create_mem = QtWidgets.QPushButton(self.mem_init)
        self.b_create_mem.setObjectName("b_create_mem")
        self.verticalLayout.addWidget(self.b_create_mem)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.mem_init_table = QtWidgets.QTableWidget(self.mem_init)
        self.mem_init_table.setStyleSheet("")
        self.mem_init_table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mem_init_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.mem_init_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.mem_init_table.setAlternatingRowColors(True)
        self.mem_init_table.setGridStyle(QtCore.Qt.SolidLine)
        self.mem_init_table.setObjectName("mem_init_table")
        self.mem_init_table.setColumnCount(2)
        self.mem_init_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        item.setFont(font)
        self.mem_init_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.mem_init_table.setHorizontalHeaderItem(1, item)
        self.mem_init_table.horizontalHeader().setCascadingSectionResizes(False)
        self.mem_init_table.horizontalHeader().setDefaultSectionSize(200)
        self.mem_init_table.horizontalHeader().setMinimumSectionSize(200)
        self.verticalLayout.addWidget(self.mem_init_table)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.tabWidget.addTab(self.mem_init, "")
        self.mem_view = QtWidgets.QWidget()
        self.mem_view.setObjectName("mem_view")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.mem_view)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.mem_view)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem7)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.mem_view)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.method_dropdown = QtWidgets.QComboBox(self.mem_view)
        self.method_dropdown.setObjectName("method_dropdown")
        self.method_dropdown.addItem("")
        self.method_dropdown.setItemText(0, "")
        self.method_dropdown.addItem("")
        self.method_dropdown.addItem("")
        self.method_dropdown.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.method_dropdown)
        self.label_2 = QtWidgets.QLabel(self.mem_view)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.in_num_seg = QtWidgets.QSpinBox(self.mem_view)
        self.in_num_seg.setObjectName("in_num_seg")
        self.in_num_seg.setMinimum(1)
        self.in_num_seg.setAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.in_num_seg)
        self.verticalLayout_5.addLayout(self.formLayout_2)
        self.b_allocate = QtWidgets.QPushButton(self.mem_view)
        self.b_allocate.setObjectName("b_allocate")
        self.verticalLayout_5.addWidget(self.b_allocate)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_5.addItem(spacerItem8)
        self.process_table = QtWidgets.QTableWidget(self.mem_view)
        self.process_table.setAlternatingRowColors(True)
        self.process_table.setObjectName("process_table")
        self.process_table.setColumnCount(2)
        self.process_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.process_table.setHorizontalHeaderItem(1, item)
        self.process_table.horizontalHeader().setDefaultSectionSize(120)
        self.process_table.horizontalHeader().setMinimumSectionSize(120)
        self.verticalLayout_5.addWidget(self.process_table)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_seg_table = QtWidgets.QLabel(self.mem_view)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_seg_table.setFont(font)
        self.label_seg_table.setObjectName("label_seg_table")
        self.verticalLayout_4.addWidget(self.label_seg_table)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem9)
        self.seg_table = QtWidgets.QTableWidget(self.mem_view)
        self.seg_table.setAlternatingRowColors(True)
        self.seg_table.setObjectName("seg_table")
        self.seg_table.setColumnCount(3)
        self.seg_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.seg_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.seg_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.seg_table.setHorizontalHeaderItem(2, item)
        self.seg_table.horizontalHeader().setDefaultSectionSize(100)
        self.seg_table.horizontalHeader().setMinimumSectionSize(100)
        self.verticalLayout_4.addWidget(self.seg_table)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_mem_layout = QtWidgets.QLabel(self.mem_view)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(50)
        self.label_mem_layout.setFont(font)
        self.label_mem_layout.setObjectName("label_mem_layout")
        self.verticalLayout_3.addWidget(self.label_mem_layout)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem10)
        self.graphicsView = QtWidgets.QGraphicsView(self.mem_view)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_3.addWidget(self.graphicsView)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem11, 0, 0, 1, 1)
        self.tabWidget.addTab(self.mem_view, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Attributes

        # Tab 0 Events
        self.in_num_holes.valueChanged.connect(self.mem_init_table_add_row)
        self.b_create_mem.clicked.connect(self.create_memory)

        # Tab 1 Events
        self.in_num_seg.valueChanged.connect(self.process_table_add_row)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Memory Creation"))
        self.label_mem_size.setText(_translate("MainWindow", "Memory Size:"))
        self.label_num_holes.setText(_translate("MainWindow", "Number of Holes:"))
        self.b_create_mem.setText(_translate("MainWindow", "Create Memory"))
        item = self.mem_init_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Base"))
        item = self.mem_init_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mem_init), _translate("MainWindow", "Memory Initialization"))
        self.label_3.setText(_translate("MainWindow", "Process Allocation"))
        self.label.setText(_translate("MainWindow", "Allocation Method"))
        self.method_dropdown.setItemText(1, _translate("MainWindow", "First Fit"))
        self.method_dropdown.setItemText(2, _translate("MainWindow", "Best Fit"))
        self.method_dropdown.setItemText(3, _translate("MainWindow", "Worst Fit"))
        self.label_2.setText(_translate("MainWindow", "Number of Segments"))
        self.b_allocate.setText(_translate("MainWindow", "Allocate"))
        item = self.process_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.process_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Size"))
        self.label_seg_table.setText(_translate("MainWindow", "Segmentation Table"))
        item = self.seg_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.seg_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Base"))
        item = self.seg_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Size"))
        self.label_mem_layout.setText(_translate("MainWindow", "Memory Layout"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mem_view), _translate("MainWindow", "Memory View"))

    # Show Error Message Popup
    def popup(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setWindowIcon(QtGui.QIcon("ram.ico"))
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)

        show_msg = msg.exec_()

    # Update Row Counts
    def mem_init_table_add_row(self):

        # Update Row Count
        self.mem_init_table.setRowCount(self.in_num_holes.value())

        # Center Align Cells
        for row in range(self.mem_init_table.rowCount()):
            for col in range(self.mem_init_table.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.mem_init_table.setItem(row, col, item)

    def process_table_add_row(self):

        # Update Row Count
        self.process_table.setRowCount(self.in_num_seg.value())

        # Center Align Cells
        for row in range(self.process_table.rowCount()):
            for col in range(self.process_table.columnCount()):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.process_table.setItem(row, col, item)

    # Create Memory
    def get_memory_data(self):

        # Memory Size Validation
        mem_size = self.in_mem_size.text()
        if mem_size == "":
            self.popup("Memory Size Error", "Please Enter Memory Size.")
            return

        elif not mem_size.isdigit():
            self.popup("Memory Size Error", "Memory Size must be a positive integer.")
            return

        # Memory Table Validation
        for row in range(self.mem_init_table.rowCount()):
            for col in range(self.mem_init_table.columnCount()):

                cell_text = self.mem_init_table.item(row, col).text()
                if cell_text == "":
                    self.popup("Memory Holes Error", "Please Fill All Table Cells.")
                    return

                elif not cell_text.isdigit():
                    self.popup("Memory Holes Error", "Base and Size must be positive integers.")
                    return

        # Get Data From Table
        mem_size = int(mem_size)
        holes = []
        for row in range(self.mem_init_table.rowCount()):

            hole_base = int(self.mem_init_table.item(row, 0).text())
            hole_size = int(self.mem_init_table.item(row, 1).text())

            if hole_base + hole_size > mem_size:
                self.popup("Memory Holes Error", "Out of Memory Bound.")
                return

            else:
                holes.append(Hole(hole_base, hole_size))

        # Make sure hole segments are separated
        for i in range(len(holes)):
            if i == 0:
                continue
            if holes[i].base <= holes[i - 1].base + holes[i - 1].size:
                self.popup("Memory Holes Error", "Hole Segments Must Be Separated.")
                return

        return mem_size, holes

    def get_memory_segments(self):

        if self.get_memory_data() is None:
            return

        mem_size, mem_holes = self.get_memory_data()
        memory_segments = []
        seg_base = 0

        old_process = Process([], old=True)

        i = 0
        for hole in mem_holes:
            delta = hole.base - seg_base
            if delta > 0:
                memory_segments.append(Segment("Old Segment " + str(i), old_process, seg_base, delta, False))
                seg_base = seg_base + delta
                i += 1

            memory_segments.append(Segment("Hole", None, hole.base, hole.size, True))
            seg_base += hole.size

        delta = mem_size - seg_base
        if delta > 0:
            memory_segments.append(Segment("Old Segment " + str(i), old_process, seg_base, delta, False))

        return memory_segments

    def create_memory(self):

        if self.get_memory_segments() is None:
            return

        memory = Memory(self.get_memory_segments())
        # TAB 1
        self.update_segmentation_table(memory.segments)
        self.tabWidget.setCurrentIndex(1)

    def update_segmentation_table(self, memory_segments):

        row = 0
        for seg in memory_segments:

            self.seg_table.insertRow(row)

            if seg.parent_process is None:
                item = QTableWidgetItem(seg.name)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seg_table.setItem(row, 0, item)
            else:
                item = QTableWidgetItem(f"{seg.name}\n({seg.parent_process.name})")
                f = QtGui.QFont()
                f.setFamily("Cambria")
                f.setPointSize(9)
                item.setFont(f)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.seg_table.setItem(row, 0, item)

            item = QTableWidgetItem(str(seg.base))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.seg_table.setItem(row, 1, item)

            item = QTableWidgetItem(str(seg.size))
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.seg_table.setItem(row, 2, item)
            row += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
