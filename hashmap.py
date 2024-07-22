import gelinktelijst

class HashSet:

    class Map: # knoop

        def __init__(self,data) -> None:
            self.key = None
            self.value = data
            self.volgende = None


        def __eq__(self, __o: object) -> bool:
            
            if isinstance(__o,HashSet.Map) == True:
                if self.value == __o.value:
                    return True
            return False
        
        def __add__(self, __o: object):            
            newitem = None                     
            volgende = __o.volgende

            while volgende != None:                                 
                
                vorige = volgende
                volgende = volgende.volgende

                if volgende == None:
                    vorige.value =  self.value
                    vorige.volgende =  self.volgende                    
                    newitem = __o
                    break          

            return newitem

        def __str__(self) -> str:
            
            output = "["
            huidige = self.data

            volgende = self.volgende

            if isinstance(volgende ,HashSet.Map) == True:

                while volgende != None:
                    huidige = volgende.value
                    volgende = volgende.volgende  
                    
                    if isinstance(volgende ,HashSet.Map) == False:
                        output += str(huidige) + str("]") 
                        break
                    else:
                        output += str(huidige) + str(",") 

            else:     
                if output == "[":
                    if huidige != None:
                        output += str(huidige) + str("]")
                    else: 
                        output = "[]"
                else:
                    output += "]"


            return output

            

        def __sizeof__(self) -> int:
            
            index = 0
            volgende = self.volgende

            while volgende != None:                                 
                
                vorige = volgende
                volgende = volgende.volgende
                index +=1

            return index


 
    def __init__(self,max_size) -> None:
        self.maxsize = max_size
        self.w = [None]*max_size
        self.node = [None]*max_size

    def insert(self,woord):
        h = hash(woord)
        pos = h % self.maxsize

        index = 0        

            
        if self.w[pos] == None:
            self.w[pos] = gelinktelijst.Gelinktelijst().get_anker()
            node = self.Map(woord)
            node.key = pos
            node.value = woord
            node.volgende = None
            self.w[pos].volgende = node


        elif self.w[pos].volgende.volgende == None:
            
                node = self.w[pos].volgende
                node = self.Map(woord)
                node.key = pos
                node.value = woord
                self.w[pos].volgende.volgende = node
                node.volgende = None

                #self.node[pos].volgende = gelinktelijst.Gelinktelijst().get_anker()
                #self.node[pos].volgende.volgende = gelinktelijst.Gelinktelijst().Knoop(woord)                
                #self.node[pos].volgende.volgende.data = woord

                #volgende = self.node[pos].volgende.volgende.volgende
                #volgende = None
                
        else:
            volgende = self.w[pos].volgende

            while volgende != None:
                vorige = volgende
                volgende = volgende.volgende

                if volgende == None:
                    node = self.Map(woord)
                    node.key = pos
                    node.value = woord
                    node.volgende = None
                    volgende = node
                    vorige.volgende = volgende
                    break
                

    def get_key(self,woord):
        h = hash(woord)
        pos = h % self.maxsize

        index = 0        

        while self.node != None:

            volgende = self.w[pos].volgende

            while volgende != None:
                vorige = volgende
                volgende = volgende.volgende
                
                if isinstance(vorige,self.Map):
                    node = vorige
                    if node.value == woord:
                        return node.key
                else:
                    break
            break 

        return -1
                        
    def get_value(self,key):
        h = hash(key)
        pos = h % self.maxsize

        index = 0        

        while self.node != None:

            volgende = self.w[pos].volgende

            while volgende != None:
                vorige = volgende
                volgende = volgende.volgende
                
                if isinstance(vorige,self.Map):
                    node = vorige
                    if node.key == key:
                        return node.value
                else:
                    break
            break 

        return -1

    def delete(self,woord):
        h = hash(woord)
        pos = h % self.maxsize

        index = 0        

        while self.w != None:

            volgende = self.w[pos].volgende

            while volgende != None:
                vorige = volgende
                volgende = volgende.volgende
                
                if isinstance(volgende,self.Map):
                    node = volgende
                    if node.key == woord:
                        vorige.volgende = node.volgende #>-> ---> >->
                        return woord
                else:
                    break
            break 

        return -1

    def __str__(self) -> str:

        index = 0        
        vorige = None
        volgende = None
        output = ""
        output += str("{")

        while isinstance(self.w[index], gelinktelijst.Gelinktelijst.Knoop) == False:
            index+=1            

        volgende = self.w[index].volgende            
            
        while volgende != None:    
            
            if volgende == None:            
                while isinstance(self.w[index], gelinktelijst.Gelinktelijst.Knoop) == False:
                    index+=1            

                if index == self.maxsize:
                    break

                volgende = self.w[index].volgende            

            if volgende != None:
                if isinstance(volgende,self.Map):
                    node = volgende
                    output += str("{") + str(node.key) + " : " + str(node.value) + str("},")    
                    volgende = volgende.volgende        
                
                        
            if volgende == None:
                if index == self.maxsize:
                    break

                while isinstance( self.w[index], gelinktelijst.Gelinktelijst.Knoop) == False:
                    index+=1                                

                if index == self.maxsize:
                    break

                volgende = self.w[index].volgende
                index +=1
            

        output = output[:-1] + ""
        output += str("}")
        
        return output


h = HashSet(10)
h.insert("Yellow")
h.insert("Blue")
h.insert("Green")
h.insert("Black")
h.insert("Orange")
h.insert("Purple")
h.insert("Gray")
h.insert("Pink")
h.insert("White")
h.insert("Red")

print(h.get_value("Yellow"))
print(h.get_value("Blue"))
print(h.get_value("Green"))
print(h.get_value("Black"))
print(h.get_value("Orange"))
print(h.get_value("Purple"))
print(h.get_value("Gray"))
print(h.get_value("Pink"))
print(h.get_value("White"))
print(h.get_value("Red"))

h.insert("Brown") 
h.insert("Indigo")
h.insert("Bronze")

h.insert("Green")
h.insert("Black")
h.insert("Orange")
h.insert("Purple")
h.insert("Gray")
h.insert("Pink")
h.insert("White")

h.insert("Blue")
h.insert("Green")
h.insert("Black")
h.insert("Orange")
h.insert("Purple")
h.insert("Gray")
h.insert("Pink")
h.insert("White")
h.insert("Red")


print(h)
print(h.get_value("Black"))
h.delete("Black")

print(h)
print(h.get_value("Black"))
h.delete("Black")

print(h)
print(h.get_value("Black"))
h.delete("Black")
print(h)
print(h.maxsize)
print("Yes")

t = HashSet(5)
t.insert("D")
t.insert("E")
t.insert("M")
t.insert("O")
t.insert("C")
t.insert("R")
t.insert("A")
t.insert("T")
t.insert("I")
t.insert("S")
t.insert("C")
t.insert("H")

print(t)
print(t.maxsize)

print(h.get_value(5))