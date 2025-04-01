import pandas as pd

def convert_simulation_to_dataframe(dictionary, time):
    """
    Converts dictionary into a pandas dataframe.

    Args:
        dictionary: Dioctionary representing simulation data over time
        time: Numpy array (vector) holding a timestep-ed time vector in years.

    Returns:
        df: Dataframe with all dictionary values as column values, row for each time

    """
    data_list = []

    for object_name, pos_array in dictionary.items():
        for i in range(len(time)):
            data_list.append([time[i], object_name, pos_array[i, 0], pos_array[i, 1], pos_array[i, 2]])

    df = pd.DataFrame(data_list, columns=["Time", "Object", "X_pos", "Y_pos", "Z_pos"])
    return df