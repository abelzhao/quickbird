#!/usr/bin/env python
# -*- encoding:utf-8 -*-
#
#        Author: ZhaoFei - zhaofei@calfdata.com
#        Create: 2017-09-19 14:26:14
# Last Modified: 2017-09-19 14:26:14
#      Filename: read_tiffile.py
#   Description: ---
# Copyright (c) 2016 Chengdu Lanjing Data&Information Co.


from collections import defaultdict
import csv
import sys


import cv2
from shapely.geometry import MultiPolygon, Polygon
import shapely.wkt
import shapely.affinity
import numpy as np
import tifffile as tiff






