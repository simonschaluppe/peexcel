from dataclasses import dataclass

import numpy as np
import pandas as pd


def parameters(p1: tuple, p2: tuple, p3: tuple, fPE=1.63):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    y1, y2, y3 = y1 / fPE, y2 / fPE, y3 / fPE

    EUI = (y3 * x3 - y1 * x1 + (y1 * x1 - y2 * x2) * ((y1 - y3) / (y1 - y2))) / (
            (x2 - x1) * (y1 - y3) / (y1 - y2) + (x1 - x3))
    dx = ((y3 * x3 - y2 * x2) + EUI * (x3 - x2)) / (y2 - y3)
    A = (y3 + EUI) * (dx + x3)

    return (A, dx, EUI, fPE)


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
    curve = (fPE * (A / (dx + GFZ * gfzscale) - EUI)) * scale
    return np.minimum(curve, cutoff * scale) if cutoff else curve


def zq_synergy_gfa(GFZ):
    return target(GFZ=GFZ, A=35.2, dx=0.15, EUI=27.3, fPE=1.63, cutoff=100.)


from enum import Enum, auto


class Bezug(Enum):
    BGF = auto()
    NGF = auto()


@dataclass
class Zielwert:
    A: float
    dx: float
    EUI: float  # = dy - PEB/fPE
    bezug: Bezug
    fPE: float = 1.63  # OIB 2019 Jahresmittel
    NGF_to_BGF: float = 0.8
    cutoff: float = None
    name: str = "generic"

    def __str__(self):
        return f"Zielwert '{self.name}': {self.bezug}, A={self.A:.3f}, dx={self.dx:.3f}, EUI={self.EUI:.3f}"

    @property
    def _bezug_str(self):
        return str(self.bezug).split(".")[-1]

    def formula(self):
        f = r"\frac{"
        cbc = r"}"
        cbo = r"{"
        string = f"$PE(GFZ) = minimum({self.fPE} * ({f}{round(self.A,1)}{cbc}{cbo}GFZ + {self.dx}{cbc} - {round(self.EUI,1)}), {round(self.cutoff,1)}) " \
                 f"[kWh_{'{PE}'}/m²_{'{'+f'{self._bezug_str}'+'}'}a]$"
        return string

    def df(self, GFZ=np.linspace(0, 5, 50), verbose=False):
        return pd.DataFrame({
            self.__str__(): self.alpha(GFZ)},
            index=GFZ)

    def series(self, GFZ):
        return self.alpha(GFZ)

    @property
    def params(self):
        return self.A, self.dx, self.EUI, self.fPE

    def set_reference(self, bezug: Bezug):
        if type(bezug) is str:
            if bezug.upper() == "BGF":
                bezug = Bezug.BGF
            elif bezug.upper() == "NGF":
                bezug = Bezug.NGF
            else:
                raise KeyError()

        if self.bezug is bezug:
            return
        if bezug is Bezug.NGF:
            self.A *= 1 / self.NGF_to_BGF
            self.EUI *= 1 / self.NGF_to_BGF
            self.cutoff *= 1 / self.NGF_to_BGF
        elif bezug is Bezug.BGF:
            self.A *= self.NGF_to_BGF
            self.EUI *= self.NGF_to_BGF
            self.cutoff *= self.NGF_to_BGF
        else:
            raise KeyError()
        self.bezug = bezug

    def alpha(self, GFZ, scale=1):
        return target(GFZ=GFZ, A=self.A, dx=self.dx, EUI=self.EUI, fPE=self.fPE, cutoff=self.cutoff, scale=scale)

    def alpha_zielwert_bgf(self, GFZ):
        bezug = self.bezug
        self.set_reference(bezug=Bezug.BGF)
        result = self.alpha(GFZ)
        self.set_reference(bezug=bezug)
        return result

    def alpha_zielwert_ngf(self, GFZ):
        bezug = self.bezug
        self.set_reference(bezug=Bezug.NGF)
        result = self.alpha(GFZ)
        self.set_reference(bezug=bezug)
        return result

    def context_factor_density_gfa(self, *args, **kwargs):
        return -self.alpha_zielwert_bgf(*args, **kwargs)

    def context_factor_density_nfa(self, *args, **kwargs):
        return -self.alpha_zielwert_ngf(*args, **kwargs)

    def plot(self, ax, ylims=(-75, 150), xlims=(0, 5), no_legend=False, **kwargs):
        ax = self.df.plot(ax=ax, **kwargs)  # linestyle, linewidth, etc
        ax.set_ylim(*ylims)
        ax.set_xlim(*xlims)
        ax.set_xlabel("Geschoßflächenzahl [-]")
        ax.grid()
        return ax

    @classmethod
    def from_points(cls, list_of_tuples, decimals=2, **kwargs):
        A, dx, EUI, fPE = parameters(*list_of_tuples)
        A, dx, EUI = round(A, decimals), round(dx, decimals), round(EUI, decimals)
        zielwert = cls(A=A, dx=dx, EUI=EUI, fPE=fPE, **kwargs)
        zielwert._points = list_of_tuples
        return zielwert

    @classmethod
    def ZQ1(cls, bezug=Bezug.NGF):
        return cls(
            A=37,
            dx=0.085,
            EUI=29.143558,  # = dy - PEB/fPE
            fPE=1.63,  # OIB 2019 Jahresmittel
            cutoff=None,
            bezug=bezug,
            name="ZQ1 (BGF Bezug)"
        )

    @classmethod
    def ZQSynergyOktober(cls, bezug=Bezug.NGF):
        return cls(
            A=35.2,
            dx=0.15,
            EUI=27.3,  # = dy - PEB/fPE
            fPE=1.63,  # OIB 2019 Jahresmittel
            cutoff=100.,
            name="ZQ Synergy Okt 2021",
            bezug=bezug
        )

    @classmethod
    def ZQSynergy(cls, bezug=Bezug.NGF):
        return cls(
            A=38,  # 30.4
            dx=0.15,
            EUI=33,  # 26.4  = dy - PEB/fPE
            fPE=1.63,  # OIB 2019 Jahresmittel
            cutoff=125.,
            bezug=bezug,
            name="ZQ Synergy"
        )


def ZQ1():
    """deprecated, use Zielwert.ZQ1() instead"""
    return Zielwert.ZQ1()


def ZQSynergy(Zielwert):
    """deprecated, use Zielwert.ZQ1() instead"""
    return Zielwert.ZQSynergy()


ZQSynergy = Zielwert.ZQSynergy()
ZQ1 = Zielwert.ZQ1()

if __name__ == "__main__":
    t = Zielwert.ZQSynergy()
