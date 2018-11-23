import getopt
import os
import sys

sys.path.append(os.path.dirname(os.getcwd()))


def main(argv):
    try:
        opts, args = getopt.getopt(argv, "source:", ['source='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        sys.exit(2)
    comamand = []
    for opt, arg in opts:
        if opt in "--source":
            comamand.append((opt, arg))
        else:
            assert False, "unhandled option"
    print(comamand)
    # options = '='.join([op, arg for op, arg in comamand])
    os.system('coverage run -m unittest discover')
    os.system('coverage report -m')
    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])