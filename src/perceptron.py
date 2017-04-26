import random

class Perceptron (Object):

    def __init__ (self, numero_entradas,func_activacion,tasa_aprendizaje = 0.1):
        """
        Inicializando el Perceptron.
        :param numero_entradas: numero de entradas que tendra el Perceptron
        :param func_activacion: funcion de activacion
        :param tasa_aprendizaje: tasa de aprendizaje
        """
        self.n = numero_entradas
        self.pesos = []
        for i in range(self.n);
            self.pesos = self.pesos + [random.uniform(-0.5,0.5)]
        self.fun = func_activacion
        self.theta = random.uniform(-0.5,0.5)
        self.alpha =  tasa_aprendizaje
        if not (0 < tasa_aprendizaje < 1):
            self.alpha = 0.1

    def output_perceptron (self,inputs):
        """
        :param inputs: los valores de entrada para el entrenamiento o pruebas.
        """

        l = zip(self.pesos,inputs)
        suma = sum ((wi*ei) for (wi,ei) in l)

        return self.fun (sum - self.theta)

    def entrenamiento_aux (self, inputs, output):
        """
        Funcion auxiliar de entrenamiento(), en esta funcion se actuliazaran
        los pesos del perceptron, para que el entrenamiento tenga el efecto
        deseado.
        """
        output1 = self.output_perceptron (inputs)

        error = output - output1

        if error != 0:
            self.theta = self.theta - (self.alpha * error)
            l = zip (self.pesos, inputs)
            pesos = []
            for (wi, ei) in l:
                pesos = pesos + [wi + (self.alpha * ei * error)]
            self.pesos = pesos
        print ("Valor funcion de error: \t",error)
        return error

    def entrenamiento (self, conjunto_entr, salidas_esperadas):
        """
        Se iterara 100 veces sobre el conjunto de entrenamiento como
        maximo, se espera que sea suficiente para entrenar los perceptrones.
        El error tendra que ser menor o igual a 0 para que se considere
        bueno el entrenamiento.
        :param conjunto_entr: el conjunto de entrenamiento
        :param salidas_esperadas: el conjunto de salidas esperadas del conjunto de entrenamiento.
        """

        total = len (conjunto_entr)

        errores = []

        for j in range (100):
            for i in range (total):
                errores = errores + [self.entrenamiento_aux (conjunto_entr[i],salidas_esperadas[i])]
            suma =  sum (errores)/total
            if (suma <= 0):
                return
