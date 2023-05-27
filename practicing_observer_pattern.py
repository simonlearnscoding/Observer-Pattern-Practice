Eventmanager

class WeatherStation:
  __init__():
    self.subscribers = {
      "good_weather" : [],
      "bad_weather" : [],
    }
  def update_weather(self, weather_type, degrees):
    for agent in self.subscribers[topic]:
      agent.notify(weather_type, degrees):
  
  def notify(self, weather_type, degrees):
     
Weather_Station_Houston = WeatherStation()    

class WeatherApp(Weather_Station_Houston):
   __init__(interests):

    for interest in interests:
       Weather_Station_Houston.(interest, self)
     
class NewsChannel:
class Farmer:



