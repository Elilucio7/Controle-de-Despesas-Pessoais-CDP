import cad_recdes
class despesa(cad_recdes.cad_recdes):
    def __init__(self, nome = None, valor = None, categoria = None):
        cad_recdes.cad_recdes.cadastrar_recdes(self)
        super().__init__( 1, valor, None, categoria, None)
        self.nome = nome #será implementado para ser pego no banco de dados

