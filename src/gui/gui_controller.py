import sys

from PyQt5.QtWidgets import QMainWindow
from gui.lipid_details_screen import LipidDetailsScreen
from gui.file_picker_screen import FilePickerScreen
from gui.input_summary_screen import InputSummaryScreen
from gui.progress_screen import ProgressScreen


class MainApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle("Lipid Inference")
        self.show()
        self.init_lipid_details_screen()

    def init_lipid_details_screen(self):
        self.setCentralWidget(LipidDetailsScreen(on_next=self.init_file_picker_screen))

    def init_file_picker_screen(self):
        self.setCentralWidget(FilePickerScreen(on_back=self.init_lipid_details_screen, on_next=self.init_input_summary_screen))

    def init_input_summary_screen(self):
        self.setCentralWidget(InputSummaryScreen(on_back=self.init_file_picker_screen, on_next=self.init_progress_screen))

    def init_progress_screen(self):
        self.setCentralWidget(ProgressScreen(on_back=self.init_input_summary_screen))