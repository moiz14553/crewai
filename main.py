from crewai.flow import Flow, listen, start
import random

class RoutFlow(Flow):

    @start
    def greeting(self):
        print("Assalamu Alaikum!")

    @listen("greeting")  # Corrected decorator
    def select_city(self):
        cities = ["Karachi", "Lahore", "Islamabad"]
        selected_city = random.choice(cities)
        print(f"Selected city: {selected_city}")

def kickoff():
    obj = RoutFlow()
    obj.run()  # Changed to .run() instead of .kickoff()

def plot():
    obj = RoutFlow()
    obj.run()  # Assuming .run() is the correct method

if __name__ == "__main__":
    kickoff()  # Start the flow
