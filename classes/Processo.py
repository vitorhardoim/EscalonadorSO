import random

class Processo(object):
    def __init__(self, arrivalTime, priority, processorTime, memoriaRam, impressoras, scanners, modems,
                 CDs, tInicio, tTotalProcesso, tTotalSuspenso, estado):
        self.__arrivalTime = arrivalTime
        self.__priority = priority
        self.__processorTime = processorTime
        self.__memoriaRam = memoriaRam
        self.__listaPerifericos = [impressoras, scanners, modems, CDs]
        self.__tInicio = tInicio
        self.__tTotalProcesso = tTotalProcesso
        self.__tTotalSuspenso = tTotalSuspenso
        self.__tTotalBloqueado = 0
        self.__tTotalExecutandoProcesso = 0
        self.__estado = estado
        self.__id = ""
        self._quantumsFeitos = 0

        # Constantes de estado do processo.
        self.NOVO = 0
        self.PRONTO = 1
        self.EXECUTANDO = 2
        self.BLOQUEADO = 3
        self.SUSPENSO = 4
        self.TERMINADO = 5

        self.__esFoiAlocada = False
        self.__ramFoiAlocada = False

    #Função de comparação usada pela classe. Usada no método "list.remove(obj)" para identificar um objeto.
    def __cmp__(self, other):
        return self.__eq__(other)

    #Método de comparação de equivalência da classe. Compara apenas o "id" (que único) do objeto.
    def __eq__(self, other):
        #Checa se "other" é instância de Processo.
        if isinstance(other, self.__class__): return self.__id == other.pegaId()
        return False

    # modelo do print de processo
    def __str__(self):
        return "Id: " + str(self.pegaId()) + "\nEstado atual: " + self.stringEstado() + "\nCiclos do processo executados: " \
               + str(self.__tTotalExecutandoProcesso) + " / " + str(self.__processorTime) + \
               "\nMemória consumida (MB): " + str(self.pegaMemoriaOcupada()) #;+ "\n" + \
        #comentado so pra enxergar na hora de executar, senao fica confuso de ver
        # '''
        #        "Tempo de chegada: " + str(self.__arrivalTime) + "\n" + \
        #        "Prioridade: " + str(self.__priority) + "\n" + \
        #        "Tempo de serviço: " + str(self.__processorTime) + "\n" + \
        #        "Memória consumida (MBytes): " + str(self.pegaMemoriaOcupada()) + "\n" + \
        #        "Impressoras usadas: " + str(self.listaPerifericos[0]) + "\n" + \
        #        "Scanners usados: " + str(self.listaPerifericos[1]) + "\n" + \
        #        "Modems usados: " + str(self.listaPerifericos[2]) + "\n" + \
        #        "Drivers de CD usados: " + str(self.listaPerifericos[3]) + "\n" + \
        #        "Tempo de início: " + str(self.__tInicio) + "\n" + \
        #        "Tempo total do processo: " + str(self.__tTotalProcesso) + "\n" + \
        #        "Tempo total suspenso: " + str(self.__tTotalSuspenso) + "\n" + \
        #        "Estado atual: " + self.printEstado()
        # '''

    #Mostra uma 'string' indicando o estado do processo em vez de printar 0,1,2,3
    def stringEstado(self):
        if (self.__estado == 0):
            return "novo\n"
        elif (self.__estado == 1):
            return "pronto\n"
        elif (self.__estado == 2):
            return "executando\n"
        elif (self.__estado == 3):
            return "bloqueado\n"
        elif (self.__estado == 4):
            return "suspenso\n"
        else:
            return "terminado\n"

    #Diversas funções "get"/"set":
    def pegaEstado(self):
        return self.__estado

    def setaEstado(self, estado):
        self.__estado = estado
        #suspenso ou bloqueado?
        # if (estado == 0):
        #     print("Processo não está pronto\n")
        # elif (estado == 1):
        #     print("Processo está pronto\n")

    def pegaPrioridade(self):
        return self.__priority

    def setaPrioridade(self, p):
        self.__priority = p

    def pegaTempoChegada(self):
        return self.__arrivalTime

    def pegaMemoriaOcupada(self):
        return self.__memoriaRam

    def setaTempoInicio(self, tInicio):
        self.__tInicio = tInicio

    def pegaTempoInicio(self):
        return self.__tInicio

    def setaTempoFim(self, tFim):
        self.__tFim = tFim

    def pegaTempoFim(self):
        return self.__tFim

    def atualizaTempoTotalDeDuracao(self):
        self.__tTotalProcesso = self.__tFim - self.__tInicio

    def pegaNumDePerifericos(self):
        return self.__listaPerifericos

    def setaId(self, novoId):
        self.__id = novoId

    def pegaId(self):
        return self.__id

    def ramFoiAlocada(self):
        return self.__ramFoiAlocada

    def esFoiAlocada(self):
        return self.__esFoiAlocada

    def setaEstadoAlocacaoRam(self, estado):
        self.__ramFoiAlocada = estado

    def setaEstadoAlocacaoES(self, estado):
        self.__esFoiAlocada = estado

    def pegaTempoTotal(self):
        return self.__tTotalProcesso

    def pegaTempoTotalExecutando(self):
        return self.__tTotalExecutandoProcesso

    def incrementaTempoDeExecucao(self, inc):
        self.__tTotalExecutandoProcesso += inc

    def incrementaTempoTotal(self, inc):
        self.__tTotalProcesso += inc

    def pegaQuantums(self):
        return self._quantumsFeitos

    def setaQuantums(self, valor):
        self._quantumsFeitos = valor

    def incrementaQuantums(self, inc):
        self._quantumsFeitos += inc

    def pegaTempoDeServico(self):
        return self.__processorTime

    def pegaTempoSuspenso(self):
        return self.__tTotalSuspenso

    def pegaTempoBloqueado(self):
        return self.__tTotalBloqueado

    def incrementaTempoSuspenso(self, inc):
        self.__tTotalSuspenso += inc

    def incrementaTempoBloqueado(self, inc):
        self.__tTotalBloqueado += inc