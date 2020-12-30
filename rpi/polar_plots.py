import  matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#Polar stuff
fig = plt.figure(figsize=(10,8))
ax = plt.subplot(111,polar=True)
ax.set_title("A line plot on a polar axis", va='bottom')
ax.set_rticks([1,2])  # fewer radial ticks
ax.set_facecolor(plt.cm.gray(.95))
ax.grid(True)


r = []
theta = []
# Animation requirements.
ln, = plt.plot([], [], 'r:',
                    markersize=1.5,
                    alpha=1,
                    animated=True)

def init():
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    return ln,

def update(frame):
    r.append(frame)
    theta.append(5*np.pi*frame)
    ln.set_data(theta, r)
    return ln,

ani = FuncAnimation(fig, update, frames=np.linspace(0,2,400),
                    init_func=init, interval=10, blit=True,repeat=True)

plt.show()
