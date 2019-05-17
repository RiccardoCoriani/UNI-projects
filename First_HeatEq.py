import pandas
import matplotlib
import pygimli as pg
import pygimli.meshtools as mt


# Create geometry definition for the modelling domain
world = mt.createWorld(start = [-20,0], end = [20,-16], layers = [-2,-8], worldMarker = False)

# Create an heterogeneous block
block = mt.createRectangle(start = [-6, -3.5], end = [6, -6], marker =4, boundaryMarker=10)

geom = mt.mergePLC([world,block])

pg.show(geom, boundaryMarker=True, savefig='geometry.pdf')



# Create a mesh from the geometry definition
mesh = mt.createMesh(geom, quality=33, area = 0.2)
pg.show(mesh, savefig='mesh.pdf')


T = pg.solver.solveFiniteElements(mesh,
                                  a=[[1, 1.0], [2, 2.0], [3, 3.0], [4, 0.1]],
                                  uB=[[8, 1.0], [4, 0.0]], verbose=True)

ax, _ = pg.show(mesh, data=T, label='Temperature $T$', cmap="hot_r")
pg.show(geom, ax=ax, fillRegion=False)


# Map regions to hydraulic conductivity in m/s

kMap = [[1, 1e-8] , [2,5e-3] , [3,1e-4], [4,8e-4]]

# Mao conductivity value per region to each given mesh cell

K = pg.solver.parseMapToCellArray(kMap, mesh)

# Dirichlet conditions for hydraulic potential

pBound = [[[1,2,3],0.75] , [[5,6,7], 0.0]]

# Solve for hydraulic potential

p = pg.solver.solveFiniteElements(mesh, a=K , uB=pBound)

ax = pg.show(mesh, data=K)
pg.show(geom, ax=ax, FillRegion=True, savefig = 'Hydraulic_Field.pdf')