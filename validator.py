def is_float(value):
    try:
        float(value)

    except ValueError:
        return False

    return True
