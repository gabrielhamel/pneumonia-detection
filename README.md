# Zoidberg 2.0

## Installation

1) Download the [dataset](https://epitechfr.sharepoint.com/sites/TDEV810/Documents%20partages/Forms/AllItems.aspx?csf=1&e=3ghePT&cid=c2cf4bd0%2D820c%2D420b%2Db5d0%2Dce4747b70428&RootFolder=%2Fsites%2FTDEV810%2FDocuments%20partages%2Fdatasets&FolderCTID=0x0120001264F80C4FAD404A92DAFE76550B2DFC) and place `chest_Xray` folder at the repository root.

2) Install python environment
    ```bash
    python3 -m venv env # Need venv or anaconda on your OS
    source env/bin/activate
    pip3 install -r requirements.txt
    ```
3) Launch jupyter in your web browser
    ```bash
    jupyter-notebook
    ```
4) Open `dataset` notebook and run it completly. (~3min). After you must see a new file `dataset.hdf5` at the repository root

## Training

1) Run completly `cnn` notebook to build a new model. You can save it on `model` folder (beware before).
