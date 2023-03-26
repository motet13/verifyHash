# verifyHash
Verify downloaded file hashed using SHA-256 algorithm.

## Dependencies
- Python3.10 or higher

## Usage

```
# see the help page
python vhash.py -h

# to verify a file in SHA-256 (Windows command-line)
python vhash.py sample.txt 89db5ec54501399bf200d5d72fb03863d8cae325f0b2a1d11f704483680e98a1

# to verify a file in SHA-256 (Linux command-line)
python vhash.py 'sample.txt' '89db5ec54501399bf200d5d72fb03863d8cae325f0b2a1d11f704483680e98a1'
```
