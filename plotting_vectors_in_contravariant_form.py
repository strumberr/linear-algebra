import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plot_limit = 10

v = np.array([1, 0])
w = np.array([0, 1])


fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)


ax_scalar1 = plt.axes([0.25, 0.05, 0.65, 0.03])
ax_scalar2 = plt.axes([0.25, 0.1, 0.65, 0.03])
scalar1_slider = Slider(ax_scalar1, 'Scalar 1', -plot_limit, plot_limit, valinit=0)
scalar2_slider = Slider(ax_scalar2, 'Scalar 2', -plot_limit, plot_limit, valinit=0)

ax_basis_v = plt.axes([0.25, 0.15, 0.65, 0.03])
ax_basis_w = plt.axes([0.25, 0.2, 0.65, 0.03])
basis_v_slider = Slider(ax_basis_v, 'Basis v', -plot_limit, 10, valinit=1)
basis_w_slider = Slider(ax_basis_w, 'Basis w', -plot_limit, 10, valinit=1)


def update(val):
    scalar1 = scalar1_slider.val
    scalar2 = scalar2_slider.val
    
    v = np.array([basis_v_slider.val, 0])
    w = np.array([0, basis_w_slider.val])
    
    point = scalar1 * v + scalar2 * w
    
    ax.clear()
    
    ax.quiver(0, 0, scalar1 * v[0], scalar1 * v[1], angles='xy', scale_units='xy', scale=1, color='r')  # plot vector av
    ax.quiver(scalar1 * v[0], scalar1 * v[1], scalar2 * w[0], scalar2 * w[1], angles='xy', scale_units='xy', scale=1, color='b')  # plot vector bw
    ax.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color='g')  # plot resulting vector
    
    ax.text(point[0], point[1], f'Scalar 1: {scalar1:2f}', ha='right', va='bottom', color='r')  # mark scalar 1
    ax.text(point[0], point[1], f'Scalar 2: {scalar2:2f}', ha='left', va='top', color='b')  # mark scalar 2
    ax.text(point[0] / 2, point[1] / 2, f'Length: {np.linalg.norm(point):.2f}', ha='center', va='center', color='g')
    
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    
    plt.draw()



basis_v_slider.on_changed(update)
basis_w_slider.on_changed(update)

scalar1_slider.on_changed(update)
scalar2_slider.on_changed(update)


update(None)


# def on_keyboard(event):
#     if event.key == 'right':
#         scalar1_slider.set_val(min(scalar1_slider.val + 1, 10))
#     elif event.key == 'left':
#         scalar1_slider.set_val(max(scalar1_slider.val - 1, -10))
#     elif event.key == 'up':
#         scalar2_slider.set_val(min(scalar2_slider.val + 1, 10))
#     elif event.key == 'down':
#         scalar2_slider.set_val(max(scalar2_slider.val - 1, -10))

# fig.canvas.mpl_connect('key_press_event', on_keyboard)

def on_mouse_move(event):
    if event.inaxes == ax:
        scalar1 = event.xdata
        scalar2 = event.ydata
        scalar1_slider.set_val(scalar1)
        scalar2_slider.set_val(scalar2)

fig.canvas.mpl_connect('motion_notify_event', on_mouse_move)

plt.show()