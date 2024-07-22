class Stack:

    class Knoop:

        def __init__(self,data) -> None:
            self.data = data
            self.volgende = None


        def __eq__(self, __o: object) -> bool:
            
            if isinstance(__o,Stack.Knoop) == True:
                if self.data == __o.data:
                    return True
            return False
        
        def __add__(self, __o: object):            
            newitem = None                     
            volgende = __o.volgende

            while volgende != None:                                 
                
                vorige = volgende
                volgende = volgende.volgende

                if volgende == None:
                    vorige.data =  self.data
                    vorige.volgende =  self.volgende                    
                    newitem = __o
                    break          

            return newitem

        def __str__(self) -> str:
            
            output = "["
            huidige = self.data

            volgende = self.volgende

            if isinstance(volgende ,Stack.Knoop) == True:

                while volgende != None:
                    huidige = volgende.data
                    volgende = volgende.volgende  
                    
                    if isinstance(volgende ,Stack.Knoop) == False:
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

    def __init__(self) -> None:
        self.t = Stack.Knoop(None) # Top
        self.t.data = None
        self.t.volgende = None

    def empty(self) -> bool:
        if self.t.__sizeof__() == 0:
            return True
        return False   

    def push(self,x):
         
        if isinstance(self,Stack.Knoop) == True:
            knoop = self
            volgende = knoop.volgende
        else:
            if isinstance(self,Stack) == False:
                if self == None:
                    self.t.volgende = None
            else:                
                if isinstance(x,Stack) == True:
                    
                    volgende = x.t

                    while volgende != None:                                 
                        
                        vorige = volgende
                        volgende = volgende.volgende

                        if volgende == None:
                            vorige.data =  self.t.data
                            vorige.volgende =  self.t.volgende                    
                            self.t = x.t
                            break
                else:                
                    knoop = Stack.Knoop(None)
                    knoop.data =  x
                    knoop.volgende = self.t
                    self.t = knoop

    
    def pop(self):
        if self.empty() == False:
            item = self.t.data
            self.t = self.t.volgende
            
            return item
        return None


    def peek(self):
        return self.t.data


s = Stack()
s.push("item1")
s.push("item2")
s.push("item3")

n = Stack()
n.push(5)
n.push(1)
n.push(8)
n.push(s)


print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
print(s.pop())
print(s.peek())
n.t = n.t + s.t
print("")