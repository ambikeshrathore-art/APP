import gc
import tracemalloc

def create_objects():
    data = []
    for i in range(100000):
        data.append([i] * 10)
    return data

def display_memory():
    current, peak = tracemalloc.get_traced_memory()
    print("Current Memory:", current)
    print("Peak Memory:", peak)

tracemalloc.start()

print("Initial Memory Usage:")
display_memory()

print("Creating Objects:")
objects = create_objects()
display_memory()

del objects

gc.set_debug(gc.DEBUG_STATS)

print("Garbage Collection:")
gc.collect()
display_memory()

gc.set_debug(0)

tracemalloc.stop()
