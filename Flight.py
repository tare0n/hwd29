class Flight:
    def __init__(self, city_from, city_to):
        self.city_from = city_from
        self.city_to = city_to

    def __str__(self):
        return f"Flight from {self.city_from} to {self.city_to}"


print(Flight(input("from:\n"), input("to:\n")))

