import os
import subprocess
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from screen.home_screen import HomeScreen
from screen.results_screen import ResultsScreen
from screen.about_screen import AboutScreen

class SpeedTestApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ip_addresses = []  
        
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        self.theme_cls.theme_style = "Light"

        # Loads the kv files
        Builder.load_file('screens_kv/about_screen.kv')
        Builder.load_file('screens_kv/results_screen.kv')
        Builder.load_file('screens_kv/home_screen.kv')

        # Loads the screens
        screen_manager = ScreenManager()
        screen_manager.add_widget(HomeScreen(name='home_screen'))
        screen_manager.add_widget(ResultsScreen(name='results_screen'))
        screen_manager.add_widget(AboutScreen(name='about_screen'))

        return screen_manager
    
    def change_screen(self, screen_name):
        """Method to change the current screen."""
        self.root.current = screen_name

    def add_ip(self, ip_address):
        """Method to add an IP address to the list."""
        if ip_address:
            self.ip_addresses.append(ip_address)
            print(f"Added IP address: {ip_address}")
            #Call the method to display the IP in the scrollview
            self.root.get_screen('home_screen').display_ip(ip_address)
        else:
            print("No IP address provided.")
            
    def start_speed_test(self):
        """Method to start the speed test across all IP addresses."""
        for ip in self.ip_addresses:
            results = []
            print(f"Testing speed for {ip}...")
            response = self.ping_ip(ip)
            results.append(f"Ping result for {ip}:\n{response}")
            print(f"Ping result for {ip}: {response}")
        # Pass the results to the ResultsScreen
        results_screen = self.root.get_screen('results_screen')
        results_screen.display_results(results)# Switch to the ResultsScreen
        print("Updated....!!")
        self.change_screen("results_screen")

    def ping_ip(self, ip):
        """Helper method to ping an IP address."""
        try:
            # Use ping command; adjust for different OS if necessary
            ping_response = subprocess.run(["ping", "-c", "4", ip], stdout=subprocess.PIPE, text=True)
            return ping_response.stdout
        except Exception as e:
            return f"Failed to ping {ip}: {str(e)}"

if __name__ == "__main__":
    SpeedTestApp().run()

#Must continue with the design.