import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('driver_trajectory_CD_LinearFit233_downParabola.csv', header=None, names=['x', 'z', 'velocity', 'time', 'CD', 'reynoldsNumber'])
data = data.apply(pd.to_numeric, errors='coerce')   
# Extract columns
x = data['x']
z = data['z']
v = data['velocity']
t = data['time']
c = data['CD']
r = data['reynoldsNumber']

# --- 1. Trajectory Plot (Height vs. Distance) ---
plt.figure(figsize=(6, 4))
plt.plot(x, z, linewidth=2.0, color='navy')
plt.xlabel('Horizontal Distance [m]', fontsize=12)
plt.ylabel('Height [m]', fontsize=12)
plt.title('Simulated Golf Ball Trajectory (Driver)', fontsize=13)
plt.grid(True, linestyle='--', alpha=0.5)
plt.ticklabel_format(style='plain')
plt.tight_layout()
plt.gca().set_aspect(0.5)
plt.savefig('trajectory_plot.png', dpi=300)
plt.savefig('trajectory_plot.pdf')
plt.show()

# --- 2. Velocity Decay Plot ---
# plt.figure(figsize=(6, 4))
# plt.plot(t, v, linewidth=2.0, color='darkred')
# plt.xlabel('Time [s]', fontsize=12)
# plt.ylabel('Velocity [m/s]', fontsize=12)
# plt.title('Velocity Decay Over Flight', fontsize=13)
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.savefig('velocity_decay.png', dpi=300)
# plt.savefig('velocity_decay.pdf')
# plt.show()
