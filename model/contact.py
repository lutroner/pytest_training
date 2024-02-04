from sys import maxsize


class Contact:
    def __init__(self, name=None, surname=None, phone=None, email=None,
                 company=None, address=None, id=None):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.company = company
        self.address = address
        self.id = id

    def __repr__(self):
        return f"{self.id}:{self.name}:{self.surname}"

    def __eq__(self, other):
        return (self.id == other.id and self.name == other.name, self.surname
                == other.surname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        return maxsize
