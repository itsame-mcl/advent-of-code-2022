def detect_position(buffer, nb_distinct):
    for i in range(nb_distinct, len(buffer)):
        if len(set(buffer[i-nb_distinct:i])) == nb_distinct:
            return i
    return None
