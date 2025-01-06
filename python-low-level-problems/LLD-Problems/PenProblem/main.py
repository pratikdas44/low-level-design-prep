# main.py
from WriteStrategy.Context import Context
from WriteStrategy.PenStrategy import PenStrategy
from Factory.PenFactory import PenFactory
from Factory.PenType import PenType
def main():
    pen = PenFactory.create_pen(PenType.PEN)
    pen.write()

    # Create the Context object
    context = Context()

    # Set the strategy at runtime
    pen_strategy = PenStrategy()
    context.set_strategy(pen_strategy)

    # Execute the strategy
    context.execute()

if __name__ == "__main__":
    main()
