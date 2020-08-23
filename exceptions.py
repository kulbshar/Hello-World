# def mpg(miles, gallons):
#     return miles / gallons


def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
        print("gallon can't be zero")
    except TypeError as ex:
        mpg = None
        print("miles and gallons can't be string")
        # raise ex
    return mpg


mpg(23, 0)

mpg("lots", "many")


try:
    1 / 0
except:  # Don't do this
    pass

try:
    1 / 0
except Exception:  # This is better
    pass

try:
    1 / 0
except ZeroDivisionError:  # This is best
    pass
