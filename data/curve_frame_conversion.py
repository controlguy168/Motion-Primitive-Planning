
import numpy as np
from pandas import *
import sys
from general_robotics_toolbox import *


col_names=['X', 'Y', 'Z','direction_x','direction_y','direction_z'] 
data = read_csv("from_interp/Curve_interp.csv", names=col_names)
curve_x=data['X'].tolist()
curve_y=data['Y'].tolist()
curve_z=data['Z'].tolist()
curve_direction_x=data['direction_x'].tolist()
curve_direction_y=data['direction_y'].tolist()
curve_direction_z=data['direction_z'].tolist()

curve=np.vstack((curve_x, curve_y, curve_z)).T
curve_direction=np.vstack((curve_direction_x, curve_direction_y, curve_direction_z))

###reference frame transformation
R=np.array([[0,0,1.],
			[1.,0,0],
			[0,1.,0]])
T=np.array([[2700.],[-800.],[500.]])
H=np.vstack((np.hstack((R,T)),np.array([0,0,0,1])))
curve=np.vstack((curve_x, curve_y, curve_z)).T
curve_base=np.zeros(curve.shape)
###checkpoint1
# print(np.dot(R,direction2R(curve_direction[0],curve[1]-curve[0])))
for i in range(len(curve)):
	curve_base[i]=np.dot(H,np.hstack((curve[i],[1])).T)[:-1]

#convert curve direction to base frame
curve_direction=np.dot(R,curve_direction).T


df=DataFrame({'x':curve_base[:,0],'y':curve_base[:,1], 'z':curve_base[:,2],'x_direction':curve_direction[:,0],'y_direction':curve_direction[:,1],'z_direction':curve_direction[:,2]})
df.to_csv('from_interp/Curve_in_base_frame.csv',header=False,index=False)