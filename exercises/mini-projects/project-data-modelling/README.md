# Data Modelling — Task summary

Goal
- use copilot to generate running code following the markdown descriptions in the iris_analysis.ipynb notebook

For steps 1,2 and 3, some code is already provided to load the data and check it.

1. Project setup
    - Install required packages and confirm kernel settings. 
    - Load the notebook and repository structure.

2. Data loading
    - Import the Iris dataset (from sklearn or CSV).
    - Display sample rows and dataset shape.

3. Quick data sanity checks
    - Check column names, data types, missing values.
    - Compute basic statistics (mean, std, min, max).
    - Add any other checks you would like to do!
    - Example prompt:
        - Determine the interquartile range of each feature in the dataframe.

4. Exploratory data analysis (EDA)
    - Get familiar with the data. Use copilot to generate plots of the data split by the different target.
    - For example you can you get copilot to use PCA to plot the dataset.
    -Example prompt:
        - Use pca on the features and colour by target. 

5. Optional: Choose a model to predict the target!
    - Get copilot to apply a model to predict the target (the plant species) from the features.
    - You can choose a model yourself from sklearn or open up the copilot chat and discuss with copilot what might be most suitable.
    - Example prompt:
        - Use K-nearest neighbours from sklearn to classify the iris dataset and predict the column 'target', print the accuracy of the model once finished.
