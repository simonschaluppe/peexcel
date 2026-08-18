"""Auto-generated SIM/timeseries schema bindings. Do not edit manually."""

from __future__ import annotations
from dataclasses import dataclass

TIMESERIES_SCHEMA_VERSION = '1_13_1_dev'

@dataclass(frozen=True)
class TimeseriesMeta:
    var_name: str
    attr_name: str
    domain: str | None = None
    measure: str | None = None
    unit: str | None = None
    formula: str | None = None

    def __repr__(self) -> str:
        parts = [self.var_name]

        if self.unit:
            parts.append(f"[{self.unit}]")

        return "<TimeseriesMeta " + " ".join(parts) + ">"


class TimeseriesMetaRegistry:
    def __init__(self):
        self.h = TimeseriesMeta(
            var_name='h',
            attr_name='h',
            domain=None,
            measure=None,
            unit=None,
            formula='1',
        )
        self.Monat_nr = TimeseriesMeta(
            var_name='Monat_nr',
            attr_name='Monat_nr',
            domain='📅 Datum und Zeit',
            measure='📅 Datum und Zeit',
            unit='int',
            formula='1',
        )
        self.Monat = TimeseriesMeta(
            var_name='Monat',
            attr_name='Monat',
            domain='📅 Datum und Zeit',
            measure='📅 Datum und Zeit',
            unit='monat',
            formula='Januar',
        )
        self.date = TimeseriesMeta(
            var_name='date',
            attr_name='date',
            domain='📅 Datum und Zeit',
            measure='📅 Datum und Zeit',
            unit='date',
            formula='43101',
        )
        self.hour_of_the_day = TimeseriesMeta(
            var_name='hour_of_the_day',
            attr_name='hour_of_the_day',
            domain='📅 Datum und Zeit',
            measure='📅 Datum und Zeit',
            unit='hotd',
            formula='0',
        )
        self.day_of_the_year = TimeseriesMeta(
            var_name='day_of_the_year',
            attr_name='day_of_the_year',
            domain='📅 Datum und Zeit',
            measure='📅 Datum und Zeit',
            unit='doty',
            formula='1',
        )
        self.Ti0uncooled = TimeseriesMeta(
            var_name='Ti0uncooled',
            attr_name='Ti0uncooled',
            domain=None,
            measure='20',
            unit='°C',
            formula='=IF(1-NFA_cooled/NFA_total>0,Tsetheat_min,#N/A)',
        )
        self.Ti0cooled = TimeseriesMeta(
            var_name='Ti0cooled',
            attr_name='Ti0cooled',
            domain=None,
            measure='20',
            unit='°C',
            formula='=IF(NFA_cooled/NFA_total>0,Tsetheat_min,#N/A)',
        )
        self.Ta = TimeseriesMeta(
            var_name='Ta',
            attr_name='Ta',
            domain='🌦️ Wetter',
            measure='Temperatur',
            unit='°C',
            formula='=OFFSET(Wetter!M25,0,(weather_index-1)*7)',
        )
        self.rel_humidity = TimeseriesMeta(
            var_name='rel_humidity',
            attr_name='rel_humidity',
            domain='🌦️ Wetter',
            measure='Luftfeuchte',
            unit='%',
            formula='=OFFSET(Wetter!N25,0,(weather_index-1)*7)',
        )
        self.Irr_nord = TimeseriesMeta(
            var_name='Irr_nord',
            attr_name='Irr_nord',
            domain='🌦️ Wetter',
            measure='Strahlung',
            unit='W/m²Nord',
            formula='=OFFSET(Wetter!H25,0,(weather_index-1)*7+4)',
        )
        self.Irr_east = TimeseriesMeta(
            var_name='Irr_east',
            attr_name='Irr_east',
            domain='🌦️ Wetter',
            measure='Strahlung',
            unit='W/m²Ost',
            formula='=OFFSET(Wetter!I25,0,(weather_index-1)*7)',
        )
        self.Irr_south = TimeseriesMeta(
            var_name='Irr_south',
            attr_name='Irr_south',
            domain='🌦️ Wetter',
            measure='Strahlung',
            unit='W/m²Süd',
            formula='=OFFSET(Wetter!J25,0,(weather_index-1)*7)',
        )
        self.Irr_west = TimeseriesMeta(
            var_name='Irr_west',
            attr_name='Irr_west',
            domain='🌦️ Wetter',
            measure='Strahlung',
            unit='W/m²West',
            formula='=OFFSET(Wetter!K25,0,(weather_index-1)*7)',
        )
        self.Irr_horizontal = TimeseriesMeta(
            var_name='Irr_horizontal',
            attr_name='Irr_horizontal',
            domain='🌦️ Wetter',
            measure='Strahlung',
            unit='W/m²Hori',
            formula='=OFFSET(Wetter!L25,0,(weather_index-1)*7-4)',
        )
        self.is_heating_period = TimeseriesMeta(
            var_name='is_heating_period',
            attr_name='is_heating_period',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='bool',
            formula='=--INDEX(heating_months, [@[Monat_nr]])',
        )
        self.is_cooling_period = TimeseriesMeta(
            var_name='is_cooling_period',
            attr_name='is_cooling_period',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='bool',
            formula='=--INDEX(cooling_months, [@[Monat_nr]])',
        )
        self.season_step = TimeseriesMeta(
            var_name='season_step',
            attr_name='season_step',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='%',
            formula='=0.5*([@[is_heating_period]]+NOT([@[is_cooling_period]]))',
        )
        self.bergangszeit = TimeseriesMeta(
            var_name='Übergangszeit',
            attr_name='bergangszeit',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='bool',
            formula='=IF([@[season_step]]=0.5,1,0)',
        )
        self.season_wave = TimeseriesMeta(
            var_name='season_wave',
            attr_name='season_wave',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='%',
            formula='=COS(([@h]+seasonal_phase_h)/8760*2*PI())/2+0.5',
        )
        self.percent_winter = TimeseriesMeta(
            var_name='percent_winter',
            attr_name='percent_winter',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='%',
            formula='=IF(seasonal_interpolation="step", [@[season_step]],[@[season_wave]])',
        )
        self.dT_uncooled = TimeseriesMeta(
            var_name='dT_uncooled',
            attr_name='dT_uncooled',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit=None,
            formula='=IFNA([@Ta]-[@Ti0uncooled],0)',
        )
        self.dT_cooled = TimeseriesMeta(
            var_name='dT_cooled',
            attr_name='dT_cooled',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit=None,
            formula='=IFNA([@Ta]-[@Ti0cooled],0)',
        )
        self.Spalte2 = TimeseriesMeta(
            var_name='Spalte2',
            attr_name='Spalte2',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit=None,
            formula=None,
        )
        self.Spalte4 = TimeseriesMeta(
            var_name='Spalte4',
            attr_name='Spalte4',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit=None,
            formula=None,
        )
        self.mobile_shading = TimeseriesMeta(
            var_name='mobile_shading',
            attr_name='mobile_shading',
            domain='🔀 Regelung',
            measure='🔀 Regelung',
            unit='%',
            formula='=fc_residential',
        )
        self.Qvinf_u = TimeseriesMeta(
            var_name='Qvinf_u',
            attr_name='Qvinf_u',
            domain='Passive Gewinne/Verluste',
            measure='💨 Infiltration',
            unit='Wh/m²uncooled',
            formula='=[@[dT_uncooled]]*NFV_u*vent_infiltration_ACH*cp_air*per_NFA_uncooled',
        )
        self.Qvinf_c = TimeseriesMeta(
            var_name='Qvinf_c',
            attr_name='Qvinf_c',
            domain='Passive Gewinne/Verluste',
            measure='💨 Infiltration',
            unit='Wh/m²cooled',
            formula='=[@[dT_cooled]]*NFV_c*vent_infiltration_ACH*cp_air*per_NFA_cooled',
        )
        self.ACH_residential = TimeseriesMeta(
            var_name='ACH_residential',
            attr_name='ACH_residential',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_residential*rh_residential*vent_scale_residential*Nutzung_Wohnen[@[Bedarf Luftwechsel]]',
        )
        self.ACH_office = TimeseriesMeta(
            var_name='ACH_office',
            attr_name='ACH_office',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_office*rh_office*vent_scale_office*Nutzung_Büro[@[Bedarf Luftwechsel]]',
        )
        self.ACH_edusec = TimeseriesMeta(
            var_name='ACH_edusec',
            attr_name='ACH_edusec',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_schoolsec*rh_schoolsec*vent_scale_school_sec*Nutzung_Schule[@[Bedarf Luftwechsel]]',
        )
        self.ACH_eduprim = TimeseriesMeta(
            var_name='ACH_eduprim',
            attr_name='ACH_eduprim',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_schoolprim*rh_schoolprim*vent_scale_school_prim*Nutzung_KIGA[@[Bedarf Luftwechsel]]',
        )
        self.ACH_retfood = TimeseriesMeta(
            var_name='ACH_retfood',
            attr_name='ACH_retfood',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_retailfood*rh_retailfood*vent_scale_supermarket*Nutzung_Handel_Food[@[Bedarf Luftwechsel]]',
        )
        self.ACH_retail = TimeseriesMeta(
            var_name='ACH_retail',
            attr_name='ACH_retail',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=NFA_retailother*rh_retailother*vent_scale_retail*Nutzung_Handel_NonFood[@[Bedarf Luftwechsel]]',
        )
        self.ACH_otherusage = TimeseriesMeta(
            var_name='ACH_otherusage',
            attr_name='ACH_otherusage',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='0',
        )
        self.ACH_mechvent_therm_u = TimeseriesMeta(
            var_name='ACH_mechvent_therm_u',
            attr_name='ACH_mechvent_therm_u',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit=None,
            formula='=SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_mech_shares,cool_passive_shares_T,1-((heat_recovery_rates_summer)+[@[percent_winter]]*(heat_recovery_rates_winter-heat_recovery_rates_summer)))',
        )
        self.ACH_mechvent_therm_c = TimeseriesMeta(
            var_name='ACH_mechvent_therm_c',
            attr_name='ACH_mechvent_therm_c',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_mech_shares,cool_active_shares_T,1-((heat_recovery_rates_summer)+[@[percent_winter]]*(heat_recovery_rates_winter-heat_recovery_rates_summer)))',
        )
        self.Spalte1 = TimeseriesMeta(
            var_name='Spalte1',
            attr_name='Spalte1',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit=None,
            formula=None,
        )
        self.ACH_mechvent_u = TimeseriesMeta(
            var_name='ACH_mechvent_u',
            attr_name='ACH_mechvent_u',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_mech_shares,cool_passive_shares_T)',
        )
        self.ACH_mechvent_c = TimeseriesMeta(
            var_name='ACH_mechvent_c',
            attr_name='ACH_mechvent_c',
            domain='Passive Gewinne/Verluste',
            measure='Air Change per Hour',
            unit='m³/h',
            formula='=SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_mech_shares,cool_active_shares_T)',
        )
        self.Qvmechvent_u = TimeseriesMeta(
            var_name='Qvmechvent_u',
            attr_name='Qvmechvent_u',
            domain='Passive Gewinne/Verluste',
            measure='💨 Lüftung',
            unit='Wh/m²uncooled',
            formula='=[@[dT_uncooled]]*[@[ACH_mechvent_therm_u]]*cp_air*per_NFA_uncooled',
        )
        self.Qvmechvent_c = TimeseriesMeta(
            var_name='Qvmechvent_c',
            attr_name='Qvmechvent_c',
            domain='Passive Gewinne/Verluste',
            measure='💨 Lüftung',
            unit='Wh/m²cooled',
            formula='=[@[dT_cooled]]*[@[ACH_mechvent_therm_c]]*cp_air*per_NFA_cooled',
        )
        self.Qvwindow_u = TimeseriesMeta(
            var_name='Qvwindow_u',
            attr_name='Qvwindow_u',
            domain='Passive Gewinne/Verluste',
            measure='💨 Lüftung',
            unit='Wh/m²uncooled',
            formula='=[@[dT_uncooled]]*cp_air*SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_window_shares,cool_passive_shares_T)*per_NFA_uncooled',
        )
        self.Qvwindow_c = TimeseriesMeta(
            var_name='Qvwindow_c',
            attr_name='Qvwindow_c',
            domain='Passive Gewinne/Verluste',
            measure='💨 Lüftung',
            unit='Wh/m²NFA',
            formula='=[@[dT_cooled]]*cp_air*SUMPRODUCT(sim[@[ACH_residential]:[ACH_otherusage]],vent_window_shares,cool_active_shares_T)*per_NFA_cooled',
        )
        self.QT_u = TimeseriesMeta(
            var_name='QT_u',
            attr_name='QT_u',
            domain='Passive Gewinne/Verluste',
            measure='🧱Transmission',
            unit='Wh/m²uncooled',
            formula='=[@[dT_uncooled]]*transmittance_Wm2',
        )
        self.QT_c = TimeseriesMeta(
            var_name='QT_c',
            attr_name='QT_c',
            domain='Passive Gewinne/Verluste',
            measure='🧱Transmission',
            unit='Wh/m²cooled',
            formula='=[@[dT_cooled]]*transmittance_Wm2',
        )
        self.QSwinter = TimeseriesMeta(
            var_name='QSwinter',
            attr_name='QSwinter',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh',
            formula='=SUMPRODUCT(sim[@[Irr_nord]:[Irr_horizontal]],apertures_winter)',
        )
        self.QSsummer = TimeseriesMeta(
            var_name='QSsummer',
            attr_name='QSsummer',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh',
            formula='=SUMPRODUCT(sim[@[Irr_nord]:[Irr_horizontal]],apertures_summer)',
        )
        self.QS_u_unshaded = TimeseriesMeta(
            var_name='QS_u_unshaded',
            attr_name='QS_u_unshaded',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh/m²uncooled',
            formula='=([@[percent_winter]]*[@QSwinter]+(1-[@[percent_winter]])*[@QSsummer])*per_NFA*(NFAfrac_u>0)',
        )
        self.QS_c_unshaded = TimeseriesMeta(
            var_name='QS_c_unshaded',
            attr_name='QS_c_unshaded',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh/m²cooled',
            formula='=([@[percent_winter]]*[@QSwinter]+(1-[@[percent_winter]])*[@QSsummer])*per_NFA*(NFAfrac_c>0)',
        )
        self.QS_u = TimeseriesMeta(
            var_name='QS_u',
            attr_name='QS_u',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh/m²uncooled',
            formula='=[@[QS_u_unshaded]]*(1-(1-mob_shading_factor_u)*AND([@[is_cooling_period]],QS_max_shading_u<[@[QS_u_unshaded]]))',
        )
        self.QS_c = TimeseriesMeta(
            var_name='QS_c',
            attr_name='QS_c',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh/m²cooled',
            formula='=[@[QS_c_unshaded]]*(1-(1-mob_shading_factor_c)*AND([@[is_cooling_period]],QS_max_shading_c<[@[QS_c_unshaded]]))',
        )
        self.Spalte9 = TimeseriesMeta(
            var_name='Spalte9',
            attr_name='Spalte9',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit=None,
            formula=None,
        )
        self.QS = TimeseriesMeta(
            var_name='QS',
            attr_name='QS',
            domain='Passive Gewinne/Verluste',
            measure='🌞 Solare Gewinne',
            unit='Wh/m²NFA',
            formula='=([@[percent_winter]]*[@QSwinter]+(1-[@[percent_winter]])*[@QSsummer])*per_NFA',
        )
        self.QI_residential = TimeseriesMeta(
            var_name='QI_residential',
            attr_name='QI_residential',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_residential*[@[percent_winter]]*Nutzung_Wohnen[@[Innere Wärmen Min]]+usage_concurrency_summer_residential*(1-[@[percent_winter]])*Nutzung_Wohnen[@[Innere Wärmen Max]])',
        )
        self.QI_office = TimeseriesMeta(
            var_name='QI_office',
            attr_name='QI_office',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_office*[@[percent_winter]]*Nutzung_Büro[@[Innere Wärmen Min]]+usage_concurrency_summer_office*(1-[@[percent_winter]])*Nutzung_Büro[@[Innere Wärmen Max]])',
        )
        self.QI_edusec = TimeseriesMeta(
            var_name='QI_edusec',
            attr_name='QI_edusec',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_schoolsec*[@[percent_winter]]*Nutzung_Schule[@[Innere Wärmen Min]]+usage_concurrency_summer_schoolsec*(1-[@[percent_winter]])*Nutzung_Schule[@[Innere Wärmen Max]])',
        )
        self.QI_eduprim = TimeseriesMeta(
            var_name='QI_eduprim',
            attr_name='QI_eduprim',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_schoolprim*[@[percent_winter]]*Nutzung_KIGA[@[Innere Wärmen Min]]+usage_concurrency_summer_schoolprim*(1-[@[percent_winter]])*Nutzung_KIGA[@[Innere Wärmen Max]])',
        )
        self.QI_retfood = TimeseriesMeta(
            var_name='QI_retfood',
            attr_name='QI_retfood',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_retailfood*[@[percent_winter]]*Nutzung_Handel_Food[@[Innere Wärmen Winter]]+usage_concurrency_summer_retailfood*(1-[@[percent_winter]])*Nutzung_Handel_Food[@[Innere Wärmen Sommer]])',
        )
        self.QI_retail = TimeseriesMeta(
            var_name='QI_retail',
            attr_name='QI_retail',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_retailother*[@[percent_winter]]*Nutzung_Handel_NonFood[@[Innere Wärmen Winter]]+usage_concurrency_summer_retailother*(1-[@[percent_winter]])*Nutzung_Handel_NonFood[@[Innere Wärmen Sommer]])',
        )
        self.QI_otherusage = TimeseriesMeta(
            var_name='QI_otherusage',
            attr_name='QI_otherusage',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²',
            formula='=(usage_concurrency_winter_other*[@[percent_winter]]*Nutzung_Handel_NonFood[@[Innere Wärmen Winter]]+usage_concurrency_summer_other*(1-[@[percent_winter]])*Nutzung_Handel_NonFood[@[Innere Wärmen Sommer]])',
        )
        self.QI_u = TimeseriesMeta(
            var_name='QI_u',
            attr_name='QI_u',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²uncooled',
            formula='=SUMPRODUCT(sim[@[QI_residential]:[QI_otherusage]],cool_passive_shares_T,NFA_shares_T)*NFA_total*per_NFA_uncooled',
        )
        self.QI_c = TimeseriesMeta(
            var_name='QI_c',
            attr_name='QI_c',
            domain='Passive Gewinne/Verluste',
            measure='👤Innere Lasten',
            unit='Wh/m²cooled',
            formula='=SUMPRODUCT(sim[@[QI_residential]:[QI_otherusage]],cool_active_shares_T,NFA_shares_T)*NFA_total*per_NFA_cooled',
        )
        self.Ti_passive_uncooled = TimeseriesMeta(
            var_name='Ti_passive_uncooled',
            attr_name='Ti_passive_uncooled',
            domain='Passive Gewinne/Verluste',
            measure='🌡',
            unit='°C',
            formula='=[@Ti0uncooled]+([@[Qvinf_u]]+[@[Qvmechvent_u]]+[@[Qvwindow_u]]+[@[QT_u]]+[@[QS_u]]+[@[QI_u]])/heat_capacity_effective_m2',
        )
        self.Ti_passive_cooled = TimeseriesMeta(
            var_name='Ti_passive_cooled',
            attr_name='Ti_passive_cooled',
            domain='Passive Gewinne/Verluste',
            measure='🌡',
            unit='°C',
            formula='=[@Ti0cooled]+([@[Qvinf_c]]+[@[Qvmechvent_c]]+[@[Qvwindow_c]]+[@[QT_c]]+[@[QS_c]]+[@[QI_c]])/heat_capacity_effective_m2',
        )
        self.dT_heating_uncooled_min = TimeseriesMeta(
            var_name='dT_heating_uncooled_min',
            attr_name='dT_heating_uncooled_min',
            domain='Nutzenergie Bedarfe',
            measure='Temperatur-Differenz',
            unit=None,
            formula='=MAX(0,IFNA(Tsetheat_min-[@[Ti_passive_uncooled]],0))',
        )
        self.dT_heating_cooled_min = TimeseriesMeta(
            var_name='dT_heating_cooled_min',
            attr_name='dT_heating_cooled_min',
            domain=None,
            measure='Temperatur-Differenz',
            unit=None,
            formula='=MAX(0,IFNA(Tsetheat_min-[@[Ti_passive_cooled]],0))',
        )
        self.dT_heating_uncooled_max = TimeseriesMeta(
            var_name='dT_heating_uncooled_max',
            attr_name='dT_heating_uncooled_max',
            domain=None,
            measure='Temperatur-Differenz',
            unit=None,
            formula='=MAX(0,IFNA(Tsetheat_flex-[@[Ti_passive_uncooled]],0))',
        )
        self.dT_heating_cooled_max = TimeseriesMeta(
            var_name='dT_heating_cooled_max',
            attr_name='dT_heating_cooled_max',
            domain=None,
            measure='Temperatur-Differenz',
            unit=None,
            formula='=MAX(0,IFNA(Tsetheat_flex-[@[Ti_passive_cooled]],0))',
        )
        self.Qh_to_room_uncooled_min = TimeseriesMeta(
            var_name='Qh_to_room_uncooled_min',
            attr_name='Qh_to_room_uncooled_min',
            domain='Heizwärmebedarf',
            measure='Wärmebereitstellung',
            unit='Wh/m²uncooled',
            formula='=MIN(QHmax_room_m2,[@[is_heating_period]]*([@[dT_heating_uncooled_min]]*heat_cap_eff_uncooled_m2))',
        )
        self.Qh_to_room_cooled_min = TimeseriesMeta(
            var_name='Qh_to_room_cooled_min',
            attr_name='Qh_to_room_cooled_min',
            domain='Heizwärmebedarf',
            measure='Wärmebereitstellung',
            unit='Wh/m²cooled',
            formula='=MIN(QHmax_room_m2,[@[is_heating_period]]*([@[dT_heating_cooled_min]]*heat_cap_eff_cooled_m2))',
        )
        self.Qh_to_room_uncooled_max = TimeseriesMeta(
            var_name='Qh_to_room_uncooled_max',
            attr_name='Qh_to_room_uncooled_max',
            domain='Heizwärmebedarf',
            measure='Wärmebereitstellung',
            unit='Wh/m²uncooled',
            formula='=MIN(QHmax_room_m2,AND([@[is_heating_period]],NOT([@[is_cooling_period]]))*([@[dT_heating_uncooled_max]]*heat_cap_eff_uncooled_m2))',
        )
        self.Qh_to_room_cooled_max = TimeseriesMeta(
            var_name='Qh_to_room_cooled_max',
            attr_name='Qh_to_room_cooled_max',
            domain='Heizwärmebedarf',
            measure='Wärmebereitstellung',
            unit='Wh/m²cooled',
            formula='=MIN(QHmax_room_m2,AND([@[is_heating_period]],NOT([@[is_cooling_period]]))*([@[dT_heating_cooled_max]]*heat_cap_eff_cooled_m2))',
        )
        self.Qh_to_room_min = TimeseriesMeta(
            var_name='Qh_to_room_min',
            attr_name='Qh_to_room_min',
            domain='Heizwärmebedarf',
            measure='HWB',
            unit='Wh/m²NFA',
            formula='=SUMPRODUCT(sim[@[Qh_to_room_uncooled_min]:[Qh_to_room_cooled_min]],$H$4:$I$4)',
        )
        self.Qh_to_room_flex_u = TimeseriesMeta(
            var_name='Qh_to_room_flex_u',
            attr_name='Qh_to_room_flex_u',
            domain='Heizwärmebedarf',
            measure='HWB',
            unit='Wh/m²uncooled',
            formula='=[@[Qh_to_room_uncooled_max]]-[@[Qh_to_room_uncooled_min]]',
        )
        self.Qh_to_room_flex_c = TimeseriesMeta(
            var_name='Qh_to_room_flex_c',
            attr_name='Qh_to_room_flex_c',
            domain='Heizwärmebedarf',
            measure='HWB',
            unit='Wh/m²cooled',
            formula='=[@[Qh_to_room_cooled_max]]-[@[Qh_to_room_cooled_min]]',
        )
        self.Qh_to_room_flex_val = TimeseriesMeta(
            var_name='Qh_to_room_flex_val',
            attr_name='Qh_to_room_flex_val',
            domain='Heizwärmebedarf',
            measure='HWB',
            unit=None,
            formula='=[@[Qh_to_room_flex_u]]*NFAfrac_u+[@[Qh_to_room_flex_c]]*+NFAfrac_c',
        )
        self.Qh_to_room_flex = TimeseriesMeta(
            var_name='Qh_to_room_flex',
            attr_name='Qh_to_room_flex',
            domain='Heizwärmebedarf',
            measure='HWB',
            unit='Wh/m²NFA',
            formula='=SUMPRODUCT(sim[@[Qh_to_room_uncooled_max]:[Qh_to_room_cooled_max]],$H$4:$I$4)-[@[Qh_to_room_min]]',
        )
        self.waste_heat_potential = TimeseriesMeta(
            var_name='waste_heat_potential',
            attr_name='waste_heat_potential',
            domain='Heizwärmebedarf',
            measure=None,
            unit='Wh/m²NFA',
            formula='0',
        )
        self.Qh_min_wasteheat = TimeseriesMeta(
            var_name='Qh_min_wasteheat',
            attr_name='Qh_min_wasteheat',
            domain='Heizwärmebedarf',
            measure=None,
            unit='Wh/m²',
            formula='=MAX(0,MIN([@[waste_heat_potential]],[@[Qh_to_room_min]]))',
        )
        self.Qh_min_1el = TimeseriesMeta(
            var_name='Qh_min_1el',
            attr_name='Qh_min_1el',
            domain='Heizwärmebedarf',
            measure='Minimale Deckung raumseitig',
            unit='Wh/m²NFA',
            formula='=MIN([@[Qh_to_room_min]]-[@[Qh_min_wasteheat]],QHmax_1el_m2)',
        )
        self.Qh_min_2th = TimeseriesMeta(
            var_name='Qh_min_2th',
            attr_name='Qh_min_2th',
            domain='Heizwärmebedarf',
            measure='Minimale Deckung raumseitig',
            unit='Wh/m²NFA',
            formula='=MIN([@[Qh_to_room_min]]-SUM(sim[@[Qh_min_wasteheat]:[Qh_min_1el]]),QHmax_2th_m2)',
        )
        self.Qh_min_3el = TimeseriesMeta(
            var_name='Qh_min_3el',
            attr_name='Qh_min_3el',
            domain='Heizwärmebedarf',
            measure='Minimale Deckung raumseitig',
            unit='Wh/m²NFA',
            formula='=MIN([@[Qh_to_room_min]]-SUM(sim[@[Qh_min_wasteheat]:[Qh_min_2th]]),QHmax_3el_m2)',
        )
        self.Qh_min_4th = TimeseriesMeta(
            var_name='Qh_min_4th',
            attr_name='Qh_min_4th',
            domain='Heizwärmebedarf',
            measure='Minimale Deckung raumseitig',
            unit='Wh/m²NFA',
            formula='=MIN([@[Qh_to_room_min]]-SUM(sim[@[Qh_min_wasteheat]:[Qh_min_3el]]),QHmax_4th_m2)',
        )
        self.Qh_wasteheat_flex = TimeseriesMeta(
            var_name='Qh_wasteheat_flex',
            attr_name='Qh_wasteheat_flex',
            domain='Heizwärmebedarf',
            measure='🔥+ Flexibles Potential',
            unit='Wh/m²NFA',
            formula='=MIN([@[Qh_to_room_flex]],[@[waste_heat_potential]]-[@[Qh_min_wasteheat]])',
        )
        self.Qh_flex_1el_potential = TimeseriesMeta(
            var_name='Qh_flex_1el_potential',
            attr_name='Qh_flex_1el_potential',
            domain='Heizwärmebedarf',
            measure='🔥+ Flexibles Potential',
            unit='Wh/m²NFA',
            formula='=FLEX_heat1_use*MIN(QHmax_1el_m2-[@[Qh_min_1el]],MAX([@[Qh_to_room_flex]]-[@[Qh_wasteheat_flex]],0))',
        )
        self.Qh_flex_3el_potential = TimeseriesMeta(
            var_name='Qh_flex_3el_potential',
            attr_name='Qh_flex_3el_potential',
            domain='Heizwärmebedarf',
            measure='🔥+ Flexibles Potential',
            unit='Wh/m²NFA',
            formula='=FLEX_heat3_use*MIN(QHmax_3el_m2-[@[Qh_min_3el]],[@[Qh_to_room_flex]]-[@[Qh_wasteheat_flex]])',
        )
        self.Qc_from_room_min = TimeseriesMeta(
            var_name='Qc_from_room_min',
            attr_name='Qc_from_room_min',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN(QCmax_room_m2,[@[is_cooling_period]]*MAX(IFNA([@[Ti_passive_cooled]]-Tsetcool_max,0),0)*heat_cap_eff_cooled_m2)',
        )
        self.Qc_from_room_flex = TimeseriesMeta(
            var_name='Qc_from_room_flex',
            attr_name='Qc_from_room_flex',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN(QCmax_room_m2-[@[Qc_from_room_min]],AND([@[is_cooling_period]],NOT([@[is_heating_period]]))*MAX(IFNA([@[Ti_passive_cooled]]-Tsetcool_flex,0),0)*heat_cap_eff_cooled_m2+[@[Qc_from_room_min]])',
        )
        self.Qc_min_0fc = TimeseriesMeta(
            var_name='Qc_min_0fc',
            attr_name='Qc_min_0fc',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN([@[Qc_from_room_min]],QCmax_freecooling)',
        )
        self.Qc_min_1el = TimeseriesMeta(
            var_name='Qc_min_1el',
            attr_name='Qc_min_1el',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN([@[Qc_from_room_min]]-[@[Qc_min_0fc]],QCmax_1el)',
        )
        self.Qc_min_2th = TimeseriesMeta(
            var_name='Qc_min_2th',
            attr_name='Qc_min_2th',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN([@[Qc_from_room_min]]-SUM(sim[@[Qc_min_0fc]:[Qc_min_1el]]),QCmax_2th)',
        )
        self.Qc_min_3el = TimeseriesMeta(
            var_name='Qc_min_3el',
            attr_name='Qc_min_3el',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=MIN([@[Qc_from_room_min]]-SUM(sim[@[Qc_min_0fc]:[Qc_min_2th]]),QCmax_3el)',
        )
        self.Qc_flex_1el = TimeseriesMeta(
            var_name='Qc_flex_1el',
            attr_name='Qc_flex_1el',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=FLEX_cool1_use*MIN(QCmax_1el-[@[Qc_min_1el]],[@[Qc_from_room_flex]])',
        )
        self.Qc_flex_3el = TimeseriesMeta(
            var_name='Qc_flex_3el',
            attr_name='Qc_flex_3el',
            domain='Kühlbedarf',
            measure='Kühbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=FLEX_cool3_use*MIN(QCmax_3el-[@[Qc_min_3el]],[@[Qc_from_room_flex]])',
        )
        self.Tdhw1_0 = TimeseriesMeta(
            var_name='Tdhw1_0',
            attr_name='Tdhw1_0',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Temperatur',
            unit='°C',
            formula='=DHW_Tmin*DHW_1_is_used',
        )
        self.Tdhw2_0 = TimeseriesMeta(
            var_name='Tdhw2_0',
            attr_name='Tdhw2_0',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Temperatur',
            unit='°C',
            formula='=DHW_Tmin*DHW_2_is_used',
        )
        self.DHW_residential_kW = TimeseriesMeta(
            var_name='DHW_residential_kW',
            attr_name='DHW_residential_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_residential*Nutzung_Wohnen[@[Warmwasserbedarf_W_m2]]*DHW_demand_residential_kWhm2/DHW_default_residential_kWhm2/1000',
        )
        self.DHW_office_kW = TimeseriesMeta(
            var_name='DHW_office_kW',
            attr_name='DHW_office_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_office*Nutzung_Büro[@[Warmwasserbedarf_W_m2]]*DHW_demand_office_kWhm2/DHW_default_office_kWhm2/1000',
        )
        self.DHW_schoolsec_kW = TimeseriesMeta(
            var_name='DHW_schoolsec_kW',
            attr_name='DHW_schoolsec_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_schoolsec*Nutzung_Schule[@[Warmwasserbedarf_W_m2]]*DHW_demand_schoolsec_kWhm2/DHW_default_schoolsec_kWhm2/1000',
        )
        self.DHW_schoolprim_kW = TimeseriesMeta(
            var_name='DHW_schoolprim_kW',
            attr_name='DHW_schoolprim_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_schoolprim*Nutzung_KIGA[@[Warmwasserbedarf_W_m2]]*DHW_demand_schoolprim_kWhm2/DHW_default_schoolprim_kWhm2/1000',
        )
        self.DHW_retailsupermarket_kW = TimeseriesMeta(
            var_name='DHW_retailsupermarket_kW',
            attr_name='DHW_retailsupermarket_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_retailfood*Nutzung_Handel_Food[@[Warmwasserbedarf_W_m2]]*DHW_demand_retailfood_kWhm2/DHW_default_retailfood_kWhm2/1000',
        )
        self.DHW_retailother_kW = TimeseriesMeta(
            var_name='DHW_retailother_kW',
            attr_name='DHW_retailother_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='=NFA_retailother*Nutzung_Handel_NonFood[@[Warmwasserbedarf_W_m2]]*DHW_demand_retailother_kWhm2/DHW_default_retailother_kWhm2/1000',
        )
        self.DHW_other_kW = TimeseriesMeta(
            var_name='DHW_other_kW',
            attr_name='DHW_other_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB je Nutzung',
            unit='kW',
            formula='0',
        )
        self.DHW_1_tap_kW = TimeseriesMeta(
            var_name='DHW_1_tap_kW',
            attr_name='DHW_1_tap_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB System 1',
            unit='kW',
            formula='=SUMPRODUCT(sim[@[DHW_residential_kW]:[DHW_other_kW]],DHW_system1_shares)',
        )
        self.DHW_2_tap_kW = TimeseriesMeta(
            var_name='DHW_2_tap_kW',
            attr_name='DHW_2_tap_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB System 2',
            unit='kW',
            formula='=SUM(sim[@[DHW_residential_kW]:[DHW_other_kW]])-[@[DHW_1_tap_kW]]',
        )
        self.DHW_storage_losses_1 = TimeseriesMeta(
            var_name='DHW_storage_losses_1',
            attr_name='DHW_storage_losses_1',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Verluste',
            unit='kW',
            formula='=([@[Tdhw1_0]]-DHW_storage_env_temp_default)*DHW_losses_1*DHW_storage_1_liter*cp_water/1000',
        )
        self.DHW_storage_losses_2 = TimeseriesMeta(
            var_name='DHW_storage_losses_2',
            attr_name='DHW_storage_losses_2',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Verluste',
            unit='kW',
            formula='=([@[Tdhw2_0]]-DHW_storage_env_temp_default)*DHW_losses_2*DHW_storage_2_liter*cp_water/1000',
        )
        self.DHW_heat_demand_1_kW = TimeseriesMeta(
            var_name='DHW_heat_demand_1_kW',
            attr_name='DHW_heat_demand_1_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Entnahme',
            unit='kW',
            formula='=DHW_1_is_used*([@[DHW_storage_losses_1]]+DHW_1_incl_distribution_factor*[@[DHW_1_tap_kW]])',
        )
        self.DHW_heat_demand_2_kW = TimeseriesMeta(
            var_name='DHW_heat_demand_2_kW',
            attr_name='DHW_heat_demand_2_kW',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Entnahme',
            unit='kW',
            formula='=DHW_2_is_used*([@[DHW_storage_losses_2]]+DHW_2_incl_distribution_factor*[@[DHW_2_tap_kW]])',
        )
        self.Tdhw1_passive_losses = TimeseriesMeta(
            var_name='Tdhw1_passive_losses',
            attr_name='Tdhw1_passive_losses',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Entnahme',
            unit=None,
            formula='=[@[Tdhw1_0]]-IFERROR([@[DHW_heat_demand_1_kW]]*1000/DHW_storage_1_liter/cp_water,0)',
        )
        self.Tdhw2_passive_losses = TimeseriesMeta(
            var_name='Tdhw2_passive_losses',
            attr_name='Tdhw2_passive_losses',
            domain='Warmwasser-Wärmebedarf',
            measure='WW Entnahme',
            unit=None,
            formula='=[@[Tdhw2_0]]-IFERROR([@[DHW_heat_demand_2_kW]]*1000/DHW_storage_2_liter/cp_water,0)',
        )
        self.Qdhw_1_min = TimeseriesMeta(
            var_name='Qdhw_1_min',
            attr_name='Qdhw_1_min',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Minimum',
            unit='Wh/m²NFA',
            formula='=MAX(0,(DHW_Tmin-[@[Tdhw1_passive_losses]])*DHW_storage_1_liter*cp_water)*per_NFA',
        )
        self.Qdhw_2_min = TimeseriesMeta(
            var_name='Qdhw_2_min',
            attr_name='Qdhw_2_min',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Minimum',
            unit='Wh/m²NFA',
            formula='=MAX(0,(DHW_Tmin-[@[Tdhw2_passive_losses]])*DHW_storage_2_liter*cp_water)*per_NFA',
        )
        self.Qdhw_min = TimeseriesMeta(
            var_name='Qdhw_min',
            attr_name='Qdhw_min',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Minimum',
            unit='Wh/m²NFA',
            formula='=SUM(sim[@[Qdhw_1_min]:[Qdhw_2_min]])',
        )
        self.Qdhw_1_flexpotential = TimeseriesMeta(
            var_name='Qdhw_1_flexpotential',
            attr_name='Qdhw_1_flexpotential',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Flexibel',
            unit='Wh/m²NFA',
            formula='=flex_dhw_use*DHW_1_is_electric*MAX(0,(DHW_Tmax-[@[Tdhw1_passive_losses]])*DHW_storage_1_liter*cp_water*per_NFA-[@[Qdhw_1_min]])',
        )
        self.Qdhw_2_flexpotential = TimeseriesMeta(
            var_name='Qdhw_2_flexpotential',
            attr_name='Qdhw_2_flexpotential',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Flexibel',
            unit='Wh/m²NFA',
            formula='=flex_dhw_use*DHW_2_is_electric*MAX(0,(DHW_Tmax-[@[Tdhw2_passive_losses]])*DHW_storage_2_liter*cp_water*per_NFA-[@[Qdhw_2_min]])',
        )
        self.Edhw_1_min_el = TimeseriesMeta(
            var_name='Edhw_1_min_el',
            attr_name='Edhw_1_min_el',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Flexibel',
            unit='Wh/m²NFA',
            formula='=[@[Qdhw_1_min]]*(DHW_conversion_1*DHW_1_is_electric+DHW_1_el_aux)',
        )
        self.Edhw_2_min_el = TimeseriesMeta(
            var_name='Edhw_2_min_el',
            attr_name='Edhw_2_min_el',
            domain='Warmwasser-Wärmebedarf',
            measure='WWWB Flexibel',
            unit='Wh/m²NFA',
            formula='=[@[Qdhw_2_min]]*(DHW_conversion_2*DHW_2_is_electric+DHW_2_el_aux)',
        )
        self.Spalte12 = TimeseriesMeta(
            var_name='Spalte12',
            attr_name='Spalte12',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte122 = TimeseriesMeta(
            var_name='Spalte122',
            attr_name='Spalte122',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte123 = TimeseriesMeta(
            var_name='Spalte123',
            attr_name='Spalte123',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.EVd_res = TimeseriesMeta(
            var_name='EVd_res',
            attr_name='EVd_res',
            domain='E-Mobilität',
            measure='EV Anzahl Vor Ort',
            unit='Cars',
            formula='=EV_count_residential*mob[@[p_res_d]]',
        )
        self.EVd_work = TimeseriesMeta(
            var_name='EVd_work',
            attr_name='EVd_work',
            domain='E-Mobilität',
            measure='EV Anzahl Vor Ort',
            unit=None,
            formula='=EV_count_work*mob[@[p_work_d]]',
        )
        self.EVd_retail = TimeseriesMeta(
            var_name='EVd_retail',
            attr_name='EVd_retail',
            domain='E-Mobilität',
            measure='EV Anzahl Vor Ort',
            unit=None,
            formula='=EV_count_retail*mob[@[p_retail_d]]',
        )
        self.EV_SOC0_d_res = TimeseriesMeta(
            var_name='EV_SOC0_d_res',
            attr_name='EV_SOC0_d_res',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit='%',
            formula='0.5',
        )
        self.EV_SOC0_d_work = TimeseriesMeta(
            var_name='EV_SOC0_d_work',
            attr_name='EV_SOC0_d_work',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit='%',
            formula='0.5',
        )
        self.EV_SOC0_d_retail = TimeseriesMeta(
            var_name='EV_SOC0_d_retail',
            attr_name='EV_SOC0_d_retail',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit='%',
            formula='0.5',
        )
        self.EV_SOC0_a_res = TimeseriesMeta(
            var_name='EV_SOC0_a_res',
            attr_name='EV_SOC0_a_res',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit=None,
            formula='0.5',
        )
        self.EV_SOC0_a_work = TimeseriesMeta(
            var_name='EV_SOC0_a_work',
            attr_name='EV_SOC0_a_work',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit=None,
            formula='0.5',
        )
        self.EV_SOC0_a_retail = TimeseriesMeta(
            var_name='EV_SOC0_a_retail',
            attr_name='EV_SOC0_a_retail',
            domain='E-Mobilität',
            measure='EV State-of-Charge',
            unit=None,
            formula='0.5',
        )
        self.EV_maxpower = TimeseriesMeta(
            var_name='EV_maxpower',
            attr_name='EV_maxpower',
            domain='E-Mobilität',
            measure=None,
            unit='Wh/m²',
            formula='=MIN(SUM(sim[@[EVd_res]:[EVd_retail]]),EV_charging_stations)*EV_charging_station_power*1000*per_NFA',
        )
        self.Eev_Cmin_res = TimeseriesMeta(
            var_name='Eev_Cmin_res',
            attr_name='Eev_Cmin_res',
            domain='E-Mobilität',
            measure='Beladung Minimum',
            unit='Wh/m²',
            formula='=MIN(MIN([@[EVd_res]],EV_charging_stations)*EV_charging_station_power,[@[EVd_res]]*EV_battsize_kWh*MIN(EV_max_charging_power_ratio,MAX(EV_soc_minimum-[@[EV_SOC0_d_res]],0))*1000*per_NFA)',
        )
        self.Eev_Cmin_work = TimeseriesMeta(
            var_name='Eev_Cmin_work',
            attr_name='Eev_Cmin_work',
            domain='E-Mobilität',
            measure='Beladung Minimum',
            unit='Wh/m²',
            formula='=MIN([@[EV_maxpower]]-[@[Eev_Cmin_res]],[@[EVd_work]]*EV_battsize_kWh*MIN(EV_max_charging_power_ratio,MAX(EV_soc_min_work-[@[EV_SOC0_d_work]],0))*1000*per_NFA)',
        )
        self.Eev_Cmin_retail = TimeseriesMeta(
            var_name='Eev_Cmin_retail',
            attr_name='Eev_Cmin_retail',
            domain='E-Mobilität',
            measure='Beladung Minimum',
            unit='Wh/m²',
            formula='=MIN([@[EV_maxpower]]-[@[Eev_Cmin_res]]-[@[Eev_Cmin_work]],[@[EVd_retail]]*EV_battsize_kWh*MIN(EV_max_charging_power_ratio,MAX(EV_soc_min_retail-[@[EV_SOC0_d_retail]],0))*1000*per_NFA)',
        )
        self.Eev_Cmin = TimeseriesMeta(
            var_name='Eev_Cmin',
            attr_name='Eev_Cmin',
            domain='E-Mobilität',
            measure='Beladung Minimum',
            unit='Wh/m²',
            formula='=SUM(sim[@[Eev_Cmin_res]:[Eev_Cmin_retail]])',
        )
        self.Eev_Cflex_pot_res = TimeseriesMeta(
            var_name='Eev_Cflex_pot_res',
            attr_name='Eev_Cflex_pot_res',
            domain='E-Mobilität',
            measure='Beladung Maximum',
            unit='Wh/m²',
            formula='=MIN([@[EV_maxpower]]-[@[Eev_Cmin]],[@[EVd_res]]*EV_battsize_kWh*MAX(MIN(1-[@[EV_SOC0_d_res]],EV_max_charging_power_ratio-MAX(EV_soc_minimum-[@[EV_SOC0_d_res]],0)),0)*1000*per_NFA)',
        )
        self.Eev_Cflex_pot_work = TimeseriesMeta(
            var_name='Eev_Cflex_pot_work',
            attr_name='Eev_Cflex_pot_work',
            domain='E-Mobilität',
            measure='Beladung Maximum',
            unit='Wh/m²',
            formula='=MIN([@[EV_maxpower]]-[@[Eev_Cmin]]-[@[Eev_Cflex_pot_res]],[@[EVd_work]]*EV_battsize_kWh*MAX(MIN(1-[@[EV_SOC0_d_work]],EV_max_charging_power_ratio-MAX(EV_soc_min_work-[@[EV_SOC0_d_work]],0)),0)*1000*per_NFA)',
        )
        self.Eev_Cflex_pot_retail = TimeseriesMeta(
            var_name='Eev_Cflex_pot_retail',
            attr_name='Eev_Cflex_pot_retail',
            domain='E-Mobilität',
            measure='Beladung Maximum',
            unit='Wh/m²',
            formula='=MIN([@[EV_maxpower]]-[@[Eev_Cmin]]-[@[Eev_Cflex_pot_res]]-[@[Eev_Cflex_pot_work]],[@[EVd_retail]]*EV_battsize_kWh*MAX(MIN(1-[@[EV_SOC0_d_retail]],EV_max_charging_power_ratio-MAX(EV_soc_min_retail-[@[EV_SOC0_d_retail]],0)),0)*1000*per_NFA)',
        )
        self.Eev_Cflex_pot = TimeseriesMeta(
            var_name='Eev_Cflex_pot',
            attr_name='Eev_Cflex_pot',
            domain='E-Mobilität',
            measure='Beladung Maximum',
            unit='Wh/m²',
            formula='=SUM(sim[@[Eev_Cflex_pot_res]:[Eev_Cflex_pot_retail]])',
        )
        self.Eev_Dflex_pot_res = TimeseriesMeta(
            var_name='Eev_Dflex_pot_res',
            attr_name='Eev_Dflex_pot_res',
            domain='E-Mobilität',
            measure='Entladung Maximum',
            unit='Wh/m²',
            formula='=ev_bidirectional_use*[@[EVd_res]]*EV_battsize_kWh*MIN(MAX([@[EV_SOC0_d_res]]-EV_soc_min_discharge,0),EV_max_charging_power_ratio)*1000*per_NFA',
        )
        self.Eev_Dflex_pot_work = TimeseriesMeta(
            var_name='Eev_Dflex_pot_work',
            attr_name='Eev_Dflex_pot_work',
            domain='E-Mobilität',
            measure='Entladung Maximum',
            unit='Wh/m²',
            formula='=FALSE*[@[EVd_work]]*EV_battsize_kWh*MIN(MAX([@[EV_SOC0_d_work]]-EV_soc_min_discharge,0),EV_max_charging_power_ratio)*1000*per_NFA',
        )
        self.Eev_Dflex_pot_retail = TimeseriesMeta(
            var_name='Eev_Dflex_pot_retail',
            attr_name='Eev_Dflex_pot_retail',
            domain='E-Mobilität',
            measure='Entladung Maximum',
            unit='Wh/m²',
            formula='=FALSE*[@[EVd_retail]]*EV_battsize_kWh*MIN(MAX([@[EV_SOC0_d_retail]]-EV_soc_min_discharge,0),EV_max_charging_power_ratio)*1000*per_NFA',
        )
        self.Eev_Dflex_pot = TimeseriesMeta(
            var_name='Eev_Dflex_pot',
            attr_name='Eev_Dflex_pot',
            domain='E-Mobilität',
            measure='Entladung Maximum',
            unit='Wh/m²',
            formula='=SUM(sim[@[Eev_Dflex_pot_res]:[Eev_Dflex_pot_retail]])',
        )
        self.Eev_S_res = TimeseriesMeta(
            var_name='Eev_S_res',
            attr_name='Eev_S_res',
            domain='E-Mobilität',
            measure='Entladung Fahrten',
            unit='Wh/m²',
            formula='=-EV_mileage_residential*EV_demand_kWhpkm*mob[@[Anteil JPkm]]*1000*per_NFA',
        )
        self.Eev_S_work = TimeseriesMeta(
            var_name='Eev_S_work',
            attr_name='Eev_S_work',
            domain='E-Mobilität',
            measure='Entladung Fahrten',
            unit='Wh/m²',
            formula='=-EV_mileage_work*EV_demand_kWhpkm*mob[@[Anteil JPkm]]*1000*per_NFA',
        )
        self.Eev_S_retail = TimeseriesMeta(
            var_name='Eev_S_retail',
            attr_name='Eev_S_retail',
            domain='E-Mobilität',
            measure='Entladung Fahrten',
            unit='Wh/m²',
            formula='=-EV_mileage_retail*EV_demand_kWhpkm*mob[@[Anteil JPkm]]*1000*per_NFA*mobility_is_included',
        )
        self.Eev_Cext_res = TimeseriesMeta(
            var_name='Eev_Cext_res',
            attr_name='Eev_Cext_res',
            domain='E-Mobilität',
            measure='Beladung Außerhalb',
            unit='Wh/m²',
            formula='=(EV_count_residential-[@[EVd_res]])*EV_battsize_kWh*MIN(EV_max_charging_power_ratio*10%,MAX(EV_soc_min_ext-[@[EV_SOC0_a_res]],0))*1000*per_NFA',
        )
        self.Eev_Cext_work = TimeseriesMeta(
            var_name='Eev_Cext_work',
            attr_name='Eev_Cext_work',
            domain='E-Mobilität',
            measure='Beladung Außerhalb',
            unit='Wh/m²',
            formula='=(EV_count_work-[@[EVd_work]])*EV_battsize_kWh*MIN(EV_max_charging_power_ratio*10%,MAX(EV_soc_min_ext-[@[EV_SOC0_a_work]],0))*1000*per_NFA',
        )
        self.Eev_Cext_retail = TimeseriesMeta(
            var_name='Eev_Cext_retail',
            attr_name='Eev_Cext_retail',
            domain='E-Mobilität',
            measure='Beladung Außerhalb',
            unit='Wh/m²',
            formula='=(EV_count_retail-[@[EVd_retail]])*EV_battsize_kWh*MIN(EV_max_charging_power_ratio*10%,MAX(EV_soc_min_ext-[@[EV_SOC0_a_retail]],0))*1000*per_NFA',
        )
        self.Eev_min_intake = TimeseriesMeta(
            var_name='Eev_min_intake',
            attr_name='Eev_min_intake',
            domain='E-Mobilität',
            measure='Beladung Minimum',
            unit='Wh/m²',
            formula='=[@[Eev_Cmin]]*EV_charging_losses_surcharge_factor',
        )
        self.Eev_flex_intake = TimeseriesMeta(
            var_name='Eev_flex_intake',
            attr_name='Eev_flex_intake',
            domain='E-Mobilität',
            measure='Beladung Maximum',
            unit='Wh/m²',
            formula='=[@[Eev_Cflex_pot]]*EV_charging_losses_surcharge_factor',
        )
        self.Spalte6 = TimeseriesMeta(
            var_name='Spalte6',
            attr_name='Spalte6',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.BATT_cap_0 = TimeseriesMeta(
            var_name='BATT_cap_0',
            attr_name='BATT_cap_0',
            domain='Batterie',
            measure='Batterie',
            unit='Wh/m²',
            formula='=Batt_SOC_init*Batt_cap_Wh_per_NFA',
        )
        self.Batt_auto_discharge = TimeseriesMeta(
            var_name='Batt_auto_discharge',
            attr_name='Batt_auto_discharge',
            domain='Batterie',
            measure='Batterie',
            unit='Wh/m²',
            formula='=[@[BATT_cap_0]]*Batt_auto_discharge_factor',
        )
        self.Batt_cap_after_losses = TimeseriesMeta(
            var_name='Batt_cap_after_losses',
            attr_name='Batt_cap_after_losses',
            domain='Batterie',
            measure='Batterie',
            unit='Wh/m²',
            formula='=Batt_is_used*([@[BATT_cap_0]]-[@[Batt_auto_discharge]])',
        )
        self.Batt_max_energy_input = TimeseriesMeta(
            var_name='Batt_max_energy_input',
            attr_name='Batt_max_energy_input',
            domain='Batterie',
            measure='Batterie',
            unit='Wh/m²',
            formula='=Batt_is_used*(Batt_cap_Wh_per_NFA-[@[Batt_cap_after_losses]])',
        )
        self.Spalte88 = TimeseriesMeta(
            var_name='Spalte88',
            attr_name='Spalte88',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte5 = TimeseriesMeta(
            var_name='Spalte5',
            attr_name='Spalte5',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Eh_min_wasteheat = TimeseriesMeta(
            var_name='Eh_min_wasteheat',
            attr_name='Eh_min_wasteheat',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=(QH_aux_wasteheat)*[@[Qh_min_wasteheat]]',
        )
        self.Eh_min_1el = TimeseriesMeta(
            var_name='Eh_min_1el',
            attr_name='Eh_min_1el',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=(QH_generation_eff_1el+QH_aux_el_to_th_1el)*[@[Qh_min_1el]]*(1+QH_distr_loss_1el)',
        )
        self.Eh_min_2th = TimeseriesMeta(
            var_name='Eh_min_2th',
            attr_name='Eh_min_2th',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=QH_aux_el_to_th_2th*[@[Qh_min_2th]]*(1+QH_distr_loss_2th)',
        )
        self.Eh_min_3el = TimeseriesMeta(
            var_name='Eh_min_3el',
            attr_name='Eh_min_3el',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=(QH_generation_eff_3el+QH_aux_el_to_th_3el)*[@[Qh_min_3el]]*(1+QH_distr_loss_3el)',
        )
        self.Eh_min_4th = TimeseriesMeta(
            var_name='Eh_min_4th',
            attr_name='Eh_min_4th',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=QH_aux_el_to_th_4th*[@[Qh_min_4th]]*(1+QH_distr_loss_4th)',
        )
        self.Eh_min = TimeseriesMeta(
            var_name='Eh_min',
            attr_name='Eh_min',
            domain='Strom Mindestbedarfe',
            measure='Heizen Minimum',
            unit='Wh_el/m²',
            formula='=SUM(sim[@[Eh_min_wasteheat]:[Eh_min_4th]])',
        )
        self.Ec_min_freecooling = TimeseriesMeta(
            var_name='Ec_min_freecooling',
            attr_name='Ec_min_freecooling',
            domain='Strom Mindestbedarfe',
            measure='Kühlen Minimum',
            unit='Wh_el/m²',
            formula='=[@[Qc_min_0fc]]*QC_aux_fc',
        )
        self.Ec_min_1el = TimeseriesMeta(
            var_name='Ec_min_1el',
            attr_name='Ec_min_1el',
            domain='Strom Mindestbedarfe',
            measure='Kühlen Minimum',
            unit='Wh_el/m²',
            formula='=$I$4*[@[Qc_min_1el]]*(1+QC_distr_losses_1el)*(QC_to_EC_1+QC_aux_1el)',
        )
        self.Ec_min_2th = TimeseriesMeta(
            var_name='Ec_min_2th',
            attr_name='Ec_min_2th',
            domain='Strom Mindestbedarfe',
            measure='Kühlen Minimum',
            unit='Wh_el/m²',
            formula='=$I$4*[@[Qc_min_2th]]*(1+QC_distr_losses_2th)*(QC_aux_2th)',
        )
        self.Ec_min_3el = TimeseriesMeta(
            var_name='Ec_min_3el',
            attr_name='Ec_min_3el',
            domain='Strom Mindestbedarfe',
            measure='Kühlen Minimum',
            unit='Wh_el/m²',
            formula='=$I$4*[@[Qc_min_3el]]*(1+QC_distr_losses_3el)*(QC_to_EC_3+QC_aux_3el)',
        )
        self.Ec_min = TimeseriesMeta(
            var_name='Ec_min',
            attr_name='Ec_min',
            domain='Strom Mindestbedarfe',
            measure='Kühlen Minimum',
            unit='Wh_el/m²',
            formula='=SUM(sim[@[Ec_min_freecooling]:[Ec_min_3el]])',
        )
        self.Ev_residential = TimeseriesMeta(
            var_name='Ev_residential',
            attr_name='Ev_residential',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_residential*Nutzung_Wohnen[@[Lüfterstrom_W_m2]]*NFA_residential*per_NFA',
        )
        self.Ev_office = TimeseriesMeta(
            var_name='Ev_office',
            attr_name='Ev_office',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_office*Nutzung_Büro[@[Lüfterstrom_W_m2]]*NFA_office*per_NFA',
        )
        self.Ev_edusec = TimeseriesMeta(
            var_name='Ev_edusec',
            attr_name='Ev_edusec',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_school_sec*Nutzung_Schule[@[Lüfterstrom_W_m2]]*NFA_schoolsec*per_NFA',
        )
        self.Ev_eduprim = TimeseriesMeta(
            var_name='Ev_eduprim',
            attr_name='Ev_eduprim',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_school_prim*Nutzung_KIGA[@[Lüfterstrom_W_m2]]*NFA_schoolprim*per_NFA',
        )
        self.Ev_retfood = TimeseriesMeta(
            var_name='Ev_retfood',
            attr_name='Ev_retfood',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_retail_food*Nutzung_Handel_Food[@[Lüfterstrom_W_m2]]*NFA_retailfood*per_NFA',
        )
        self.Ev_retail = TimeseriesMeta(
            var_name='Ev_retail',
            attr_name='Ev_retail',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=Ev_scale_retail_other*Nutzung_Handel_NonFood[@[Lüfterstrom_W_m2]]*NFA_retailother*per_NFA',
        )
        self.Ev_otherusage = TimeseriesMeta(
            var_name='Ev_otherusage',
            attr_name='Ev_otherusage',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='0',
        )
        self.Ev_min = TimeseriesMeta(
            var_name='Ev_min',
            attr_name='Ev_min',
            domain='Strom Mindestbedarfe',
            measure='Lüftung Minimum',
            unit='Wh_el/m²',
            formula='=SUM(sim[@[Ev_residential]:[Ev_otherusage]])',
        )
        self.Eaux = TimeseriesMeta(
            var_name='Eaux',
            attr_name='Eaux',
            domain='Strom Mindestbedarfe',
            measure='Aux',
            unit='Wh_el/m²',
            formula='=Nutzungsprofil[@[Aufzug, Regelung etc._W_m2]]',
        )
        self.Elight_office = TimeseriesMeta(
            var_name='Elight_office',
            attr_name='Elight_office',
            domain='Strom Mindestbedarfe',
            measure='💡Beleuchtung',
            unit='Wh_el/m²office',
            formula='=lighting_factor_office*IF(Nutzung_Büro[@[Betriebszeit_-]]>0,1,0)*(Plight_min_office*(1-daylightcontr_office)+daylightcontr_office*IF([@[Irr_horizontal]]*100*Daylightcoefficient_office>illuminance_min_office,0,Plight_max_office))',
        )
        self.Elight_schoolsec = TimeseriesMeta(
            var_name='Elight_schoolsec',
            attr_name='Elight_schoolsec',
            domain='Strom Mindestbedarfe',
            measure='💡Beleuchtung',
            unit='Wh_el/m²schoolsec',
            formula='=lighting_factor_schoolsec*IF(Nutzung_Schule[@[Personen_Pers_m2]]>0,1,0)*(Plight_min_schoolsec*(1-daylightcontr_schoolsec)+daylightcontr_schoolsec*IF([@[Irr_horizontal]]*100*Daylightcoefficient_schoolsec>illuminance_min_schoolsec,0,Plight_max_schoolsec))',
        )
        self.Elight_schoolprim = TimeseriesMeta(
            var_name='Elight_schoolprim',
            attr_name='Elight_schoolprim',
            domain='Strom Mindestbedarfe',
            measure='💡Beleuchtung',
            unit='Wh_el/m²schoolprim',
            formula='=lighting_factor_schoolprim*IF(Nutzung_KIGA[@[Personen_Pers_m2]]>0,1,0)*(Plight_min_schoolprim*(1-daylightcontr_schoolprim)+daylightcontr_schoolprim*IF([@[Irr_horizontal]]*100*Daylightcoefficient_schoolprim>illuminance_min_schoolprim,0,Plight_max_schoolprim))',
        )
        self.Elight = TimeseriesMeta(
            var_name='Elight',
            attr_name='Elight',
            domain='Strom Mindestbedarfe',
            measure='💡Beleuchtung',
            unit='Wh_el/m²',
            formula='=per_NFA*([@[Elight_office]]*NFA_office+[@[Elight_schoolsec]]*NFA_schoolsec+[@[Elight_schoolprim]]*NFA_schoolprim+Nutzung_Handel_Food[@[Beleuchtung_W_m2]]*lighting_factor_retailfood*NFA_retailfood+Nutzung_Handel_NonFood[@[Beleuchtung_W_m2]]*lighting_factor_retailother*NFA_retailother)',
        )
        self.Edhw_min = TimeseriesMeta(
            var_name='Edhw_min',
            attr_name='Edhw_min',
            domain='Strom Mindestbedarfe',
            measure='WW Minimum',
            unit='Wh_el/m²',
            formula='=[@[Edhw_1_min_el]]+[@[Edhw_2_min_el]]',
        )
        self.Ehvac_min = TimeseriesMeta(
            var_name='Ehvac_min',
            attr_name='Ehvac_min',
            domain='Strom Mindestbedarfe',
            measure='HKLS Minimum',
            unit='Wh_el/m²',
            formula='=[@[Eh_min]]+[@[Ec_min]]+[@[Ev_min]]+[@[Edhw_min]]',
        )
        self.Test = TimeseriesMeta(
            var_name='Test',
            attr_name='Test',
            domain='Strom Mindestbedarfe',
            measure=None,
            unit=None,
            formula='=INDEX(Eplug_hotd[residential],[@[hour_of_the_day]]+IF(WEEKDAY([@[day_of_the_year]],2)<6,1,25))*INDEX(Eplug_month[residential],[@[Monat_nr]])',
        )
        self.E_plugAuxLight = TimeseriesMeta(
            var_name='E_plugAuxLight',
            attr_name='E_plugAuxLight',
            domain='Strom Mindestbedarfe',
            measure='👤Nutzerstrom',
            unit='Wh_el/m²',
            formula='=Nutzungsprofil[@[Nutzerstrom_W_m2]]+[@Eaux]+[@Elight]',
        )
        self.Eev_min = TimeseriesMeta(
            var_name='Eev_min',
            attr_name='Eev_min',
            domain='Strom Mindestbedarfe',
            measure='E-Cars',
            unit='Wh_el/m²',
            formula='=[@[Eev_min_intake]]',
        )
        self.Ed_min = TimeseriesMeta(
            var_name='Ed_min',
            attr_name='Ed_min',
            domain='Strom Mindestbedarfe',
            measure=None,
            unit='Wh_el/m²',
            formula='=[@[Ehvac_min]]+[@[E_plugAuxLight]]+[@[Eev_min]]',
        )
        self.Space3 = TimeseriesMeta(
            var_name='Space3',
            attr_name='Space3',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Eh_el1_flex_potential = TimeseriesMeta(
            var_name='Eh_el1_flex_potential',
            attr_name='Eh_el1_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=(QH_generation_eff_1el+QH_aux_el_to_th_1el)*[@[Qh_flex_1el_potential]]*(1+QH_distr_loss_1el)',
        )
        self.Eh_el3_flex_potential = TimeseriesMeta(
            var_name='Eh_el3_flex_potential',
            attr_name='Eh_el3_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=(QH_generation_eff_3el+QH_aux_el_to_th_3el)*[@[Qh_flex_3el_potential]]*(1+QH_distr_loss_3el)',
        )
        self.Ec_el1_flex_potential = TimeseriesMeta(
            var_name='Ec_el1_flex_potential',
            attr_name='Ec_el1_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=$I$4*[@[Qc_flex_1el]]*(1+QC_distr_losses_1el)*(QC_to_EC_1+QC_aux_1el)',
        )
        self.Ec_el3_flex_potential = TimeseriesMeta(
            var_name='Ec_el3_flex_potential',
            attr_name='Ec_el3_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=$I$4*[@[Qc_flex_3el]]*(1+QC_distr_losses_3el)*(QC_to_EC_3+QC_aux_3el)',
        )
        self.Edhw_1_flex_potential = TimeseriesMeta(
            var_name='Edhw_1_flex_potential',
            attr_name='Edhw_1_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=DHW_1_is_electric*[@[Qdhw_1_flexpotential]]*(DHW_1_el_aux+DHW_conversion_1)',
        )
        self.Edhw_2_flex_potential = TimeseriesMeta(
            var_name='Edhw_2_flex_potential',
            attr_name='Edhw_2_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=DHW_2_is_electric*[@[Qdhw_2_flexpotential]]*(DHW_2_el_aux+DHW_conversion_2)',
        )
        self.Eev_flex_potential = TimeseriesMeta(
            var_name='Eev_flex_potential',
            attr_name='Eev_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=[@[Eev_flex_intake]]',
        )
        self.Ebatt_charge_potential = TimeseriesMeta(
            var_name='Ebatt_charge_potential',
            attr_name='Ebatt_charge_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit='Wh/m²',
            formula='=IFERROR(Batt_is_used*MIN(Batt_max_power_specific,[@[Batt_max_energy_input]]/Batt_eff_factor_charge),0)',
        )
        self.Etotal_flex_potential = TimeseriesMeta(
            var_name='Etotal_flex_potential',
            attr_name='Etotal_flex_potential',
            domain='FLEX Speicher Potential',
            measure='Strom Flexibel Maximal zusätzlich',
            unit=None,
            formula='=SUM(sim[@[Eh_el1_flex_potential]:[Ebatt_charge_potential]])',
        )
        self.Space13 = TimeseriesMeta(
            var_name='Space13',
            attr_name='Space13',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.PV_yield = TimeseriesMeta(
            var_name='PV_yield',
            attr_name='PV_yield',
            domain='PV Nutzung',
            measure='Ertrag',
            unit='Wh/m²',
            formula='=PV_is_used*PV_scale*PV_efficiency*pv_profiles[@[Gewählte Variante]]*1000*per_NFA',
        )
        self.PV_to_user = TimeseriesMeta(
            var_name='PV_to_user',
            attr_name='PV_to_user',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=MIN([@[PV_yield]],[@[E_plugAuxLight]])',
        )
        self.PV_to_Eh_min = TimeseriesMeta(
            var_name='PV_to_Eh_min',
            attr_name='PV_to_Eh_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit=None,
            formula='=MIN([@[Eh_min]],[@[PV_yield]]-[@[PV_to_user]])',
        )
        self.PV_to_Ec_min = TimeseriesMeta(
            var_name='PV_to_Ec_min',
            attr_name='PV_to_Ec_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit=None,
            formula='=MIN([@[Ec_min]],[@[PV_yield]]-SUM(sim[@[PV_to_user]:[PV_to_Eh_min]]))',
        )
        self.PV_to_Edhw_min = TimeseriesMeta(
            var_name='PV_to_Edhw_min',
            attr_name='PV_to_Edhw_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit=None,
            formula='=MIN([@[Edhw_min]],[@[PV_yield]]-SUM(sim[@[PV_to_user]:[PV_to_Ec_min]]))',
        )
        self.PV_to_Ev_min = TimeseriesMeta(
            var_name='PV_to_Ev_min',
            attr_name='PV_to_Ev_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit=None,
            formula='=MIN([@[Ev_min]],[@[PV_yield]]-SUM(sim[@[PV_to_user]:[PV_to_Edhw_min]]))',
        )
        self.Valid_PV_direct_HVAC_use = TimeseriesMeta(
            var_name='Valid_PV_direct_HVAC_use',
            attr_name='Valid_PV_direct_HVAC_use',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit=None,
            formula='=IF(SUM(sim[@[PV_to_Eh_min]:[PV_to_Ev_min]])-[@[PV_to_HVAC_min]]<0.00000001,1,0)',
        )
        self.PV_to_HVAC_min = TimeseriesMeta(
            var_name='PV_to_HVAC_min',
            attr_name='PV_to_HVAC_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=MIN([@[PV_yield]]-[@[PV_to_user]],[@[Eh_min]]+[@[Ec_min]]+[@[Edhw_min]]+[@[Ev_min]])',
        )
        self.PV_to_Eev_min = TimeseriesMeta(
            var_name='PV_to_Eev_min',
            attr_name='PV_to_Eev_min',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=MIN([@[PV_yield]]-[@[PV_to_user]]-[@[PV_to_HVAC_min]],[@[Eev_min]])',
        )
        self.PV_total_direct_use = TimeseriesMeta(
            var_name='PV_total_direct_use',
            attr_name='PV_total_direct_use',
            domain='PV Nutzung',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=[@[PV_to_user]]+[@[PV_to_HVAC_min]]+[@[PV_to_Eev_min]]',
        )
        self.PV_surplus = TimeseriesMeta(
            var_name='PV_surplus',
            attr_name='PV_surplus',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=[@[PV_yield]]-[@[PV_total_direct_use]]',
        )
        self.PV_to_Eh_flex_1el = TimeseriesMeta(
            var_name='PV_to_Eh_flex_1el',
            attr_name='PV_to_Eh_flex_1el',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[PV_surplus]],[@[Eh_el1_flex_potential]])',
        )
        self.PV_to_Eh_flex_3el = TimeseriesMeta(
            var_name='PV_to_Eh_flex_3el',
            attr_name='PV_to_Eh_flex_3el',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[PV_surplus]],[@[Eh_el3_flex_potential]])',
        )
        self.PV_to_Ec_flex_1el = TimeseriesMeta(
            var_name='PV_to_Ec_flex_1el',
            attr_name='PV_to_Ec_flex_1el',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[Ec_el1_flex_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Eh_flex_3el]]))',
        )
        self.PV_to_Ec_flex_3el = TimeseriesMeta(
            var_name='PV_to_Ec_flex_3el',
            attr_name='PV_to_Ec_flex_3el',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[Ec_el3_flex_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Eh_flex_3el]]))',
        )
        self.PV_to_Edhw1_flex = TimeseriesMeta(
            var_name='PV_to_Edhw1_flex',
            attr_name='PV_to_Edhw1_flex',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[Edhw_1_flex_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Ec_flex_3el]]))',
        )
        self.PV_to_Edhw2_flex = TimeseriesMeta(
            var_name='PV_to_Edhw2_flex',
            attr_name='PV_to_Edhw2_flex',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[Edhw_2_flex_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Ec_flex_3el]]))',
        )
        self.PV_to_Eev_flex = TimeseriesMeta(
            var_name='PV_to_Eev_flex',
            attr_name='PV_to_Eev_flex',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*MIN([@[Eev_flex_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Edhw2_flex]]))',
        )
        self.PV_to_Batt = TimeseriesMeta(
            var_name='PV_to_Batt',
            attr_name='PV_to_Batt',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used*Batt_is_used*MIN([@[Ebatt_charge_potential]],[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_Eev_flex]]))',
        )
        self.PV_to_Storage = TimeseriesMeta(
            var_name='PV_to_Storage',
            attr_name='PV_to_Storage',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used',
        )
        self.PV_to_epatron = TimeseriesMeta(
            var_name='PV_to_epatron',
            attr_name='PV_to_epatron',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=FLEX_PV_is_used',
        )
        self.PV_total_flex_use = TimeseriesMeta(
            var_name='PV_total_flex_use',
            attr_name='PV_total_flex_use',
            domain='PV Nutzung',
            measure='Speicherbeladung',
            unit=None,
            formula='=SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_epatron]])',
        )
        self.PV_to_Egrid = TimeseriesMeta(
            var_name='PV_to_Egrid',
            attr_name='PV_to_Egrid',
            domain='PV Nutzung',
            measure='Netzeinspeisung',
            unit='Wh/m²',
            formula='=[@[PV_surplus]]-SUM(sim[@[PV_to_Eh_flex_1el]:[PV_to_epatron]])',
        )
        self.Batt_discharge_potential = TimeseriesMeta(
            var_name='Batt_discharge_potential',
            attr_name='Batt_discharge_potential',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit='Wh/m²',
            formula='=Batt_is_used*NOT(AND(Batt_is_not_used_during_signals,[@Signal]))*MIN(Batt_max_power_specific,[@[Batt_cap_after_losses]]*Batt_eff_factor_discharge)',
        )
        self.Batt_to_user = TimeseriesMeta(
            var_name='Batt_to_user',
            attr_name='Batt_to_user',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit='Wh/m²',
            formula='=MIN(([@[E_plugAuxLight]]-[@[PV_to_user]]),[@[Batt_discharge_potential]])*Batt_is_used_for_plugloads',
        )
        self.Batt_to_Eh_min = TimeseriesMeta(
            var_name='Batt_to_Eh_min',
            attr_name='Batt_to_Eh_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit=None,
            formula='=MIN(([@[Eh_min]]-[@[PV_to_Eh_min]]),[@[Batt_discharge_potential]]-[@[Batt_to_user]])*Batt_is_used_for_HVACminimum',
        )
        self.Batt_to_Ec_min = TimeseriesMeta(
            var_name='Batt_to_Ec_min',
            attr_name='Batt_to_Ec_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit=None,
            formula='=MIN(([@[Ec_min]]-[@[PV_to_Ec_min]]),[@[Batt_discharge_potential]]-SUM(sim[@[Batt_to_user]:[Batt_to_Eh_min]]))*Batt_is_used_for_HVACminimum',
        )
        self.Batt_to_Edhw_min = TimeseriesMeta(
            var_name='Batt_to_Edhw_min',
            attr_name='Batt_to_Edhw_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit=None,
            formula='=MIN(([@[Edhw_min]]-[@[PV_to_Edhw_min]]),[@[Batt_discharge_potential]]-SUM(sim[@[Batt_to_user]:[Batt_to_Ec_min]]))*Batt_is_used_for_HVACminimum',
        )
        self.Batt_to_Ev_min = TimeseriesMeta(
            var_name='Batt_to_Ev_min',
            attr_name='Batt_to_Ev_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit=None,
            formula='=MIN(([@[Ev_min]]-[@[PV_to_Ev_min]]),[@[Batt_discharge_potential]]-SUM(sim[@[Batt_to_user]:[Batt_to_Edhw_min]]))*Batt_is_used_for_HVACminimum',
        )
        self.Batt_to_HVAC_min = TimeseriesMeta(
            var_name='Batt_to_HVAC_min',
            attr_name='Batt_to_HVAC_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit='Wh/m²',
            formula='=SUM(sim[@[Batt_to_Eh_min]:[Batt_to_Ev_min]])',
        )
        self.Batt_to_Eev_min = TimeseriesMeta(
            var_name='Batt_to_Eev_min',
            attr_name='Batt_to_Eev_min',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit='Wh/m²',
            formula='=MIN(([@[Eev_min]]-[@[PV_to_Eev_min]]),[@[Batt_discharge_potential]]-[@[Batt_to_user]]-[@[Batt_to_HVAC_min]])*Batt_is_used_for_EV',
        )
        self.Batt_total_discharge = TimeseriesMeta(
            var_name='Batt_total_discharge',
            attr_name='Batt_total_discharge',
            domain='Batterie Nutzung',
            measure='🔋 Batterienutzung Mindestbedarfe',
            unit='Wh/m²',
            formula='=IFERROR(([@[Batt_to_user]]+[@[Batt_to_HVAC_min]]+[@[Batt_to_Eev_min]])/Batt_eff_factor_discharge,0)',
        )
        self.Spalte19 = TimeseriesMeta(
            var_name='Spalte19',
            attr_name='Spalte19',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Signal = TimeseriesMeta(
            var_name='Signal',
            attr_name='Signal',
            domain=None,
            measure=None,
            unit=None,
            formula='=INDEX(Signals,ROW()-ROW(Signals[#Headers]),flex_Signals_selected_column)',
        )
        self.VRGrid_potential = TimeseriesMeta(
            var_name='VRGrid_potential',
            attr_name='VRGrid_potential',
            domain='Flexibler Netzbezug',
            measure='Potential',
            unit='Wh/m²',
            formula='=FLEX_is_used*FLEX_grid_maxpower_Wm2*[@Signal]',
        )
        self.VRGrid_to_user = TimeseriesMeta(
            var_name='VRGrid_to_user',
            attr_name='VRGrid_to_user',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=FLEX_is_used_for_plugloads*MIN([@[VRGrid_potential]],[@[E_plugAuxLight]]-[@[PV_to_user]]-[@[Batt_to_user]])',
        )
        self.VRGrid_to_Eh_min = TimeseriesMeta(
            var_name='VRGrid_to_Eh_min',
            attr_name='VRGrid_to_Eh_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit=None,
            formula='=FLEX_is_used_for_HVAC_min*MIN([@[Eh_min]]-[@[PV_to_Eh_min]]-[@[Batt_to_Eh_min]],[@[VRGrid_potential]]-[@[VRGrid_to_user]])',
        )
        self.VRGrid_to_Ec_min = TimeseriesMeta(
            var_name='VRGrid_to_Ec_min',
            attr_name='VRGrid_to_Ec_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit=None,
            formula='=FLEX_is_used_for_HVAC_min*MIN([@[Ec_min]]-[@[PV_to_Ec_min]]-[@[Batt_to_Ec_min]],[@[VRGrid_potential]]-[@[VRGrid_to_user]]-[@[VRGrid_to_Eh_min]])',
        )
        self.VRGrid_to_Edhw_min = TimeseriesMeta(
            var_name='VRGrid_to_Edhw_min',
            attr_name='VRGrid_to_Edhw_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit=None,
            formula='=FLEX_is_used_for_HVAC_min*MIN([@[Edhw_min]]-[@[PV_to_Edhw_min]]-[@[Batt_to_Edhw_min]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_to_user]:[VRGrid_to_Ec_min]]))',
        )
        self.VRGrid_to_Ev_min = TimeseriesMeta(
            var_name='VRGrid_to_Ev_min',
            attr_name='VRGrid_to_Ev_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit=None,
            formula='=FLEX_is_used_for_HVAC_min*MIN([@[Ev_min]]-[@[PV_to_Ev_min]]-[@[Batt_to_Ev_min]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_to_user]:[VRGrid_to_Edhw_min]]))',
        )
        self.VRGrid_to_HVAC_min = TimeseriesMeta(
            var_name='VRGrid_to_HVAC_min',
            attr_name='VRGrid_to_HVAC_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=SUM(sim[@[VRGrid_to_Eh_min]:[VRGrid_to_Ev_min]])',
        )
        self.VRGrid_to_Eev_min = TimeseriesMeta(
            var_name='VRGrid_to_Eev_min',
            attr_name='VRGrid_to_Eev_min',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=FLEX_is_used_for_ev_min*MIN([@[VRGrid_potential]]-SUM(sim[@[VRGrid_to_user]:[VRGrid_to_Ev_min]]),[@[Eev_min]]-[@[PV_to_Eev_min]]-[@[Batt_to_Eev_min]])',
        )
        self.VRGrid_total_min_use = TimeseriesMeta(
            var_name='VRGrid_total_min_use',
            attr_name='VRGrid_total_min_use',
            domain='Flexibler Netzbezug',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=[@[VRGrid_to_user]]+[@[VRGrid_to_HVAC_min]]+[@[VRGrid_to_Eev_min]]',
        )
        self.VRGrid_to_Eh_flex_1el = TimeseriesMeta(
            var_name='VRGrid_to_Eh_flex_1el',
            attr_name='VRGrid_to_Eh_flex_1el',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[VRGrid_potential]]-[@[VRGrid_total_min_use]],[@[Eh_el1_flex_potential]]-[@[PV_to_Eh_flex_1el]])',
        )
        self.VRGrid_to_Eh_flex_3el = TimeseriesMeta(
            var_name='VRGrid_to_Eh_flex_3el',
            attr_name='VRGrid_to_Eh_flex_3el',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[VRGrid_potential]]-[@[VRGrid_total_min_use]],[@[Eh_el3_flex_potential]]-[@[PV_to_Eh_flex_3el]])',
        )
        self.VRGrid_to_Ec_flex_1el = TimeseriesMeta(
            var_name='VRGrid_to_Ec_flex_1el',
            attr_name='VRGrid_to_Ec_flex_1el',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[Ec_el1_flex_potential]]-[@[PV_to_Ec_flex_1el]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_total_min_use]:[VRGrid_to_Eh_flex_3el]]))',
        )
        self.VRGrid_to_Ec_flex_3el = TimeseriesMeta(
            var_name='VRGrid_to_Ec_flex_3el',
            attr_name='VRGrid_to_Ec_flex_3el',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[Ec_el3_flex_potential]]-[@[PV_to_Ec_flex_3el]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_total_min_use]:[VRGrid_to_Eh_flex_3el]]))',
        )
        self.VRGrid_to_Edhw1_flex = TimeseriesMeta(
            var_name='VRGrid_to_Edhw1_flex',
            attr_name='VRGrid_to_Edhw1_flex',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[Edhw_1_flex_potential]]-[@[PV_to_Edhw1_flex]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_total_min_use]:[VRGrid_to_Ec_flex_3el]]))',
        )
        self.VRGrid_to_Edhw2_flex = TimeseriesMeta(
            var_name='VRGrid_to_Edhw2_flex',
            attr_name='VRGrid_to_Edhw2_flex',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[Edhw_2_flex_potential]]-[@[PV_to_Edhw2_flex]],[@[VRGrid_potential]]-SUM(sim[@[VRGrid_total_min_use]:[VRGrid_to_Ec_flex_3el]]))',
        )
        self.VRGrid_to_HVAC_flex = TimeseriesMeta(
            var_name='VRGrid_to_HVAC_flex',
            attr_name='VRGrid_to_HVAC_flex',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit=None,
            formula='=SUM(sim[@[VRGrid_to_Eh_flex_1el]:[VRGrid_to_Edhw2_flex]])',
        )
        self.VRGrid_to_Eev_flex = TimeseriesMeta(
            var_name='VRGrid_to_Eev_flex',
            attr_name='VRGrid_to_Eev_flex',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=MIN([@[Eev_flex_potential]]-[@[PV_to_Eev_flex]],[@[VRGrid_potential]]-[@[VRGrid_total_min_use]]-[@[VRGrid_to_HVAC_flex]])',
        )
        self.VRGrid_to_Batt = TimeseriesMeta(
            var_name='VRGrid_to_Batt',
            attr_name='VRGrid_to_Batt',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=Batt_is_gridcharged*MIN([@[Ebatt_charge_potential]]-[@[PV_to_Batt]],[@[VRGrid_potential]]-[@[VRGrid_total_min_use]]-[@[VRGrid_to_HVAC_flex]]-[@[VRGrid_to_Eev_flex]])',
        )
        self.VRGrid_total_flex_use = TimeseriesMeta(
            var_name='VRGrid_total_flex_use',
            attr_name='VRGrid_total_flex_use',
            domain='Flexibler Netzbezug',
            measure='Speicherbeladung',
            unit='Wh/m²',
            formula='=SUM(sim[@[VRGrid_to_HVAC_flex]:[VRGrid_to_Batt]])',
        )
        self.VRGrid_to_building = TimeseriesMeta(
            var_name='VRGrid_to_building',
            attr_name='VRGrid_to_building',
            domain=None,
            measure=None,
            unit='Wh/m²',
            formula='=[@[VRGrid_total_min_use]]+[@[VRGrid_total_flex_use]]-[@[VRGrid_to_Eev_min]]-[@[VRGrid_to_Eev_flex]]',
        )
        self.Eev_discharge_potential = TimeseriesMeta(
            var_name='Eev_discharge_potential',
            attr_name='Eev_discharge_potential',
            domain='Vehicle-to-Building',
            measure='Potential',
            unit='Wh/m²',
            formula='=SUM(sim[@[Eev_Dflex_pot_res]:[Eev_Dflex_pot_retail]])*EV_charging_efficiency',
        )
        self.Eev_to_user = TimeseriesMeta(
            var_name='Eev_to_user',
            attr_name='Eev_to_user',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=-MIN([@[Eev_discharge_potential]],[@[E_plugAuxLight]]-[@[PV_to_user]]-[@[Batt_to_user]]-[@[VRGrid_to_user]])',
        )
        self.Eev_to_Eh_min = TimeseriesMeta(
            var_name='Eev_to_Eh_min',
            attr_name='Eev_to_Eh_min',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=-MIN([@[Eh_min]]-[@[PV_to_Eh_min]]-[@[Batt_to_Eh_min]]-[@[VRGrid_to_Eh_min]],[@[Eev_discharge_potential]]-[@[Eev_to_user]])',
        )
        self.Eev_to_Ec_min = TimeseriesMeta(
            var_name='Eev_to_Ec_min',
            attr_name='Eev_to_Ec_min',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=-MIN([@[Ec_min]]-[@[PV_to_Ec_min]]-[@[Batt_to_Ec_min]]-[@[VRGrid_to_Ec_min]],[@[Eev_discharge_potential]]-[@[Eev_to_user]]-[@[Eev_to_Eh_min]])',
        )
        self.Eev_to_Edhw_min = TimeseriesMeta(
            var_name='Eev_to_Edhw_min',
            attr_name='Eev_to_Edhw_min',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=-MIN([@[Edhw_min]]-[@[PV_to_Edhw_min]]-[@[Batt_to_Edhw_min]]-[@[VRGrid_to_Edhw_min]],[@[Eev_discharge_potential]]-[@[Eev_to_user]]-[@[Eev_to_Eh_min]]-[@[Eev_to_Ec_min]])',
        )
        self.Eev_to_Ev_min = TimeseriesMeta(
            var_name='Eev_to_Ev_min',
            attr_name='Eev_to_Ev_min',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=-MIN([@[Ev_min]]-[@[PV_to_Ev_min]]-[@[Batt_to_Ev_min]]-[@[VRGrid_to_Ev_min]],[@[Eev_discharge_potential]]-SUM(sim[@[Eev_to_user]:[Eev_to_Edhw_min]]))',
        )
        self.Eev_to_HVAC = TimeseriesMeta(
            var_name='Eev_to_HVAC',
            attr_name='Eev_to_HVAC',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=SUM(sim[@[Eev_to_Eh_min]:[Eev_to_Ev_min]])',
        )
        self.v_2 = TimeseriesMeta(
            var_name='#2',
            attr_name='v_2',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula=None,
        )
        self.v_3 = TimeseriesMeta(
            var_name='#3',
            attr_name='v_3',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula=None,
        )
        self.Eev_discharge_total = TimeseriesMeta(
            var_name='Eev_discharge_total',
            attr_name='Eev_discharge_total',
            domain='Vehicle-to-Building',
            measure='Direktnutzung',
            unit='Wh/m²',
            formula='=(-[@[Eev_to_HVAC]]-[@[Eev_to_user]])/EV_charging_efficiency',
        )
        self.v_5 = TimeseriesMeta(
            var_name='#5',
            attr_name='v_5',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Grid_to_user = TimeseriesMeta(
            var_name='Grid_to_user',
            attr_name='Grid_to_user',
            domain='🔌Netzbezug',
            measure='Nutzerstrom',
            unit='Wh/m²',
            formula='=[@[E_plugAuxLight]]-[@[PV_to_user]]-[@[Batt_to_user]]-[@[VRGrid_to_user]]+[@[Eev_to_user]]',
        )
        self.Grid_to_Eh_min = TimeseriesMeta(
            var_name='Grid_to_Eh_min',
            attr_name='Grid_to_Eh_min',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit=None,
            formula='=[@[Eh_min]]-[@[PV_to_Eh_min]]-[@[Batt_to_Eh_min]]-[@[VRGrid_to_Eh_min]]+[@[Eev_to_Eh_min]]',
        )
        self.Grid_to_Ec_min = TimeseriesMeta(
            var_name='Grid_to_Ec_min',
            attr_name='Grid_to_Ec_min',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit=None,
            formula='=[@[Ec_min]]-[@[PV_to_Ec_min]]-[@[Batt_to_Ec_min]]-[@[VRGrid_to_Ec_min]]+[@[Eev_to_Ec_min]]',
        )
        self.Grid_to_Edhw_min = TimeseriesMeta(
            var_name='Grid_to_Edhw_min',
            attr_name='Grid_to_Edhw_min',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit=None,
            formula='=[@[Edhw_min]]-[@[PV_to_Edhw_min]]-[@[Batt_to_Edhw_min]]-[@[VRGrid_to_Edhw_min]]+[@[Eev_to_Edhw_min]]',
        )
        self.Grid_to_Ev_min = TimeseriesMeta(
            var_name='Grid_to_Ev_min',
            attr_name='Grid_to_Ev_min',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit=None,
            formula='=[@[Ev_min]]-[@[PV_to_Ev_min]]-[@[Batt_to_Ev_min]]-[@[VRGrid_to_Ev_min]]+[@[Eev_to_Ev_min]]',
        )
        self.test_grid_hvac = TimeseriesMeta(
            var_name='test_grid_hvac',
            attr_name='test_grid_hvac',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit=None,
            formula='=[@[Ehvac_min]]-[@[PV_to_HVAC_min]]-[@[Batt_to_HVAC_min]]-[@[VRGrid_to_HVAC_min]]+[@[Eev_to_HVAC]]',
        )
        self.Grid_to_HVAC_min = TimeseriesMeta(
            var_name='Grid_to_HVAC_min',
            attr_name='Grid_to_HVAC_min',
            domain='🔌Netzbezug',
            measure='HKLS',
            unit='Wh/m²',
            formula='=SUM(sim[@[Grid_to_Eh_min]:[Grid_to_Ev_min]])',
        )
        self.Grid_to_Eev_min = TimeseriesMeta(
            var_name='Grid_to_Eev_min',
            attr_name='Grid_to_Eev_min',
            domain='🔌Netzbezug',
            measure='EV',
            unit=None,
            formula='=[@[Eev_min]]-[@[PV_to_Eev_min]]-[@[Batt_to_Eev_min]]-[@[VRGrid_to_Eev_min]]',
        )
        self.Grid_to_building_min = TimeseriesMeta(
            var_name='Grid_to_building_min',
            attr_name='Grid_to_building_min',
            domain='🔌Netzbezug',
            measure='Gebäude',
            unit=None,
            formula='=[@[Grid_to_HVAC_min]]+[@[Grid_to_user]]',
        )
        self.Spalte15 = TimeseriesMeta(
            var_name='Spalte15',
            attr_name='Spalte15',
            domain='🔌Netzbezug',
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte16 = TimeseriesMeta(
            var_name='Spalte16',
            attr_name='Spalte16',
            domain='🔌Netzbezug',
            measure=None,
            unit=None,
            formula=None,
        )
        self.E_grid = TimeseriesMeta(
            var_name='E_grid',
            attr_name='E_grid',
            domain='🔌Netzbezug',
            measure='Insgesamt',
            unit=None,
            formula='=SUM([@[Grid_to_user]],[@[Grid_to_HVAC_min]],[@[Grid_to_Eev_min]])',
        )
        self.Spalte7 = TimeseriesMeta(
            var_name='Spalte7',
            attr_name='Spalte7',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Eh_flex_1el_final = TimeseriesMeta(
            var_name='Eh_flex_1el_final',
            attr_name='Eh_flex_1el_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Eh_flex_1el]]+[@[VRGrid_to_Eh_flex_1el]]',
        )
        self.Eh_flex_3el_final = TimeseriesMeta(
            var_name='Eh_flex_3el_final',
            attr_name='Eh_flex_3el_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Eh_flex_3el]]+[@[VRGrid_to_Eh_flex_3el]]',
        )
        self.Ec_flex_1el_final = TimeseriesMeta(
            var_name='Ec_flex_1el_final',
            attr_name='Ec_flex_1el_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Ec_flex_1el]]+[@[VRGrid_to_Ec_flex_1el]]',
        )
        self.Ec_flex_3el_final = TimeseriesMeta(
            var_name='Ec_flex_3el_final',
            attr_name='Ec_flex_3el_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Ec_flex_3el]]+[@[VRGrid_to_Ec_flex_3el]]',
        )
        self.Edhw1_flex_final = TimeseriesMeta(
            var_name='Edhw1_flex_final',
            attr_name='Edhw1_flex_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Edhw1_flex]]+[@[VRGrid_to_Edhw1_flex]]',
        )
        self.Edhw2_flex_final = TimeseriesMeta(
            var_name='Edhw2_flex_final',
            attr_name='Edhw2_flex_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='HKLS',
            unit='Wh/m²',
            formula='=[@[PV_to_Edhw2_flex]]+[@[VRGrid_to_Edhw2_flex]]',
        )
        self.Eev_flex_final = TimeseriesMeta(
            var_name='Eev_flex_final',
            attr_name='Eev_flex_final',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='EV',
            unit='Wh/m²',
            formula='=([@[PV_to_Eev_flex]]+[@[VRGrid_to_Eev_flex]])*EV_charging_efficiency',
        )
        self.Eev_flex_final_res = TimeseriesMeta(
            var_name='Eev_flex_final_res',
            attr_name='Eev_flex_final_res',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='EV',
            unit='Wh/m²',
            formula='=IFERROR([@[Eev_flex_final]]*[@[Eev_Cflex_pot_res]]/[@[Eev_Cflex_pot]],0)',
        )
        self.Eev_flex_final_work = TimeseriesMeta(
            var_name='Eev_flex_final_work',
            attr_name='Eev_flex_final_work',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='EV',
            unit='Wh/m²',
            formula='=IFERROR([@[Eev_flex_final]]*[@[Eev_Cflex_pot_work]]/[@[Eev_Cflex_pot]],0)',
        )
        self.Eev_flex_final_ret = TimeseriesMeta(
            var_name='Eev_flex_final_ret',
            attr_name='Eev_flex_final_ret',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='EV',
            unit='Wh/m²',
            formula='=IFERROR([@[Eev_flex_final]]*[@[Eev_Cflex_pot_retail]]/[@[Eev_Cflex_pot]],0)',
        )
        self.Batt_total_charge = TimeseriesMeta(
            var_name='Batt_total_charge',
            attr_name='Batt_total_charge',
            domain='Speicherladung (aus PV + Netzsignal)',
            measure='BESS',
            unit='Wh/m²',
            formula='=([@[PV_to_Batt]]+[@[VRGrid_to_Batt]])*Batt_eff_factor_charge',
        )
        self.Spalte14 = TimeseriesMeta(
            var_name='Spalte14',
            attr_name='Spalte14',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Qh_min_excl_distr_losses = TimeseriesMeta(
            var_name='Qh_min_excl_distr_losses',
            attr_name='Qh_min_excl_distr_losses',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²',
            formula='=SUM(sim[@[Qh_min_wasteheat]:[Qh_min_4th]])',
        )
        self.Qh_flex_wasteheat_final = TimeseriesMeta(
            var_name='Qh_flex_wasteheat_final',
            attr_name='Qh_flex_wasteheat_final',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit=None,
            formula='=[@[Qh_wasteheat_flex]]',
        )
        self.Qh_flex_1el_final = TimeseriesMeta(
            var_name='Qh_flex_1el_final',
            attr_name='Qh_flex_1el_final',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²',
            formula='=IFERROR([@[Qh_flex_1el_potential]]*[@[Eh_flex_1el_final]]/[@[Eh_el1_flex_potential]],0)',
        )
        self.Qh_flex_3el_final = TimeseriesMeta(
            var_name='Qh_flex_3el_final',
            attr_name='Qh_flex_3el_final',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²',
            formula='=IFERROR([@[Qh_flex_3el_potential]]*[@[Eh_flex_3el_final]]/[@[Eh_el3_flex_potential]],0)',
        )
        self.Qh_total_final = TimeseriesMeta(
            var_name='Qh_total_final',
            attr_name='Qh_total_final',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²',
            formula='=SUM(sim[@[Qh_min_excl_distr_losses]:[Qh_flex_3el_final]])',
        )
        self.Qh_u = TimeseriesMeta(
            var_name='Qh_u',
            attr_name='Qh_u',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²uncooled',
            formula='=IFERROR([@[Qh_min_excl_distr_losses]]*[@[Qh_to_room_uncooled_min]]/[@[Qh_to_room_min]],0)+IFERROR(SUM(sim[@[Qh_flex_1el_final]:[Qh_flex_3el_final]])*[@[Qh_to_room_flex_u]]/[@[Qh_to_room_flex]],0)',
        )
        self.Qh_c = TimeseriesMeta(
            var_name='Qh_c',
            attr_name='Qh_c',
            domain='Heizenergie',
            measure='HWB Raumseitig',
            unit='Wh/m²cooled',
            formula='=IFERROR([@[Qh_min_excl_distr_losses]]*[@[Qh_to_room_cooled_min]]/[@[Qh_to_room_min]],0)+IFERROR(SUM(sim[@[Qh_flex_1el_final]:[Qh_flex_3el_final]])*[@[Qh_to_room_flex_c]]/[@[Qh_to_room_flex]],0)',
        )
        self.Qhed_1el = TimeseriesMeta(
            var_name='Qhed_1el',
            attr_name='Qhed_1el',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=([@[Qh_min_1el]]+[@[Qh_flex_1el_final]])*(1+QH_distr_loss_1el)',
        )
        self.Qhed_2th = TimeseriesMeta(
            var_name='Qhed_2th',
            attr_name='Qhed_2th',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=[@[Qh_min_2th]]*(1+QH_distr_loss_2th)',
        )
        self.Qhed_3el = TimeseriesMeta(
            var_name='Qhed_3el',
            attr_name='Qhed_3el',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=([@[Qh_min_3el]]+[@[Qh_flex_3el_final]])*(1+QH_distr_loss_3el)',
        )
        self.Qhed_4th = TimeseriesMeta(
            var_name='Qhed_4th',
            attr_name='Qhed_4th',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=[@[Qh_min_4th]]*(1+QH_distr_loss_4th)',
        )
        self.Qhed_total = TimeseriesMeta(
            var_name='Qhed_total',
            attr_name='Qhed_total',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=SUM(sim[@[Qhed_1el]:[Qhed_4th]])',
        )
        self.Qh_distr_losses = TimeseriesMeta(
            var_name='Qh_distr_losses',
            attr_name='Qh_distr_losses',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²',
            formula='=[@[Qhed_total]]-[@[Qh_total_final]]',
        )
        self.Eh_aux = TimeseriesMeta(
            var_name='Eh_aux',
            attr_name='Eh_aux',
            domain='Heizenergie',
            measure='Heizenergiebedarf (inkl. Verteilverluste)',
            unit=None,
            formula='=[@[Qhed_1el]]*QH_aux_el_to_th_1el+[@[Qhed_2th]]*QH_aux_el_to_th_2th+[@[Qhed_3el]]*QH_aux_el_to_th_3el+[@[Qhed_4th]]*QH_aux_el_to_th_4th',
        )
        self.Night_schedule = TimeseriesMeta(
            var_name='Night_schedule',
            attr_name='Night_schedule',
            domain='Kühlenergie',
            measure='Nachtlüften',
            unit=None,
            formula='TRUE',
        )
        self.Night_use = TimeseriesMeta(
            var_name='Night_use',
            attr_name='Night_use',
            domain='Kühlenergie',
            measure='Nachtlüften',
            unit=None,
            formula='=IFERROR([@[Night_schedule]]*[@Ti0uncooled]>Tsetcool_max,FALSE)',
        )
        self.ACH_nightvent = TimeseriesMeta(
            var_name='ACH_nightvent',
            attr_name='ACH_nightvent',
            domain='Kühlenergie',
            measure='Nachtlüften',
            unit='m³/h',
            formula='=[@[Night_use]]*IF(-[@[dT_uncooled]]>2,ACH_night_m3,0)',
        )
        self.Qv_nightvent = TimeseriesMeta(
            var_name='Qv_nightvent',
            attr_name='Qv_nightvent',
            domain='Kühlenergie',
            measure='Nachtlüften',
            unit='Wh/m²uncooled',
            formula='=[@[ACH_nightvent]]*cp_air*[@[dT_uncooled]]*per_NFA_uncooled',
        )
        self.Spalte11 = TimeseriesMeta(
            var_name='Spalte11',
            attr_name='Spalte11',
            domain='Kühlenergie',
            measure=None,
            unit=None,
            formula=None,
        )
        self.Qc_min_excl_losses = TimeseriesMeta(
            var_name='Qc_min_excl_losses',
            attr_name='Qc_min_excl_losses',
            domain='Kühlenergie',
            measure='Kühlbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=-SUM(sim[@[Qc_min_0fc]:[Qc_min_3el]])',
        )
        self.Qc_flex_1el_final = TimeseriesMeta(
            var_name='Qc_flex_1el_final',
            attr_name='Qc_flex_1el_final',
            domain='Kühlenergie',
            measure='Kühlbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=-IFERROR([@[Qc_flex_1el]]*[@[Ec_flex_1el_final]]/[@[Ec_el1_flex_potential]],0)',
        )
        self.Qc_flex_3el_final = TimeseriesMeta(
            var_name='Qc_flex_3el_final',
            attr_name='Qc_flex_3el_final',
            domain='Kühlenergie',
            measure='Kühlbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=-IFERROR([@[Qc_flex_3el]]*[@[Ec_flex_3el_final]]/[@[Ec_el3_flex_potential]],0)',
        )
        self.Qc_flex_excl_losses = TimeseriesMeta(
            var_name='Qc_flex_excl_losses',
            attr_name='Qc_flex_excl_losses',
            domain='Kühlenergie',
            measure='Kühlbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=[@[Qc_flex_1el_final]]+[@[Qc_flex_3el_final]]',
        )
        self.QC_total_final = TimeseriesMeta(
            var_name='QC_total_final',
            attr_name='QC_total_final',
            domain='Kühlenergie',
            measure='Kühlbedarf raumseitig',
            unit='Wh/m²cooled',
            formula='=[@[Qc_min_excl_losses]]+[@[Qc_flex_excl_losses]]',
        )
        self.Qced_1el = TimeseriesMeta(
            var_name='Qced_1el',
            attr_name='Qced_1el',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²cooled',
            formula='=([@[Qc_min_1el]]-[@[Qc_flex_1el_final]])*(1+QC_distr_losses_1el)',
        )
        self.Qced_2th = TimeseriesMeta(
            var_name='Qced_2th',
            attr_name='Qced_2th',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²cooled',
            formula='=[@[Qc_min_2th]]*(1+QC_distr_losses_2th)',
        )
        self.Qced_3el = TimeseriesMeta(
            var_name='Qced_3el',
            attr_name='Qced_3el',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit='Wh/m²cooled',
            formula='=([@[Qc_min_3el]]-[@[Qc_flex_3el_final]])*(1+QC_distr_losses_3el)',
        )
        self.Qced_total = TimeseriesMeta(
            var_name='Qced_total',
            attr_name='Qced_total',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit=None,
            formula='=SUM(sim[@[Qced_1el]:[Qced_3el]])',
        )
        self.Qc_distr_losses = TimeseriesMeta(
            var_name='Qc_distr_losses',
            attr_name='Qc_distr_losses',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit=None,
            formula='=[@[Qced_total]]+[@[QC_total_final]]',
        )
        self.Ec_aux = TimeseriesMeta(
            var_name='Ec_aux',
            attr_name='Ec_aux',
            domain='Kühlenergie',
            measure='Kühlenergiebedarf (inkl. Verteilverluste)',
            unit=None,
            formula='=[@[Ec_min_freecooling]]+[@[Qced_1el]]*QC_aux_1el+[@[Qced_2th]]*QC_aux_2th+[@[Qced_3el]]*QC_aux_3el',
        )
        self.Qdhw_1_flex2 = TimeseriesMeta(
            var_name='Qdhw_1_flex2',
            attr_name='Qdhw_1_flex2',
            domain='Warmwasser',
            measure='Warmwasser-Wärmebedarf',
            unit='Wh/m²',
            formula='=IFERROR([@[Edhw1_flex_final]]*(1-DHW_1_el_aux)/(DHW_conversion_1*DHW_1_is_electric+DHW_1_el_aux),0)',
        )
        self.Qdhw_2_flex = TimeseriesMeta(
            var_name='Qdhw_2_flex',
            attr_name='Qdhw_2_flex',
            domain='Warmwasser',
            measure='Warmwasser-Wärmebedarf',
            unit='Wh/m²',
            formula='=IFERROR([@[Edhw2_flex_final]]*(1-DHW_2_el_aux)/(DHW_conversion_2*DHW_2_is_electric+DHW_2_el_aux),0)',
        )
        self.Qdhw_1_total = TimeseriesMeta(
            var_name='Qdhw_1_total',
            attr_name='Qdhw_1_total',
            domain='Warmwasser',
            measure='Warmwasser-Wärmebedarf',
            unit='Wh/m²',
            formula='=[@[Qdhw_1_min]]+[@[Qdhw_1_flex2]]',
        )
        self.Qdhw_2_total = TimeseriesMeta(
            var_name='Qdhw_2_total',
            attr_name='Qdhw_2_total',
            domain='Warmwasser',
            measure='Warmwasser-Wärmebedarf',
            unit='Wh/m²',
            formula='=[@[Qdhw_2_min]]+[@[Qdhw_2_flex]]',
        )
        self.Qdhw_total = TimeseriesMeta(
            var_name='Qdhw_total',
            attr_name='Qdhw_total',
            domain='Warmwasser',
            measure='Warmwasser-Wärmebedarf',
            unit='Wh/m²',
            formula='=SUM(sim[@[Qdhw_1_total]:[Qdhw_2_total]])',
        )
        self.Spalte20 = TimeseriesMeta(
            var_name='Spalte20',
            attr_name='Spalte20',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte21 = TimeseriesMeta(
            var_name='Spalte21',
            attr_name='Spalte21',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.EV_SOCc_d_res = TimeseriesMeta(
            var_name='EV_SOCc_d_res',
            attr_name='EV_SOCc_d_res',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_d_res]]+([@[Eev_Cmin_res]]+[@[Eev_flex_final_res]]-[@[Eev_discharge_total]])/1000*NFA_total/[@[EVd_res]]/EV_battsize_kWh,0)',
        )
        self.EV_SOCc_d_work = TimeseriesMeta(
            var_name='EV_SOCc_d_work',
            attr_name='EV_SOCc_d_work',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_d_work]]+([@[Eev_Cmin_work]]+[@[Eev_flex_final_work]])/1000*NFA_total/[@[EVd_work]]/EV_battsize_kWh,0)',
        )
        self.EV_SOCc_d_retail = TimeseriesMeta(
            var_name='EV_SOCc_d_retail',
            attr_name='EV_SOCc_d_retail',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_d_retail]]+([@[Eev_Cmin_retail]]+[@[Eev_flex_final_ret]])/1000*NFA_total/[@[EVd_retail]]/EV_battsize_kWh,0)',
        )
        self.EV_SOCc_a_res = TimeseriesMeta(
            var_name='EV_SOCc_a_res',
            attr_name='EV_SOCc_a_res',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_a_res]]+([@[Eev_S_res]]+[@[Eev_Cext_res]])/(EV_count_residential-[@[EVd_res]])/EV_battsize_kWh/1000*NFA_total,0)',
        )
        self.EV_SOCc_a_work = TimeseriesMeta(
            var_name='EV_SOCc_a_work',
            attr_name='EV_SOCc_a_work',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_a_work]]+([@[Eev_S_work]]+[@[Eev_Cext_work]])/(EV_count_work-[@[EVd_work]])/EV_battsize_kWh/1000*NFA_total,0)',
        )
        self.EV_SOCc_a_retail = TimeseriesMeta(
            var_name='EV_SOCc_a_retail',
            attr_name='EV_SOCc_a_retail',
            domain='E-Mobilität',
            measure='E-Mobilität Beladung',
            unit=None,
            formula='=IFERROR([@[EV_SOC0_a_retail]]+([@[Eev_S_retail]]+[@[Eev_Cext_retail]])/(EV_count_retail-[@[EVd_retail]])/EV_battsize_kWh/1000*NFA_total,0)',
        )
        self.Spalte238 = TimeseriesMeta(
            var_name='Spalte238',
            attr_name='Spalte238',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte239 = TimeseriesMeta(
            var_name='Spalte239',
            attr_name='Spalte239',
            domain=None,
            measure=None,
            unit=None,
            formula=None,
        )
        self.Ti_final_uncooled = TimeseriesMeta(
            var_name='Ti_final_uncooled',
            attr_name='Ti_final_uncooled',
            domain='Zustände',
            measure='Thermische Speicher',
            unit='°C',
            formula='=[@[Ti_passive_uncooled]]+([@[Qh_u]]+[@[Qv_nightvent]])/heat_cap_eff_uncooled_m2',
        )
        self.Ti_final_cooled = TimeseriesMeta(
            var_name='Ti_final_cooled',
            attr_name='Ti_final_cooled',
            domain='Zustände',
            measure='Thermische Speicher',
            unit='°C',
            formula='=[@[Ti_passive_cooled]]+([@[Qh_c]]+[@[QC_total_final]])/heat_cap_eff_cooled_m2',
        )
        self.Tdhw_1_final = TimeseriesMeta(
            var_name='Tdhw_1_final',
            attr_name='Tdhw_1_final',
            domain='Zustände',
            measure='Thermische Speicher',
            unit='°C',
            formula='=IFERROR([@[Tdhw1_passive_losses]]+[@[Qdhw_1_total]]*NFA_total/DHW_storage_1_liter/cp_water,0)',
        )
        self.Tdhw_2_final = TimeseriesMeta(
            var_name='Tdhw_2_final',
            attr_name='Tdhw_2_final',
            domain='Zustände',
            measure='Thermische Speicher',
            unit='°C',
            formula='=IFERROR([@[Tdhw2_passive_losses]]+[@[Qdhw_2_total]]*NFA_total/DHW_storage_2_liter/cp_water,0)',
        )
        self.Spalte8 = TimeseriesMeta(
            var_name='Spalte8',
            attr_name='Spalte8',
            domain='Zustände',
            measure=None,
            unit=None,
            formula=None,
        )
        self.Batt_final_Whm2 = TimeseriesMeta(
            var_name='Batt_final_Whm2',
            attr_name='Batt_final_Whm2',
            domain='Zustände',
            measure='BESS',
            unit='Wh/m²',
            formula='=[@[Batt_cap_after_losses]]-[@[Batt_total_discharge]]+[@[Batt_total_charge]]',
        )
        self.SOC_preheat_u = TimeseriesMeta(
            var_name='SOC_preheat_u',
            attr_name='SOC_preheat_u',
            domain='Zustände',
            measure='Thermische Speicher',
            unit=None,
            formula='=IFERROR(([@[Ti_final_uncooled]]-Tsetheat_min)/flex_heat_dT,0)',
        )
        self.SOC_preheat_c = TimeseriesMeta(
            var_name='SOC_preheat_c',
            attr_name='SOC_preheat_c',
            domain='Zustände',
            measure='Thermische Speicher',
            unit=None,
            formula='=IFERROR(1-(Tsetheat_flex-[@[Ti_final_cooled]])/flex_heat_dT,0)',
        )
        self.SOC_precool_c = TimeseriesMeta(
            var_name='SOC_precool_c',
            attr_name='SOC_precool_c',
            domain='Zustände',
            measure='Thermische Speicher',
            unit=None,
            formula='=IFERROR(1-([@[Ti_final_cooled]]-Tsetcool_flex)/flex_cool_dT,0)',
        )
        self.SOC_dhw1 = TimeseriesMeta(
            var_name='SOC_dhw1',
            attr_name='SOC_dhw1',
            domain='Zustände',
            measure='Thermische Speicher',
            unit=None,
            formula='=IFERROR(1-(DHW_Tmax-[@[Tdhw_1_final]])/(DHW_Tmax-DHW_Tmin),0)',
        )
        self.SOC_dhw2 = TimeseriesMeta(
            var_name='SOC_dhw2',
            attr_name='SOC_dhw2',
            domain='Zustände',
            measure='Thermische Speicher',
            unit=None,
            formula='=IFERROR(1-(DHW_Tmax-[@[Tdhw_2_final]])/(DHW_Tmax-DHW_Tmin),0)',
        )
        self.EV_SOC_d_res = TimeseriesMeta(
            var_name='EV_SOC_d_res',
            attr_name='EV_SOC_d_res',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_res_d]]-mob[@[p_res_leave]])*[@[EV_SOCc_d_res]]+mob[@[p_res_return]]*[@[EV_SOCc_a_res]])/(mob[@[p_res_d]]+mob[@[p_res_return]]-mob[@[p_res_leave]])',
        )
        self.EV_SOC_d_work = TimeseriesMeta(
            var_name='EV_SOC_d_work',
            attr_name='EV_SOC_d_work',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_work_d]]-mob[@[p_work_leave]])*[@[EV_SOCc_d_work]]+mob[@[p_work_return]]*[@[EV_SOCc_a_work]])/(mob[@[p_work_d]]+mob[@[p_work_return]]-mob[@[p_work_leave]])',
        )
        self.EV_SOC_d_retail = TimeseriesMeta(
            var_name='EV_SOC_d_retail',
            attr_name='EV_SOC_d_retail',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_retail_d]]-mob[@[p_retail_leave]])*[@[EV_SOCc_d_retail]]+mob[@[p_retail_return]]*[@[EV_SOCc_a_retail]])/(mob[@[p_retail_d]]+mob[@[p_retail_return]]-mob[@[p_retail_leave]])',
        )
        self.EV_SOC_d = TimeseriesMeta(
            var_name='EV_SOC_d',
            attr_name='EV_SOC_d',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula=None,
        )
        self.EV_SOC_a_res = TimeseriesMeta(
            var_name='EV_SOC_a_res',
            attr_name='EV_SOC_a_res',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_res_a]]-mob[@[p_res_return]])*[@[EV_SOCc_a_res]]+mob[@[p_res_leave]]*[@[EV_SOCc_d_res]])/(mob[@[p_res_a]]-mob[@[p_res_return]]+mob[@[p_res_leave]])',
        )
        self.EV_SOC_a_work = TimeseriesMeta(
            var_name='EV_SOC_a_work',
            attr_name='EV_SOC_a_work',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_work_a]]-mob[@[p_work_return]])*[@[EV_SOCc_a_work]]+mob[@[p_work_leave]]*[@[EV_SOCc_d_work]])/(mob[@[p_work_a]]-mob[@[p_work_return]]+mob[@[p_work_leave]])',
        )
        self.EV_SOC_a_retail = TimeseriesMeta(
            var_name='EV_SOC_a_retail',
            attr_name='EV_SOC_a_retail',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=((mob[@[p_retail_a]]-mob[@[p_retail_return]])*[@[EV_SOCc_a_retail]]+mob[@[p_retail_leave]]*[@[EV_SOCc_d_retail]])/(mob[@[p_retail_a]]-mob[@[p_retail_return]]+mob[@[p_retail_leave]])',
        )
        self.EV_SOC_res = TimeseriesMeta(
            var_name='EV_SOC_res',
            attr_name='EV_SOC_res',
            domain='Zustände',
            measure='E-Mobilität',
            unit='is this performant?',
            formula='=[@[EV_SOC_d_res]]*mob[@[p_res_d]]+[@[EV_SOC_a_res]]*mob[@[p_res_a]]',
        )
        self.EV_SOC_work = TimeseriesMeta(
            var_name='EV_SOC_work',
            attr_name='EV_SOC_work',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=[@[EV_SOC_d_work]]*mob[@[p_work_d]]+[@[EV_SOC_a_work]]*mob[@[p_work_a]]',
        )
        self.EV_SOC_retail = TimeseriesMeta(
            var_name='EV_SOC_retail',
            attr_name='EV_SOC_retail',
            domain='Zustände',
            measure='E-Mobilität',
            unit=None,
            formula='=[@[EV_SOC_d_retail]]*mob[@[p_retail_d]]+[@[EV_SOC_a_retail]]*mob[@[p_retail_a]]',
        )
        self.SOC_Batt = TimeseriesMeta(
            var_name='SOC_Batt',
            attr_name='SOC_Batt',
            domain=None,
            measure=None,
            unit=None,
            formula='=[@[Batt_final_Whm2]]/Batt_cap_Wh_per_NFA',
        )
        self.Eh_1el = TimeseriesMeta(
            var_name='Eh_1el',
            attr_name='Eh_1el',
            domain='Endenergie',
            measure='Heizen',
            unit='Wh/m²',
            formula='=SUM([@[Eh_min_1el]],[@[Eh_flex_1el_final]])',
        )
        self.Eh_3el = TimeseriesMeta(
            var_name='Eh_3el',
            attr_name='Eh_3el',
            domain=None,
            measure=None,
            unit='Wh/m²',
            formula='=SUM([@[Eh_min_3el]],[@[Eh_flex_3el_final]])',
        )
        self.Ec_1el = TimeseriesMeta(
            var_name='Ec_1el',
            attr_name='Ec_1el',
            domain=None,
            measure='Kühlen',
            unit='Wh/m²',
            formula='=SUM([@[Ec_min_1el]],[@[Ec_flex_1el_final]])',
        )
        self.Ec_3el = TimeseriesMeta(
            var_name='Ec_3el',
            attr_name='Ec_3el',
            domain=None,
            measure='Kühlen',
            unit='Wh/m²',
            formula='=SUM([@[Ec_min_3el]],[@[Ec_flex_3el_final]])',
        )
        self.Edhw_1el = TimeseriesMeta(
            var_name='Edhw_1el',
            attr_name='Edhw_1el',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=[@[Qdhw_1_total]]*(DHW_conversion_1*DHW_1_is_electric)',
        )
        self.Edhw_2el = TimeseriesMeta(
            var_name='Edhw_2el',
            attr_name='Edhw_2el',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=[@[Qdhw_2_total]]*(DHW_conversion_2*DHW_2_is_electric)',
        )
        self.Qenv_h_1el = TimeseriesMeta(
            var_name='Qenv_h_1el',
            attr_name='Qenv_h_1el',
            domain=None,
            measure='Heizen',
            unit='Wh/m131',
            formula='=[@[Qhed_1el]]-[@[Eh_1el]]',
        )
        self.Qenv_h_3el = TimeseriesMeta(
            var_name='Qenv_h_3el',
            attr_name='Qenv_h_3el',
            domain=None,
            measure=None,
            unit='Wh/m132',
            formula='=[@[Qhed_3el]]-[@[Eh_3el]]',
        )
        self.Qenv_c_1el = TimeseriesMeta(
            var_name='Qenv_c_1el',
            attr_name='Qenv_c_1el',
            domain=None,
            measure='Kühlen',
            unit='Wh/m²',
            formula='=[@[Qced_1el]]+[@[Ec_1el]]',
        )
        self.Qenv_c_3el = TimeseriesMeta(
            var_name='Qenv_c_3el',
            attr_name='Qenv_c_3el',
            domain=None,
            measure='Kühlen',
            unit='Wh/m²',
            formula='=[@[Qced_3el]]+[@[Ec_3el]]',
        )
        self.Qenv_dhw_1 = TimeseriesMeta(
            var_name='Qenv_dhw_1',
            attr_name='Qenv_dhw_1',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=[@[Qdhw_1_total]]-[@[Edhw_1el]]',
        )
        self.Qenv_dhw_2 = TimeseriesMeta(
            var_name='Qenv_dhw_2',
            attr_name='Qenv_dhw_2',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=[@[Qdhw_2_total]]-[@[Edhw_2el]]',
        )
        self.EUIh_2th = TimeseriesMeta(
            var_name='EUIh_2th',
            attr_name='EUIh_2th',
            domain=None,
            measure='Heizen',
            unit='Wh/m²',
            formula='=[@[Qh_min_2th]]*(1+QH_distr_loss_2th)*QH_generation_eff_2th',
        )
        self.EUIh_4th = TimeseriesMeta(
            var_name='EUIh_4th',
            attr_name='EUIh_4th',
            domain=None,
            measure=None,
            unit='Wh/m²',
            formula='=[@[Qh_min_4th]]*(1+QH_distr_loss_4th)*QH_generation_eff_4th',
        )
        self.EUIc_2th = TimeseriesMeta(
            var_name='EUIc_2th',
            attr_name='EUIc_2th',
            domain=None,
            measure='Kühlen',
            unit='Wh/m²',
            formula='=[@[Qc_min_2th]]*(1+QC_distr_losses_2th)*QC_generation_eff_2th',
        )
        self.EUIdhw_1th = TimeseriesMeta(
            var_name='EUIdhw_1th',
            attr_name='EUIdhw_1th',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=NOT(DHW_1_is_electric)*[@[Qdhw_1_min]]*DHW_conversion_1',
        )
        self.EUIdhw_2th = TimeseriesMeta(
            var_name='EUIdhw_2th',
            attr_name='EUIdhw_2th',
            domain=None,
            measure='WW',
            unit='Wh/m²',
            formula='=NOT(DHW_2_is_electric)*[@[Qdhw_2_min]]*DHW_conversion_2',
        )
        self.cf_PEI_grid = TimeseriesMeta(
            var_name='cf_PEI_grid',
            attr_name='cf_PEI_grid',
            domain='Primärenergie',
            measure='Konversionsfaktor',
            unit='-',
            formula='=INDEX(fPE[@],,fPE_grid_column)',
        )
        self.cf_PEI_flex_grid = TimeseriesMeta(
            var_name='cf_PEI_flex_grid',
            attr_name='cf_PEI_flex_grid',
            domain='Primärenergie',
            measure='Konversionsfaktor',
            unit=None,
            formula='=[@[cf_PEI_grid]]*fPE_flex_factor',
        )
        self.cf_PEI_flex_gridsub = TimeseriesMeta(
            var_name='cf_PEI_flex_gridsub',
            attr_name='cf_PEI_flex_gridsub',
            domain='Primärenergie',
            measure='Konversionsfaktor',
            unit=None,
            formula='=[@[cf_PEI_grid]]-[@[cf_PEI_flex_grid]]',
        )
        self.cf_PEI_PV = TimeseriesMeta(
            var_name='cf_PEI_PV',
            attr_name='cf_PEI_PV',
            domain='Primärenergie',
            measure='Konversionsfaktor',
            unit=None,
            formula='0',
        )
        self.cf_PEI_PV_gridsub = TimeseriesMeta(
            var_name='cf_PEI_PV_gridsub',
            attr_name='cf_PEI_PV_gridsub',
            domain='Primärenergie',
            measure='Konversionsfaktor',
            unit=None,
            formula='=[@[cf_PEI_grid]]-[@[cf_PEI_PV]]',
        )
        self.PEI_el_user = TimeseriesMeta(
            var_name='PEI_el_user',
            attr_name='PEI_el_user',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=[@[cf_PEI_grid]]*[@[E_plugAuxLight]]',
        )
        self.PEI_el_hvac = TimeseriesMeta(
            var_name='PEI_el_hvac',
            attr_name='PEI_el_hvac',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=[@[cf_PEI_grid]]*SUM([@[Ehvac_min]],sim[@[Eh_flex_1el_final]:[Edhw2_flex_final]])',
        )
        self.PEI_district_heating = TimeseriesMeta(
            var_name='PEI_district_heating',
            attr_name='PEI_district_heating',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=SUMPRODUCT(sim[@[EUIh_2th]:[EUIdhw_2th]],TRANSPOSE(is_district_heating),TRANSPOSE(pe_conversion_factors_thermal))',
        )
        self.PEI_natural_gas = TimeseriesMeta(
            var_name='PEI_natural_gas',
            attr_name='PEI_natural_gas',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=SUMPRODUCT(sim[@[EUIh_2th]:[EUIdhw_2th]],TRANSPOSE(is_natural_gas),TRANSPOSE(pe_conversion_factors_thermal))',
        )
        self.PEI_biomass = TimeseriesMeta(
            var_name='PEI_biomass',
            attr_name='PEI_biomass',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=SUMPRODUCT(sim[@[EUIh_2th]:[EUIdhw_2th]],TRANSPOSE(is_biomass),TRANSPOSE(pe_conversion_factors_thermal))',
        )
        self.PEI_other = TimeseriesMeta(
            var_name='PEI_other',
            attr_name='PEI_other',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=SUMPRODUCT(sim[@[EUIh_2th]:[EUIdhw_2th]],TRANSPOSE(is_other_thermal_pe),TRANSPOSE(pe_conversion_factors_thermal))',
        )
        self.PEI_mob_el = TimeseriesMeta(
            var_name='PEI_mob_el',
            attr_name='PEI_mob_el',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=[@[cf_PEI_grid]]*([@[Eev_min]]+[@[Eev_flex_final]])',
        )
        self.PEI_mob_ext = TimeseriesMeta(
            var_name='PEI_mob_ext',
            attr_name='PEI_mob_ext',
            domain='Primärenergie',
            measure='Bedarf',
            unit=None,
            formula='=[@[cf_PEI_grid]]*SUM(sim[@[Eev_Cext_res]:[Eev_Cext_retail]])',
        )
        self.PEI_el_demand = TimeseriesMeta(
            var_name='PEI_el_demand',
            attr_name='PEI_el_demand',
            domain='Primärenergie',
            measure='Bedarf',
            unit='WhPE/m²',
            formula='=[@[cf_PEI_grid]]*[@[E_grid]]',
        )
        self.Spalte18 = TimeseriesMeta(
            var_name='Spalte18',
            attr_name='Spalte18',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula=None,
        )
        self.PEI_flex_grid = TimeseriesMeta(
            var_name='PEI_flex_grid',
            attr_name='PEI_flex_grid',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula='=[@[cf_PEI_flex_grid]]*([@[VRGrid_total_min_use]]+[@[VRGrid_total_flex_use]])',
        )
        self.PEI_flex_grid_substitution = TimeseriesMeta(
            var_name='PEI_flex_grid_substitution',
            attr_name='PEI_flex_grid_substitution',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula='=[@[cf_PEI_grid]]*([@[VRGrid_total_min_use]]+[@[VRGrid_total_flex_use]])',
        )
        self.PEI_PV_direct = TimeseriesMeta(
            var_name='PEI_PV_direct',
            attr_name='PEI_PV_direct',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula='=[@[cf_PEI_grid]]*[@[PV_total_direct_use]]',
        )
        self.Spalte10 = TimeseriesMeta(
            var_name='Spalte10',
            attr_name='Spalte10',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula=None,
        )
        self.Spalte13 = TimeseriesMeta(
            var_name='Spalte13',
            attr_name='Spalte13',
            domain='Primärenergie',
            measure=None,
            unit=None,
            formula=None,
        )
        self.cf_GHG_grid = TimeseriesMeta(
            var_name='cf_GHG_grid',
            attr_name='cf_GHG_grid',
            domain='☁ THG',
            measure='Konversionsfaktor',
            unit='kgCO2eq./WhEE',
            formula='=INDEX(fGHG[@],,fGHG_grid_column)',
        )
        self.GHG_plugloads = TimeseriesMeta(
            var_name='GHG_plugloads',
            attr_name='GHG_plugloads',
            domain='☁ THG',
            measure='Nutzerstrom',
            unit='gCO2eq./m²NGF',
            formula='=[@[cf_GHG_grid]]*([@[Grid_to_user]]+[@[VRGrid_to_user]])',
        )
        self.GHG_hvac = TimeseriesMeta(
            var_name='GHG_hvac',
            attr_name='GHG_hvac',
            domain='☁ THG',
            measure='HKLS',
            unit='gCO2eq./m²NGF',
            formula='=[@[cf_GHG_grid]]*SUM([@[Grid_to_HVAC_min]],[@[VRGrid_to_HVAC_min]],sim[@[VRGrid_to_Eh_flex_1el]:[VRGrid_to_Edhw2_flex]])',
        )
        self.cost_E_grid = TimeseriesMeta(
            var_name='cost_E_grid',
            attr_name='cost_E_grid',
            domain='Kosten Netzbezug',
            measure=None,
            unit='€ (Wh/m² * m²NGF /1000*€/kWh )',
            formula="=[@[E_grid]]*NFA_total*prices[@[Bezug '[€']]]/1000",
        )
        self.cost_VRGrid_flex = TimeseriesMeta(
            var_name='cost_VRGrid_flex',
            attr_name='cost_VRGrid_flex',
            domain='Kosten Netzbezug',
            measure=None,
            unit=None,
            formula="=([@[VRGrid_total_min_use]]+[@[VRGrid_total_flex_use]])*prices[@[Bezug '[€']]]/1000",
        )
        self.cost_PV_to_Egrid = TimeseriesMeta(
            var_name='cost_PV_to_Egrid',
            attr_name='cost_PV_to_Egrid',
            domain='Kosten Netzbezug',
            measure=None,
            unit=None,
            formula="=[@[PV_to_Egrid]]*prices[@[Einspeisung '[€']]]/1000",
        )
        self.Spalte3 = TimeseriesMeta(
            var_name='Spalte3',
            attr_name='Spalte3',
            domain='Kosten Netzbezug',
            measure=None,
            unit=None,
            formula=None,
        )

TIMESERIES_META = TimeseriesMetaRegistry()

TIMESERIES_ATTR_NAME_MAP: dict[str, str] = {
    'h': 'h',
    'Monat_nr': 'Monat_nr',
    'Monat': 'Monat',
    'date': 'date',
    'hour_of_the_day': 'hour_of_the_day',
    'day_of_the_year': 'day_of_the_year',
    'Ti0uncooled': 'Ti0uncooled',
    'Ti0cooled': 'Ti0cooled',
    'Ta': 'Ta',
    'rel_humidity': 'rel_humidity',
    'Irr_nord': 'Irr_nord',
    'Irr_east': 'Irr_east',
    'Irr_south': 'Irr_south',
    'Irr_west': 'Irr_west',
    'Irr_horizontal': 'Irr_horizontal',
    'is_heating_period': 'is_heating_period',
    'is_cooling_period': 'is_cooling_period',
    'season_step': 'season_step',
    'Übergangszeit': 'bergangszeit',
    'season_wave': 'season_wave',
    'percent_winter': 'percent_winter',
    'dT_uncooled': 'dT_uncooled',
    'dT_cooled': 'dT_cooled',
    'Spalte2': 'Spalte2',
    'Spalte4': 'Spalte4',
    'mobile_shading': 'mobile_shading',
    'Qvinf_u': 'Qvinf_u',
    'Qvinf_c': 'Qvinf_c',
    'ACH_residential': 'ACH_residential',
    'ACH_office': 'ACH_office',
    'ACH_edusec': 'ACH_edusec',
    'ACH_eduprim': 'ACH_eduprim',
    'ACH_retfood': 'ACH_retfood',
    'ACH_retail': 'ACH_retail',
    'ACH_otherusage': 'ACH_otherusage',
    'ACH_mechvent_therm_u': 'ACH_mechvent_therm_u',
    'ACH_mechvent_therm_c': 'ACH_mechvent_therm_c',
    'Spalte1': 'Spalte1',
    'ACH_mechvent_u': 'ACH_mechvent_u',
    'ACH_mechvent_c': 'ACH_mechvent_c',
    'Qvmechvent_u': 'Qvmechvent_u',
    'Qvmechvent_c': 'Qvmechvent_c',
    'Qvwindow_u': 'Qvwindow_u',
    'Qvwindow_c': 'Qvwindow_c',
    'QT_u': 'QT_u',
    'QT_c': 'QT_c',
    'QSwinter': 'QSwinter',
    'QSsummer': 'QSsummer',
    'QS_u_unshaded': 'QS_u_unshaded',
    'QS_c_unshaded': 'QS_c_unshaded',
    'QS_u': 'QS_u',
    'QS_c': 'QS_c',
    'Spalte9': 'Spalte9',
    'QS': 'QS',
    'QI_residential': 'QI_residential',
    'QI_office': 'QI_office',
    'QI_edusec': 'QI_edusec',
    'QI_eduprim': 'QI_eduprim',
    'QI_retfood': 'QI_retfood',
    'QI_retail': 'QI_retail',
    'QI_otherusage': 'QI_otherusage',
    'QI_u': 'QI_u',
    'QI_c': 'QI_c',
    'Ti_passive_uncooled': 'Ti_passive_uncooled',
    'Ti_passive_cooled': 'Ti_passive_cooled',
    'dT_heating_uncooled_min': 'dT_heating_uncooled_min',
    'dT_heating_cooled_min': 'dT_heating_cooled_min',
    'dT_heating_uncooled_max': 'dT_heating_uncooled_max',
    'dT_heating_cooled_max': 'dT_heating_cooled_max',
    'Qh_to_room_uncooled_min': 'Qh_to_room_uncooled_min',
    'Qh_to_room_cooled_min': 'Qh_to_room_cooled_min',
    'Qh_to_room_uncooled_max': 'Qh_to_room_uncooled_max',
    'Qh_to_room_cooled_max': 'Qh_to_room_cooled_max',
    'Qh_to_room_min': 'Qh_to_room_min',
    'Qh_to_room_flex_u': 'Qh_to_room_flex_u',
    'Qh_to_room_flex_c': 'Qh_to_room_flex_c',
    'Qh_to_room_flex_val': 'Qh_to_room_flex_val',
    'Qh_to_room_flex': 'Qh_to_room_flex',
    'waste_heat_potential': 'waste_heat_potential',
    'Qh_min_wasteheat': 'Qh_min_wasteheat',
    'Qh_min_1el': 'Qh_min_1el',
    'Qh_min_2th': 'Qh_min_2th',
    'Qh_min_3el': 'Qh_min_3el',
    'Qh_min_4th': 'Qh_min_4th',
    'Qh_wasteheat_flex': 'Qh_wasteheat_flex',
    'Qh_flex_1el_potential': 'Qh_flex_1el_potential',
    'Qh_flex_3el_potential': 'Qh_flex_3el_potential',
    'Qc_from_room_min': 'Qc_from_room_min',
    'Qc_from_room_flex': 'Qc_from_room_flex',
    'Qc_min_0fc': 'Qc_min_0fc',
    'Qc_min_1el': 'Qc_min_1el',
    'Qc_min_2th': 'Qc_min_2th',
    'Qc_min_3el': 'Qc_min_3el',
    'Qc_flex_1el': 'Qc_flex_1el',
    'Qc_flex_3el': 'Qc_flex_3el',
    'Tdhw1_0': 'Tdhw1_0',
    'Tdhw2_0': 'Tdhw2_0',
    'DHW_residential_kW': 'DHW_residential_kW',
    'DHW_office_kW': 'DHW_office_kW',
    'DHW_schoolsec_kW': 'DHW_schoolsec_kW',
    'DHW_schoolprim_kW': 'DHW_schoolprim_kW',
    'DHW_retailsupermarket_kW': 'DHW_retailsupermarket_kW',
    'DHW_retailother_kW': 'DHW_retailother_kW',
    'DHW_other_kW': 'DHW_other_kW',
    'DHW_1_tap_kW': 'DHW_1_tap_kW',
    'DHW_2_tap_kW': 'DHW_2_tap_kW',
    'DHW_storage_losses_1': 'DHW_storage_losses_1',
    'DHW_storage_losses_2': 'DHW_storage_losses_2',
    'DHW_heat_demand_1_kW': 'DHW_heat_demand_1_kW',
    'DHW_heat_demand_2_kW': 'DHW_heat_demand_2_kW',
    'Tdhw1_passive_losses': 'Tdhw1_passive_losses',
    'Tdhw2_passive_losses': 'Tdhw2_passive_losses',
    'Qdhw_1_min': 'Qdhw_1_min',
    'Qdhw_2_min': 'Qdhw_2_min',
    'Qdhw_min': 'Qdhw_min',
    'Qdhw_1_flexpotential': 'Qdhw_1_flexpotential',
    'Qdhw_2_flexpotential': 'Qdhw_2_flexpotential',
    'Edhw_1_min_el': 'Edhw_1_min_el',
    'Edhw_2_min_el': 'Edhw_2_min_el',
    'Spalte12': 'Spalte12',
    'Spalte122': 'Spalte122',
    'Spalte123': 'Spalte123',
    'EVd_res': 'EVd_res',
    'EVd_work': 'EVd_work',
    'EVd_retail': 'EVd_retail',
    'EV_SOC0_d_res': 'EV_SOC0_d_res',
    'EV_SOC0_d_work': 'EV_SOC0_d_work',
    'EV_SOC0_d_retail': 'EV_SOC0_d_retail',
    'EV_SOC0_a_res': 'EV_SOC0_a_res',
    'EV_SOC0_a_work': 'EV_SOC0_a_work',
    'EV_SOC0_a_retail': 'EV_SOC0_a_retail',
    'EV_maxpower': 'EV_maxpower',
    'Eev_Cmin_res': 'Eev_Cmin_res',
    'Eev_Cmin_work': 'Eev_Cmin_work',
    'Eev_Cmin_retail': 'Eev_Cmin_retail',
    'Eev_Cmin': 'Eev_Cmin',
    'Eev_Cflex_pot_res': 'Eev_Cflex_pot_res',
    'Eev_Cflex_pot_work': 'Eev_Cflex_pot_work',
    'Eev_Cflex_pot_retail': 'Eev_Cflex_pot_retail',
    'Eev_Cflex_pot': 'Eev_Cflex_pot',
    'Eev_Dflex_pot_res': 'Eev_Dflex_pot_res',
    'Eev_Dflex_pot_work': 'Eev_Dflex_pot_work',
    'Eev_Dflex_pot_retail': 'Eev_Dflex_pot_retail',
    'Eev_Dflex_pot': 'Eev_Dflex_pot',
    'Eev_S_res': 'Eev_S_res',
    'Eev_S_work': 'Eev_S_work',
    'Eev_S_retail': 'Eev_S_retail',
    'Eev_Cext_res': 'Eev_Cext_res',
    'Eev_Cext_work': 'Eev_Cext_work',
    'Eev_Cext_retail': 'Eev_Cext_retail',
    'Eev_min_intake': 'Eev_min_intake',
    'Eev_flex_intake': 'Eev_flex_intake',
    'Spalte6': 'Spalte6',
    'BATT_cap_0': 'BATT_cap_0',
    'Batt_auto_discharge': 'Batt_auto_discharge',
    'Batt_cap_after_losses': 'Batt_cap_after_losses',
    'Batt_max_energy_input': 'Batt_max_energy_input',
    'Spalte88': 'Spalte88',
    'Spalte5': 'Spalte5',
    'Eh_min_wasteheat': 'Eh_min_wasteheat',
    'Eh_min_1el': 'Eh_min_1el',
    'Eh_min_2th': 'Eh_min_2th',
    'Eh_min_3el': 'Eh_min_3el',
    'Eh_min_4th': 'Eh_min_4th',
    'Eh_min': 'Eh_min',
    'Ec_min_freecooling': 'Ec_min_freecooling',
    'Ec_min_1el': 'Ec_min_1el',
    'Ec_min_2th': 'Ec_min_2th',
    'Ec_min_3el': 'Ec_min_3el',
    'Ec_min': 'Ec_min',
    'Ev_residential': 'Ev_residential',
    'Ev_office': 'Ev_office',
    'Ev_edusec': 'Ev_edusec',
    'Ev_eduprim': 'Ev_eduprim',
    'Ev_retfood': 'Ev_retfood',
    'Ev_retail': 'Ev_retail',
    'Ev_otherusage': 'Ev_otherusage',
    'Ev_min': 'Ev_min',
    'Eaux': 'Eaux',
    'Elight_office': 'Elight_office',
    'Elight_schoolsec': 'Elight_schoolsec',
    'Elight_schoolprim': 'Elight_schoolprim',
    'Elight': 'Elight',
    'Edhw_min': 'Edhw_min',
    'Ehvac_min': 'Ehvac_min',
    'Test': 'Test',
    'E_plugAuxLight': 'E_plugAuxLight',
    'Eev_min': 'Eev_min',
    'Ed_min': 'Ed_min',
    'Space3': 'Space3',
    'Eh_el1_flex_potential': 'Eh_el1_flex_potential',
    'Eh_el3_flex_potential': 'Eh_el3_flex_potential',
    'Ec_el1_flex_potential': 'Ec_el1_flex_potential',
    'Ec_el3_flex_potential': 'Ec_el3_flex_potential',
    'Edhw_1_flex_potential': 'Edhw_1_flex_potential',
    'Edhw_2_flex_potential': 'Edhw_2_flex_potential',
    'Eev_flex_potential': 'Eev_flex_potential',
    'Ebatt_charge_potential': 'Ebatt_charge_potential',
    'Etotal_flex_potential': 'Etotal_flex_potential',
    'Space13': 'Space13',
    'PV_yield': 'PV_yield',
    'PV_to_user': 'PV_to_user',
    'PV_to_Eh_min': 'PV_to_Eh_min',
    'PV_to_Ec_min': 'PV_to_Ec_min',
    'PV_to_Edhw_min': 'PV_to_Edhw_min',
    'PV_to_Ev_min': 'PV_to_Ev_min',
    'Valid_PV_direct_HVAC_use': 'Valid_PV_direct_HVAC_use',
    'PV_to_HVAC_min': 'PV_to_HVAC_min',
    'PV_to_Eev_min': 'PV_to_Eev_min',
    'PV_total_direct_use': 'PV_total_direct_use',
    'PV_surplus': 'PV_surplus',
    'PV_to_Eh_flex_1el': 'PV_to_Eh_flex_1el',
    'PV_to_Eh_flex_3el': 'PV_to_Eh_flex_3el',
    'PV_to_Ec_flex_1el': 'PV_to_Ec_flex_1el',
    'PV_to_Ec_flex_3el': 'PV_to_Ec_flex_3el',
    'PV_to_Edhw1_flex': 'PV_to_Edhw1_flex',
    'PV_to_Edhw2_flex': 'PV_to_Edhw2_flex',
    'PV_to_Eev_flex': 'PV_to_Eev_flex',
    'PV_to_Batt': 'PV_to_Batt',
    'PV_to_Storage': 'PV_to_Storage',
    'PV_to_epatron': 'PV_to_epatron',
    'PV_total_flex_use': 'PV_total_flex_use',
    'PV_to_Egrid': 'PV_to_Egrid',
    'Batt_discharge_potential': 'Batt_discharge_potential',
    'Batt_to_user': 'Batt_to_user',
    'Batt_to_Eh_min': 'Batt_to_Eh_min',
    'Batt_to_Ec_min': 'Batt_to_Ec_min',
    'Batt_to_Edhw_min': 'Batt_to_Edhw_min',
    'Batt_to_Ev_min': 'Batt_to_Ev_min',
    'Batt_to_HVAC_min': 'Batt_to_HVAC_min',
    'Batt_to_Eev_min': 'Batt_to_Eev_min',
    'Batt_total_discharge': 'Batt_total_discharge',
    'Spalte19': 'Spalte19',
    'Signal': 'Signal',
    'VRGrid_potential': 'VRGrid_potential',
    'VRGrid_to_user': 'VRGrid_to_user',
    'VRGrid_to_Eh_min': 'VRGrid_to_Eh_min',
    'VRGrid_to_Ec_min': 'VRGrid_to_Ec_min',
    'VRGrid_to_Edhw_min': 'VRGrid_to_Edhw_min',
    'VRGrid_to_Ev_min': 'VRGrid_to_Ev_min',
    'VRGrid_to_HVAC_min': 'VRGrid_to_HVAC_min',
    'VRGrid_to_Eev_min': 'VRGrid_to_Eev_min',
    'VRGrid_total_min_use': 'VRGrid_total_min_use',
    'VRGrid_to_Eh_flex_1el': 'VRGrid_to_Eh_flex_1el',
    'VRGrid_to_Eh_flex_3el': 'VRGrid_to_Eh_flex_3el',
    'VRGrid_to_Ec_flex_1el': 'VRGrid_to_Ec_flex_1el',
    'VRGrid_to_Ec_flex_3el': 'VRGrid_to_Ec_flex_3el',
    'VRGrid_to_Edhw1_flex': 'VRGrid_to_Edhw1_flex',
    'VRGrid_to_Edhw2_flex': 'VRGrid_to_Edhw2_flex',
    'VRGrid_to_HVAC_flex': 'VRGrid_to_HVAC_flex',
    'VRGrid_to_Eev_flex': 'VRGrid_to_Eev_flex',
    'VRGrid_to_Batt': 'VRGrid_to_Batt',
    'VRGrid_total_flex_use': 'VRGrid_total_flex_use',
    'VRGrid_to_building': 'VRGrid_to_building',
    'Eev_discharge_potential': 'Eev_discharge_potential',
    'Eev_to_user': 'Eev_to_user',
    'Eev_to_Eh_min': 'Eev_to_Eh_min',
    'Eev_to_Ec_min': 'Eev_to_Ec_min',
    'Eev_to_Edhw_min': 'Eev_to_Edhw_min',
    'Eev_to_Ev_min': 'Eev_to_Ev_min',
    'Eev_to_HVAC': 'Eev_to_HVAC',
    '#2': 'v_2',
    '#3': 'v_3',
    'Eev_discharge_total': 'Eev_discharge_total',
    '#5': 'v_5',
    'Grid_to_user': 'Grid_to_user',
    'Grid_to_Eh_min': 'Grid_to_Eh_min',
    'Grid_to_Ec_min': 'Grid_to_Ec_min',
    'Grid_to_Edhw_min': 'Grid_to_Edhw_min',
    'Grid_to_Ev_min': 'Grid_to_Ev_min',
    'test_grid_hvac': 'test_grid_hvac',
    'Grid_to_HVAC_min': 'Grid_to_HVAC_min',
    'Grid_to_Eev_min': 'Grid_to_Eev_min',
    'Grid_to_building_min': 'Grid_to_building_min',
    'Spalte15': 'Spalte15',
    'Spalte16': 'Spalte16',
    'E_grid': 'E_grid',
    'Spalte7': 'Spalte7',
    'Eh_flex_1el_final': 'Eh_flex_1el_final',
    'Eh_flex_3el_final': 'Eh_flex_3el_final',
    'Ec_flex_1el_final': 'Ec_flex_1el_final',
    'Ec_flex_3el_final': 'Ec_flex_3el_final',
    'Edhw1_flex_final': 'Edhw1_flex_final',
    'Edhw2_flex_final': 'Edhw2_flex_final',
    'Eev_flex_final': 'Eev_flex_final',
    'Eev_flex_final_res': 'Eev_flex_final_res',
    'Eev_flex_final_work': 'Eev_flex_final_work',
    'Eev_flex_final_ret': 'Eev_flex_final_ret',
    'Batt_total_charge': 'Batt_total_charge',
    'Spalte14': 'Spalte14',
    'Qh_min_excl_distr_losses': 'Qh_min_excl_distr_losses',
    'Qh_flex_wasteheat_final': 'Qh_flex_wasteheat_final',
    'Qh_flex_1el_final': 'Qh_flex_1el_final',
    'Qh_flex_3el_final': 'Qh_flex_3el_final',
    'Qh_total_final': 'Qh_total_final',
    'Qh_u': 'Qh_u',
    'Qh_c': 'Qh_c',
    'Qhed_1el': 'Qhed_1el',
    'Qhed_2th': 'Qhed_2th',
    'Qhed_3el': 'Qhed_3el',
    'Qhed_4th': 'Qhed_4th',
    'Qhed_total': 'Qhed_total',
    'Qh_distr_losses': 'Qh_distr_losses',
    'Eh_aux': 'Eh_aux',
    'Night_schedule': 'Night_schedule',
    'Night_use': 'Night_use',
    'ACH_nightvent': 'ACH_nightvent',
    'Qv_nightvent': 'Qv_nightvent',
    'Spalte11': 'Spalte11',
    'Qc_min_excl_losses': 'Qc_min_excl_losses',
    'Qc_flex_1el_final': 'Qc_flex_1el_final',
    'Qc_flex_3el_final': 'Qc_flex_3el_final',
    'Qc_flex_excl_losses': 'Qc_flex_excl_losses',
    'QC_total_final': 'QC_total_final',
    'Qced_1el': 'Qced_1el',
    'Qced_2th': 'Qced_2th',
    'Qced_3el': 'Qced_3el',
    'Qced_total': 'Qced_total',
    'Qc_distr_losses': 'Qc_distr_losses',
    'Ec_aux': 'Ec_aux',
    'Qdhw_1_flex2': 'Qdhw_1_flex2',
    'Qdhw_2_flex': 'Qdhw_2_flex',
    'Qdhw_1_total': 'Qdhw_1_total',
    'Qdhw_2_total': 'Qdhw_2_total',
    'Qdhw_total': 'Qdhw_total',
    'Spalte20': 'Spalte20',
    'Spalte21': 'Spalte21',
    'EV_SOCc_d_res': 'EV_SOCc_d_res',
    'EV_SOCc_d_work': 'EV_SOCc_d_work',
    'EV_SOCc_d_retail': 'EV_SOCc_d_retail',
    'EV_SOCc_a_res': 'EV_SOCc_a_res',
    'EV_SOCc_a_work': 'EV_SOCc_a_work',
    'EV_SOCc_a_retail': 'EV_SOCc_a_retail',
    'Spalte238': 'Spalte238',
    'Spalte239': 'Spalte239',
    'Ti_final_uncooled': 'Ti_final_uncooled',
    'Ti_final_cooled': 'Ti_final_cooled',
    'Tdhw_1_final': 'Tdhw_1_final',
    'Tdhw_2_final': 'Tdhw_2_final',
    'Spalte8': 'Spalte8',
    'Batt_final_Whm2': 'Batt_final_Whm2',
    'SOC_preheat_u': 'SOC_preheat_u',
    'SOC_preheat_c': 'SOC_preheat_c',
    'SOC_precool_c': 'SOC_precool_c',
    'SOC_dhw1': 'SOC_dhw1',
    'SOC_dhw2': 'SOC_dhw2',
    'EV_SOC_d_res': 'EV_SOC_d_res',
    'EV_SOC_d_work': 'EV_SOC_d_work',
    'EV_SOC_d_retail': 'EV_SOC_d_retail',
    'EV_SOC_d': 'EV_SOC_d',
    'EV_SOC_a_res': 'EV_SOC_a_res',
    'EV_SOC_a_work': 'EV_SOC_a_work',
    'EV_SOC_a_retail': 'EV_SOC_a_retail',
    'EV_SOC_res': 'EV_SOC_res',
    'EV_SOC_work': 'EV_SOC_work',
    'EV_SOC_retail': 'EV_SOC_retail',
    'SOC_Batt': 'SOC_Batt',
    'Eh_1el': 'Eh_1el',
    'Eh_3el': 'Eh_3el',
    'Ec_1el': 'Ec_1el',
    'Ec_3el': 'Ec_3el',
    'Edhw_1el': 'Edhw_1el',
    'Edhw_2el': 'Edhw_2el',
    'Qenv_h_1el': 'Qenv_h_1el',
    'Qenv_h_3el': 'Qenv_h_3el',
    'Qenv_c_1el': 'Qenv_c_1el',
    'Qenv_c_3el': 'Qenv_c_3el',
    'Qenv_dhw_1': 'Qenv_dhw_1',
    'Qenv_dhw_2': 'Qenv_dhw_2',
    'EUIh_2th': 'EUIh_2th',
    'EUIh_4th': 'EUIh_4th',
    'EUIc_2th': 'EUIc_2th',
    'EUIdhw_1th': 'EUIdhw_1th',
    'EUIdhw_2th': 'EUIdhw_2th',
    'cf_PEI_grid': 'cf_PEI_grid',
    'cf_PEI_flex_grid': 'cf_PEI_flex_grid',
    'cf_PEI_flex_gridsub': 'cf_PEI_flex_gridsub',
    'cf_PEI_PV': 'cf_PEI_PV',
    'cf_PEI_PV_gridsub': 'cf_PEI_PV_gridsub',
    'PEI_el_user': 'PEI_el_user',
    'PEI_el_hvac': 'PEI_el_hvac',
    'PEI_district_heating': 'PEI_district_heating',
    'PEI_natural_gas': 'PEI_natural_gas',
    'PEI_biomass': 'PEI_biomass',
    'PEI_other': 'PEI_other',
    'PEI_mob_el': 'PEI_mob_el',
    'PEI_mob_ext': 'PEI_mob_ext',
    'PEI_el_demand': 'PEI_el_demand',
    'Spalte18': 'Spalte18',
    'PEI_flex_grid': 'PEI_flex_grid',
    'PEI_flex_grid_substitution': 'PEI_flex_grid_substitution',
    'PEI_PV_direct': 'PEI_PV_direct',
    'Spalte10': 'Spalte10',
    'Spalte13': 'Spalte13',
    'cf_GHG_grid': 'cf_GHG_grid',
    'GHG_plugloads': 'GHG_plugloads',
    'GHG_hvac': 'GHG_hvac',
    'cost_E_grid': 'cost_E_grid',
    'cost_VRGrid_flex': 'cost_VRGrid_flex',
    'cost_PV_to_Egrid': 'cost_PV_to_Egrid',
    'Spalte3': 'Spalte3',
}
