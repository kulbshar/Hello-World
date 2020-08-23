def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    except TypeError as ex:
        print("you need to provide numbers")
        raise ex
    else:
        mpg = float(mpg) if mpg is not None else mpg
    finally:
        print(f"mpg({miles}, {gallons})")
    return mpg


print(mpg(23, 0))

print(mpg(23, 3))

# print(mpg("lots", "many"))
