from rich import print


def swap(a, b):
    return b, a


if __name__ == "__main__":
    A = 23
    B = 5
    C = 74
    D = 12
    E = 61

    B, D = swap(B, D)
    A, D = swap(A, D)
    C, B = swap(C, B)
    E, A = swap(E, A)

    print(f"A = {A}, B = {B}, C = {C}, D = {D}, E = {E}")
