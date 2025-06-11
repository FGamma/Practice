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
        raise e
    except Exception as e:
        raise RuntimeError(f"Unexpected error : {e}") from e


if __name__ == "__main__":
    main()
