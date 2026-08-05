import pandas as pd
import geopandas as gpd

def load_grdc_discharge(filepath):
    df = pd.read_csv(filepath, comment="#", skip_blank_lines=True)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df.dropna(subset=["date"])

def load_grace_groundwater(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

def load_era5_climate(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.strip().lower() for c in df.columns]
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    return df

def load_worldpop_raster_stats(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.strip().lower() for c in df.columns]
    return df

def load_un_water_dependency(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def load_water_withdrawal(filepath):
    df = pd.read_csv(filepath)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df

def load_basin_boundaries(filepath):
    gdf = gpd.read_file(filepath)
    gdf.columns = [c.strip().lower() if isinstance(c, str) else c for c in gdf.columns]
    return gdf
