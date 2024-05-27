from .orders import process_delivered_order, process_new_order, process_shipped_order

def process_order0(order):
    if order['status'] == 'new':
        process_new_order(order)
    elif order['status'] == 'shipped':
        process_shipped_order(order)
    elif order['status'] == 'delivered':
        process_delivered_order(order)


# 
# if conditions
# no undesired condition check [order can be null, order->status, order->'status'->'pending']


# Refactored Code
def process_order(order):

    if not order and order.get("status"):
        raise "Invalid order"
    
    status_handlers = {
        'new': process_new_order,
        'shipped': process_shipped_order,
        'delivered': process_delivered_order,
        # 'pending': process_pending_order
    }
    handler = status_handlers.get(order['status'])

    if not handler:
        raise "Invalid order status"

    if handler:
        handler(order)

# Early returns

# Common refactoring areas
# - Avoid usage of print statements and add proper loggers wherever required
# - Conditional statements reduction to improve redability
# - Common logic to get current user
# - Consistent response builder across all the APIs [Do not reinvent the wheel]
# - Move business logic from controller to service files
# - Reduce duplicate query on database (user, user)
# - Ensure transactions on database are atomic
# - Permission Classes on class level instead on every methods in the class
# - Decorator to check if User has company assigned
# - Decorator to check if user has permission to access the company
# - Decorator to check if user has permission to access the table
# https://github.com/RamailoTech/nl2query-be/pull/29
        

# Points to consider while refactoring
# - Proper test cases

# Example
        
# Get Table Description
    # - Table doesn't exist	Expected - 400, Actual - 400 {}
    # - No permission to access the table	Expected - 400, Actual - 400 
    # - Success	200