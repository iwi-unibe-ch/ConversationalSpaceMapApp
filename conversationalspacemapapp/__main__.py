import conversationalspacemapapp.App.TogaApp.app as togaApp
import conversationalspacemapapp.App.QtApp.app as QtApp

def main(toga=True):
    if toga:
        togaApp.main().main_loop()
    else:
        import sys
        from PyQt6.QtWidgets import QApplication
        app = QApplication(sys.argv)
        window = QtApp.main()
        window.show()
        sys.exit(app.exec())

if __name__ == "__main__":
    main()

