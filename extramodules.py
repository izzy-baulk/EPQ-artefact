#modules pulled from Davies, A (2022) kinematics_visualisaion.py (Commit 18da47a)[Source code]. https://github.com/ad-1/3DKinematicsVisualisation/blob/master/kinematics_visualisaion.py
import numpy as np
def vector_derivative(vector, wrt):
    return [component.diff(wrt) for component in vector] #wrt is symbolic variable from t, returns x y z components

def vector_magnitude(vector):
    magnitude = 0
    for component in vector:
        magnitude += component ** 2
    return magnitude ** (1 / 2)

def evaluate_vector(vector, time_step, t):
    numerical_vector = [float(component.subs(t, time_step).evalf()) for component in vector]
    magnitude = vector_magnitude(numerical_vector)
    return numerical_vector, magnitude
