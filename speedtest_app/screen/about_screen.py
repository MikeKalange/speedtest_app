from kivymd.uix.screen import MDScreen
import webbrowser

class AboutScreen(MDScreen):
    def open_website(self, url):
        webbrowser.open(url)