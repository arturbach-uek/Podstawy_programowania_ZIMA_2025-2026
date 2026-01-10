import queue

def convert_to_binary(number): 
    binary = queue.LifoQueue()
    while number != 0:
        reminder = number % 2
        binary.put(reminder)
        number = number // 2
    binary_string = ""
    while not binary.empty():
        binary_string += str(binary.get())

    return binary_string

print(convert_to_binary(18))