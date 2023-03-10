import os
import pandas as pd
import json
from shutil import copyfile
import numpy as np
import math
import torch


filenames = os.listdir('raw/3d_detection/second')    # 7481
filenames.sort()

for i in range(len(filenames)):
    _3d_pt_path = os.path.join('raw/3d_detection/second', filenames[i])
    _3d_dict = torch.load(_3d_pt_path)[0]


    names = _3d_dict['name']
    scores = _3d_dict['score']
    boxes_lidar = _3d_dict['boxes_lidar']
    r_y = _3d_dict['rotation_y']

    token = _3d_dict['frame_id']

    assert len(names) == len(scores)
    assert len(names) == len(boxes_lidar)

    content_3d = ''
    for j in range(len(names)):
        loc = boxes_lidar[j][0:3]         # x y z
        dim = boxes_lidar[j][3:6]         # l w h
        # dim[0], dim[1] = dim[1], dim[0]   # w l h

        angle = boxes_lidar[j][6]

        line = names[j] + ' ' + str(loc) + ' ' + str(dim) + ' ' + str(angle) + ' ' + str(r_y[j]) + ' ' + str(scores[j]) + '\n'

        content_3d = content_3d + line
    
    # 最后一行加3d token
    content_3d = content_3d + token

    _3d_file = open('new/3d_detection/second/{}.txt'.format(str(i).zfill(6)), 'w')
    _3d_file.write(content_3d)
    _3d_file.close()

    print(i)
