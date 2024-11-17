import math
import time
import numpy as np
import torch
from d2l import torch as d2l

n = 10000
a = torch.ones([n])
b = torch.ones([n])

c = torch.zeros(n)
for i in range(n):
    c[i] = a[i] + b[i]
