# Creates visualizations from processed orbital simulation 
import simulate_orbits
import matplotlib.pyplot as plt

def plot_object(df, object_name, x_axis = "Time", y_axis = "X_pos"):
    """
    Plots the given x axis value of an orbiting object over chosen y axis value. 

    Args:
        df: a pandas DataFrame containing the simulation data.
        object_name: A string representing the name of the object being plotted.
        x_axis: A string representing the column name of values to plot on the x-axis.
        y_axis: A string representing the column name of values to plot on the y-axis.
    """
    object_data = df[df["Object"] == object_name]
    plt.plot(object_data[x_axis], object_data[y_axis], label=f"{object_name} {y_axis}")
    if x_axis == "Time":
        plt.xlabel("Time (years)")
        x_unit = "years"
    elif "pos" in x_axis:
        plt.ylabel(f"{x_axis} Position (km)")
        x_unit = "km"

    if y_axis == "Time":
        plt.ylabel("Time (years)")
        y_unit = "years"
    elif "pos" in y_axis:
        plt.ylabel(f"{y_axis} Position (km)")
        y_unit = "km"
    plt.title(f"{object_name}'s {x_axis} ({x_unit}) over {y_axis} ({y_unit})")
    plt.legend()
    plt.grid()
    
    # Show plot
    plt.show()


def plot_system(system, df, x_axis = "Time", y_axis ="X_pos"):
    """
    Plots the given x axis value of all orbiting objects in a system over chosen y axis value. 

    Args:
        system: An OrbitalSystem representing the orbital system that df holds simulation data for.
        df: a pandas DataFrame containing the simulation data.
        x_axis: A string representing the column name of values to plot on the x-axis.
        y_axis: A string representing the column name of values to plot on the y-axis.

    """
    plt.figure(figsize=(8, 5))

    # Loop through each unique object in the system
    for object in df["Object"].unique():
        object_data = df[df["Object"] == object]
        plt.plot(object_data[x_axis], object_data[y_axis], label=f"{object} {y_axis}")
    if x_axis == "Time":
        plt.xlabel("Time (years)")
        x_unit = "years"
    elif "pos" in x_axis:
        plt.ylabel(f"{x_axis} Position (km)")
        x_unit = "km"

    if y_axis == "Time":
        plt.ylabel("Time (years)")
        y_unit = "years"
    elif "pos" in y_axis:
        plt.ylabel(f"{y_axis} Position (km)")
        y_unit = "km"
    plt.title(f"{system.name} {x_axis} ({x_unit}) over {y_axis} ({y_unit})")
    plt.legend()
    plt.grid()
    plt.show()
