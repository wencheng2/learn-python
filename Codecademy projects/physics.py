# physics.py
# Getting Ready for Physics Class exercise from Codecademy

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below: 

# Define function to convert Fahrenheit to Celcius
def f_to_c(f_temp):
  # Use formula = Temp (C) = (Temp (F) - 32) * 5/9
  c_temp = (f_temp - 32) * 5 / 9
  return c_temp

f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

# Define function to convert Celcius to Fahrenheit
def c_to_f(c_temp):
  # Use formala = Temp (F) = Temp (C) * (9/5) + 32
  f_temp = c_temp * 9 / 5 + 32
  return f_temp

c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)

# Define function to find values of force
def get_force(mass, acceleration):
  force = mass * acceleration
  return force

train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force")

# Define function that finds value energy where the constant c is the speed of light
def get_energy(mass, c = 3 * 10 ** 8):
  energy = mass * c ** 2
  return energy

bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules")

# Define function that finds value of work where work = force x distance
def get_work(mass, acceleration, distance):
  work = get_force(mass, acceleration) * distance
  return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")