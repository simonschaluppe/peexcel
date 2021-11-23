from abc import abstractmethod
from dataclasses import dataclass

import numpy as np
import pandas as pd


def parameters(p1: tuple, p2: tuple, p3: tuple, fPE=1., scale=1.):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    y1, y2, y3 = y1/fPE/scale, y2/fPE/scale, y3/fPE/scale

    EUI = (y3*x3-y1*x1 + (y1*x1 - y2*x2)*((y1-y3)/(y1-y2))) / ((x2-x1)*(y1-y3)/(y1-y2) + (x1 - x3))
    dx = ((y3*x3 - y2*x2) + EUI*(x3-x2))/(y2-y3)
    A = (y3 + EUI)*(dx+x3)

    return (A,dx,EUI,fPE,scale)



from functools import partial


def target(
        GFZ,
        A=35.2,
        dx=0.15,
        EUI=27.3,
        fPE=1.63,  # OIB 2019 Jahresmittel
        scale=1.,
        cutoff=300.,
        gfzscale=1.,
) -> pd.DataFrame:
    curve = (fPE * (A/(dx + GFZ*gfzscale) - EUI )) * scale
    return np.minimum(curve, cutoff) if cutoff else curve

def zq_synergy_gfa(GFZ):
    return target(GFZ=GFZ, A=35.2, dx=0.15, EUI=27.3, fPE=1.63, cutoff=100.)


@dataclass
class Zielwert:
    A: float
    dx: float
    EUI: float              # = dy - PEB/fPE
    fPE: float      = 1.63  # OIB 2019 Jahresmittel
    NGF_to_BGF: float = 0.8
    cutoff: float   = None

    def alpha_zielwert_bgf(self, GFZ):
        return target(GFZ=GFZ, A=self.A, dx=self.dx, EUI=self.EUI, fPE=self.fPE, cutoff=self.cutoff)

    def alpha_zielwert_ngf(self, GFZ):
        return target(GFZ=GFZ, A=self.A, dx=self.dx, EUI=self.EUI, fPE=self.fPE, scale=1 / self.NGF_to_BGF,
                      cutoff=self.cutoff)

    def context_factor_density_gfa(self, *args, **kwargs):
        return -self.alpha_zielwert_bgf(*args, **kwargs)

    def context_factor_density_nfa(self, *args, **kwargs):
        return -self.alpha_zielwert_ngf(*args, **kwargs)


    @classmethod
    def from_points(cls, list_of_tuples, decimals=2, cutoff=None, fPE=1.63, scale=1.):
        A, dx, EUI, fPE, scale = parameters(*list_of_tuples, fPE=fPE, scale=scale)
        A, dx, EUI = round(A, decimals), round(dx, decimals), round(EUI, decimals)
        zielwert = cls(A=A, dx=dx, EUI=EUI, fPE=fPE, cutoff=cutoff)
        zielwert._points = list_of_tuples
        return zielwert

    @classmethod
    def ZQ1(cls):
        return cls(
            A = 37,
            dx = 0.085,
            EUI = 29.143558,  # = dy - PEB/fPE
            fPE = 1.63,  # OIB 2019 Jahresmittel
            cutoff = None,
        )
    @classmethod
    def ZQSynergyOktober(cls):
        return cls(
            A=35.2,
            dx=0.15,
            EUI=27.3,  # = dy - PEB/fPE
            fPE=1.63,  # OIB 2019 Jahresmittel
            cutoff=100.,
        )

    @classmethod
    def ZQSynergy(cls):
        return cls(
            A=35.2,
            dx=0.15,
            EUI=27.3,  # = dy - PEB/fPE
            fPE=1.63,  # OIB 2019 Jahresmittel
            cutoff=100.,
        )

@dataclass
class ZQ1(Zielwert):
    """deprecated, use Zielwert.ZQ1() instead"""
    A: float    = 37
    dx: float   = 0.085
    EUI: float  = 29.143558  # = dy - PEB/fPE
    fPE: float  = 1.63  # OIB 2019 Jahresmittel
    cutoff: float = None

class ZQSynergy(Zielwert):
    """deprecated, use Zielwert.ZQ1() instead"""
    A: float    = 35.2
    dx: float   = 0.15
    EUI: float  = 27.3  # = dy - PEB/fPE
    fPE: float  = 1.63  # OIB 2019 Jahresmittel
    cutoff: float = 100.

if __name__ == "__main__":
    t = ZQ1()