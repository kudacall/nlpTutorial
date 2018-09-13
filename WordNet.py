'''
These scripts below use wordnet.  Wordnet is basically a network library and hierarchy of words 
(entities) and their relationships with one another.
'''
#SET OBJECT HERE:
obj = "cancer"

from nltk.corpus import wordnet as wn
syn=wn.synsets(obj) #this returns synonym sets.  'beautiful' has two synsets

for sets in syn:
    print sets
    print "synonyms/lemmas:"
    print sets.lemma_names() #returns synonyms
    print "definition:" + sets.definition() #returns definition
    print "hyponyms"
    print  sets.hyponyms() #hyponyms are more precise examples
    print "meronyms:"
    print sets.part_meronyms() #parts of the object
    print sets.substance_meronyms() #what object is made of
    print "holonyms and hypernyms"
    print sets.member_holonyms() #what object is a member of
    print sets.hypernyms() #theres are terms with broader/less specific scope definition
    print sets.entailments() #works mostly for verbs but what activity includes (entails)
    #Meronyms are components of objects.  Ex. Tree: Limb, stump, trunk
    #holonyms are what contains objects.  Ex. Tree: Forest, jungle.
    
#Another useful tool with synsets is that you can find the closeness of two synsets based on the distance
#the two synsets are from each other.  This is helpful to calibrate your baseline and make sure that the
#objects returned are relevant to what you are actually searching for.

turtle = wn.synset("turtle.n.02")
tortoise = wn.synset("tortoise.n.01")
leopard = wn.synset("leopard.n.01")
cactus = wn.synset("cactus.n.01")
print(turtle.path_similarity(tortoise))
print(turtle.path_similarity(leopard))
print(turtle.path_similarity(cactus))

