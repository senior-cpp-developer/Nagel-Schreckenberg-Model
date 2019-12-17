from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter
from model import CarModel

def agent_portrayal(agent):
    """Holds the parameters for how the agents are displayed"""

    def calculate_color():
        """Calculates the color for a agent based on the amount they reduced there speed from maximum"""

        factor_maximum_speed = agent.speed / agent.speed_limit

        # Inverts the number so that bigger speed reduction for agents equels a higer number
        color_multiplication = 1 - factor_maximum_speed

        # Green == Less delay Red == More delay
        green = int(255 - (color_multiplication * 250))
        red = int(1 + color_multiplication * 250)

        return '#{:02x}{:02x}{:02x}'.format(red, green, 0)

    color = calculate_color()
    portrayal = {"Shape": "circle",
                 "Filled": "true",
                 "Color": color,
                 "Layer": 0,
                 "r": 0.6}

    return portrayal

def create_vizualization_model():
    """Creates the vizualization model"""
    # Creates grid to be displayed
    grid = CanvasGrid(agent_portrayal, 150, 1, 900, 100)

    # Values for vizualisation
    model_par_dict = {"car_count": UserSettableParameter("number", "Car count", 25),
                    "width": 150, "height": 1,
                    "acceleration": UserSettableParameter("number", "acceleration", 1),
                    "vision_range": UserSettableParameter("number", "vision_range", 100),
                    "speed_limit": UserSettableParameter("number", "max speed", 10),
                    "randomization": UserSettableParameter("number", "randomization", 0.05)}

    server = ModularServer(CarModel, [grid], "Car Model", model_par_dict)
    return server

if __name__ == "__main__":
    server = create_vizualization_model()
    server.port = 8521  # The default
    server.launch()