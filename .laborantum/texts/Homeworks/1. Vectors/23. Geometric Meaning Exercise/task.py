import numpy as np
import math as m


answer = {
    'dot_product': 1,
    'proj_x_to_y': 1
}


x_vector = np.array([4])
y_vector = np.array([3])
ϕ = np.pi / 6

dot_product = 4 * 3 * np.cos(ϕ)

answer['dot_product'] = dot_product


projection_x_on_y = 3 * np.cos(ϕ)


answer['proj_x_to_y'] = projection_x_on_y

print(answer)