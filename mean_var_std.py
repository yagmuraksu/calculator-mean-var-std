import numpy as np

def calculate(list):

  if len(list) < 9:
    raise ValueError("List must contain nine numbers.")
  
  test_arr_flat = np.asarray(list)
  test_arr_3by3 = np.copy(test_arr_flat)
  test_arr_3by3.resize(3,3)
  calculations = {}

  #mean
  mean_axis0 = np.mean(test_arr_3by3, axis=0)
  mean_axis1 = np.mean(test_arr_3by3, axis=1)
  mean_flat = np.mean(test_arr_flat)
  calculations['mean'] = [mean_axis0.tolist(), mean_axis1.tolist(), mean_flat.tolist()]

  #variance
  var_axis0 = np.var(test_arr_3by3, axis=0)
  var_axis1 = np.var(test_arr_3by3, axis=1)
  var_flat = np.var(test_arr_flat)
  calculations['variance'] = [var_axis0.tolist(), var_axis1.tolist(), var_flat.tolist()]

  #std
  std_axis0 = np.std(test_arr_3by3, axis=0)
  std_axis1 = np.std(test_arr_3by3, axis=1)
  std_flat = np.std(test_arr_flat)
  calculations['standard deviation'] = [std_axis0.tolist(), std_axis1.tolist(), std_flat.tolist()]
  
  #max
  max_axis0 = np.max(test_arr_3by3, axis=0)
  max_axis1 = np.max(test_arr_3by3, axis=1)
  max_flat = np.max(test_arr_flat)
  calculations['max'] = [max_axis0.tolist(), max_axis1.tolist(), max_flat.tolist()]

  #min
  min_axis0 = np.min(test_arr_3by3, axis=0)
  min_axis1 = np.min(test_arr_3by3, axis=1)
  min_flat = np.min(test_arr_flat)
  calculations['min'] = [min_axis0.tolist(), min_axis1.tolist(), min_flat.tolist()]

  #sum of the rows
  sum_axis0 = np.sum(test_arr_3by3, axis=0)
  sum_axis1 = np.sum(test_arr_3by3, axis=1)
  sum_flat = np.sum(test_arr_flat)
  calculations['sum'] = [sum_axis0.tolist(), sum_axis1.tolist(), sum_flat.tolist()]

  return calculations