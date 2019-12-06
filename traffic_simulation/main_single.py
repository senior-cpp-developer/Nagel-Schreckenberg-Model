from traffic_simulation.model import CarModel
import matplotlib.pyplot as plt

# Config
n = 5
width = 1000
height = 1
acceleration = 1
deceleration = 1
vision_range = 100
speed_limit = 5
randomization = 0.1

all_speeds = []
model = CarModel(n, width, height, acceleration, deceleration, vision_range, randomization, speed_limit)
for i in range(10):
    model.step()

    # Store the results
    for agent in model.schedule.agents:
        all_speeds.append(agent.speed)

print('all_speeds:',all_speeds)
plt.xlabel("Steps")
plt.ylabel("Average speed")
plt.plot(all_speeds)
plt.show()