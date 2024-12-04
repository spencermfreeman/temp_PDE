import matplotlib.pyplot as plt
import numpy as np

T_0 = 200
k = 0.466
rod_length = 2
x_step = 0.05
max_time = 10

#for now we define two points in the 1D system
def initialize_1D(T_0, x_step, system_length, k):
    x_step = x_step
    time_step = stability_condition(x_step, k)
    n_points = int(system_length/x_step)
    x_values = np.zeros(n_points)
    x_values[0], x_values[int(system_length/x_step)-1] = T_0, T_0
    return x_values, time_step

def simulation(system_arr, x_step, max_time, time_step, k):
    time_axis = np.linspace(0, max_time, int(max_time/time_step))
    for time in time_axis:
        for i in range(1, len(system_arr)-1):
            system_arr[i] = system_arr[i] + temp_change(system_arr, i*x_step, x_step, time_step, k)
        plot_animation(system_arr, time, max_time)
    plt.show()
    
def temp_change(system_arr, x, x_step, time_step, k):
    index = x_to_index(x, x_step)
    if(check_bounds(system_arr, index)):
        temp_difference_per_time = k*(system_arr[index+1]-2*system_arr[index]+system_arr[index-1])/x_step**2
        return temp_difference_per_time*time_step
    else:
        print("Index error in temp method")
        return -1

def stability_condition(delta_x,k):
    delta_t = delta_x**2/(2*k)
    return delta_t

def check_bounds(system_arr, index):
    if(index+1<len(system_arr) and index-1>-1):
        return True
    else:
        return False
    
def x_to_index(x, x_step):
    return int(x/x_step)

def plot_animation(system_arr, time, max_time):
    x_axis = np.linspace(0,20, len(system_arr))
    plt.plot(x_axis, system_arr)
    time = float(f"{time:.3f}")
    plt.title(f"1D Temperature Distribution, Time: {time}")
    plt.xlabel("Position (m*(10^-1))")
    plt.ylabel("Temperature (K)")
    plt.ylim(0, T_0+10)
    plt.pause(.01)
    if(abs(max_time-time)>0.01):
        plt.cla()
    
if __name__ == "__main__":
    system_arr, time_step = initialize_1D(T_0, x_step, rod_length, k)
    simulation(system_arr, x_step, max_time, stability_condition(x_step, k), k)
