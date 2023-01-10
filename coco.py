import pathlib
import numpy as np

labels_path = pathlib.Path('coco128')

txt = sorted(list(labels_path.glob('labels/train2017/*.txt')))

for i in txt:
    ary = np.genfromtxt(str(i))

    bbox = ary[:,1:]

    x_center = bbox[:,0]
    y_center = bbox[:,1]

    width = bbox[:,2]
    height = bbox[:,3]

    x1 = x_center - width/2
    y1 = y_center - width/2

    x2 = x_center + width/2
    y2 = y_center + width/2

    print(x1)
    print(y1)
    break