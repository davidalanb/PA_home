import os
import zipfile
import subprocess

def run_scripts(dest, f):

    level=0
    for (dirpath, dirnames, filenames) in os.walk( dest ):
        level+=1
        if( level > 1):
            break

    for filename in filenames:
        if filename.endswith( '.py'):

            srcfile=os.path.join(dirpath,filename)
            f.write('\n'+filename+';')

            srcfile=os.path.join(dirpath,filename)
            report=dest+'/report_'+filename+'.txt'
            report=report.replace(' ','_')

            cmd='py "'+srcfile+'" < input.txt > '+report + ' 2>&1'

            ret=os.system(cmd)
            f.write(str(ret)+';')

            r=open(report,'r')
            for line in r:
                f.write(line.strip()+' ')

            f.write(';')

def main(f):
    for (dirpath, dirnames, filenames) in os.walk( '.' ):
        break

    for filename in filenames:
        if filename.endswith( '.zip' ):
            print("---extracting: "+filename)
            try:
                zf = zipfile.ZipFile( filename )
                dest='temp/'+filename.replace(' ','_')+'_unzip'
                zf.extractall( dest )

                f.write( '\n--- Grading: '+filename+';')
                run_scripts( dest,f )
            except:
                print("\terror extracting: " + filename + ", moving on...")

#------------------------------------------------

f = open('reportfile.txt','w')
main(f)
f.close()









