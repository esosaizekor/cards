class Gelinktelijst:

    class Knoop:

        def __init__(self,data) -> None:
            self.data = data
            self.volgende = None


        def __eq__(self, __o: object) -> bool:
            
            if isinstance(__o,Gelinktelijst.Knoop) == True:
                if self.data == __o.data:
                    return True
            return False
        
        def __add__(self, __o: object):
            
            volgende = self.volgende
            eerste =  Gelinktelijst.Knoop(None)
            newitem = Gelinktelijst.Knoop(None)
                     

            if isinstance(__o,Gelinktelijst.Knoop) == True:
                            
                while volgende != None:                                 
                        vorige = volgende
                        volgende = volgende.volgende

                        if volgende == None:           
                            item = vorige.data    
                                                             
                            Gelinktelijst.voegtoe(newitem,item)
                            volgende = __o.volgende
                            if __o.data != None:
                                item = __o.data
                                Gelinktelijst.voegtoe(newitem,item)

                            while volgende != None:                                 
                                item = volgende.data
                                Gelinktelijst.voegtoe(newitem,item)
                                volgende = volgende.volgende
                            break
                        else:                      
                            item = vorige.data
                            Gelinktelijst.voegtoe(newitem,item)
                        
            return newitem
        
        def __str__(self) -> str:
            
            output = "["
            huidige = self.data

            volgende = self.volgende

            if isinstance(volgende ,Gelinktelijst.Knoop) == True:

                while volgende != None:
                    huidige = volgende.data
                    volgende = volgende.volgende  
                    
                    if isinstance(volgende ,Gelinktelijst.Knoop) == False:
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
        
    def __init__(self) -> None:
        self.eerste = self.Knoop(None)
        #self.b = self.Knoop(None)
        #self.eerste.volgende = self.b
        

        #print(self.b)  #output 
        #append
    
        self.voegtoe("Players1")
        self.voegtoe("Players2")
        self.voegtoe("Players3")
        self.voegtoe("Players4")
        self.voegtoe(self.Knoop("Yellow"))
        self.voegtoe(self.Knoop("Red"))

        #object output
        #print(self.index(self.b,self.Knoop("Yellow")))
        #print(self.b)
        #self.c = self.b + self.Knoop("Gray")
        #print(self.c)
        #self.c = self.b + self.c
        #print(self.b + self.c)
        #print(self.c)

        # get_item
        #print(self.get_item(self.b,4))
        # index
        #print(self.index(self.b,self.Knoop("Red")))
        #delete
        #self.verwijder(self.b,self.Knoop("Red"))
        #print(self.b)
        #self.verwijder(self.b,self.Knoop("Yellow"))
        #print(self.b)
        #self.verwijder(self.b,"Players3")
        #print(self.b)

    def zoek(self,item):
        
        volgende = self.volgende

        while volgende != None:                                 
            if item == volgende.data:
                return volgende
            
            vorige = volgende
            volgende = volgende.volgende
        
        if volgende == None:
            if item == self.data:
                return self
            

    def verwijder(self,knoop,item):
            eerste =  Gelinktelijst.Knoop(None)    
            newitem = Gelinktelijst.Knoop(None)    
            volgende = knoop.volgende
             
            if volgende == None:
                if knoop.data == item:
                    newitem.data = None
                    newitem.volgende = None

            while volgende != None:                                 
                vorige = volgende
                volgende = volgende.volgende
                
                if item != vorige.data:     
                    Gelinktelijst.voegtoe(newitem,vorige.data)   

            knoop.volgende = newitem.volgende               
            return knoop
            
            

    def voegtoe(self,item):
        
            ref = Gelinktelijst.Knoop(None)
            ref.data = item
            
            if isinstance(self,Gelinktelijst.Knoop) == True:
                knoop = self
                volgende = knoop.volgende
            else:
                if isinstance(self,Gelinktelijst) == False:
                    if self == None:
                        volgende = None
                else:
                    knoop = self.get_anker()
                    volgende = knoop.volgende

            while volgende != None:                                 
                    vorige = volgende
                    volgende = volgende.volgende

                    if volgende == None:
                        
                        volgende = ref
                        vorige.volgende = volgende
                        break

            if volgende == None:                                
                knoop.data = ref.data
                knoop.volgende = Gelinktelijst.Knoop(None)
            
        

    
    def get_item(self,knoop,i):
        
        index = 0
        volgende = knoop.volgende

        while volgende != None:                                 
             if index == i:
                return volgende.data
             
             vorige = volgende
             volgende = volgende.volgende
             index +=1
        
    def index(self,knoop,i):
        
        index = 0
        volgende = knoop.volgende

        while volgende != None:                                 
             
             vorige = volgende
             volgende = volgende.volgende
             index +=1
             if i == volgende.data:
                return index
            
    def size(self,knoop):
        
        index = 0
        volgende = knoop.volgende

        while volgende != None:                                 
             
             vorige = volgende
             volgende = volgende.volgende
             index +=1

        return index
    
    def get_anker(self):
       
       return self.eerste
    
    def invert(self):
        ref = Gelinktelijst.Knoop(None)
        invertlijst = [] 
        invertlijst.append(ref)

        if isinstance(self,Gelinktelijst.Knoop) == True:
            knoop = self
            volgende = knoop.volgende
        else:
            if isinstance(self,Gelinktelijst) == False:
                if self == None:
                    volgende = None
            else:
                knoop = self.get_anker()
                volgende = knoop.volgende

        while volgende != None:                                 
                vorige = volgende
                volgende = volgende.volgende
                invertlijst.append(volgende) # invert lijst

                if volgende == None:
                    
                    volgende = ref
                    vorige.volgende = volgende
                    break
        
        if volgende == None:                                
            knoop.data = ref.data
            knoop.volgende = Gelinktelijst.Knoop(None)

        
        knoop = self.get_anker()
        volgende = knoop.volgende

        s = self.size(knoop)
        i = 0

        for i in range(s-1,0):            
            vorige = volgende
            volgende = volgende.volgende

            if volgende == None:                    
                volgende = ref
                vorige.volgende = volgende
            
            volgende.data = invertlijst[i]
            volgende = Gelinktelijst.Knoop(None)


            
                            




        

mylist = Gelinktelijst()
mylist.invert()




    
