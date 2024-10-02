

#def __init__(self):
#        self.listamusica = []

#def listamusica(self, cancion):
#    self.listamusica.append(cancion)
#    print(f"dentro del metodo la lista va asi {self.listamusica}")
        
#    return self.listamusica

#def listamusica(cancion,lis=None):
#    if lis is None:
#        lis=[]
#        auxlis=lis.append(cancion)
#    else:
#        auxlis=lis.append(cancion)
#        print(f"dentro del metodo la lista va asi {auxlis}")
        
#    return auxlis

def listamusica(cancion,listamusica=None):
    if listamusica is None:
        listamusica = []
    listamusica.append(cancion)
    print (f"dentro del metodo la lista va asi {listamusica}")
    return listamusica



