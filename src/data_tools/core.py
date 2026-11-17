import os
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from functools import partial
from tqdm import tqdm

def _read_excel(file: str, dtype:dict):
    return pd.read_excel(io=file, dtype=dtype)

def core(folder_path: str, ext_type: str, dtype: dict, max_workers: int = 4):
    file_path_list = [
        os.path.join(folder_path, f)
        for f in os.listdir(folder_path)
        if f.lower().endswith(ext_type.lower()) and not f.startswith("~$")
    ]

    read_func = partial(_read_excel, dtype=dtype)

    dfs = []
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        for df in tqdm(
            executor.map(read_func, file_path_list),
            total=len(file_path_list),
            desc="Loading files"
        ):
            dfs.append(df)
    
    return pd.concat(dfs, ignore_index=True)