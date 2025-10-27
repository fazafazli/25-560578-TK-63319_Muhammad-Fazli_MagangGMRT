import math

def fungsi(theta1_deg, theta2_deg, l1, l2):
    # konversi derajat ke radian
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg)
    
    # rumus FK column ke-3
    x = l1 * math.cos(theta1) + l2 * math.cos(theta1 + theta2)
    y = l1 * math.sin(theta1) + l2 * math.sin(theta1 + theta2)
    
    return x, y

# data dari study case
theta1 = 40
theta2 = 30
l1 = 78
l2 = 19

x, y = fungsi(theta1, theta2, l1, l2)
print(f"FK 2 DoF")
print(f"Koordinat titik akhir: ({x:.2f}, {y:.2f})")