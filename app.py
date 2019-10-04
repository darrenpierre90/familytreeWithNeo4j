from py2neo import *
from py2neo.ogm import * 
"py2neo reference page:https://github.com/elena/py2neo-quickstart"
Graph = Graph("bolt://localhost:7687",auth=('neo4j', 'Basketball77'))
nodes_matcher = NodeMatcher(Graph)
Guerrier="Guerrier"
Pierre="Pierre"
RelationName="Is_Parent_OF"


class Person(GraphObject):
    __primarykey__ = "name"

    name = Property()
    lastName=Property()
    gender=Property()
    child = RelatedFrom("Person","Parents_Of")
    parent = RelatedTo("Person")


class Parents_Of(Relationship):
    pass


def createPerson(name,lastName):
    person=Person()
    person.name=name
    person.lastName=lastName
    return person



def createChildren(parentName,parentFamilyName,children):
    RelationName="Is_Parent_OF"
    parent=createPerson(parentName,parentFamilyName)
    for child in children:
        person=createPerson(child,parentFamilyName)
        Graph.merge( Relationship(parent.__ogm__.node, RelationName, person.__ogm__.node))


def script():
    pegChildren=[
          "Carole","Nyrva","Hebert","Cazeau","Chris","Hebert",
          "Bonnie","Christella","Falide","Lynda","Betelair","Edline"
    ]
    
    createChildren("Edgard",Guerrier,pegChildren)

    chrisKids=["Jennifer","Carl-Henry","Dortina"]
    createChildren("Chris",Guerrier,chrisKids)
    
    edlineKids=["Give-Lord","Nirlan"]
    createChildren("Edline",Guerrier,edlineKids)

    milenekids=["Annete","Beaugeles","Andre","Ernst"]
    createChildren("Milene",Pierre,milenekids)
    createChildren("Beaugess",Pierre,milenekids)

    beaugessKids=["Odenis","Mona","Odolos","Millin"]
    createChildren("Beaugess",Pierre,beaugessKids)


def findParents(targetNode):
    print("hello")


def main():
    
    people =(Graph.nodes.match("Person"))
    print(list(people))
    for ppl in people:
        print(f"the Person is {ppl['name']}")
        gender=input("what is it gender?")
        ppl['gender']= 'Male' if gender=='m' else 'Female'
        Graph.create(ppl)
        

    print(list(people))
    
    

if __name__ == "__main__":
   main()