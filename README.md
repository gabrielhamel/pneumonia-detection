# Zoidberg 2.0

## Installation

0) Clone the project and go into
    ```bash
    git clone git@github.com:EpitechMscPro2020/zoidberg2.0_2020_35.git
    cd zoidberg2.0_2020_35
    ```

1) Download the [dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia) and place `chest_Xray` folder at the repository root.

2) Create python environment. You must have [venv](https://docs.python.org/3/library/venv.html) or [conda](https://conda.io/projects/conda/en/latest/index.html) on your machine
    ```bash
    # venv
    python3 -m venv env
    # or with conda
    conda create -n env python=3
    ````
3) Install dependencies
    ```bash
    source env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
4) Launch jupyter web browser
    ```bash
    jupyter-notebook
    ```
## Notebooks
1) Dataset
    - Prepare data before training, it is mandatory before execution of another notebook
    - It will create a new file `dataset.hdf5`
2) CNN
    - Train AI on previous created dataset with CNN model
## Binary

We made a GUI to use our already trained model in `./model/cnn`.
You just need to upload image with `upload` button. The GUI will show the classification label and her prediction accuracy

> Doesn't need notebooks execution or any dataset

> You must have enabled the virtual env (goto installation 2.)
```bash
python prgm/ui/main.py
```
