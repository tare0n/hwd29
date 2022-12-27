from functools import wraps
import math


class Derivative:
    def __init__(self, spacing=0.0001):
        self.spacing = spacing

    def __call__(self, func):
        @wraps(func)
        def wrapper(x):
            forward = x + self.spacing/2
            backward = x - self.spacing/2
#           forward[0] += self.spacing/2
#           backward[0] -= self.spacing/2
            central_diff = func(forward) - func(backward)
            return central_diff/self.spacing
        return wrapper


@Derivative()
def _sin(x):
    return math.sin(x)


inputs_list = [0]
for i in range(1, 12):
    inputs_list.append(inputs_list[i-1]+math.pi/3)

for number in inputs_list:
    print(f"cos({number}) = {math.cos(number)}; sin'({number}) = {_sin(number)}")

