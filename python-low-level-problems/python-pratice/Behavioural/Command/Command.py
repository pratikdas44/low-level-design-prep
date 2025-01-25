from abc import ABC, abstractmethod

# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

# Device interface
class Device(ABC):
    @abstractmethod
    def turn_on(self) -> None:
        pass
    
    @abstractmethod
    def turn_off(self) -> None:
        pass

# Concrete device
class TV(Device):
    def turn_on(self) -> None:
        print("TV turned On")
    
    def turn_off(self) -> None:
        print("TV turned Off")

# Concrete commands
class TurnOnCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device
    
    def execute(self) -> None:
        self._device.turn_on()

class TurnOffCommand(Command):
    def __init__(self, device: Device) -> None:
        self._device = device
    
    def execute(self) -> None:
        self._device.turn_off()

# Invoker
class RemoteControl:
    
    def set_command(self, command: Command) -> None:
        self._command = command
    
    def press_button(self) -> None:
        if self._command is None:
            raise ValueError("No command set")
        self._command.execute()

# Client code
def main():
    # Create receiver
    tv = TV()
    
    # Create commands
    turn_on_command = TurnOnCommand(tv)
    turn_off_command = TurnOffCommand(tv)
    
    # Create invoker
    remote_control = RemoteControl()
    
    # Execute commands
    remote_control.set_command(turn_on_command)
    remote_control.press_button()  # Outputs: TV turned On
    
    remote_control.set_command(turn_off_command)
    remote_control.press_button()  # Outputs: TV turned Off

if __name__ == "__main__":
    main()