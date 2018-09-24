import re, random  # biblioteca p/ tratar das strings
from classes import Processo as proc

# from classes.Processo import *

class Despachante():
    def __init__(self, arqProcessos, totalRamSistema):
        self.__totalRAMSistema = totalRamSistema
        self.fEntrada = []
        self.fSubmetidos = []
        self.fTempoReal = []
        self.fUsuarioP1 = []
        self.fUsuarioP2 = []
        self.fUsuarioP3 = []

        self.trEnviados = 0
        self.usEnviados = 0
        #Abre o arquivo e cria a lista de entrada que é igual ao arquivo
        self.file = open(arqProcessos, 'r')
        self.leArq()

    #Lê o arquivo texto passado como parâmetro na inicialização da instância da classe Despachante, criando uma lista
    #de processos a partir do mesmo:
    def leArq(self):
        # copia o arquivo p/ a lista
        for line in self.file:
            # separa a string recebida do arquivo para envia-la p/ lista
            separador = re.compile("^\s+|\s*,\s*|\s+$")
            processoAtual = [x for x in separador.split(line) if x]
            novo = proc.Processo(int(processoAtual[0]), int(processoAtual[1]), int(processoAtual[2]), int(processoAtual[3]),
                           int(processoAtual[4]), int(processoAtual[5]), int(processoAtual[6]), int(processoAtual[7]),
                            0, 0, 0, 0)
            if (self.verificaProcesso(novo)): self.fEntrada.append(novo)

        self.fEntrada.sort(key=lambda x: x.pegaTempoChegada())
        self.criaID(self.fEntrada)

    #Verifica se um determinado processo pode ser executado tendo em vista as limitações de hardware da máquina/sistema em questão:
    def verificaProcesso(self, processo):
        if ((processo.pegaMemoriaOcupada() > self.__totalRAMSistema) or (processo.pegaNumDePerifericos()[0] > 2) or (processo.pegaNumDePerifericos()[1] > 1) or
            (processo.pegaNumDePerifericos()[2] > 1) or (processo.pegaNumDePerifericos()[3] > 2) or (processo.pegaMemoriaOcupada() < 0) or
            (processo.pegaNumDePerifericos()[0] < 0) or (processo.pegaNumDePerifericos()[1] < 0) or (processo.pegaNumDePerifericos()[2] < 0)
            or (processo.pegaNumDePerifericos()[3] < 0)):
            return False
        return True

    #Cria um identificador único para cada processo na lista de entrada:
    def criaID(self, fEntrada):
        for i in range(len(fEntrada)):
            if fEntrada[i].pegaPrioridade() == 0:
                self.trEnviados += 1
                fEntrada[i].setaId("TR-" + str(self.trEnviados))
            else:
                self.usEnviados += 1
                fEntrada[i].setaId("U-" + str(self.usEnviados))

    #Organiza as filas/listas de prioridade de processo com base numa lista de entrada contendo todos os processos a serem executados:
    def submeteProcessos(self, tAtual):
        self.fTempoReal = []
        self.fUsuarioP1 = []
        self.fUsuarioP2 = []
        self.fUsuarioP3 = []
        for pr in self.fEntrada[:]:
            if (self.processoDeveSerEnviado(pr, tAtual)):
                self.fEntrada.remove(pr)
                self.fSubmetidos.append(pr)
                if (pr.pegaPrioridade() == 0): self.fTempoReal.append(pr)
                elif (pr.pegaPrioridade() == 1): self.fUsuarioP1.append(pr)
                elif (pr.pegaPrioridade() == 2): self.fUsuarioP2.append(pr)
                else: self.fUsuarioP3.append(pr)
        return self.fTempoReal, self.fUsuarioP1, self.fUsuarioP2, self.fUsuarioP3

    def processoDeveSerEnviado(self, pr, tAtual): return pr.pegaTempoChegada() <= tAtual

    #"Funções "get" para as filas de prioridade:
    def pegafTempoReal(self):
        return self.fTempoReal

    def pegafUsuarioP1(self):
        return self.fUsuarioP1

    def pegafUsuarioP2(self):
        return self.fUsuarioP2

    def pegafUsuarioP3(self):
        return self.fUsuarioP3

    def imprimeFila(self, fila, i):
        txt = "Fila "+str(i)+": ["
        for pr in fila:
            txt += str(pr.pegaId()) + ", "
        print(txt + "]\n")
