from database.DAO import DAO
from model.model import Model

mymodel = Model()
myLinee = DAO.getAllLinee()
mymodel.buildGraph()
print(mymodel.getNumNodes())
print(mymodel.getNumEdges())
print(myLinee)