def to_float(data: str) -> float:
    try:
        return float(data)
    except ValueError:
        return 0.0


if __name__=="__main__":
    print(to_float('1.0e4'))
    print(to_float(''))
    print(to_float('1.ww1'))