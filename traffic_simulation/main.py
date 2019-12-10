from model import CarModel
import matplotlib.pyplot as plt

# Config
n = 1000  # Amount of model steps
car_count = 20  # Amount of cars in model
height = 1
acceleration = 1
speed_limit = 5
randomization = 0.25

vision_range = speed_limit*2
width = n*car_count+vision_range+1

all_speeds = []
all_tracked_agent_speeds = []
model = CarModel(car_count, width, height, acceleration, vision_range, randomization, speed_limit)
for i in range(n):
    model.step()

    # Store the results
    total = 0
    tracked_agent_total = 0
    for agent in model.schedule.agents:
        total += agent.speed
        if agent.unique_id==5:
            tracked_agent_total+=agent.speed
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
