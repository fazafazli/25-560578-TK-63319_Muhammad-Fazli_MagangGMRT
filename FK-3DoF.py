import math

def fungsi(theta1_deg, theta2_deg, theta3_deg, l1, l2, l3):
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg)
    theta3 = math.radians(theta3_deg)
    
    # rumus untuk 3 DoF
    x = (l1 * math.cos(theta1) + 
         l2 * math.cos(theta1 + theta2) + 
         l3 * math.cos(theta1 + theta2 + theta3))

    y = (l1 * math.sin(theta1) + 
         l2 * math.sin(theta1 + theta2) + 
         l3 * math.sin(theta1 + theta2 + theta3))
    
    return x, y

# data dari study case
theta1 = 40
theta2 = 30
theta3 = 25 # misal 25 derajat
l1 = 78
l2 = 19
l3 = 23 # misal sepanjang 23 satuan

x, y = fungsi(theta1, theta2, theta3, l1, l2, l3)
print(f"FK 3 DoF")
print(f"Koordinat titik akhir: ({x:.2f}, {y:.2f})")