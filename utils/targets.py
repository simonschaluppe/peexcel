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



def target(
        GFZ,
        fPE=1.63, # OIB 2019 Jahresmittel
        A=35.2,
        dx=0.15,
        EUI=27.3,
        cutoff=300,
        scale=1.,
        gfzscale=1.,
) -> pd.DataFrame:
    curve = (fPE * (A/(dx + GFZ*gfzscale) - EUI )) * scale
    return np.minimum(curve, cutoff) if cutoff else curve


from functools import partial

def zq_synergy_gfa(GFZ):
    return target(
        GFZ=GFZ,
        fPE=1.63,
        A=35.2,
        dx=0.15,
        EUI=27.3,
        cutoff=100.,
    )




class Zielwert:
    @abstractmethod
    def alpha_zielwert_bgf(self):
        pass
    @abstractmethod
    def alpha_zielwert_ngf(self):
        pass
    @abstractmethod
    def beta_zielwert_bgf(self):
        pass
    @abstractmethod
    def beta_zielwert_ngf(self):
        pass
    @abstractmethod
    def omega_zielwert_bgf(self):
        pass
    @abstractmethod
    def omega_zielwert_ngf(self):
        pass

@dataclass
class ZQ1(Zielwert):
    fPE: float  = 1.63  # OIB 2019 Jahresmittel
    A: float    = 37
    dx: float   = 0.085
    EUI: float  = 29.143558  # = dy - PEB/fPE

    def alpha_zielwert_bgf(self, GFZ):
        return target(GFZ=GFZ,
                      fPE=self.fPE,
                      A=self.A,
                      dx=self.dx,
                      EUI=self.EUI,
                      cutoff=None,
                      )

    def alpha_zielwert_ngf(self, GFZ, NGF_to_BGF=0.8):
        return target(GFZ=GFZ,
                      fPE=self.fPE,
                      A=self.A,
                      dx=self.dx,
                      EUI=self.EUI,
                      cutoff=None,
                      scale=1/NGF_to_BGF,
                      )


class ZQSynergy(Zielwert):
    fPE: float  = 1.63  # OIB 2019 Jahresmittel
    A: float    = 35.2
    dx: float   = 0.15
    EUI: float  = 27.3  # = dy - PEB/fPE
    cutoff: float = 100.

    def alpha_zielwert_bgf(self, GFZ):
        return target(GFZ=GFZ,
                      fPE=self.fPE,
                      A=self.A,
                      dx=self.dx,
                      EUI=self.EUI,
                      cutoff=self.cutoff,
                      )

    def alpha_zielwert_ngf(self, GFZ, NGF_to_BGF=0.8):
        return target(GFZ=GFZ,
                      fPE=self.fPE,
                      A=self.A,
                      dx=self.dx,
                      EUI=self.EUI,
                      cutoff=self.cutoff,
                      scale=1/NGF_to_BGF,
                      )

    def context_factor_density_gfa(self, *args, **kwargs):
        return -self.alpha_zielwert_bgf(*args, **kwargs)

    def context_factor_density_nfa(self, *args, **kwargs):
        return -self.alpha_zielwert_ngf(*args, **kwargs)
