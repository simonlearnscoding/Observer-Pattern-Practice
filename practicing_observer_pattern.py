
class WeatherStation:
  __init__():
    self.subscribers = {
      "good_weather" : [],
      "bad_weather" : [],
    }
  def update_weather(self, weather_type, degrees):
    for agent in self.subscribers[topic]:
      agent.notify(weather_type, degrees):

 def subscribe(self, weather_type, agent):
    self.subscribers[weather_type].append(agent)

     
Weather_Station_Houston = WeatherStation()    


class parentClass(Weather_Station_Houston):
   __init__(interests):
    for interest in interests:
       Weather_Station_Houston.subscribe(interest, self)
        
    def notify(self, weather_type, degrees):
        print("Weather App: It is {} degrees and {} in Houston".format(degrees, weather_type))

        
class WeatherApp(Weather_Station_Houston):
   __init__(interests):
        super().__init__(interests) 

class NewsChannel:
   __init__(interests):
        super().__init__(interests) 
    
class Farmer:
   __init__(interests):
    
        super().__init__(interests) 
     
# -------------------------


class WeatherStation:
    def __init__(self):
        self.subscribers = {
            "good_weather": [],
            "bad_weather": [],
        }

    def update_weather(self, weather_type, degrees):
        for agent in self.subscribers[weather_type]:
            agent.notify(weather_type, degrees)

    def subscribe(self, weather_type, agent):
        self.subscribers[weather_type].append(agent)


class WeatherObserver:
    def __init__(self, name):
        self.name = name

    def notify(self, weather_type, degrees):
        pass  # This will be overridden by subclasses.


class WeatherApp(WeatherObserver):
    def notify(self, weather_type, degrees):
        print(f"Weather App: It is {degrees} degrees and {weather_type} in Houston")


class NewsChannel(WeatherObserver):
    def notify(self, weather_type, degrees):
        print(f"News Channel: Breaking news! It is {degrees} degrees and {weather_type} in Houston")


class Farmer(WeatherObserver):
    def notify(self, weather_type, degrees):
        if weather_type == "bad_weather":
            print(f"Farmer: It's {weather_type}, better cover the crops!")
        else:
            print(f
