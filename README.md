# Zoidberg 2.0

## Installation

1) Download the [dataset](https://epitechfr.sharepoint.com/sites/TDEV810/Documents%20partages/Forms/AllItems.aspx?csf=1&e=3ghePT&cid=c2cf4bd0%2D820c%2D420b%2Db5d0%2Dce4747b70428&RootFolder=%2Fsites%2FTDEV810%2FDocuments%20partages%2Fdatasets&FolderCTID=0x0120001264F80C4FAD404A92DAFE76550B2DFC) and place `chest_Xray` folder at the repository root.

2) Install python environment. You must have `Venv` or `Anaconda` on your machine
    ```bash
    python -m venv env
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
3) Launch jupyter web browser
    ```bash
    jupyter-notebook
    ```
4) Open `notebooks/dataset.ipynb` notebook and run it completly. (~3min). After you must see a new file `dataset.hdf5` at the repository root

## Training

1) Run completly `notebooks/cnn.ipynb` notebook to build a new model. You can save it on `model` folder (beware before).
