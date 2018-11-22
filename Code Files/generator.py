import sys
from Cgenerator import generator

def main():

    sys.stdin = open('input.txt', 'r')
    lines = [line.rstrip('\n') for line in sys.stdin]

    message=lines[0].strip()
    generatorFunction=lines[1].strip()
    generator_object=generator(message,generatorFunction)
    remainder,transmittedMessage=generator_object.generate()

    sys.stdout.write(generatorFunction+"\n")
    sys.stdout.write(transmittedMessage+"\n")

    
if __name__ == "__main__":
    main()