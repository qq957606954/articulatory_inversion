from nnmnkwii.datasets import FileSourceDataset
import numpy as np
from data_utils import MFCCSource

mfcc_x = FileSourceDataset(MFCCSource("trainfiles.txt"))
mfcc_x_val = FileSourceDataset(MFCCSource("validationfiles.txt"))
mfcc_x_test = FileSourceDataset(MFCCSource("testfiles.txt"))

for sample in mfcc_x:
    mfcc, name = sample
    new_path = name.replace("all", "npy")
    np.save(new_path, mfcc)

for sample in mfcc_x_val:
    mfcc, name = sample
    new_path = name.replace("all", "npy")
    np.save(new_path, mfcc)

for sample in mfcc_x_test:
    mfcc, name = sample
    new_path = name.replace("all", "npy")
    np.save(new_path, mfcc)