import scipy
import numpy as np


def get_stats(cir_data):
    curr_dict = dict()

    curr_dict["kurtosis"] = scipy.stats.kurtosis(cir_data)
    curr_dict["variance"] = np.var(cir_data)
    curr_dict["mean"] = np.mean(cir_data)
    curr_dict["amplitude"] = np.max(np.fabs(cir_data))

    return curr_dict
