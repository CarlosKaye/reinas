Tabla =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

PosActual=[]
Segc = 0
PosC = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def reinas(NCReinas, Tabla, Segc,PosC):
    MatCe = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    cont = 0
    print("reinas que faltan "+str(NCReinas))
    
    if NCReinas == 1:
        return solucion(Tabla)
    else: 
        for t in range(len(Tabla)):
            for r in range(len(Tabla[t])):
        
                if cont == 0:
                    if PosC[t][r] != 3:
                        if(Tabla[t][r] == 0):
                           
                            if NCReinas == 4:
                                PosC[t][r] = 3
                            Tabla[t][r] = 1
                            cont = cont + 1
                            
                            PosActual.append([t,r])
        
        Tabla = vertHorz(Tabla,PosActual)
       
        PosActual.pop(0)
        for t in Tabla:

            if 0 in t:
               
                Segc = 0
            else:
               
                Segc = 1
        if Segc == 1:
            NCReinas=4
            Segc=0
            print("Matriz llena")
            return reinas(NCReinas,MatCe,Segc,PosC)
        if Segc == 0:
            NCReinas=NCReinas-1
            return reinas(NCReinas,Tabla,Segc,PosC)

def vertHorz(Tabla,PosActual):
    print("-----------------------------------------------------------")
    a = PosActual[0][0]
    b = PosActual[0][1]
    r = range(len(Tabla))
    bb = b
    aa = a
    print(PosActual)
    
    for t in range(len(Tabla)):
        for r in range(len(Tabla[t])):
            Tabla[a][r] = 2
            Tabla[t][b] = 2
    imp(Tabla)
    for t in range(len(Tabla)):
        bb = bb-1
        aa = aa -1
        if (bb >= 0)and(aa >=0):
            Tabla[aa][bb] = 2
    bb = b
    aa = a
    
    imp(Tabla)
    for t in range(len(Tabla)):
        aa = aa +1
        bb = bb +1
        if (aa <= r)and(bb <= r):
            Tabla[aa][bb] = 2

    bb = b
    aa = a
    
    imp(Tabla)
    for t in range(len(Tabla)):
        bb = bb+1
        aa = aa -1
        if (bb < r)and(aa >=0):
            Tabla[aa][bb] = 2
    bb = b
    aa = a
    
    imp(Tabla)
    for t in range(len(Tabla)):
        bb = bb-1
        aa = aa + 1
        if (bb >= 0)and(aa <r):
            Tabla[aa][bb] = 2
    Tabla[a][b]=1
    
    imp(Tabla)
    print("------------------------------------------")
    return Tabla
    

def solucion(Tabla):
    for t in range(len(Tabla)):
        for r in range(len(Tabla[t])):
            if (Tabla[t][r]) == 0:
                Tabla[t][r] = 1
    print("     Respuesta  ")
    for t in Tabla:
        print(t)

def imp(Tabla):
    print("--------------------")
    for t in Tabla:
        print(t)

reinas(4,Tabla,0,PosC)

