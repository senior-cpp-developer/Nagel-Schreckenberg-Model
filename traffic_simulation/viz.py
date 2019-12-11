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

model_par_dict =  {"n":10, "car_count":20, "height":10,"acceleration":1,"speed_limit":5, "randomization":0.1}

server = ModularServer(CarModel, [grid], "Car Model", model_par_dict)
server.port = 8521 # The default
server.launch()