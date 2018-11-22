import sys
import time
from Cgenerator import generator
lines=[]
for line in sys.stdin:
    lines.append(line.rstrip('\n'))
    
    #sys.stderr.write(line)
    #sys.stderr.flush()
    #time.sleep(3)
def verifier(remndr):                
                                               
        if(int(remndr,2) == 0):                  
            return ("Message is correct")      
        else:
            return ("Message is not correct")                                    

def main():
     
    transimited_message=lines[1]
    generatorFunction=lines[0]
    outputFile=open("output.txt","w")
    if len(lines)>2:
        generator_object=generator(lines[2],generatorFunction)
        remainder,_=generator_object.generate()
        print("a.  transmitted_message  ->  "+transimited_message, file = outputFile)
        print("a.  transmitted_message  ->  "+transimited_message)
        print("b.  altered_message      ->  "+lines[2], file = outputFile)
        print("b.  altered_message      ->  "+lines[2])
        print("c.  Message              ->  "+verifier(remainder), file = outputFile)
        print("c.  Message              ->  "+verifier(remainder))
    else:
        generator_object=generator(transimited_message,generatorFunction)
        remainder,_=generator_object.generate()
        print("a.  transmitted_message  ->  "+transimited_message, file = outputFile)
        print("a.  transmitted_message  ->  "+transimited_message)
        print("b.  Message              ->  "+verifier(remainder), file = outputFile)
        print("b.  Message              ->  "+verifier(remainder))


    

    
    
       

    
    outputFile.close()
   
   
    

    
if __name__ == "__main__":
    main()