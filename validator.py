def is_float(value):
    try:
        float(value)

    except ValueError:
        return False

    return True


def is_int(value):
    try:
        int(value)

    except ValueError:
        return False

    return True