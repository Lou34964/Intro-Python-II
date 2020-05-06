from print_wrapper import print_wrapper


class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_take(self):
    print_wrapper(f"You have picked up {self.name}")

  def on_drop(self):
    print_wrapper(f"You have dropped the {self.name}")