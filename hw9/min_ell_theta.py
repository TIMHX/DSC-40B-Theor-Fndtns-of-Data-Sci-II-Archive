import numpy as np

def learn_theta(data, colors):
    max_blue = 0
    min_red = np.inf
    for i in range(len(colors)):
        if (colors[i] == 'blue') and data[i] >= max_blue:
            max_blue = data[i]
        elif (colors[i] == 'red') and data[i] <= min_red:
            min_red = data[i]
    return (max_blue + min_red)/2

def compute_ell(data, colors, theta):
    num_blue = 0
    num_red = 0
    for i in range(len(colors)):
        if (colors[i] == 'blue') and data[i] > theta:
            num_blue = num_blue + 1
        elif (colors[i] == 'red') and data[i] < theta:
            num_red = num_red + 1
    return float(num_blue + num_red)

def minimize_ell(data, colors):
    l = sorted(zip(data, colors))   # Using Timsort with time nlog(n)

    min_loss = np.inf
    out_theta = 0
    for i in range(1, len(l)):     # time n 
        theta = (l[i][0] + l[i-1][0])/2
        num_blue = 0
        num_red = 0
        for v in range(len(l)):    # calculate loss time n
            if (l[v][1] == 'blue') and l[v][0] > theta:
                num_blue = num_blue + 1
            elif (l[v][1] == 'red') and l[v][0] < theta:
                num_red = num_red + 1
                
        if num_blue + num_red < min_loss:    # save the minimized theta and its loss
            min_loss = num_blue + num_red
            out_theta = theta
    return out_theta       # in general, time complexity is nlog(n) + n^2


def minimize_ell_sorted(data, colors):
    loss = np.inf
    theta = 0
    n_blue = len(data)/2
    n_red_left = 0
    n_blue_right = 4
    for i in range(len(data)):
        if colors[i] == 'blue':
            n_blue_right = n_blue_right - 1
        elif colors[i] == 'red':
            n_red_left = n_red_left + 1
        if n_blue_right + n_red_left < loss: 
            if i != len(data) - 1:
                loss = n_blue_right + n_red_left
                theta = (data[i] + data[i+1])/2
            else:
                loss = 4
                theta = data[i] + 0.05
    return theta
