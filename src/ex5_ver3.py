# add metric conversions and round them to 2 decimal places

# declare variables
name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # pounds
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# metric conversions
metric_height = height * 2.54
rounded_metric_height = round(metric_height, 2)
metric_weight = weight * 0.453592
rounded_metric_weight = round(metric_weight, 2)

# display info about Zed
print(f"Let's talk about {name}.")
print(f"He's {rounded_metric_height} centimeters tall.")
print(f"He's {rounded_metric_weight} kilograms heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + rounded_metric_height + rounded_metric_weight
print(f"If I add {age}, {rounded_metric_height}, and {rounded_metric_weight} I get {total}.")
