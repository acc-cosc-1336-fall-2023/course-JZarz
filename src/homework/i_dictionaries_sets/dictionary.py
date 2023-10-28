def add_inventory(widget_name,quantity, inventory):
    inventory[widget_name] = quantity
    if widget_name in inventory:
        inventory[widget_name] = quantity

def remove_inventory(widget_name, inventory):
    if widget_name in inventory:
        del inventory[widget_name]