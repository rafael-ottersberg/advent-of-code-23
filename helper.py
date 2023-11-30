def read_file_lines(file_name, strip_lines=False):
    with open(file_name, 'r') as f:
        lines =  []
        for line in f:
            lines.append(line)

    if strip_lines:
        lines = [line.strip() for line in lines]

    return lines

