def carParkingRoof(cars: list, k):

    cars.sort()
    to_cover = cars[:k]

    mx = max(to_cover)
    mi = min(to_cover)

    return mx - (mi - 1)


def process_file(filename: str) -> tuple:
    fptr = open(filename, "w")
    print("file opened")

    cars_count = int(input().strip())

    cars = []

    for _ in range(cars_count):
        cars_item = int(input().strip())
        cars.append(cars_item)

    k = int(input().strip())

    print("running code...")
    result = carParkingRoof(cars, k)

    fptr.write(str(result) + "\n")

    fptr.close()


if __name__ == "__main__":
    # print(carParkingRoof([1], 3))
    # print(carParkingRoof([6, 2, 12, 7], 3))
    # print(carParkingRoof([2, 10, 8, 17], 3))
    # print(carParkingRoof([1, 2, 3, 10], 4))

    process_file("./andela/car_park_test_case.txt")
