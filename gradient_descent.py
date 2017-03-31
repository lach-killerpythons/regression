
from numpy import *

# hyperparameteres - how fast model learns (needs to be optimised)
learning_rate = 0.0001  # rate of convergence
# y=mx+b
initial_b = 0  # intercept
initial_m = 0  # slope
num_iterations = 1000


def compute_error_given_points(b,m,points): #SS ERROR
    #SS Error = 1/n SUM[N,i=1] (Yi - (MXi + B))^2
    totalError = 0
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y - (m * x + b)) ** 2
    return totalError/float(len(points))

#FIND LOCAL MINIMUM - first order derivative/ ideal y-int and slope
# gradients from partial derivatives B and M:
# d/dM = 2/N SUM[N,i=1] -Xi(Yi - (MXi + B))
# d/dB = 2/N SUM[N,i=1] -(Yi-(MXi+B))

def step_gradient(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]

def gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations):
    b = initial_b
    m = initial_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b,m]


def SGD(b_current, m_current, points, learning_rate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0,len(points)):
        x = points[i, 0]
        y = points[i, 1]
        b_gradient += -(2/N) * (y - ((m_current * x) + b_current))
        m_gradient += -(2/N) * x * (y - ((m_current * x) + b_current))
    new_b = b_current - (learning_rate * b_gradient)
    new_m = m_current - (learning_rate * m_gradient)
    return [new_b, new_m]

def SGD_run(points, initial_b, initial_m, learning_rate, num_iterations):
    b = initial_b
    m = initial_m
    for i in range(num_iterations):
        b, m = step_gradient(b, m, array(points), learning_rate)
    return [b,m]



def run():
    points = genfromtxt('data.csv', delimiter=",")
    [b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print ("Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error_given_points(initial_b, initial_m, points)))
    print ("Running...")
    [b, m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print("After {0} iterations b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error_given_points(b, m, points)))


if __name__ == '__main__':
    run()