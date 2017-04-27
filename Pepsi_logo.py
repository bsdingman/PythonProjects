#############################################################
# Bryan Dingman
# Create a logo using matplotlib
# The following logo is what I used for reference
# http://img.brainjet.com/filter:scale/slides/3/3/9/6/5/1/3396513027/ed6eb3f201d6dd08b24b0feb74d314233a617dc2.jpeg?mw=615
#############################################################

import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as patches

# Circle Verts
c_verts = [
    (-1., 0.), 
    (-1., 1.5),
    (1., 1.5), 
    (1., 0.), 
    (1., 0.),
    (1., -1.5),
    (-1., -1.5),
    (-1., 0.)
    ]

# Circle Codes
c_codes = [Path.MOVETO,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4,
         Path.MOVETO,
         Path.CURVE4,
         Path.CURVE4,
         Path.CURVE4
         ]

# Circle Path
c_path = Path(c_verts, c_codes)

# Red part verts
r_verts = [
    (-0.75, -0.7),
    (-1.35, 0.3),
    (-0.5, 1.5),
    (0.5, 0.9),
    
    (0.5, 0.9),
    (0.5, 0.2),
    (-0.25, -0.4),
    (-0.75, -0.7)
    ]

# Red Part codes
r_codes = [Path.MOVETO,
           Path.CURVE4,
           Path.CURVE4,
           Path.CURVE4,
           Path.MOVETO,
           Path.CURVE4,
           Path.CURVE4,
           Path.CURVE4
           
         ]

# Red Part Paths
r_path = Path(r_verts, r_codes)


# Blue Part Verts
b_verts = [
    (-0.7, -0.75),
    (0.2, -1.6),
    (1.4, -0.6),
    (0.74, 0.71),
    
    (0.74, 0.71),
    (0.95, -0.4),
    (0.1, -0.3),
    (-0.7, -0.75)
    ]

# Blue part codes
b_codes = [Path.MOVETO,
           Path.CURVE4,
           Path.CURVE4,
           Path.CURVE4,
           
           Path.MOVETO,
           Path.CURVE4,
           Path.CURVE4,
           Path.CURVE4
         ]

# Blue part paths
b_path = Path(b_verts, b_codes)

# Create our fiture
fig = plt.figure("Pepsi Logo")
ax = fig.add_subplot(1,1,1)

# AAdd the path for the circle
patch = patches.PathPatch(c_path, edgecolor='#0053A3', facecolor='none', lw=1)
ax.add_patch(patch)

# Add the path for the red part
patch = patches.PathPatch(r_path, edgecolor='#EC1A23', facecolor='#EC1A23', lw=1)
ax.add_patch(patch)

# Add the path for the blue part
patch = patches.PathPatch(b_path, edgecolor='#0053A3', facecolor='#0053A3', lw=1)
ax.add_patch(patch)

"""
# Uncomment this if you want to see the plot points graphed as well
# Plot points for the circle
xs, ys = zip(*c_verts)
ax.plot(xs, ys, 'x--', lw=1, color='blue', ms=5)

# Plot points for the red part
xs, ys = zip(*r_verts)
ax.plot(xs, ys, 'x--', lw=1, color='red', ms=5)

# Plot points for the Blue part
xs, ys = zip(*b_verts)
ax.plot(xs, ys, 'x--', lw=1, color='blue', ms=5)
"""

# set the axis limit
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)

# Plot!
plt.show()