import os
import zipfile
import sys
sys.path.append( 'C:\\Users\\Ashley\\Dave\\Submit\\ProgSet2' )
from tests import testMath, testTurtle

sys.stdin=open('../input.txt')

def run_scripts(dest, f):

    level=0
    for (dirpath, dirnames, filenames) in os.walk( dest ):
        level+=1
        if( level > 1):
            break

    for filename in filenames:

        if filename.endswith( '.py'):
            print('\t',filename, file=f)

            if (filename == "myMath.py"):
                try:
                    testMath( dirpath, f )
                except Exception as e:
                    print('\t\t',e, file=f)

            if ( filename=="myTurtle.py"):
                try:
                    testTurtle( dirpath,f)
                except Exception as e:
                    print('\t\t',e, file=f)

def main(f):
    os.system('rm -rf temp/*')

    for (dirpath, dirnames, filenames) in os.walk( '.' ):
        break

    for filename in filenames:
        if filename.endswith( '.zip' ):
            print("---extracting: "+filename)
            try:
                zf = zipfile.ZipFile( filename )
                fn,ext=os.path.splitext(filename)
                dest='temp/'+fn
                zf.extractall( dest )

                f.write( '\n--- Grading: '+filename+'\n')
                run_scripts( dest,f )
            except:
                try:
                    print( '\ttrying with iz' )
                    # command is 'iz -ef <directory> <file.zip>'
                    # automatically makes subdirectory <file>
                    iz = 'C:\\Users\\Ashley\\Dave\\IZArc2Go\\IZArc2Go.exe'
                    #dest = 'C:\\Users\\Ashley\\Dave\\Submit\\ProgSet2\\pF\\temp'
                    dest=os.getcwd()+'\\temp'

                    #print( dest )
                    #print( dirpath )

                    cmd=iz+' -ef '+dest+' '+filename
                    ret=os.system(cmd)

                    f.write("--- Grading: "+filename+'\n')
                    fn,ext=os.path.splitext(filename)
                    run_scripts( 'temp/'+fn, f )
                except:
                    print("\terror extracting: " + filename + ", moving on...")

#------------------------------------------------

f = open('reportfile.txt','w')
main(f)
f.close()









