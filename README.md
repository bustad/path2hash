# path2hash

These are utilities to help clean up disk space, backup important files, find new files and changed files, and to verify written files.

## Disk clean-up

To save space one can run [the following](https://unix.stackexchange.com/questions/106330/sort-all-directories-based-on-their-size) in WSL to list folders that take up the most amount of space:
```
du -sh -- *  | sort -rh  # Files and directories, or
du -sh -- */ | sort -rh  # Directories only
```
(A [double-dash](https://www.tutorialspoint.com/what-does-a-double-dash-in-shell-commands-mean) is a syntax used in shell commands to signify end of command options and beginning of positional arguments.)
<!---  ---> 

## Generate text files with hashes

The script `path2hash.py` is written to be run from Windows (install from [https://www.python.org/](https://www.python.org/)) so that the Windows paths are saved to the text files. Usage:
```
python path2hash.py [-h] -o OUTPUT [-ctime] [-mtime] path [path ...]
# -h prints help.
# -o writes output to the specified text file.
# -ctime includes creation time.
# -mtime includes modification time.

# Examples:
python path2hash.py -o test.txt "D:\test" "D:\test2"
python path2hash.py -o test.txt -ctime -mtime "D:\test" "D:\test2"
```
Now the script is using base85 to write each SHA-512 hash to a text file. One could also use base64 or hex. The files and folders in the [tree](https://stackoverflow.com/questions/10989005/do-i-understand-os-walk-right) are [sorted](https://stackoverflow.com/questions/18282370/in-what-order-does-os-walk-iterates-iterate) when the hashes are calculated. Each line in the resulting text files will follow this structure:
```
SHA-512  SIZE  [CTIME]  [MTIME]  FILENAME
```

## Use tools to compare text files to find new and changed files and to verify file contents

The Linux `diff` command in WSL can be used to check for differences. Several text files can be concatenated using `cat`:
```
cat file1 file2 file3 > newfile
```
The output from `cat` can also be fed directly into `diff` using:
```
diff <(this_command) <(that_command)
```
where the `<(COMMAND)` sequence expands to the name of a pseudo-file (such as /dev/fd/63) from which you can read the output of the command.
An alternative is:
```
cat file1 file2 file3 | diff file4 -
```
Another useful command is `cut`:
```
cut -c LIST [FILE]
cut -c -148,162- "Some file.txt" # An example
```
where LIST is made up of one range or many ranges separated by commas. Each range is one of N, N-, N-M or -M. With no FILE or when FILE is - `cut` reads standard input.