class User:
    """
    Classe représentant un employé de la ville de Boston.
    Sert d’exemple de structure de données pour le modèle ETL.
    """
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def __repr__(self):
        return f"User({self.name}, {self.department}, {self.salary})"
