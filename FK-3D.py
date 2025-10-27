import math
import numpy as np

def fungsi(theta1_deg, theta2_deg, theta3_deg, l1, l2, l3, z_height=0):
    # konversi ke radian
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg)
    theta3 = math.radians(theta3_deg)
    
    # matrix transformasi homogen 3D (4x4)
    # rotasi sendi 1 (Z)
    R1 = np.array([
        [math.cos(theta1), -math.sin(theta1), 0, 0],
        [math.sin(theta1),  math.cos(theta1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # translasi l1 (X)
    T1 = np.array([
        [1, 0, 0, l1],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # rotasi sendi 2 (Z)  
    R2 = np.array([
        [math.cos(theta2), -math.sin(theta2), 0, 0],
        [math.sin(theta2),  math.cos(theta2), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # translasi l2 (X)
    T2 = np.array([
        [1, 0, 0, l2],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # rotasi sendi 3 (Z)
    R3 = np.array([
        [math.cos(theta3), -math.sin(theta3), 0, 0],
        [math.sin(theta3),  math.cos(theta3), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # translasi l3 (X)
    T3 = np.array([
        [1, 0, 0, l3],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])
    
    # translasi base height (Z)
    T_base = np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, z_height],
        [0, 0, 0, 1]
    ])
    
    H_total = T_base @ R1 @ T1 @ R2 @ T2 @ R3 @ T3
    
    # titik akhir
    titik_akhir = H_total @ np.array([0, 0, 0, 1])
    
    return titik_akhir[0], titik_akhir[1], titik_akhir[2]

# data dari study case
theta1 = 40
theta2 = 30
theta3 = 25 
l1 = 78
l2 = 19
l3 = 23

# hitung koordinat
x, y, z = fungsi(theta1, theta2, theta3, l1, l2, l3, 18) #misal ketinggian 18 dari titk pusat

print("FK 3D")
print(f"Koordinat titik akhir: ({x:.2f}, {y:.2f}, {z:.2f})")