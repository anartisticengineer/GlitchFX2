def pixels_generator(w, h):
    i = 0
    while i < (w * h):
        yield divmod(i, w)
        i = i + 1
