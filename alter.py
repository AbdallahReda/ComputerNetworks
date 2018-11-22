import sys
import time
from Cgenerator import generator
lines=[]
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    #sys.stderr.write(line)
    #sys.stderr.flush()
    #time.sleep(3)
def alter(transmitted_message,bitNO): #alter function which invert a certain bitNO in the transmitted message 
         
        transmitted = int(transmitted_message,2)
        transmitted = transmitted^(0b1<<int(bitNO))# Compute mask, an integer with just bit 'index' set.
        return str((bin(transmitted))[2:]) # to output "00101010" not "0b00101010"                               

def main():
    transimited_message=lines[1]
    generatorFunction=lines[0]
    
    altered_message=alter(transimited_message, sys.argv[1])
    
    sys.stdout.write(generatorFunction+"\n")
    sys.stdout.write(transimited_message+"\n")
    sys.stdout.write(altered_message+"\n")
    

    
if __name__ == "__main__":
    main()