from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from model import CarModel

def agent_portrayal(agent):
    """Holds the parameters for how the agents are displayed"""
    
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.6}
    return portrayal

#Creates grid to be displayed
grid = CanvasGrid(agent_portrayal, 125, 1, 800, 100)

n = 1000  # Amount of model steps
car_count = 20  # Amount of cars in model
height = 1
acceleration = 1
speed_limit = 5
randomization = 0.25
vision_range = speed_limit*2
width = n*car_count+vision_range+1

model_par_dict =  {"car_count":car_count, "width":width, "height":height, "acceleration":acceleration,
                  "vision_range":vision_range ,"speed_limit":speed_limit, "randomization":randomization}

server = ModularServer(CarModel, [grid], "Car Model", model_par_dict)
server.port = 8521 # The default
server.launch()