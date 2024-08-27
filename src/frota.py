class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __motor_on : False
    __tanque : float
    consumo : float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque:
                       float, consumo : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.consumo = consumo

    def ligar(self):
        if not self.__motor_on:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:
            if ((velocidade * tempo) / self.consumo) <= self.__tanque:
                self.__odometro += velocidade * tempo
                self.__tanque -= (velocidade * tempo) / self.consumo
            else:
                raise Exception("Erro: Não tem gasolina suficiente para essa distância.")

        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")
        
    def get_tanque(self):
        return self.__tanque    

    def get_odometro(self):
        return self.__odometro
    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}, '
                f'__tanque {self.__tanque}, consumo {self.consumo}')
        return info

    def __repr__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}, '
                f'__tanque {self.__tanque},consumo {self.consumo}')



