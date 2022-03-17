#!/bin/python
def strike_temp(ambient_temp, target_temp, ratio):
    """
    Calculate the temperature of the strike liquor
    :param ambient_temp: [float] Ambient temperature in any units (both temps
    must agree)
    :param ratio: [float] desired ratio in quarts / pound
    :param target_temp: [float] Target wort resting temperature
    :return: [float] strike temperature in units given
    """
    return (target_temp - ambient_temp) / (5 * ratio) + target_temp


def strike_volume(grain_mass, ratio):
    """
    Calculate amount of liquor to strike the grain with
    :param grain_mass: [float] in pounds
    :param ratio: [float] desired ratio in quarts / pound
    :return: [float] quarts of H2O
    """
    return grain_mass * ratio


def c2f(celsius):
    """
    Covert Celsius to Fahrenheit
    :param celsius: [float] Degrees Celsius
    :return: [float] Degrees Fahrenheit
    """
    return (9 / 5 * celsius) + 32


def f2c(fahrenheit):
    """
    Covert Fahrenheit to Celsius
    :param fahrenheit: [float] Degrees Fahrenheit
    :return: [float] Degrees Celsius
    """
    return 5 / 9 * (fahrenheit - 32)


def main(ambient_temp, target_temp, grain_mass, ratio):
    """
    Return the volume (gal) and temperature of strike liquor to add to a mash
    tun
    :param ambient_temp: [float] Ambient temperature in any units (both temps
    must agree)
    :param target_temp: [float] Target wort resting temperature
    :param grain_mass: [float] in pounds
    :param ratio: [float] desired ratio in quarts / pound
    :return: [(float, float)] volume in gal and temp in given units
    """
    ts = strike_temp(ambient_temp, target_temp, ratio)
    vs = strike_volume(grain_mass, ratio)
    return vs, ts


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description=(
            "Calculate volume of liquor at specific temperature to "
            "strike the grain"
        )
    )
    parser.add_argument(
        "--ambient", "-a", type=float, dest="ta", help="Ambient Temperature"
    )
    parser.add_argument(
        "--target",
        "-t",
        type=float,
        dest="tt",
        help="Target Wort Rest Temperature",
    )
    parser.add_argument(
        "--mass", "-m", type=float, dest="mg", help="Mass of grain in pounds"
    )
    parser.add_argument(
        "--ratio",
        "-r",
        type=float,
        dest="r",
        help="Ratio of liquor volume to grain in quarts per pound",
    )
    args = parser.parse_args()
    vs, ts = main(args.ta, args.tt, args.mg, args.r)
    print(
        f"Volume of liquor needed: {vs} quarts ({vs / 4} gal) at {ts} degrees"
    )
