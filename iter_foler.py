#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path ## for better path operation

def ls_dir(path="."):
    return [p for p in Path(path).iterdir() if p.is_dir()]

from lxml import etree
import os
import re

import logging
logging.basicConfig(level = logging.DEBUG)
allfiles = []###所有文件的path


def gen_filetree(startpath='.',filetype=""):
    '''利用os.walk 遍历某个目录，收集其内的文件，返回
    (文件路径列表, 本路径下的文件列表)
    比如:
    (['shortly'], ['shortly.py'])
(['shortly', 'templates'], ['shortly.py'])
(['shortly', 'static'], ['shortly.py'])

    第一个可选参数 startpath  默认值 '.'
    第二个参数  filetype  正则表达式模板 默认值是"" 其作用是只选择某些文件
    如果是空值，则所有的文件都将被选中。比如 "html$|pdf$" 将只选中 html和pdf文件。
    '''
    for root, dirs, files in os.walk(startpath):
        dirs.sort()#排序
        filelist = []
        for f in files:
            fileName,fileExt = os.path.splitext(f)
            if filetype:
                if re.search(filetype,fileExt):
                    filelist.append(f)
            else:
                filelist = files
        if filelist:#空文件夹不加入
            dirlist = root.split(os.path.sep)
            dirlist = dirlist[1:]
            if dirlist:
                yield (dirlist, filelist)
            else:
                yield (['.'], filelist)


def get_dirpath(dirlist):
    return os.path.join(*dirlist)

def get_filepath(dirlist,filename):
    return os.path.join(get_dirpath(dirlist),filename)

def inter_folder(filetype):
    for dirlist,filelist in gen_filetree(filetype=filetype):
        if 'templates' in dirlist:
            continue
        elif 'backups' in dirlist:
            continue
        elif 'images' in dirlist:
            continue
        elif dirlist == ['.']:
            continue

        yield (dirlist,filelist)

def remove_tempfile():
    for dl,fl in inter_folder("~$"):
        for f in fl:
            filename = get_filepath(dl,f)
            os.remove(filename)

def gen_md_file():
    for dl,fl in inter_folder(".org$"):
        for f in fl:
            filename = get_filepath(dl,f)
            print(filename)
            import subprocess
            subprocess.call("emacs {filename} -u 'wanze' --batch  -f org-md-export-to-markdown".format(filename=filename), shell=True)
            # remove the org file
            os.remove(filename)


def main():
    remove_tempfile()
    gen_md_file()

if __name__ == '__main__':
    main()

