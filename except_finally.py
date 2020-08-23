def mpg(miles, gallons):
    try:
        mpg = miles / gallons
    except ZeroDivisionError:
        mpg = None
    except TypeError:
        print("you need to provide numbers")
        # raise ex
        mpg = None
    finally:
        print(f"mpg({miles}, {gallons})")
    return mpg


# mpg(23, 0)

mpg("lots", "many")
