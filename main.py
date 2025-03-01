def rng_generator(number):
    return_num = 1
    if number == 'inf':
        return_num = 0
        while True:
            yield return_num
            return_num += 1
    else:
        while return_num != number + 1:
            yield return_num
            return_num += 1