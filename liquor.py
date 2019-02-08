#!/bin/python
def strike_temp(ambient_temp, target_temp, ratio):
    """
    Calculate the temperature of the strike liquor
    :param ambient_temp:
    :param ratio:
    :param target_temp:
    :return:
    """
    return (target_temp - ambient_temp)/(5 * ratio) + target_temp


def strike_volume(grain_mass, ratio):
    """
    Calculate amount of liquor to strike the grain with
    :param grain_mass: in pounds
    :param ratio: desired ratio in quarts / pound
    :return: quarts of H2O
    """
    return grain_mass * ratio


def main(ambient_temp, target_temp, grain_mass, ratio):
    ts = strike_temp(ambient_temp, target_temp, ratio)
    vs = strike_volume(grain_mass, ratio)
    return vs, ts


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description="Calculate volume of liquor at specific temperature to "
                    "strike the grain")
    parser.add_argument('--ambient', '-a', type=float, dest='ta',
                        help='Ambient Temperature')
    parser.add_argument('--target', '-t', type=float, dest='tt',
                        help='Target Wort Rest Temperature')
    parser.add_argument('--mass', '-m', type=float, dest='mg',
                        help='Mass of grain in pounds')
    parser.add_argument('--ratio', '-r', type=float, dest='r',
                        help='Ratio of liquor volume to grain in quarts per '
                             'pound')
    args = parser.parse_args()
    vs, ts = main(args.ta, args.tt, args.mg, args.r)
    print(f'Volume of liquor needed: {vs} quarts ({vs/4} gal) at {ts} degrees')
