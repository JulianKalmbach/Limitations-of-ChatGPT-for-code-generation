import math

def cone_area(radius: float, height: float) -> float:
    """
    Berechnet die Mantelfläche eines Kegels.

    Args:
        radius (float): Der Radius des Kegels.
        height (float): Die Höhe des Kegels.

    Returns:
        float: Die Mantelfläche des Kegels.
    """
    return math.pi * radius * math.sqrt(radius ** 2 + height ** 2)