import numpy as np

def calculate_ndvi(red_band, nir_band):
    ndvi = (nir_band - red_band) / (nir_band + red_band)
    return ndvi

# Assuming you have the red and near-infrared bands as numpy arrays
red_band = np.array([0.1, 0.2, 0.3, 0.4])
nir_band = np.array([0.5, 0.6, 0.7, 0.8])

ndvi = calculate_ndvi(red_band, nir_band)
print("NDVI:", ndvi)







