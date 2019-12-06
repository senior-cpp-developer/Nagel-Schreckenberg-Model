from model import CarModel
import matplotlib.pyplot as plt

# Config
n = 10 # Amount of model steps
width = 1000
height = 1
acceleration = 1
deceleration = 1
vision_range = 100
speed_limit = 5
randomization = 0.1

all_speeds = []
model = CarModel(n, width, height, acceleration, deceleration, vision_range, randomization, speed_limit)
for i in range(25):
    model.step()

    # Store the results
    total = 0
    for agent in model.schedule.agents:
        total += agent.speed
    all_speeds.append(total/model.num_agents)

print('all_speeds:', all_speeds)
plt.xlabel("Steps")
plt.ylabel("Average speed")
plt.plot(all_speeds)
plt.show()