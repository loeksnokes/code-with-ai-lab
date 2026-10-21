# `analyze_iris.py` code-origin and license audit

**Scope:** `analyze_iris.py` only, reviewed against its current contents and the
package metadata/licenses installed in the repository's `venv` on 2026-10-21.
This is a practical source review, not legal advice or a complete dependency
license scan.

## Code-origin and license table

| Script lines | Code patch / origin | License identified | Classification | Copyleft? |
| --- | --- | --- | --- | --- |
| 1-121 | The script's analysis flow, printed output, PCA chart setup, and KNN evaluation were written for this repository. No block copied or adapted from an identifiable third-party source was found during this review. | The repository's top-level `LICENSE` says MIT, but its text includes the placeholder “replace with full license text before publishing.” Therefore, the intended project license is stated as MIT, but the checked-in file is incomplete and should not be relied upon as a complete grant. | The script is project-authored; its intended project license appears to be an open-source permissive license (MIT), subject to fixing the incomplete file. | No, MIT is permissive, not copyleft. |
| 4-5, 24 | `pathlib` and `sys` are Python standard-library imports; no standard-library implementation code is copied into this script. | Python Software Foundation (PSF) License. | Open-source permissive. | No. |
| 11, 31-58, 117 | Calls to pandas APIs for DataFrame creation, summaries, grouping, formatting, and display. These are API uses, not copied pandas implementation code. Installed version: pandas 3.0.0. | BSD 3-Clause License, as identified in the installed pandas distribution. | Open-source permissive. | No. |
| 7-10, 65-89 | Calls to Matplotlib APIs to create and save the PCA plot. No Matplotlib implementation code is copied. Installed version: Matplotlib 3.10.8. | Matplotlib License Agreement for Matplotlib 1.3.0 and later; the project describes this as based on the PSF License and BSD-compatible. | Open-source permissive. Preserve Matplotlib's notices if redistributing Matplotlib itself. | No. |
| 12-19, 30, 60-63, 91-115 | Calls to scikit-learn APIs for the bundled Iris data, preprocessing, PCA, train/test splitting, KNN, and metrics. These are API uses, not copied scikit-learn implementation code. Installed version: scikit-learn 1.8.0. | BSD 3-Clause License, as identified in the installed scikit-learn distribution. | Open-source permissive. | No. |

“Copyright” is not a mutually exclusive license category: permissive and
copyleft works can both be copyrighted. The table therefore identifies license
terms and whether they are copyleft; “open-source permissive” describes the
license category, not the absence of copyright.

## Important scope notes

- Importing or calling a library does not, by itself, mean its source code has
  been copied into this script. This review found dependency API usage, not
  borrowed implementation patches.
- `load_iris()` supplies a copy of the classic Iris dataset along with the
  scikit-learn package. The dataset contains 150 flower records, with four
  measurements per flower and three species. UCI describes it as a classic
  dataset from Fisher (1936), credits R. A. Fisher, and notes that the archived
  data differs in a few entries from the data in Fisher's article. The script
  loads the copy bundled with scikit-learn; it does not download data from UCI
  when run.
- Dataset provenance and data-specific terms are distinct from the license on
  scikit-learn. The UCI dataset page/API reviewed here did not state a dataset
  license, so this audit does not assign the data a license or assume the
  scikit-learn software license covers the dataset.
- This table covers the direct libraries visible in the script. It does not
  enumerate every transitive dependency or audit the generated PNG and dataset
  as separate distributable assets.
- Before treating the project as MIT-licensed for distribution, replace the
  placeholder in the root `LICENSE` with the complete intended license text.

## License references

- [Python Software Foundation License](https://docs.python.org/3/license.html)
- [Matplotlib license](https://matplotlib.org/stable/project/license.html)
- [pandas license file](https://github.com/pandas-dev/pandas/blob/main/LICENSE)
- [scikit-learn license file](https://github.com/scikit-learn/scikit-learn/blob/main/COPYING)
- [scikit-learn `load_iris` documentation](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)
- [UCI Iris dataset record](https://archive.ics.uci.edu/dataset/53/iris)
