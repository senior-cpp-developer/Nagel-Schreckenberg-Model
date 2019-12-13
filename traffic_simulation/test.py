from model import CarModel
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Config
n = 1000  # Amount of model steps
width = 500  # Road size
acceleration = 1
randomization = 0.005

traffic_occupations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25, 50]  # Car counts
speed_limits = [5, 8, 10, 13]

results_speed = []
results_delay = []
for num, cars in enumerate(traffic_occupations, start=0):
    print("Running: " + str(cars) + " cars..")
    results_speed.append([])
    results_delay.append([])
    settings = []
    for x in speed_limits:
        settings.append([cars, 100, 1, acceleration, max(speed_limits) * 3, randomization, x])

    for num_setting, setting in enumerate(settings, start=0):
        results_speed[num].append([])
        results_delay[num].append([])
        all_delay = []
        all_speeds = []
        model = CarModel(*setting)
        for i in range(n):
            model.step()

            # Store the results
            total = 0
            for agent in model.schedule.agents:
                total += agent.speed
            ave_speed = total / model.num_agents
            all_delay.append(abs(setting[6] - ave_speed))
            all_speeds.append(ave_speed)
        results_speed[num][num_setting] = np.mean(all_speeds)
        results_delay[num][num_setting] = np.mean(all_delay)
		# plt.plot(all_speeds, label="Snelheidslimiet: "+str(setting[6]))

def plot_line(x_data, y_data, y_label):
	plt.plot(x_data, y_data)
	plt.xticks(x_data)
	plt.title("Effect van wegbezetting en snelheidslimiet op verkeersflow")
	plt.xlabel("Weg bezetting (%)")
	plt.ylabel(y_label)
	# plt.xlim(0, len(traffic_occupations))
	labels = []
	for x in settings:
		labels.append("Snelheidslimiet: " + str(x[6]))
	plt.legend(labels)
	plt.grid()
	plt.show()

plot_line(traffic_occupations, results_delay, "Gemiddelde vertraging")
plot_line(traffic_occupations, results_speed, "Gemiddelde snelheid")