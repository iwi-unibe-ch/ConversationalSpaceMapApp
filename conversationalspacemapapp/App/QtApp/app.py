import PyQt6.QtWidgets

class ConversationalSpaceMapAppQt(PyQt6.QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Initialize tab screen
        self.tabs = PyQt6.QtWidgets.QTabWidget()
        self.tab1 = PyQt6.QtWidgets.QWidget()
        self.tab2 = PyQt6.QtWidgets.QWidget()
        self.tab3 = PyQt6.QtWidgets.QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Geeks")
        self.tabs.addTab(self.tab2, "For")
        self.tabs.addTab(self.tab3, "Geeks")

        # Add tabs to widget
        self.setCentralWidget(self.tabs)



def main():
    return ConversationalSpaceMapAppQt()