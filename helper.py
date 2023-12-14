def read_file_lines(file_name, strip_lines=False):
    with open(file_name, 'r') as f:
        lines =  []
        for line in f:
            lines.append(line)

    if strip_lines:
        lines = [line.strip() for line in lines]

    return lines

def benchmark(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f'Function {func.__name__} took {(end-start)*1000:.4f}ms to complete.')
        return result
    return wrapper


def transpose(grid):
    return list(zip(*grid))
