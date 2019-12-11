from model import CarModel
import matplotlib.pyplot as plt
import numpy as np

# Config
n = 100  # Amount of model steps
car_count = 20  # Amount of cars in model
width = 100  # Road size
height = 1
acceleration = 1
speed_limit = 5
randomization = 0.005
vision_range = speed_limit * 3

# traffic_occupations = [5, 10, 15, 20, 50]
traffic_occupations = [5]
results = [[],[],[],[],[]]
for num, cars in enumerate(traffic_occupations, start=0):
	results[num] = []
	# [car_count, width, height, acceleration, vision_range, randomization, speed_limit]
	config_5 = [cars, 150, height, acceleration, 30, randomization, 5]
	config_10 = [cars, 150, height, acceleration, 30, randomization, 10]
	config_13 = [cars, 150, height, acceleration, 30, randomization, 13]

	settings = [config_5, config_10, config_13]

	for setting in settings:
		all_speeds = []
		model = CarModel(*setting)
		for i in range(n):
			model.step()

			# Store the results
			total = 0
			for agent in model.schedule.agents:
				total += agent.speed
			ave_speed = total/model.num_agents
			all_speeds.append(ave_speed-setting[6])
		results[num].append(all_speeds)
		# plt.plot(all_speeds, label="Snelheidslimiet: "+str(setting[6]))

r = np.asarray(results)

for num in range(0, len(traffic_occupations)):
	plt.plot(r.mean(0, num))

plt.xlabel("Steps")
plt.ylabel("Gemiddelde vertraging")
plt.xlim(0, len(traffic_occupations))
plt.legend()
plt.grid()
plt.show()
