import enum

class HomesiteStatus(enum.Enum):
    LOT = 'Lot'
    PRESALE = 'Available for presale'
    COMING_SOON = 'Coming Soon'
    UNDER_CONSTRUCTION = 'Under Construction'
    MOVE_IN_READY = 'Move-in Ready'

    @classmethod
    def values(cls):
        return tuple((key.value, key.name) for key in cls)

class HomesiteSaleStatus(enum.Enum):
    AVAILABLE = 'Available'
    CONTRACT = 'Under Contract'
    RESERVED = 'Reserved'
    SOLD = 'Sold'

    @classmethod
    def values(cls):
        return tuple((key.value, key.name) for key in cls)
