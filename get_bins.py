

import numpy as np
import pandas as pd

from data_tools.data_utils import get_data_bins
data = pd.read_csv("./data_files/conversion.csv")


print(data.info())
bins = get_data_bins(data['cvr'], 9)
print(bins)