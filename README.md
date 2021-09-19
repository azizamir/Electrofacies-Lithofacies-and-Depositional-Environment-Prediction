# Electrofacies-Lithofacies-and-Depositional-Environment-Prediction

## Overview
This research was conducted to be presented at ISPG Research Forum 2021. In this research, my partner and I are implemented the usage of machine learning in petroleum geoscience by utilized the K-Nearest Neighbors (KNN) as the supervised learning model algorithm to predict electrofacies pattern, lithofacies, and depositional environment classification of three wells from The Browse Basin using P-2 and K-1 well data as training dataset and B-1 well data as testing dataset whereas all of the wells are on the same area. This implementation is intended to aid hydrocarbon exploration activities by reducing subsurface uncertainty and interpretation time.

## Tools Used
- Python version: 3.6.9
- Packages: Numpy, Matplotlib, pandas, jcopml, scikit-learn

## Data Cleaning
Based on the data observation from missing values and data plotting, there are several outliers on GR, DTCO, and NPHI features that needed to be replaced by NaN, so it can be imputed on the preprocessing stages. 

## Preprocessing
Since all of the features are numerical, I imputed the 'NaN' values with mean of the features that contained it and also applied transform using 'yeo-johnson' on the depositional environment and electrofacies model, and scaled the features using standard scaler on the lithofacies model.

## Model Building
I started build the machine learning model using K-Nearest Neighbors algorithm and tuned several hyperparameters, namely:
- n_neighbors = odd numbers start from 1 to 29
- Distance calculation method (p) = manhattan, euclidian, and minkowski distance
- weights = uniform and distance

## Model performance 
The confusion matrix result from validation stages shows that the KNN algorithm generates a quite similar prediction compared with the actual data and produces a good test score with an accuracy value above 0.75 from three prediction cases. 

<img src="https://github.com/azizamir/electrofacies--lithofacies--and-depositional-environment-prediction/blob/main/results/matrix.png" width="800" height="300" />

## Geoscience interpretation
The model also generates quite good electrofacies, lithofacies, and depositional environment classification patterns based on the B-1 well plot and indicates that there is a Plover Fm continuity as the reservoir zone at depth ~4780 m to ~4870 m that predicted having a dominant Siltstone-Sandstone facies and marine-influenced depositional environment.

<img src="https://github.com/azizamir/electrofacies--lithofacies--and-depositional-environment-prediction/blob/main/results/B-1%20Prediction.png" width="900" height="500" />

