class HashSet:

    FLAG = -999999
 
    def __init__(self,max_size) -> None:
        self.maxsize = max_size
        self.w = [None]*max_size

    def insert(self,element):
        h = hash(element)
        pos = h % self.maxsize

        index = 0        


        while self.w != None:

            if self.index_of(element) != -1:
                index = 0
                break
            
            if self.w[pos] == None or self.w[pos] == self.FLAG:
                self.w[pos] = element
                break
            else:
                index = 0
                i = int(self.maxsize  / 2)   
                if self.w[i] == None or self.w[i] == self.FLAG:
                    self.w[i] = element
                    break

                it = 0

                if pos <= int(self.maxsize / 2):
                    it = 1
                    Left = True
                    Right = False
                else:
                    it = -1
                    Right = True
                    Left = False
                
                
                while index < self.maxsize:
                    if Right == True:

                        for i in range(self.maxsize-1,0,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == None or self.w[e] == self.FLAG:
                                self.w[e] = element
                                index = self.maxsize
                                break

                            index+=1
                    else:

                        for i in range(0,self.maxsize-1,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == None or self.w[e] == self.FLAG:
                                self.w[e] = element
                                index = self.maxsize
                                break
                            
                        
                            index+=1

                    #enable primary clustering

                    if index == self.maxsize-1:                        
                  
                        hashSet = HashSet(self.maxsize + self.maxsize)
     
                        for i in range(0,self.maxsize-1,1):
                           hashSet.insert(self.w[i])
                        
                        self.maxsize = hashSet.maxsize
                        self.w = hashSet.w
                    
                    else:
                        break



            break

    def index_of(self,element):
        h = hash(element)
        pos = h % self.maxsize

        index = 0        

        

        while self.w != None:
            
            if self.w[pos] == element:
                return pos    
            else:
                index = 0
                i = int(self.maxsize  / 2)   
                if self.w[i] == element:
                    return i
                    break

                it = 0

                if pos <= int(self.maxsize / 2):
                    it = 1
                    Left = True
                    Right = False
                else:
                    it = -1
                    Right = True
                    Left = False
                
                
                while index < self.maxsize:
                    if Right == True:

                        for i in range(self.maxsize-1,0,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == element:
                                index = self.maxsize
                                return e                                
                            index+=1
                    else:

                        for i in range(0,self.maxsize-1,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == element:
                                index = self.maxsize
                                return e
                        
                            index+=1

                return -1
            break

        if self.w[pos] == self.FLAG:
            return -1    

    def delete(self,element):
        h = hash(element)
        pos = h % self.maxsize

        index = 0        

        while self.w != None:
            
            if self.w[pos] == element:
                self.w[pos] = self.FLAG
                break
            else:
                index = 0
                i = int(self.maxsize  / 2)   
                if self.w[i] == element:
                    self.w[i] = self.FLAG
                    break

                it = 0

                if pos <= int(self.maxsize / 2):
                    it = 1
                    Left = True
                    Right = False
                else:
                    it = -1
                    Right = True
                    Left = False
                
                
                while index < self.maxsize:
                    if Right == True:

                        for i in range(self.maxsize-1,0,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == element:
                                self.w[e] = self.FLAG
                                index = self.maxsize
                                break
                    else:

                        for i in range(0,self.maxsize-1,it):
                            
                            if Right == True:
                                e = int((self.maxsize-1)  - (i%(self.maxsize-1)))
                            elif Left == True:
                                e = int(0 + (i%(self.maxsize-1)))

                            if self.w[e] == element:
                                self.w[e] = self.FLAG
                                index = self.maxsize
                                break
                        
                    index+=1

                
            break

    def __str__(self) -> str:
        
        index = 0
        output = ""
        output += str("[")

        while index < self.maxsize:            
            output += str(self.w[index]) + "," 
            index +=1

        output = output[:-1] + ""
        output += str("]")
        
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

print(h.index_of("Yellow"))
print(h.index_of("Blue"))
print(h.index_of("Green"))
print(h.index_of("Black"))
print(h.index_of("Orange"))
print(h.index_of("Purple"))
print(h.index_of("Gray"))
print(h.index_of("Pink"))
print(h.index_of("White"))
print(h.index_of("Red"))

h.insert("Brown") #to enable primary clustering on linear address mode
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
print(h.index_of("Black"))
h.delete("Black")

print(h)
print(h.index_of("Black"))
h.delete("Black")

print(h)
print(h.index_of("Black"))
h.delete("Black")
print(h)
print(h.maxsize)
print("Yes")

t = HashSet(10)
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


t.insert("1")
t.insert("2")
t.insert("3")
t.insert("4")
t.insert("5")
t.insert("6")
t.insert("7")
t.insert("8")
t.insert("9")
t.insert("10")


print(t)
print(t.maxsize)

