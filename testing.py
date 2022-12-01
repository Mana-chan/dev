import argsparse 

def testing():
    pass

if __name__ == "__main__":
    parser = argsparse.Argumentparser()
    parser.add_argument(
        "-b", metavar= "INT", type = int, action = "store", help = "testing argsparse")