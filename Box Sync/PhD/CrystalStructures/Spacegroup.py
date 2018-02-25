#!/usr/bin/env python

# Space group transformations for a subset of the 230 space groups.

def choose(spacegroup):
    if spacegroup == 'Pbca':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0.5],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,-1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]],
                      [[1,0,0,0.5],[0,1,0,0],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0],[0,-1,0,0.5],[0,0,1,0.5],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0.5],[0,0,1,0],[0,0,0,1]]]
                      
    elif spacegroup == 'Cc':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[1,0,0,0],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,1,0,0.5],[0,0,1,0],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,1,0.5],[0,0,0,1]]]

    elif spacegroup == 'P21/c':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0.5],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0],[0,-1,0,0.5],[0,0,1,0.5],[0,0,0,1]]]

    elif spacegroup == 'P21':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0.5],[0,0,-1,0],[0,0,0,1]]]

    elif spacegroup == 'Pna21':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0.5],[0,0,1,0.5],[0,0,0,1]]]

    elif spacegroup == 'PBCN':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,-1,0,0.5],[0,0,1,0.5],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,-1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]],
                      [[1,0,0,0.5],[0,1,0,0.5],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0.5],[0,0,1,0],[0,0,0,1]]]

    elif spacegroup == 'P212121':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0.5],[0,0,-1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,-1,0],[0,0,0,1]]]

    elif spacegroup == 'C2/c':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0],[0,0,-1,0.5],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]],
                      [[1,0,0,0],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,1,0,0.5],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0.5],[0,0,-1,0.5],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,-1,0,0.5],[0,0,-1,0],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0.5],[0,0,1,0.5],[0,0,0,1]]]

    elif spacegroup == 'P-1':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,-1,0],[0,0,0,1]]]

    elif spacegroup == 'Pca21':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,-1,0,0],[0,0,1,0.5],[0,0,0,1]],
                      [[1,0,0,0.5],[0,-1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0],[0,0,1,0.5],[0,0,0,1]]]

    elif spacegroup == 'C2':
        Transforms = [ [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0],[0,1,0,0],[0,0,-1,0],[0,0,0,1]],
                      [[1,0,0,0.5],[0,1,0,0.5],[0,0,1,0],[0,0,0,1]],
                      [[-1,0,0,0.5],[0,1,0,0.5],[0,0,-1,0],[0,0,0,1]]]

    return Transforms

