from abc import abstractmethod
from dataclasses import dataclass

import numpy as np
import pandas as pd


def target(
        GFZ,
        fPE=1.63, # OIB 2019 Jahresmittel
        A=35.2,
        dx=0.15,
        EUI=27.3,
        cutoff=100,
        scale=1.
) -> pd.DataFrame:
    curve = (fPE * (A/(dx + GFZ) - EUI )) * scale
    return np.minimum(curve, cutoff) if cutoff else curve

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
