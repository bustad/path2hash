# path2hash

## Disk clean-up

To save space one can run the following in WSL to list folders that take up the most amount of space:
```
du -sh -- *  | sort -rh  # Files and directories, or
du -sh -- */ | sort -rh  # Directories only
```
<!--- https://unix.stackexchange.com/questions/106330/sort-all-directories-based-on-their-size ---> 

## Generate text files with hashes

The script `path2hash` is written to be run from Windows so that the Windows paths are saved to the text files.

Now using base85 to write each hash to a text file. Could also use base64 or hex.

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