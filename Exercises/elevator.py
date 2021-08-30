class Elevador:
    """Um elevador pro InfinityElevator8000.

    Atributos:
        andar: em qual andar ele está.
        direção: se está parado, subindo ou descendo.
        funcionando: True a menos que esteja quebrado.
        chamados: lista de andares por visitar.

    Métodos:
        chamar(andar): adiciona o andar na lista de chamados.
        display(): exibe uma string com o status do elevador.
    """
    def __init__(self, andar, direcao="parado", quebrado=False):
        """Inicializa um elevador com andar,
        direção e condição caso esteja quebrado."""
        self.andar = andar
        self.direcao = direcao
        self.funcionando = not quebrado
        self.chamados = []
        pass

    def quebra(self): 
        """Marca o elevador como fora de operação"""
        self.funcionando = False

    def display(self):
        """Exibe o status do elevador."""
        if not self.funcionando:
            return f"Fora de Operação"
        return f"Estamos no andar {self.andar} e estamos {self.direcao}"

    def chama(self, andar):
        """Recebe um chamado."""
        self.chamados.append(andar)
        self.chamados.sort()

    def atualiza_chamados(self):
        if self.andar in self.chamados:
            self.chamados = [
                chamado for chamado in self.chamados
                if chamado != self.andar]

    def sobe(self):
        self.direcao = 'subindo'
        proximos = [
            chamado for chamado in self.chamados
            if chamado > self.andar]
        if proximos:
            self.andar += 1
            self.atualiza_chamados()
            return True
    
    def desce(self):
        self.direcao = 'descendo'
        proximos = [
            chamado for chamado in self.chamados
            if chamado < self.andar]
        if proximos:
            self.andar -= 1
            self.atualiza_chamados()
            return True

    def tic(self):
        """Move o elevador se necessário"""
        if not self.chamados:
            self.direcao = "parado"
            return
        
        if self.direcao == 'subindo':
            self.sobe() or self.desce()
        else: # só pode estar descendo
            self.desce() or self.sobe()        
        

    
elevador_a = Elevador(0)
elevador_b = Elevador(0, quebrado=True)