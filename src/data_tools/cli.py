import sys
import pickle
import argparse
from .core import core

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", required=True)
    parser.add_argument("--ext", default=".xlsx")
    parser.add_argument("--max_workers", type=int, default=None)
    parser.add_argument("--dtype_pickle", required=True, help="Path dtype pickle")
    args = parser.parse_args()

    with open(args.dtype_pickle, "rb") as f:
        dtype = pickle.load(f)

    dfs = core(
        folder_path=args.folder,
        ext_type=args.ext,
        dtype=dtype,
        max_workers=args.max_workers
    )

    pickle.dump(dfs, sys.stdout.buffer)

if __name__ == "__main__":
    main()