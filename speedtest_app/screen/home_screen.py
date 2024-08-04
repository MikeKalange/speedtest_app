from kivymd.uix.screen import MDScreen
from kivymd.uix.list import OneLineListItem

class HomeScreen(MDScreen):
    def add_ip(self, ip):
        """Add the entered Ip or website to the list."""
        if ip:
            #Create a new list item with the IP/Website
            list_item = OneLineListItem(text=ip, on_release=lambda x: self.remove_ip(x))
            #Add the list item to the MDList in the scrollview
            self.ids.ip_list.add_widget(list_item)
            #Clear the input field
            self.ids.ip_input.text = ""
            
    def remove_ip(self, list_item):
        """"Remove the selected IP or wesite from the list"""
        self.ids.ip_list.remove_widget(list_item)
        
    def start_speed_test(self):
        """Start the speed test n the list of IPs/Websites."""
        ips = [item.text for item in self.ids.ip_list.children]
        if ips:
            print("Starting speed test for the follwing IPs/Websites:")
            for ip in ips:
                print(f"- {ip}")
                #Must implement speed test logic here
                
        else:
            print("No IPs or Websites to test.")
            
    def display_ip(self, ip_address):
        if ip_address:
            self.ids.ip_list.add_widget(OneLineListItem(text=ip_address))
            
    def open_settings_screen(self):
        self.manager.current = "settings_screen"
        
    def change_screen(self, screen_name):
        self.manager.current = screen_name
        print(f"{screen_name}")
        
    def to_next(self):
        self.manager.current = "results_screen"