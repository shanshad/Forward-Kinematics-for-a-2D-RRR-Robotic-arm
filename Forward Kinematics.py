import numpy as np

t1=int(input("enter your 1st angle in degree : "))
t2=int(input("enter your 2st angle in degree : "))
t3=int(input("enter your 3rd angle in degree : "))
l0=int(input("enter the distance from fixed frame to 0th joint : "))
l1=int(input("enter the distance from first frame to next joint : "))
l3=int(input("enter the distancw from second frame to next joint : "))

h1=np.matrix([[np.cos(np.deg2rad(t1)), np.sin(np.deg2rad(-t1)), l0],[np.sin(np.deg2rad(t1)), np.cos(np.deg2rad(t1)), 0],[0, 0 ,1]])
h2=np.matrix([[np.cos(np.deg2rad(t2)), np.sin(-(np.deg2rad(t2))), l1],[np.sin(np.deg2rad(t2)), np.cos(np.deg2rad(t2)), 0],[0, 0 ,1]])
h3=np.matrix([[np.cos(np.deg2rad(t3)), np.sin(-(np.deg2rad(t3))), l3],[np.sin(np.deg2rad(t3)), np.cos(np.deg2rad(t3)), 0],[0, 0 ,1]])

print(f"Your first transformation matrix = \n {h1} \n")
print(f"Your second transformation matrix = \n {h2} \n")
print(f"Your third transformation matrix = \n {h3} \n")
h=h1*h2*h3
print(f"your final transformation matrix = \n {h} \n")
theta=np.rad2deg(np.arccos(h[0,0]))
x=h[0,2]
y=h[1,2]
print(f"the end effector frame is {theta} degree tilted in anticlock wise direction compared to fixed frame \nand is in ({x},{y}) position compared to base frame ")