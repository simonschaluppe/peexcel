import numpy as np
import pytest

from .. import targets


GFZ = np.linspace(0.0, 8, 800)

def test_ZQ1():
    ZQ1 = targets.ZQ1(GFZ=1)
    print()