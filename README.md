# Freshwater Stress Predictor

> Predicting global freshwater availability and population-weighted water scarcity risk across river basins using machine learning.

**Status:** In Progress

---

## What This Project Does

This project builds a machine learning pipeline that predicts variations in freshwater availability across global river basins, and combines that with population data to estimate **water stress** — how scarce a water source is relative to the number of people who depend on it as their primary water source.

The final deliverable is an interactive dashboard where a user can select a region, see historical water levels, and view predicted future stress classifications.

---

## Why It Matters

Over 2 billion people currently live in water-stressed regions. As climate change accelerates and populations grow, predicting where and when freshwater will become scarce is one of the most important data problems of our time. This project directly addresses **UN Sustainable Development Goal 6: Clean Water and Sanitation**.

---

## Tech Stack

| Area | Tools |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| Geospatial Analysis | GeoPandas, Rasterio, Rasterstats |
| Machine Learning | XGBoost, TensorFlow/Keras (LSTM) |
| Visualization | Plotly, Folium, Matplotlib |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |

---

## Data Sources

| Dataset | What It Provides | Source |
|---|---|---|
| NASA GRACE / GRACE-FO | Groundwater storage anomalies | grace.jpl.nasa.gov |
| GRDC | River discharge time series | portal.grdc.bafg.de |
| ERA5 (Copernicus) | Precipitation, temperature, evapotranspiration | cds.climate.copernicus.eu |
| HydroBASINS | Watershed boundary polygons | hydrosheds.org |
| WorldPop | Gridded population counts | worldpop.org |
| WHO/UNICEF JMP | % population relying on surface water as primary source | washdata.org |
| FAO AQUASTAT | Water withdrawal by sector | fao.org/aquastat |

---

## Project Structure

```
freshwater-prediction/
├── data/
│   ├── raw/              # Raw downloaded datasets
│   ├── processed/        # Cleaned and merged tables
│   ├── hydrology/        # GRDC, GRACE, ERA5 extracts
│   ├── population/       # WorldPop rasters
│   └── dependency/       # JMP, AQUASTAT tables
├── notebooks/
│   ├── 01_eda_hydrology.ipynb
│   ├── 02_eda_population.ipynb
│   ├── 03_spatial_join_basins.ipynb
│   ├── 04_feature_engineering.ipynb
│   └── 05_modeling.ipynb
├── models/               # Saved trained models
├── app/
│   └── streamlit_app.py  # Interactive dashboard
├── utils/
│   ├── data_loader.py
│   ├── spatial_join.py
│   ├── feature_engineering.py
│   └── train_models.py
├── requirements.txt
└── README.md
```

---

## Modeling Approach

**Water Stress Formula:**
```
Water Stress = f(supply_variation, population_demand, dependency_ratio)
```

**Falkenmark Water Stress Index (output classification):**

| Per-Capita Water (m³/person/yr) | Classification |
|---|---|
| > 1,700 | No Stress |
| 1,000 – 1,700 | Stress |
| 500 – 1,000 | Scarcity |
| < 500 | Absolute Scarcity |

**Models used:**
- **XGBoost** — tabular regression on lag/climate/demand features to predict next-period discharge
- **LSTM** — sequence model for longer-horizon time series forecasting per basin

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/freshwater-prediction.git
cd freshwater-prediction
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the dashboard**
```bash
streamlit run app/streamlit_app.py
```

---

## Roadmap

- [x] Project scaffold and structure
- [ ] Data acquisition (GRDC, ERA5, WorldPop, JMP)
- [ ] Exploratory data analysis
- [ ] Geospatial population-to-basin join
- [ ] Feature engineering
- [ ] XGBoost baseline model
- [ ] LSTM sequence model
- [ ] Streamlit dashboard
- [ ] Deploy to Streamlit Community Cloud

---

## Author

**Iyada** — Data Science Student  
[GitHub](https://github.com/yourusername)
