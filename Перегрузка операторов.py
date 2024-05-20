class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __str__(self):
        return f'{self.buildingType} got {self.numberOfFloors} floors'

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(60, 'Небоскреб')
building2 = Building(10, 'Офис')


if building1 == building2:
    print('Здания одинаковы')
else:
    print('Здания разные')

print(str(building1))
print(str(building2))