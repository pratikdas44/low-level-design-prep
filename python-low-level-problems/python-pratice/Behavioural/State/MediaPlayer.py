from abc import ABC, abstractmethod
class MediaPlayerState(ABC):
    @abstractmethod
    def handle_request(self):
        pass

class Play(MediaPlayerState):
    def handle_request(self):
        print("Playing video")

class Pause(MediaPlayerState):
    def handle_request(self):
        print("Pausing video")

class Stop(MediaPlayerState):
    def handle_request(self):
        print("stopping video")

class MediaContext:
    def __init__(self):
        self._state = None

    def set_state(self, state):
        self._state = state
    
    def request(self):
        if self._state is None:
            raise ValueError("State not set")
        self._state.handle_request()

vending_machine = MediaContext()

# Set initial state
vending_machine.set_state(Play())

# Request state change
vending_machine.request()

# Change state
vending_machine.set_state(Pause())
vending_machine.request()

# Change state
vending_machine.set_state(Stop())
vending_machine.request()
