from abc import ABC, abstractmethod

# Abstract base class for Logger
class Logger(ABC):
    # Class-level constants
    OUTPUT_INFO = 1
    ERROR_INFO = 2
    DEBUG_INFO = 3
    
    def __init__(self, levels: int) -> None:
        self._next_logger: Logger | None = None
        self._levels = levels
    
    def next_logger(self, logger: 'Logger') -> None:
        self._next_logger = logger
    
    @abstractmethod
    def display_log_info(self, msg: str) -> None:
        pass
    
    def log_message(self, levels: int, msg: str) -> None:
        if self._levels <= levels:
            self.display_log_info(msg)
        
        if self._next_logger is not None:
            self._next_logger.log_message(levels, msg)

# Concrete logger classes
class ConsoleLogger(Logger):
    def __init__(self, levels: int) -> None:
        super().__init__(levels)
    
    def display_log_info(self, msg: str) -> None:
        print(f"CONSOLE LOGGER INFO: {msg}")

class ErrorLogger(Logger):
    def __init__(self, levels: int) -> None:
        super().__init__(levels)
    
    def display_log_info(self, msg: str) -> None:
        print(f"ERROR LOGGER INFO: {msg}")

class DebugLogger(Logger):
    def __init__(self, levels: int) -> None:
        super().__init__(levels)
    
    def display_log_info(self, msg: str) -> None:
        print(f"DEBUG LOGGER INFO: {msg}")

# Helper function to set up the chain
def do_chaining() -> Logger:
    console_logger = ConsoleLogger(Logger.OUTPUT_INFO)
    
    error_logger = ErrorLogger(Logger.ERROR_INFO)
    console_logger.next_logger(error_logger)
    
    debug_logger = DebugLogger(Logger.DEBUG_INFO)
    error_logger.next_logger(debug_logger)
    
    return console_logger

def main():
    chain_logger = do_chaining()
    
    chain_logger.log_message(Logger.OUTPUT_INFO, "Enter the sequence of values")
    chain_logger.log_message(Logger.ERROR_INFO, "An error is occurred now")
    chain_logger.log_message(Logger.DEBUG_INFO, "This was the error now debugging is completed")

if __name__ == "__main__":
    main()