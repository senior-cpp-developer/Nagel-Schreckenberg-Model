from mesa import Model, Agent
from mesa.space import MultiGrid
from mesa.time import SimultaneousActivation
import random

class CarAgent(Agent):
	def __init__(self, unique_id, model, acceleration, vision_range, randomization, speed_limit):
		super().__init__(unique_id, model)
		self.acceleration = acceleration
		self.vision_range = vision_range
		self.speed = speed_limit
		self.randomization = randomization
		self.speed_limit = speed_limit
		self.iteration = 0
		self.distance_to_precursor = 0
		self.state = "Cruising"

	def perceive(self):
		""" Checks how far the  """
		self.distance_to_precursor = 0
		for t in range(self.pos[0]+1, self.vision_range):
			tile = (t, 0)
			if self.model.grid.is_cell_empty(tile):
				self.distance_to_precursor += 1
			else:
				break
		if self.distance_to_precursor == 0:
			self.distance_to_precursor = self.vision_range

	def update(self):
		""" Updates the current state """
		ran = random.randrange(0, 100)
		if self.speed > 1 and ran / 100 < self.randomization:
			self.state = "RandomBraking"
		elif self.distance_to_precursor < self.speed and self.speed > 1:
			self.state = "Braking"
		elif self.distance_to_precursor == self.speed and self.speed > 0 or self.speed == self.speed_limit:
			self.state = "Cruising"
		else:
			self.state = "Accelerating"

	def act(self):
		""" Looks at current state and adjust the speed according to the state of the agent."""
		if self.state == "Braking":
			self.speed = self.distance_to_precursor
		if self.state == "RandomBraking":
			self.speed -= self.acceleration
		if self.state == "Accelerating":
			self.speed += self.acceleration

		if self.speed < 1:
			self.speed = 1
		if self.speed > self.speed_limit:
			self.speed = self.speed_limit

	def move(self):
		""" Moves car x tiles forward where x is speed"""
		pos = list(self.pos)
		pos[0] += self.speed
		self.model.grid.move_agent(self, tuple(pos))

	def step(self):
		"""  """
		self.perceive()
		self.update()

	def advance(self):
		self.act()
		self.move()
		self.iteration += 1

class CarModel(Model):
	"""A model with some number of agents."""

	def __init__(self, car_count, width, acceleration, vision_range, randomization, speed_limit):
		self.num_agents = car_count
		self.grid = MultiGrid(width, 1, torus=True)

		self.schedule = SimultaneousActivation(self)
		self.running = True

		# Create agents
		for i in range(car_count):
			a = CarAgent(i, self, acceleration, vision_range, randomization, speed_limit)
			self.schedule.add(a)
			# Add the agent to a random grid cell
			ran = random.randrange(0, width)
			self.grid.place_agent(a, (ran, 0))

	def step(self):
		""" All cars anticipate for next step."""
		self.schedule.step()