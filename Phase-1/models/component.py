class Component:
    def __init__(self, id, name, owner, status="Available"):
        self.id = id
        self.name = name
        self.owner = owner
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "owner": self.owner,
            "status": self.status
        }