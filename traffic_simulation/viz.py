from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import CarModel

def agent_portrayal(agent):
    """Holds the parameters for how the agents are displayed"""
    
    def calculate_color():
        """Calculates the color for a agent based on the delay they are experiencing"""

        factor_maximum_speed = agent.speed/agent.speed_limit
        
        #Inverts the number so that bigger speed reduction for agents equels a higer number
        color_multiplication = 1 - factor_maximum_speed
        
        #Green == Less delay Red == More delay
        green = int(255 - (color_multiplication * 200))
        red = int(1 + color_multiplication * 200)

        return '#{:02x}{:02x}{:02x}'.format(red, green,0)

    color = calculate_color()
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Color": color,
                 "Layer": 0,
                 "r": 0.6}
    
    return portrayal


#Standard starting values
width = 150 # Road size
height = 1  # Amount of lanes
acceleration = 1
randomization = 0.1
vision_range = 100

#Creates grid to be displayed
grid = CanvasGrid(agent_portrayal, 180, 1, 900, 100)

#Values for vizualisation
model_par_dict =  {"car_count": UserSettableParameter("number", "Car count", 50),
                  "width":width, "height":height,
                  "acceleration":UserSettableParameter("number", "acceleration", 1),
                  "vision_range":vision_range ,"speed_limit": UserSettableParameter("number", "max speed", 10),
                  "randomization":randomization}

server = ModularServer(CarModel, [grid], "Car Model", model_par_dict)
server.port = 8521 # The default
server.launch()