from PyQt5 import QtCore, QtGui, QtWidgets
import navBar

class Ui_Formz(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2181, 957)
        Form.setStyleSheet("")
        
        # Create the main layout for the form
        self.mainLayout = QtWidgets.QHBoxLayout(Form)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)
        
        # 1. Side Navbar
        self.navbar = QtWidgets.QWidget(Form)
        self.navbar.setFixedWidth(200)
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #D2B48C;  /* Gradient from beige to dark brown */
                border-right: 2px solid #F5F5DC;  /* Beige border */
            }
        """)
        self.navLayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navLayout.setContentsMargins(10, 10, 10, 10)
        navBar.navBar(self.navLayout, Form)
        # Add a spacer to push buttons to the top
        self.navLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))
        
        # Add the navbar to the main layout
        self.mainLayout.addWidget(self.navbar)
        
        # 2. Main Content Area
        self.contentArea = QtWidgets.QWidget(Form)
        self.contentArea.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;  /* White background for main content */
            }
        """)
        self.contentLayout = QtWidgets.QVBoxLayout(self.contentArea)
        self.contentLayout.setContentsMargins(10, 10, 10, 10)
        
        # Example content (your existing labels and widgets)
        self.label = QtWidgets.QLabel(self.contentArea)
        self.label.setGeometry(QtCore.QRect(0, -20, 2321, 361))
        self.label.setStyleSheet("background-image: url(./resources/last.png);"
                                 "background-position: center;"
                                 "font-size: 50px; color: #5D4037; font-family: Georgia;"
                                 "text-align: center;"
                                 "padding-top: 100px;"                                 
                                 )
        self.label.setText("ABOUT US")
        self.label.setObjectName("label")
        self.contentLayout.addWidget(self.label)
        
        self.label_2 = QtWidgets.QLabel(self.contentArea)
        self.label_2.setGeometry(QtCore.QRect(0, 340, 2471, 691))
        self.label_2.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #D2B48C,      /* Light brown */
                    stop:1 #A57A5A       /* Dark beige */
                );
                background-repeat: no-repeat;
                background-position: center;
            }
        """)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.contentLayout.addWidget(self.label_2)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(430, 430, 481, 41))
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("""
        QLabel {
            font-size: 15px;       /* Change font size */
            color:  #5D4037;        /* Change text color to gold */
            font-family: Georgia;    /* Set the font family */
        }
    """)
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(430, 470, 491, 16))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("""
        QLabel {
            font-size: 15px;       /* Change font size */
            color:  #5D4037;        /* Change text color to gold */
            font-family: Georgia;    /* Set the font family */
        }
    """)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(430, 500, 501, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("""
        QLabel {
            font-size: 15px;       /* Change font size */
           color:  #5D4037;        /* Change text color to gold */
            font-family: Georgia;    /* Set the font family */
        }
    """)
        self.mainLayout.addWidget(self.contentArea)
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form","Welcome to our platform! We are a team of dedicated professional"))
        self.label_6.setText(_translate("Form", "Our core values include innovation, integrity, and collaboration."))
        self.label_7.setText(_translate("Form",  "Thank you for being a part of our journey!"))
        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formz()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
