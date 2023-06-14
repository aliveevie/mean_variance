import numpy as np

def calculate(list):
    if len(list) > 9:
        return "List must contain nine numbers."
    calculations = dict()
    my_list = np.array(list)
    
    matrix = my_list.reshape(3,3)
    mean_axis_0 = np.mean(matrix, axis=0).tolist()
    mean_axis_1 = np.mean(matrix, axis=1).tolist()
    mean_flattened = np.mean(matrix.flatten())
    
    mean = [mean_axis_0, mean_axis_1, mean_flattened]
    
    
    sum_axis_0 = np.sum(matrix, axis=0).tolist()
    sum_axis_1 = np.sum(matrix, axis=1).tolist()
    sum_flattened = np.sum(matrix.flatten())
    
    sum_list = [sum_axis_0, sum_axis_1, sum_flattened]
    
    # Compute the Max
    max1 = np.max(matrix, axis=0).tolist()
    max2 = np.max(matrix, axis=1).tolist()
    flattenmx = np.max(matrix.flatten())
    
    maximum = [max1, max2, flattenmx]
    
    # Compute the min
    
    min1 = np.min(matrix, axis=0).tolist()
    min2 = np.min(matrix, axis=1).tolist()
    flattenmx = np.min(matrix.flatten())
    
    minimum = [min1, min2, flattenmx]
    
    
    # Compute the Variance and Standard deviations
    var1 = np.var(matrix, axis=0).tolist()
    var2 = np.var(matrix, axis=1).tolist()
    flattenvr = np.var(matrix.flatten())
    
    std1 = np.std(matrix, axis=0).tolist()
    std2 = np.std(matrix, axis=1).tolist()
    flattenstd = np.std(matrix.flatten())
    
    variance = [var1, var2, flattenvr]
    
    standard_deviation = [std1, std2, flattenstd]
    
    calculations = {
        "mean": mean,
        "variance":variance,
        "Standard deviation": standard_deviation,
        "max": maximum,
        "min": minimum,
        "sum":sum_list
    }

    return calculations