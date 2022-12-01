# PlotMI
Simple 3D plotting for medical images in python


## Installation

Requirements:
- numpy
- matplotlib

```
git clone https://github.com/Lugges991/plotMI.git
cd plotMI
pip3 install .
```

OR:

```
pip3 install git+https://github.com/Lugges991/plotMI.git
```

## Usage:
```
import numpy as np
from plotMI import PlotMI

img = numpy.random.rand((64, 64, 64))

pm = PlotMI(img)
pm()
```
