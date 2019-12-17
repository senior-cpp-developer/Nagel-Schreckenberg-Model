from model import CarModel
import matplotlib.pyplot as plt

# Config
n = 100  # Amount of model steps
car_count = 20  # Amount of cars in model
width = 100  # Road size
acceleration = 1
speed_limit = 5
randomization = 0.05
vision_range = speed_limit*3

all_speeds = []
all_tracked_agent_speeds = []
model = CarModel(car_count, width, acceleration, vision_range, randomization, speed_limit)
for i in range(n):
    model.step()

    total = 0
    tracked_agent_total = 0
    for agent in model.schedule.agents:
        total += agent.speed
        if agent.unique_id == round(car_count/2):
            tracked_agent_total += agent.speed
    all_speeds.append(total/model.num_agents)
    all_tracked_agent_speeds.append(tracked_agent_total)

print('all_speeds:', all_speeds)
plt.xlabel("Steps")
plt.ylabel("Average speed")
plt.plot(all_tracked_agent_speeds, label="Agent 5 speed")
plt.plot(all_speeds, label="Average speed")
plt.legend()
plt.grid()
plt.show()
