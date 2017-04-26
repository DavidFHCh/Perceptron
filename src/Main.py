from perceptron import Perceptron

tabla_entradas = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]

tabla_salidas_or = [0,1,1,1,1,1,1,1]
tabla_salidas_and = [0,0,0,0,0,0,0,1]

f = lamda x : 1 if x > 0 else 0

if __name__ == '__main__':


    #conjuntos de entrenamiento

    #conjunto1
    entradas1 = [tabla_entradas[0],tabla_entradas[7]]
    salidas1 = [0,1]

    #conjunto2
    entradas2 = tabla_entradas
    salidas2_or = tabla_salidas_or
    salidas2_and = tabla_salidas_and

    #conjunto3
    entradas3 = [tabla_entradas[1],tabla_entradas[3],tabla_entradas[5],tabla_entradas[7]]
    salidas3_or = [1,1,1,1]
    salidas3_and = [0,0,0,1]

    #conjunto4
    entradas4 = [tabla_entradas[0],tabla_entradas[2],tabla_entradas[4]]
    salidas4_or = [0,1,1]
    salidas4_and = [0,0,0]

    #conjunto5
    entradas5 = [tabla_entradas[0],tabla_entradas[3],tabla_entradas[4],tabla_entradas[6],tabla_entradas[7]]
    salidas5_or = [0,1,1,1,1]
    salidas5_and = [0,0,0,0,1]

    #fin de conjuntos de entrenamiento

    #Conjuntos para probar perceptrones

    c_prueba_entrada = [tabla_entradas[0],tabla_entradas[5],tabla_entradas[2],tabla_entradas[7]]
    c_prueba_salida_or = [0,1,1,1]
    c_prueba_salida_and = [0,0,0,1]

    #Fin de Conjuntos para probar perceptrones


    #Perceptrones OR

    #Perceptron1
    print ("*********Primer Perceptron OR")
    p1_or = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas1)
    print ("Se empieza el entrenamiento...")
    p1_or.entrenamiento (entradas1,salidas1)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p1_or.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])



    #Perceptron2
    print ("*********Segundo Perceptron OR")
    p2_or = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas2)
    print ("Se empieza el entrenamiento...")
    p2_or.entrenamiento (entradas2,salidas2_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p2_or.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])



    #Perceptron3
    print ("*********Tercer Perceptron OR")
    p3_or = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas3)
    print ("Se empieza el entrenamiento...")
    p3_or.entrenamiento (entradas3,salidas3_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p3_or.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])



    #Perceptron4
    print ("*********Cuarto Perceptron OR")
    p4_or = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas4)
    print ("Se empieza el entrenamiento...")
    p4_or.entrenamiento (entradas4,salidas4_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p4_or.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])



    #Perceptron5
    print ("*********Quinto Perceptron OR")
    p5_or = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas5)
    print ("Se empieza el entrenamiento...")
    p5_or.entrenamiento (entradas5,salidas5_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p5_or.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])

    #Fin de perceptrones OR


    #Perceptrones AND

    #Perceptron1
    print ("*********Primer Perceptron AND")
    p1_and = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas1)
    print ("Se empieza el entrenamiento...")
    p1_and.entrenamiento (entradas1,salidas1)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p1_and.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_or[i])



    #Perceptron2
    print ("*********Segundo Perceptron AND")
    p2_and = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_or.alpha)
    print ("Conjunto de entrenamiento: \t",entradas2)
    print ("Se empieza el entrenamiento...")
    p2_and.entrenamiento (entradas2,salidas2_and)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p2_and.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_and[i])



    #Perceptron3
    print ("*********Tercer Perceptron AND")
    p3_and = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_and.alpha)
    print ("Conjunto de entrenamiento: \t",entradas3)
    print ("Se empieza el entrenamiento...")
    p3_and.entrenamiento (entradas3,salidas3_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p3_and.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_and[i])



    #Perceptron4
    print ("*********Cuarto Perceptron AND")
    p4_and = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_and.alpha)
    print ("Conjunto de entrenamiento: \t",entradas4)
    print ("Se empieza el entrenamiento...")
    p4_and.entrenamiento (entradas4,salidas4_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p4_and.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_and[i])



    #Perceptron5
    print ("*********Quinto Perceptron AND")
    p5_and = Perceptron (2,f,0.2)
    print ("taza de aprendizaje: \t", p1_and.alpha)
    print ("Conjunto de entrenamiento: \t",entradas5)
    print ("Se empieza el entrenamiento...")
    p5_and.entrenamiento (entradas5,salidas5_or)
    print ("Entrenamiento terminado.")
    #Probando
    for i in range(4):
        salida = p5_and.salida(c_prueba_entrada[i])
        print("Entrada: \t",c_prueba_entrada[i],"Salida: \t",salida,"Salida esperada: \t",c_prueba_salida_and[i])

    #Fin de perceptrones AND
