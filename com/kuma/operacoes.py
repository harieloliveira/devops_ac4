class operacoes:
    def soma(self, valores):
        val = 0
        for v in valores:
            val += v
        return val

    def subtracao(self, valores):
        val=0
        for v in valores:
            val -= v
        return val
    
    def petenciacao(self, valores):
        val=0
        for v in valores:
            val *= v
        return val
    
    def total_letras(self,palavra):
        return len(palavra)
        
        