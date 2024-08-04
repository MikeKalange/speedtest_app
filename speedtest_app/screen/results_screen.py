from kivymd.uix.screen import MDScreen
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.label import MDLabel

class ResultsScreen(MDScreen):
    
    def display_results(self, results):
        """Method to display the results in the ScrollView."""
        self.ids.results_list.clear_widgets()  # Clear existing results
        for result in results:
            self.ids.results_list.add_widget(MDLabel(text=result, size_hint_y=None, height=40))
    
    def on_pre_enter(self):
        """Load the test results before entering the screen."""
        self.load_results()

    def load_results(self):
        """Loads the test results into the list."""
        results = self.get_test_results()

        self.ids.results_list.clear_widgets()
        for result in results:
            # Create a list item for each test result
            list_item = TwoLineListItem(
                text=f"IP/Website: {result['ip']}",
                secondary_text=f"Ping: {result['ping']} ms | Packet Loss: {result['packet_loss']}%"
            )
            self.ids.results_list.add_widget(list_item)

    def get_test_results(self):
        """Fetch test results. This method should be replaced with actual data fetching."""
        # Placeholder data. Replace with real test results.
        return [
            {"ip": "192.168.1.1", "ping": 20, "packet_loss": 0},
            {"ip": "8.8.8.8", "ping": 15, "packet_loss": 0},
            {"ip": "example.com", "ping": 30, "packet_loss": 2},
        ]

    def save_results(self):
        """Save the test results to a file."""
        # Implement logic to save the results to a file
        print("Saving results...")

    def share_results(self):
        """Share the test results."""
        # Implement logic to share the results
        print("Sharing results...")
