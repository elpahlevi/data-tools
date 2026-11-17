# data-tools

A collection of helper utilities for data analysis and engineering workflows.

This is a personal toolkit of reusable functions that make everyday data work faster. It will grow over time as new helpers are added.

## Installation

Download the latest `.whl` file from the [Releases](https://github.com/elpahlevi/data-tools/releases) page, then install it:

```bash
pip install data_tools-1.0.0-py3-none-any.whl
```

Or install directly from the release URL:

```bash
pip install https://github.com/elpahlevi/data-tools/releases/download/v1.0.0/data_tools-1.0.0-py3-none-any.whl
```

With [uv](https://docs.astral.sh/uv/):

```bash
uv pip install https://github.com/elpahlevi/data-tools/releases/download/v1.0.0/data_tools-1.0.0-py3-none-any.whl
```

**Requirements:** Python 3.9+. Dependencies (`pandas`, `tqdm`, `openpyxl`) are installed automatically.

## Functions

### `read_multi_excel_concurrent`

Loads multiple Excel files from a folder concurrently and combines them into a single DataFrame. Works in both Jupyter notebooks and regular Python scripts.

```python
from data_tools import read_multi_excel_concurrent

df = read_multi_excel_concurrent(
    folder="path/to/folder",
    dtype={"card_no": "str"},
    max_workers=6,
)
```

| Parameter     | Type   | Default   | Description                                         |
| ------------- | ------ | --------- | --------------------------------------------------- |
| `folder`      | `str`  | required  | Folder containing the Excel files                   |
| `dtype`       | `dict` | required  | Column dtypes passed to `pandas.read_excel`         |
| `max_workers` | `int`  | `4`       | Number of worker processes                          |
| `ext`         | `str`  | `".xlsx"` | File extension to look for                          |

**Returns:** a `pandas.DataFrame` with all files concatenated (`ignore_index=True`).

**How it works:** the files are read in a separate Python process using `ProcessPoolExecutor`, and the result is passed back to the caller. This keeps it safe to call from Jupyter, where multiprocessing on macOS and Windows (`spawn`) normally causes problems.

**Notes:**

- All files in the folder are expected to have compatible columns, since they are concatenated into one DataFrame.
- `data_tools` must be installed in the same Python environment that runs your code.
- A progress bar is shown in the terminal or notebook output while files load.

## Development

This project uses [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
uv sync
uv build
```

The built wheel will be in `dist/`.
