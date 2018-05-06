"""
Perfect Minimum N Cube

Joonhaeng Lee

"Perfect Minimum N Cube" concept was developed during pavilion design project on yonsei university architectural design studio 3, 2010.
Initially, possible combination of Perfect Minimum N cube (n = 4) were hand calculated with help of Kangdacool.
2016, development of code started to generate possible combination of Perfect Minimum N Cube.

"""

"""

N : integer

Cube: Cube which edges length are 1. Cube exist on 3 dimentional space and all of it's edges are on X = c,y = c ,or Z = c. 

NCube: Group of Cubes, contains N*N*N Cubes. length of each edge on NCube are N.

SubNCube: subgroup of NCube.

Perfect: let's difine SubNCube is "PERFECT" When projected SubNCube on Xy, yZ, XZ plane makes full N*N size square without empty space.

Perfect Minimum N Cube: SubNCube which is Perfect and have N*N Cubes.

Perfect Minimum N Cube representation: 
Perfect Minimum N Cube is reperesented by nested List Z. 
Z = [ y0,y1,y2,...,y(N-1) ]

Each List yk have N unique numbers in range of (0, n-1) 

"""