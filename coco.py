import pathlib
import numpy as np

labels_path = pathlib.Path('coco128')

txt = sorted(list(labels_path.glob('labels/train2017/*.txt')))

for i in txt:
    ary = np.genfromtxt(str(i))
    print(ary)
    break