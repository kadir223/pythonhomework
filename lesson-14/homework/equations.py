import numpy as np
from PIL import Image

# Task 1: Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

vectorized_conversion = np.vectorize(fahrenheit_to_celsius)
temperatures_f = np.array([32, 68, 100, 212, 77])
temperatures_c = vectorized_conversion(temperatures_f)
print("Temperatures in Celsius:", temperatures_c)

# Task 2: Power function
def power_function(base, exponent):
    return base ** exponent

vectorized_power = np.vectorize(power_function)
bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])
results = vectorized_power(bases, exponents)
print("Power Results:", results)

# Task 3: Solve the system of equations
A = np.array([[4, 5, 6],
              [3, -1, 1],
              [2, 1, -2]])
B = np.array([7, 4, 5])
x = np.linalg.solve(A, B)
print("Solution (x, y, z):", x)

# Task 4: Solve electrical circuit equations
A_circuit = np.array([[10, -2, 3],
                       [-2, 8, -1],
                       [3, -1, 6]])
B_circuit = np.array([12, -5, 15])
currents = np.linalg.solve(A_circuit, B_circuit)
print("Currents (I1, I2, I3):", currents)

# Image Manipulation with NumPy and PIL
def flip_image(image_array):
    return np.flip(image_array, axis=(0, 1))

def add_noise(image_array):
    noise = np.random.randint(0, 50, image_array.shape, dtype=np.uint8)
    return np.clip(image_array + noise, 0, 255)

def brighten_channels(image_array, increase_value=40):
    return np.clip(image_array + increase_value, 0, 255)

def apply_mask(image_array, mask_size=(100, 100)):
    h, w, _ = image_array.shape
    start_h, start_w = (h - mask_size[0]) // 2, (w - mask_size[1]) // 2
    image_array[start_h:start_h + mask_size[0], start_w:start_w + mask_size[1]] = 0
    return image_array

# Load image
image_path = "images/birds.jpg"
image = Image.open(image_path)
image_array = np.array(image)

# Apply transformations
flipped_image = flip_image(image_array)
noisy_image = add_noise(image_array)
brightened_image = brighten_channels(image_array)
masked_image = apply_mask(image_array)

# Save results
Image.fromarray(flipped_image).save("flipped_birds.jpg")
Image.fromarray(noisy_image).save("noisy_birds.jpg")
Image.fromarray(brightened_image).save("brightened_birds.jpg")
Image.fromarray(masked_image).save("masked_birds.jpg")
