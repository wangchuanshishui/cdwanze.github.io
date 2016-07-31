#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals

import logging

class BSTree(object):
    '''use hash(str(data)) for support list object etc.'''
    def __init__(self, data=None, parent=None):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

    def __repr__(self):
        return '<BSTree {}>'.format(self.data)

    def insert(self, data):
        '''insert data'''
        if hash(str(data)) < hash(str(self.data)):
            if self.left is None:
                self.left = BSTree(data,parent=self)
            else:
                self.left.insert(data)
        elif hash(str(data)) > hash(str(self.data)):
            if self.right is None:
                self.right = BSTree(data,parent=self)
            else:
                self.right.insert(data)
        else:
            self.data = data

    def find(self,data):
        if hash(str(data)) < hash(str(self.data)):
            if self.left is None:
                raise KeyError
            else:
                return self.left.find(data)
        elif hash(str(data)) > hash(str(self.data)):
            if self.right is None:
                raise KeyError
            else:
                return self.right.find(data)
        else:
            return self

    def introspection(self):
        '''walk a round,and get myself information'''
        stack = []
        node = self
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right

    def get_ymove(self):
        if self.parent is None:
            return 0
        return self.parent.get_ymove() + 1

    def get_xmove(self):
        if self.parent is None:
            return 0

        if self == self.parent.left:
            return self.parent.get_xmove() - 1
        elif self == self.parent.right:
            return self.parent.get_xmove() + 1

    def draw(self):
        from PIL import Image,ImageDraw,ImageFont
        font = ImageFont.truetype("arial.ttf", 15)
        w = 800
        h = 600
        image = Image.new('RGB',(w,h),(255,255,255))
        draw = ImageDraw.Draw(image)
        last_x = None
        last_y = None
        for node in self.introspection():
            node_point_x = node.get_xmove()*50 + 400
            node_point_y = node.get_ymove()*50 + 50


            if node.parent is not None:
                node_point_x_parent = node.parent.get_xmove()*50 +400
                node_point_y_parent = node.parent.get_ymove()*50 +50

                draw.line((node_point_x_parent + 15,node_point_y_parent,node_point_x + 15,node_point_y),fill=(0,0,0))
            #del draw
            draw.ellipse([(node_point_x,node_point_y),(node_point_x+30,node_point_y+30)],outline=(0,0,0))

            draw.text((node_point_x + 15,node_point_y),str(node.data),fill=(0,0,0),font=font)

            last_x = node_point_x
            last_y = node_point_y

        image.show()

    def children_count(self):
        """Return the number of children

        @returns number of children: 0, 1, 2
        """
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt




tree = BSTree(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(4)
tree.insert(7)
tree.insert(14)
tree.insert(13)








#if __name__ == '__main__':
