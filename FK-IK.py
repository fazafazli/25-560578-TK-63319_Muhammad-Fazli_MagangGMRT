import math

def forward_kinematics(theta1, theta2, l1, l2):
    theta1_rad = math.radians(theta1)
    theta2_rad = math.radians(theta2)
    
    x = l1 * math.cos(theta1_rad) + l2 * math.cos(theta1_rad + theta2_rad)
    y = l1 * math.sin(theta1_rad) + l2 * math.sin(theta1_rad + theta2_rad)
    
    return x, y

def inverse_kinematics(x, y, l1, l2):
    # hitung theta2
    D = (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2)
    theta2_rad = math.acos(D)
    
    # hitung theta1
    theta1_rad = math.atan2(y, x) - math.atan2(l2 * math.sin(theta2_rad), l1 + l2 * math.cos(theta2_rad))
    
    # konversi ke derajat
    theta1 = math.degrees(theta1_rad)
    theta2 = math.degrees(theta2_rad)
    
    return theta1, theta2

# data dari study case
theta1 = 40
theta2 = 30
l1 = 78
l2 = 19

# Forward Kinematics
x, y = forward_kinematics(theta1, theta2, l1, l2)
print("Forward Kinematics:")
print(f"dengan theta1 = {theta1}°, theta2 = {theta2}°")
print(f"didapat: x = {x:.2f}, y = {y:.2f}")

# Inverse Kinematics
theta1_calc, theta2_calc = inverse_kinematics(x, y, l1, l2)
print("\nInverse Kinematics:")
print(f"dengan x = {x:.2f}, y = {y:.2f}")
print(f"didapat: theta1 = {theta1_calc:.2f}°, theta2 = {theta2_calc:.2f}°")