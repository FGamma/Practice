from math import pi


def sphere_volume(r: float) -> float:
    """
    Calculate the volume of a sphere given the radius.

    Parameters
    ----------
    r : float
        Radius of the sphere (must be >= 0)

    Returns
    -------
    float
        Volume of the sphere
    """
    if r < 0:
        raise ValueError("Radius cannot be negative")
    return (4 / 3) * pi * (r**3)


def main():
    try:
        # Prompt the user to enter the radius
        radius = float(input("Enter the radius of the sphere: "))

        # Calculate the volume
        volume = sphere_volume(radius)

        # Display the result rounded to 2 decimal places
        print(f"The volume of a sphere with radius {radius} is {round(volume, 2)}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
