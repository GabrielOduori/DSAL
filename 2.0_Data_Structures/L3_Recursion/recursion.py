def recursive(input):
    if input <= 0:
        return input
    else:
        output = recursive(input-1)
        return output


x = recursive(0)

print(x)