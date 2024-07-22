class DubbeleGelinktelijst:

    class Ankercomponent:

        def __init__(self) -> None:
        
            self.vorige = None
            self.data = None
            self.volgende = None  

    class Knoop:

        def __init__(self,data) -> None:
            self.data = data
            self.volgende = None
            self.vorige = None


        def __eq__(self, __o: object) -> bool:
            
            if isinstance(__o,DubbeleGelinktelijst.Knoop) == True:
                if self.data == __o.data:
                    return True
            return False
        
        def __add__(self, __o: object):
            
            volgende = self.vorige
            eerste =  DubbeleGelinktelijst.Ankercomponent()            
            newitem = DubbeleGelinktelijst.Knoop(None)
            laatste =  DubbeleGelinktelijst.Ankercomponent()            
                     
            eerste.vorige = None
            eerste.volgende = newitem
            newitem.volgende = laatste
            newitem.vorige = eerste
            laatste.volgende = None
            laatste.vorige = newitem


            if isinstance(__o,DubbeleGelinktelijst.Knoop) == True:
                            
                while volgende != None:                                 
                        vorige = volgende
                        volgende = volgende.volgende

                        if volgende == None:           
                            item = vorige.data    
                                                             
                            DubbeleGelinktelijst.voegtoe(newitem,item)
                            volgende = __o.vorige
                            if __o.data != None:
                                item = __o.data
                                DubbeleGelinktelijst.voegtoe(newitem,item)

                            while volgende != None:                                 
                                item = volgende.data
                                DubbeleGelinktelijst.voegtoe(newitem,item)
                                volgende = volgende.volgende
                            break
                        else:                      
                            item = vorige.data
                            DubbeleGelinktelijst.voegtoe(newitem,item)
                    
            return newitem
        
        def __str__(self) -> str:
            
            output = "[" 
            if self.vorige != None:
                huidige = self.vorige.data
                volgende = self.vorige.volgende
            else:
                huidige = self.data
                volgende = self.volgende

            

            if isinstance(volgende ,DubbeleGelinktelijst.Knoop) == True:

                while volgende != None:
                    huidige = volgende.data
                    volgende = volgende.volgende  
                    
                    if isinstance(volgende ,DubbeleGelinktelijst.Knoop) == False:
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
        
        self.eerste = self.Ankercomponent()
        self.laatste = self.Ankercomponent()

        #self.b = self.Knoop(None)
        
        #self.eerste.vorige = None
        #self.eerste.volgende = self.b
        #self.b.volgende = self.laatste
        #self.b.vorige = self.eerste
        #self.laatste.volgende = None
        #self.laatste.vorige = self.b
        
        self.eerste.vorige = None
        self.eerste.volgende = self.laatste
        self.laatste.volgende = None
        self.laatste.vorige = self.eerste

        #print(self.b)  #output 
        #append
    
        #self.voegtoe("Players1")
        #self.voegtoe("Players2")
        #self.voegtoe("Players3")
        #self.voegtoe("Players4")
        #self.voegtoe(self.Knoop("Yellow"))
        #self.voegtoe(self.Knoop("Red"))
        

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
            eerste =  DubbeleGelinktelijst.Ankercomponent()    
            newitem = DubbeleGelinktelijst.Knoop(None)   
            laatste = DubbeleGelinktelijst.Ankercomponent()    

            eerste.vorige = None
            eerste.volgende = newitem
            newitem.volgende = laatste
            newitem.vorige = eerste
            laatste.volgende = None
            laatste.vorige = newitem

            volgende = knoop.volgende
             
            if volgende == None:
                if knoop.data == item:
                    newitem.data = None
                    newitem.volgende = eerste
                    newitem.vorige = laatste

            while volgende != None:                                 
                vorige = volgende
                volgende = volgende.volgende
                
                if item != vorige.data:  
                    if vorige.data != None:   
                        DubbeleGelinktelijst.voegtoe(newitem,vorige.data)  
                 

            knoop.volgende = newitem.volgende        
                   
            return knoop
            
            

    def voegtoe(self,item):
        
            ref = DubbeleGelinktelijst.Knoop(None)
            ref.data = item
            
            if isinstance(self,DubbeleGelinktelijst.Knoop) == True:
                knoop = self
                if self.__sizeof__() == 0:                
                    volgende = knoop.volgende
                    volgende.vorige = None
                else:
                    volgende = knoop.volgende
                    volgende.vorige = knoop
            
            else:
                if isinstance(self,DubbeleGelinktelijst) == False:
                    if self == None:
                        volgende = None
                else:
                    knoop = self.get_first_anker()
                    volgende = knoop.volgende
                    volgende.vorige = knoop

            while volgende != None:                                 
                    vorige = volgende
                    
                    if isinstance(volgende,DubbeleGelinktelijst.Knoop) == True:                        
                        if isinstance(volgende.volgende,DubbeleGelinktelijst.Ankercomponent) == True:                                                       
                            if volgende.data == None:
                                volgende.data = ref.data   #data
                                if isinstance(self,DubbeleGelinktelijst.Knoop) == True:
                                    volgende.volgende = DubbeleGelinktelijst.Ankercomponent()
                                    volgende.volgende.vorige = volgende
                                else:
                                    volgende.volgende = self.get_last_anker()                      
                                    volgende.volgende.vorige = volgende
                                break
                    elif isinstance(volgende,DubbeleGelinktelijst.Ankercomponent) == True:                                                    
                            #volgende.vorige.volgende = DubbeleGelinktelijst.Knoop(None)
                            #volgende.vorige.volgende.data = ref.data   #data
                            #volgende.vorige.volgende.vorige = vorige
                            #volgende.vorige.volgende.volgende = DubbeleGelinktelijst.Ankercomponent()
                            #volgende.vorige.volgende.volgende.vorige = vorige.vorige
                            #volgende.vorige.volgende.volgende = volgende.vorige.volgende.volgende
                        
                            del volgende
                            newitem = DubbeleGelinktelijst.Knoop(ref.data)
                            newitem.vorige = vorige.vorige                            
                            vorige.vorige.volgende = newitem

                            newitem.volgende =  DubbeleGelinktelijst.Ankercomponent()
                            newitem.volgende.vorige = newitem
                            vorige.volgende = newitem                 

                            break
                                                    
                    volgende = volgende.volgende #volgende
                    
    
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
             if(isinstance(volgende,DubbeleGelinktelijst.Ankercomponent)):
                break
             vorige = volgende
             volgende = volgende.volgende
             index +=1
             if isinstance(volgende,DubbeleGelinktelijst.Knoop):
                if i == volgende.data:
                    return index
            
    def __sizeof__(self) -> int:
        
        index = 0
        if(isinstance(self,DubbeleGelinktelijst.Knoop)):
            volgende = self.volgende
        else:
            volgende = self.get_first_anker().volgende
        
        while volgende != None:                                 

             if isinstance(volgende,DubbeleGelinktelijst.Knoop):
                index +=1
             
             vorige = volgende
             volgende = volgende.volgende

        return index
    
    def get_first_anker(self):
       return self.eerste

    def get_last_anker(self):
       return self.laatste

mylist = DubbeleGelinktelijst()
print(mylist.__sizeof__())


    
