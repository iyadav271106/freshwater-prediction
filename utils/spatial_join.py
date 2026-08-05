import geopandas as gpd
import pandas as pd
from rasterstats import zonal_stats

def population_per_basin(basin_gdf, population_raster_path, basin_id_col="basin_id"):
    stats = zonal_stats(basin_gdf, population_raster_path, stats=["sum"], nodata=-99999, all_touched=True)
    result = basin_gdf[[basin_id_col]].copy()
    result["population_sum"] = [s["sum"] if s["sum"] is not None else 0 for s in stats]
    return result

def merge_dependency_ratio(population_df, dependency_df, basin_to_country_map, basin_id_col="basin_id"):
    merged = population_df.merge(basin_to_country_map, on=basin_id_col, how="left")
    merged = merged.merge(
        dependency_df[dependency_df["source_type"] == "surface_water"], on="country", how="left"
    )
    merged["dependent_population"] = merged["population_sum"] * (merged["pct_population_using"] / 100.0)
    return merged[[basin_id_col, "population_sum", "pct_population_using", "dependent_population"]]

def compute_falkenmark_index(df, annual_renewable_supply_m3_col, population_col):
    out = df.copy()
    out["per_capita_m3"] = out[annual_renewable_supply_m3_col] / out[population_col].replace(0, pd.NA)
    def classify(x):
        if pd.isna(x): return "Unknown"
        if x > 1700: return "No Stress"
        elif x > 1000: return "Stress"
        elif x > 500: return "Scarcity"
        else: return "Absolute Scarcity"
    out["water_stress_class"] = out["per_capita_m3"].apply(classify)
    return out
