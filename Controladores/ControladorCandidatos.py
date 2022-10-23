from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.ModeloCandidato import ModeloCandidato

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()

    def index(self):
        return self.repositorioCandidato.findAll()

    def create(self, infoCandidato):
        nuevoCandidato=ModeloCandidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)

    def show(self, id):
        elCandidato=ModeloCandidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoActual=ModeloCandidato(self.repositorioCandidato.findById(id))
        candidatoActual.cedula=infoCandidato["cedula"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioEstudiante.save(estudianteActual)
    def delete(self,id):
        return self.repositorioEstudiante.delete(id)