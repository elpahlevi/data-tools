import os
import sys
import pickle
import tempfile
import subprocess
import pandas as pd

def read_multi_excel_concurrent(folder: str, dtype: dict, max_workers: int = 4, ext: str = ".xlsx") -> pd.DataFrame:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pkl") as tmp:
        pickle.dump(dtype, tmp)
        dtype_path = tmp.name

    try:
        proc = subprocess.run(
            [sys.executable, "-m", "data_tools.cli",
             "--folder", folder, "--ext", ext,
             "--max_workers", str(max_workers),
             "--dtype_pickle", dtype_path],
            stdout=subprocess.PIPE,
            check=False,
        )
        if proc.returncode != 0:
            raise RuntimeError(f"data_tools.cli gagal (exit {proc.returncode})")
        return pickle.loads(proc.stdout)
    finally:
        os.remove(dtype_path)