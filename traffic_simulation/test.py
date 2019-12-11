from model import CarModel
import matplotlib.pyplot as plt
import numpy as np

# Config
n = 2000  # Amount of model steps
width = 100  # Road size
acceleration = 1
speed_limit = 5
randomization = 0.005
vision_range = speed_limit * 3

traffic_occupations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 50]  # Car counts
speed_limits = [5, 8, 10, 13]

results = []
for num, cars in enumerate(traffic_occupations, start=0):
	print("Running: "+str(cars)+" cars..")
	results.append([])
	settings = []
	for x in speed_limits:
		settings.append([cars, 150, 1, acceleration, 30, randomization, x])

	for num_setting, setting in enumerate(settings, start=0):
		results[num].append([])
		all_speeds = []
		model = CarModel(*setting)
		for i in range(n):
			model.step()

			# Store the results
			total = 0
			for agent in model.schedule.agents:
				total += agent.speed
			ave_speed = total/model.num_agents
			all_speeds.append(ave_speed)
		results[num][num_setting] = np.mean(all_speeds)
		# plt.plot(all_speeds, label="Snelheidslimiet: "+str(setting[6]))

plt.plot(traffic_occupations, results)
plt.xticks(traffic_occupations)

plt.title("Effect van wegbezetting en snelheidslimiet op verkeersflow")
plt.xlabel("Weg bezetting (%)")
plt.ylabel("Gemiddelde snelheid")
# plt.xlim(0, len(traffic_occupations))
labels = []
for x in settings:
	labels.append("Snelheidslimiet: "+str(x[6]))
plt.legend(labels)
plt.grid()
plt.show()
