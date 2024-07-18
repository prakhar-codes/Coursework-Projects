import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def spherical_to_cartesian_point(r, theta, phi):
    x = r * np.sin(phi) * np.cos(theta)
    y = r * np.sin(phi) * np.sin(theta)
    z = r * np.cos(phi)
    return x, y, z

def spherical_to_cartesian_vector(v_r, v_theta, v_phi, r, theta, phi):
    v_x = v_r*np.sin(phi)*np.cos(theta) + v_theta*np.cos(phi)*np.cos(theta) - v_phi*np.sin(theta)
    v_y = v_r*np.sin(phi)*np.sin(theta) + v_theta*np.cos(phi)*np.sin(theta) + v_phi*np.cos(theta)
    v_z = v_r*np.cos(phi) - v_theta*np.sin(phi)
    return v_x, v_y, v_z

# Define point in spherical coordinates
r_point = 1
theta_point = 0
phi_point = np.pi/2

# Define vector and starting point in spherical coordinates
r_start_point = 2
theta_start_point = 0
phi_start_point = np.pi/2
r_vector = 0
theta_vector = -np.sin(np.pi/4)
phi_vector = np.cos(np.pi/4)

# Convert spherical coordinates to Cartesian coordinates
x_start_point, y_start_point, z_start_point = spherical_to_cartesian_point(r_start_point, theta_start_point, phi_start_point)
x_point, y_point, z_point = spherical_to_cartesian_point(r_point, theta_point, phi_point)
x_vector, y_vector, z_vector = spherical_to_cartesian_vector(r_vector, theta_vector, phi_vector, r_point, theta_point, phi_point)

# Create 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot transparent sphere with radius 1
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_surface(x_sphere, y_sphere, z_sphere, color='b', alpha=0.2)

# Plot circular disk in xy-plane
theta_disk = np.linspace(0, 2*np.pi, 100)
x_disk = np.cos(theta_disk)
y_disk = np.sin(theta_disk)
z_disk = np.zeros_like(theta_disk)
ax.plot(x_disk, y_disk, z_disk, color='b', alpha=0.5)

# Plot point
ax.scatter(x_start_point, y_start_point, z_start_point, color='black', label='Point')

# Plot vector starting from the point
ax.quiver(x_start_point, y_start_point, z_start_point, x_vector, y_vector, z_vector, color='r', label='Vector')

# Plot dotted line from origin to the point
ax.plot([0, x_start_point], [0, y_start_point], [0, z_start_point], 'k--')

# Set labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
ax.set_zlim([-2, 2])

# Set aspect ratio to 'equal'
ax.set_box_aspect([1,1,1])

# Add legend
# ax.legend()

plt.show()