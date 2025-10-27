import numpy as np
import math

# rotasi matix 2D
def rotation_matrix(theta):
    return np.array([
        [math.cos(theta), -math.sin(theta), 0],
        [math.sin(theta), math.cos(theta), 0],
        [0, 0, 1]
    ])

# translasi matrix 3D
def translation_matrix(tx, ty):
    return np.array([
        [1, 0, tx],
        [0, 1, ty],
        [0, 0, 1]
    ])

def fungsi(theta1_deg, theta2_deg, l1, l2):
    theta1 = math.radians(theta1_deg)
    theta2 = math.radians(theta2_deg) # konversi radian ke derajat
    
    # perkalian matrix untuk mendapatkan H0, 4
    H1 = rotation_matrix(theta1) 
    H2 = translation_matrix(l1, 0) 
    H3 = rotation_matrix(theta2) 
    H4 = translation_matrix(l2, 0) 

    H_total = H1 @ H2 @ H3 @ H4
    
    titik_akhir = H_total @ np.array([0, 0, 1])
    
    return titik_akhir[0], titik_akhir[1]

# data dari study case:
theta1 = 40
theta2 = 30
l1 = 78
l2 = 19

x, y = fungsi(theta1, theta2, l1, l2)
print(f"FK dengan Matrix")
print(f"Koordinat titik akhir: ({x:.2f}, {y:.2f})")