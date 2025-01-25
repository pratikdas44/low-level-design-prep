from abc import ABC, abstractmethod
from typing import Dict, List, Optional, TypeVar, Generic
from Models import Movie, Show, Booking, Customer

T = TypeVar('T')

class BaseRepository(ABC, Generic[T]):
    def __init__(self):
        self._data: Dict[str, T] = {}

    def save(self, entity: T) -> T:
        self._data[entity.id] = entity
        return entity

    def get_by_id(self, id: str) -> Optional[T]:
        return self._data.get(id)

    def get_all(self) -> List[T]:
        return list(self._data.values())

    def delete(self, id: str) -> None:
        if id in self._data:
            del self._data[id]

class MovieRepository(BaseRepository[Movie]):
    pass

class ShowRepository(BaseRepository[Show]):
    pass

class BookingRepository(BaseRepository[Booking]):
    pass

class CustomerRepository(BaseRepository[Customer]):
    pass