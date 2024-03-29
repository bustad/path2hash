import argparse
import sys
import os
import hashlib
import base64
import datetime
from pathlib import Path

p = argparse.ArgumentParser(description='Write SHA-512 hash, creation time, modification time, file size and file path for each file in one or more directory tree to a text file.')
p.add_argument('path', nargs='+', help='One or more file paths.')
p.add_argument('-o', '--output', required=True, help='Output text file.')
p.add_argument('-ctime', action='store_true', help='Write creation time.')
p.add_argument('-mtime', action='store_true', help='Write modification time.')
args = p.parse_args()

for k in args.path:
    if not Path(k).is_dir():
        sys.exit(f"{k} is not a directory.")

print("Calculating hashes for these paths:\n" + "\n".join(args.path) + "\n")
print(f"Writing output to {args.output}.\n")

with open(args.output, "w", encoding="utf-8") as fo:
    for k in args.path:
        for path, dirs, files in os.walk(k):
            dirs.sort(key=str.casefold)
            for file in sorted(files, key=str.casefold):
                filename = os.path.join(path,file)

                with open(filename, 'rb', buffering=0) as fi:
                    digest = hashlib.file_digest(fi, 'sha512')
                s = base64.b85encode(digest.digest()).decode('utf-8')
                print(s, end="")
                fo.write(s)

                stats = Path(filename).stat()

                s = f"{str(stats.st_size):>13}"
                print(s, end=" ")
                fo.write(s + " ")

                if args.ctime:
                    s = f"{datetime.datetime.fromtimestamp(stats.st_ctime).isoformat():<26}"
                    print(s, end=" ")
                    fo.write(s + " ")

                if args.mtime:
                    s = f"{datetime.datetime.fromtimestamp(stats.st_mtime).isoformat():<26}"
                    print(s, end=" ")
                    fo.write(s + " ")

                print(filename[3:])
                fo.write(filename[3:] + "\n")
