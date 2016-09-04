#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pygments.styles import get_all_styles

styles = list(get_all_styles())

for style in styles:
    import subprocess
    print('pygmentize -f html -S {style} -a .highlight>{style}.css'.format(style=style))
    subprocess.call('pygmentize -f html -S {style} -a .highlight>{style}.css'.format(style=style),shell=True)


#if __name__ == '__main__':
