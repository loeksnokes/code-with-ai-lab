#!/usr/bin/env python3
"""Run the data checks, PCA visualization, and optional classifier from the README."""

from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import sklearn
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


def main() -> None:
    print("Project environment")
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    print(
        f"pandas: {pd.__version__} | scikit-learn: {sklearn.__version__} | "
        f"matplotlib: {matplotlib.__version__}"
    )

    iris = load_iris(as_frame=True)
    df = iris.data.copy()
    df["target"] = iris.target
    features = list(iris.feature_names)

    print("Iris dataset")
    print(f"Rows: {len(df)} | Features: {len(features)} | Shape: {df.shape}")
    print(f"Feature columns: {features}")
    print(f"Target classes: {[str(name) for name in iris.target_names]}")
    print("\nFirst five rows:")
    print(df.head().to_string(index=False))

    print("\nColumn data types:")
    print(df.dtypes.to_string())
    print("\nMissing values per column:")
    print(df.isna().sum().to_string())
    print("\nFeature summary statistics:")
    print(df[features].describe().T.to_string())

    grouped = df.groupby("target")[features]
    grouped_stats = grouped.agg(["count", "mean", "median", "std", "min", "max"])
    grouped_stats.index = iris.target_names[grouped_stats.index]
    print("\nFeature statistics by species:")
    print(grouped_stats.round(2).to_string())

    iqr = grouped.quantile(0.75) - grouped.quantile(0.25)
    iqr.index = iris.target_names[iqr.index]
    print("\nFeature interquartile ranges (IQR) by species:")
    print(iqr.round(2).to_string())

    scaled_features = StandardScaler().fit_transform(df[features])
    pca = PCA(n_components=2)
    components = pca.fit_transform(scaled_features)
    explained = pca.explained_variance_ratio_

    fig, ax = plt.subplots(figsize=(8, 6))
    for target, name in enumerate(iris.target_names):
        mask = iris.target.to_numpy() == target
        ax.scatter(
            components[mask, 0],
            components[mask, 1],
            label=name,
            alpha=0.8,
            edgecolors="white",
            linewidths=0.4,
        )
    ax.set(
        title="Iris species in the first two PCA components",
        xlabel=f"Principal component 1 ({explained[0]:.1%} variance)",
        ylabel=f"Principal component 2 ({explained[1]:.1%} variance)",
    )
    ax.legend(title="Species")
    ax.grid(alpha=0.2)
    fig.tight_layout()

    plot_path = Path(__file__).with_name("iris_pca.png")
    fig.savefig(plot_path, dpi=150)
    plt.close(fig)
    print(f"\nPCA plot saved to: {plot_path}")
    print(f"Variance explained by first two components: {explained.sum():.1%}")

    X_train, X_test, y_train, y_test = train_test_split(
        df[features],
        iris.target,
        test_size=0.2,
        random_state=42,
        stratify=iris.target,
    )
    model = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=5))
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    print("\nOptional model: 5-nearest-neighbors classifier")
    print(f"Training rows: {len(X_train)} | Test rows: {len(X_test)}")
    print(f"Test accuracy: {accuracy_score(y_test, predictions):.1%}")
    print("\nClassification report:")
    print(
        classification_report(
            y_test,
            predictions,
            labels=range(len(iris.target_names)),
            target_names=iris.target_names,
            zero_division=0,
        )
    )
    matrix = confusion_matrix(y_test, predictions, labels=range(len(iris.target_names)))
    print("Confusion matrix (rows = actual, columns = predicted):")
    print(pd.DataFrame(matrix, index=iris.target_names, columns=iris.target_names).to_string())


if __name__ == "__main__":
    main()
