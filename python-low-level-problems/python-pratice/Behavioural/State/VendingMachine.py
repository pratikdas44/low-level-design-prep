from abc import ABC, abstractmethod

# State interface
class VendingMachineState(ABC):
    @abstractmethod
    def handle_request(self) -> None:
        pass

# Concrete states
class ReadyState(VendingMachineState):
    def handle_request(self) -> None:
        print("Ready state: Please select a product.")

class ProductSelectedState(VendingMachineState):
    def handle_request(self) -> None:
        print("Product selected state: Processing payment.")

class PaymentPendingState(VendingMachineState):
    def handle_request(self) -> None:
        print("Payment pending state: Dispensing product.")

class OutOfStockState(VendingMachineState):
    def handle_request(self) -> None:
        print("Out of stock state: Product unavailable. Please select another product.")

# Context
class VendingMachineContext:
    def __init__(self) -> None:
        self._state: VendingMachineState | None = None
    
    def set_state(self, state: VendingMachineState) -> None:
        self._state = state
    
    def request(self) -> None:
        if self._state is None:
            raise ValueError("State not set")
        self._state.handle_request()

# Client code
def main():
    # Create context
    vending_machine = VendingMachineContext()
    
    # Set initial state
    vending_machine.set_state(ReadyState())
    
    # Request state change
    vending_machine.request()
    
    # Change state
    vending_machine.set_state(ProductSelectedState())
    vending_machine.request()
    
    # Change state
    vending_machine.set_state(PaymentPendingState())
    vending_machine.request()
    
    # Change state
    vending_machine.set_state(OutOfStockState())
    vending_machine.request()

if __name__ == "__main__":
    main()