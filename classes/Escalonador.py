from classes import Processo as proc

# Responsável pelo escalonamento (execução, suspensão e término) de processos.
class Escalonador(object):
    def __init__(self, totalQuantums):
        self.tAtual = 0
        self.pAtual = None
        self.totalQuantums = totalQuantums
        self.TR = 0
        self.U1 = 1
        self.U2 = 2
        self.U3 = 3
        self.filas = [[], [], [], []]

    #Responsável por escalonar um processo. Emprega "round robin" (fila de TR) e "feedback" (filas de prioridade de usuário) para isso.
    def escalona(self, p, tAtual):
        self.tAtual = tAtual
        if (p.pegaEstado() == p.EXECUTANDO):
            # Atualiza o tempo de execução do processo:
            p.incrementaTempoDeExecucao(1)
            if ((p.pegaTempoTotalExecutando() - 1) == p.pegaTempoDeServico()): p.setaEstado(p.TERMINADO)
            #Para processos de usuário (prioridades 1-3):
            else:
                #Filas de prioridade de usuário. Seguem a política de escalonanamento "feedback", usando quantum = 2.
                if (p.pegaPrioridade() > 0):
                    if (p.pegaQuantums() < self.totalQuantums): p.incrementaQuantums(1)
                    else:
                        p.setaQuantums(0)
                        # Define-em em qual fila o processo atual será inserido:
                        for i in range(len(self.filas[:])):
                            if p in self.filas[i]: self.filas[i].remove(p)
                        novaPrioridade = (p.pegaPrioridade() % 3) + 1  # Calcula qual será a fila em que o processo será inserido com
                        # base na fila em que ele se encontra atualmente
                        p.setaPrioridade(novaPrioridade)
                        self.filas[p.pegaPrioridade()].append(p)  # Adiciona na próxima fila (política de feedback).
        if (p.pegaEstado() == p.TERMINADO): self.pAtual = None
        else: self.pAtual = p
        return p

    #Seleciona um determinado processo de uma das filas de prioridade conforme o parâmetro passado como índice para a função:
    def pegaProcesso(self, fila, indice):
        if fila == 0: return self.filas[self.TR][indice]
        elif fila == 1: return self.filas[self.U1][indice]
        elif fila == 1: return self.filas[self.U2][indice]
        else: return self.filas[self.U3][indice]

    def atualizaFilas(self, fTReal, fUs1, fUs2, fUs3):
        for pr in fTReal:
            for fila in self.filas:
                if (pr in fila): break
            if pr not in self.filas[self.TR]: self.filas[self.TR].append(pr)
        for pr in fUs1:
            for fila in self.filas:
                if (pr in fila): break
            if pr not in self.filas[self.U1]: self.filas[self.U1].append(pr)
        for pr in fUs2:
            for fila in self.filas:
                if (pr in fila): break
            if pr not in self.filas[self.U2]: self.filas[self.U2].append(pr)
        for pr in fUs3:
            for fila in self.filas:
                if (pr in fila): break
            if pr not in self.filas[self.U3]: self.filas[self.U3].append(pr)

    def imprimeFila(self, fila, i):
        txt = "Fila "+str(i)+": ["
        for pr in fila:
            txt += str(pr.pegaId()) + ", "
        print(txt + "]\n")
