class Vehicle:

    def __init__(self, owner='', plate='', model='', brand='', year=0) -> None:
        self._owner: str= owner
        self._vehicle_plate: str= plate
        self._model_vehicle: str= model
        self._brand: str = brand
        self._year: int = year

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner: str):
        if owner is not None:
                self._owner = owner
        else:
            raise ValueError('Valor Deve ser Informado!!') from None

    @property
    def vehicle_plate(self):
        return self._vehicle_plate

    @vehicle_plate.setter
    def vehicle_plate(self, plate: str):
        if len(plate) == 7:
            self._vehicle_plate = plate
        else: 
            raise ValueError('Placa Inválida') from None

    @property
    def model(self):
        return self._model_vehicle

    @model.setter
    def model(self, model:str):
        if model is not None:
            self._model_vehicle = model
        else:
            raise ValueError('Modelo Inválido') from None

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year:int):
        if year is not None:
            self._year = year
        else:
            raise ValueError('Ano Inválido') from None 

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand: str):
        if brand is not None:
            self._brand = brand
        else:
            raise ValueError('Marca Inválido') from None
