import logging

import numpy as np
import pytest

from .. import targets

GFZ = np.linspace(0.0, 8, 800)


def test_ZQ1_GFZ_as_float():
    GFZ = 1
    zq1 = targets.ZQ1()
    logging.debug(zq1.alpha_zielwert_bgf(GFZ))
    assert zq1.alpha_zielwert_bgf(GFZ=GFZ) == pytest.approx(8.0813, 0.001)
    assert zq1.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.8) == pytest.approx(10.10157, 0.001)
    assert zq1.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.65) == pytest.approx(12.4327, 0.001)


def test_ZQSynergy_GFZ_as_float():
    GFZ = 1
    zqsynergy = targets.ZQSynergy()
    assert zqsynergy.alpha_zielwert_bgf(GFZ=GFZ) == pytest.approx(5.3932, 0.001)
    assert zqsynergy.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.8) == pytest.approx(6.7415, 0.001)
    assert zqsynergy.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.65) == pytest.approx(8.2972, 0.001)


def test_ZQSynergy_GFZ_as_nparray():
    GFZ = np.linspace(0.0, 8, 11)

    zqsynergy = targets.ZQSynergy()
    bgf_results = zqsynergy.alpha_zielwert_bgf(GFZ=GFZ)
    zqs_results = np.array([100., 15.89678947, -11.71271429, -21.99860784,
                            -27.37183582, -30.67345783, -32.90788889, -34.52056522,
                            -35.73930534, -36.6927415, -37.459])
    for i, j in zip(bgf_results, zqs_results):
        assert i == pytest.approx(j, 0.001)

    ngf08_results = zqsynergy.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.8)
    logging.debug(ngf08_results)
    zqs_results_ngf = np.array([100., 19.87098684, -14.64089286, -27.4982598, -34.21479478, -38.34182229,
                                -41.13486111, -43.15070652, -44.67413168, -45.86592687, -46.82375])
    for i, j in zip(ngf08_results, zqs_results_ngf):
        assert i == pytest.approx(j, 0.001)

    ngf065_results = zqsynergy.alpha_zielwert_ngf(GFZ=GFZ, NGF_to_BGF=0.65)
    logging.debug(ngf065_results)
    zqs_results_ngf065 = np.array([100.,24.45659919, -18.01956044, -33.84401207, -42.11051665, -47.18993513,
                                   -50.62752137, -53.10856187, -54.98354668, -56.45037153, -57.62923077])
    for i, j in zip(ngf065_results, zqs_results_ngf065):
        assert i == pytest.approx(j, 0.001)

def test_contextfactors():
    zqsynergy = targets.ZQSynergy()
    assert zqsynergy.alpha_zielwert_bgf(1) == -zqsynergy.context_factor_density_gfa(1)
    assert zqsynergy.alpha_zielwert_ngf(1) == -zqsynergy.context_factor_density_nfa(1)

    GFZ = np.linspace(0.0, 8, 11)
    bgf_results = zqsynergy.context_factor_density_gfa(GFZ=GFZ)
    zqs_results = np.array([100., 15.89678947, -11.71271429, -21.99860784,
                            -27.37183582, -30.67345783, -32.90788889, -34.52056522,
                            -35.73930534, -36.6927415, -37.459])
    for i, j in zip(bgf_results, zqs_results):
        assert i == pytest.approx(-j, 0.001)