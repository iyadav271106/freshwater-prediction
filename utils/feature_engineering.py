import pandas as pd
import numpy as np

def build_time_series_features(hydrology_df, date_col="date"):
    df = hydrology_df.sort_values(["basin_id", date_col]).copy()
    df["month"] = df[date_col].dt.month
    df["year"] = df[date_col].dt.year
    df["season"] = df["month"] % 12 // 3 + 1
    grp = df.groupby("basin_id")["discharge_m3s"]
    for lag in [1, 3, 6, 12]:
        df[f"discharge_lag_{lag}m"] = grp.shift(lag)
    df["discharge_roll_mean_3m"] = grp.transform(lambda s: s.rolling(3, min_periods=1).mean())
    df["discharge_roll_std_3m"] = grp.transform(lambda s: s.rolling(3, min_periods=1).std())
    df["discharge_roll_mean_12m"] = grp.transform(lambda s: s.rolling(12, min_periods=1).mean())
    df["discharge_yoy_pct_change"] = grp.pct_change(periods=12)
    return df

def build_climate_features(climate_df):
    df = climate_df.copy()
    df["water_balance_mm"] = df["precip_mm"] - df["evapotranspiration_mm"]
    df["precip_zscore"] = df.groupby("basin_id")["precip_mm"].transform(
        lambda s: (s - s.mean()) / s.std()
    )
    df["drought_flag"] = (df["precip_zscore"] < -1.0).astype(int)
    return df

def build_demand_features(population_df):
    df = population_df.sort_values(["basin_id", "year"]).copy()
    df["population_growth_rate"] = df.groupby("basin_id")["population_sum"].pct_change()
    df["dependency_ratio"] = df["dependent_population"] / df["population_sum"].replace(0, np.nan)
    return df

def assemble_master_table(hydrology_features, climate_features, demand_features):
    merged = hydrology_features.merge(climate_features, on=["basin_id", "date"], how="left")
    merged = merged.merge(demand_features, on=["basin_id", "year"], how="left")
    merged = merged.sort_values(["basin_id", "date"])
    merged["target_discharge_next_month"] = merged.groupby("basin_id")["discharge_m3s"].shift(-1)
    return merged
