class PersistenceException(Exception):
    """
    Excepción personalizada para errores de persistencia.
    """
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
