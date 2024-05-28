# Faulty code
def process_data0(data):
    for item in data:
        if type(item) == dict and 'value' in item:
            if item['value'] > 0:
                print("Processing:", item['value'])
            else:
                print("Negative value:", item['value'])
        else:
            print("Invalid item:", item)

# After refactoring and applying defensive coding
def process_data(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list")
    
    for item in data:
        if not isinstance(item, dict) or 'value' not in item:
            print("Invalid item:", item)
            continue
        
        value = item['value']
        if value > 0:
            print("Processing:", value)
        else:
            print("Negative value:", value)