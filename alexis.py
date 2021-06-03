

# 1 -> 32 -> 8 octets
# 98989 -> 32
# "alexis" -> 1 * longueur la chaine
# [1, 2, 8, 9] -> 4 * 8 octets
# |1       |2       |8        |9         |'a''l'              |
# |&0|
#                                                                            77
# |&77|&78|"alexis"|                                                         |

#     0
# 77     78



### Comment ça marche
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

        # self.children = [  ....  ]

    def printTree(self):
        print(self.data, "(")
        if self.left:
            print(self.left.printTree())
        print(", ")
        if self.right:
            print(self.right.printTree())
        print(")")

    def size (self):
        taille = 1
        if self.left != None:
            taille += self.left.size()
        if self.right != None:
            taille += self.right.size()
        return taille

# 1 -> 2 -> 3 -> .....

# List
# self.data = 1
# self.next = List(...)

#####

# alexis (remy (mishi (,) None ,) None , robin (shapa (,) None , groco (,) None) None)

# Program

alexisNode = Node("alexis")
#####
alexisNode.children[0] = Node("remy")
alexisNode.children[0].children[0] = Node("mishi")
alexisNode.children[0].children[1] = Node("robin")
alexisNode.children[0].children[2] = Node("shapa")
####

alexisNode.printTree();


print("taille : ", alexisNode.size())


#   alexis
#    /  \
# remy   robin
#  /      /   \
# mishi  shapa groco

#   alexis
#    /
# remy
#/     /       /      /
#robin mishi  shapa groco

# alexis(remy(mishi), robin(shapa, groco))



# 1 -> 2 -> 3 -> .....

 &0 (taille 2*4)
 |1, &99|"bitealexis"|2, &900|"biteremy"|3, 

(&0, taille 4*4 -> taille / 4)
|(&0) 1, (&(0 + 4) 2, (&(0 + 4 * n))3, 4|
|'a', 'l'|   -> taille / 1


integer -> 4 octet
character -> 1 octet

1 octet = 8 bit
32 bit = 4 * 8 bit


|'alexis', 'remy', 'robin', - 10000000000 - 'shapa'|


nombre de gens (40) * taille tableau

          |a, b|
          p1, p2
          multiplier par 2 en parallèle




###### Hash table

def hash(nom) -> int
def hash(data) -> int

# fonction de hashage qui fait la somme des numeros de caractere
'n(a) + n(l) + n(e) + n(x)...' = x = hash(alexis)
hash(sixela) = x

hash(a) -> 0
hash(ab) -> 0 + 1 = 1
hash(b) -> 1 = 1
hash(abb) -> 0 + 1 + 1 = 2
hash(abc) -> 0 + 1 + 2 = 3
hash(acc) -> 0 + 2 + 2 = 4
hash(caca) ->


|Boite1|Boite2|Boite2|Boite3|Boite4|
                       5000   8




BoiteX = |nom1|nom2|







# List
# self.data = 1
# self.next = List(...)



