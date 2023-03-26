import hashlib
import sys
from pathlib import PurePath, Path


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('Type: python vhash.py -h for help')
        sys.exit()

    if len(sys.argv[1]) > 0:
        # Print Help
        if sys.argv[1] == '-h':
            print('\nDescription:')
            print('  Verify and match downloaded file using SHA256. Returns either PASSED or FAILED')
            print('\nSyntax: python vhash.py [ option[-h] ] [ filePath ] [ str(matchWith) ]')
            print('\nExample: Print this help page')
            print('  python vhash.py -h')
            print('\nUsage:')
            print('  Windows OS:')
            print('      python vhash.py C:\\path\\to\\file AaAaAaAa0B0443c2bb14cffffd9c67jgm256707eb6be661398e9c01e9752f5')
            print('\n  Linux OS:')
            print("       python vhash.py '/path/to/file' 'AaAaAaAa0B0443c2bb14cffffd9c67jgm256707eb6be661398e9c01e9752f5'")
            print("\n  Caution: Notice that for Linux users, each arguments are enclosed within two single quotation marks(').")
            print('\nNote: The 2nd argument after the filePath is just an example of a calculated SHA256. This value is')
            print('      usually given by where you have downloaded the file to verify that the file is not broken.')
            print('\nResult Output:')
            print('\n    *** [ PASSED ] ***')
            print('\n         -- OR --\n')
            print('    *** [ FAILED ] ***')
            print('\nFor Testing, you can use sample.txt as the downloaded file and the calculated SHA256 hash in sample.sha256.txt')
            sys.exit()

    if len(sys.argv) != 3:
        print('Type: python vhash.py -h for help')
        sys.exit()
    else:
        if len(sys.argv[1]) > 0 and len(sys.argv[2]) > 0:

            formattedPath = sys.argv[1].split('\\')
            formattedPath = '/'.join(formattedPath)
            filePath = Path(formattedPath)
            filePurePath = PurePath(formattedPath)
            
            if filePath.exists():  
                matchTo = sys.argv[2]
                starLen = len(f'[ Calculating ] ... : {filePurePath.name}')
                print('\n' + '*'*starLen + '\n')
                print(f'[ Calculating ] ... : {filePurePath.name}')
                print('[ Please wait ] ...')

                #Read given file and digest
                with open(filePath, "rb") as f:
                    digest = hashlib.file_digest(f, "sha256")

                calculatedHash = digest.hexdigest()

                if calculatedHash == matchTo:
                    print(f'Calculated Hash(256): {calculatedHash}')
                    print(f'Must Match Value    : {matchTo}')
                    print('\n*** [ PASSED ] ***')
                else:
                    print(f'Calculated Hash(256): {calculatedHash}')
                    print(f'Must Match Value    : {matchTo}')
                    print('\n*** [ FAILED ] ***')
            else:
                print('File does not exists!')
                print('Exiting...')
                sys.exit()
