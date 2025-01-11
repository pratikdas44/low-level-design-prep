from abc import ABC, abstractmethod

class CacheObserver:
    def notify(self, action: str, key: str, value: str = None):
        """
        Notify the observer of a change in the cache.
        
        :param action: The action that triggered the notification (e.g., 'put', 'delete')
        :param key: The key that was affected
        :param value: The value associated with the key (if applicable)
        """
        raise NotImplementedError("Subclasses should implement this method.")


class CacheLogger(CacheObserver):
    def notify(self, action: str, key: str, value: str = None):
        if action == "put":
            print(f"Cache put: Key = {key}, Value = {value}")
        elif action == "delete":
            print(f"Cache delete: Key = {key}")

