#!/usr/bin/python3

import os 
import pathlib

dirname = '../../notebooks/'

def getit(nbfullpath):
    p = pathlib.Path(nbfullpath)

    if p.suffix != '.ipynb':
        print ('not .ipynb.', p.suffix)
        return
    #
    filename = [p.stem, p.suffix]
    print ('@ ', p, filename)

    cmd = 'jupyter nbconvert --to notebook --execute {} --output {}'.format(nbfullpath, p.name)
    print (cmd)
    os.system(cmd)

    rstcmd = 'jupyter nbconvert --to rst --execute {}'.format(nbfullpath)
    os.system(rstcmd)

    mvcmd = 'mv ' + dirname+filename[0] + '.rst' + '  .'
    os.system(mvcmd)

    mvcmd2 = 'mv ' + dirname+filename[0] + '_files' + '  .'
    os.system('rm -rf ' + filename[0] + '_files')
    os.system(mvcmd2)



def do_all():
    notebooks = os.listdir(dirname)
    for nb in notebooks:
        getit (dirname+nb)
#

def do_1(nbpath):
#    print ('suf: ', p.suffix, 'parent: ', p.parent, 'stem: ', p.stem, 'name: ', p.name)

    getit (nbpath)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print ('usage: ', sys.argv, 'all | notebook_file')
    elif sys.argv[1] == 'all':
        do_all()
    else:
        do_1 (sys.argv[1])
    