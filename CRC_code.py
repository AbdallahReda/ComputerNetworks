import binascii

def generator(message, gen):    #Generator function which takes message and gen as paramters, performing crc algorithm  
                                #then return the transmitted message and the remndr of divison operation
    frame = message             # Make frame = message  
    for i in range(len(gen)-1): # for loop to iterate over the frame and append zeros to it 
        frame += '0'            # Appending zeros to frame

    divisor0 = 0                # Divisor0 which used in xor operation with remndr (when remndr = 0)
    divisor1 = int(gen,2)       # Convert gen string into an integer with binary represtantion 
    dividend = frame[:len(gen)] # Take the first n-bits of the frame (where n = gen length)  

    iterations = (len(frame) - len(gen)) + 1  # + 1 is for, after the last bit in frame is used the loop stops
                                              # so to obtain final remainder an extra iteration is added.
    next_bit = len(gen)         # location of the next bit in the frame to be added to the remndr of division in each step
    
    for i in range(iterations):     #iterate over the frame bits from bit=len(gen) to the latest bit of the frame
        if (dividend[0] == '1'):    #check if the first bit of dividend is "1"
            divisor = divisor1      #if bit = 1 then divisor = divisor1 = generator
        else:
            divisor = divisor0      #if bit = 0 then divisor = divisor0 = 0

        dividend = int(dividend,2)  #Convert dividend string into an integer with base = 2         
        remndr = bin(dividend^divisor).replace('b','')  #Remndr = dividend xor divisor
                                                        #We replace "b" with "" as bin(1) -> 0b001 not 001
        if(len(remndr) == len(gen)):#Check whether len of remndr = len of gen
            remndr = remndr[1:]     #if true then negelect the MSB in the remndr

        if(i != (iterations - 1)):  #if we dont reach the final iteration
            dividend = remndr+(frame[next_bit]) #dividend = remndr + next bit of the frame
            if(len(dividend) < len(gen)):       #if len of dividend < len of gen   
                dividend = ( "0" *  (len(gen) - len(dividend)) ) + dividend #add zeros to the left in dividend

        next_bit += 1 #location of next bit in the frame is next_bit++

    transmitted = bin(int(frame,2) ^ int(remndr,2))[2:] #transmitted message = frame(message after appending zeros) xor gen
    #transmitted = bin({int(message,2)[2:]}{int(remndr,2)[2:]}) #transmitted message = message appended with gen
    return remndr, transmitted

def verifier(transmitted,gen):               #verifier function which takes message and gen as paramters, calling generator function
                                             #then check if transmitted message is correct or not
    remndr , _ = generator(transmitted, gen) #Pass the transmitted message to generator function
                                             #Computing the remndr then return it
    if(int(remndr,2) == 0):                  #if remndr = 0 then the message is correct
        return ("Message is correct")      
    else:                                    #if remndr !=0 then the message is not correct
        return ("Message is not correct")
      
      
def alter(transmitted,bitNO):   #alter function which invert a certain bitNO in the transmitted message 
                                            
   transmitted = int(transmitted,2)
   transmitted ^= ~(1 << bitNO) # Compute mask, an integer with just bit 'index' set.
   return str((bin(transmitted))[2:]) # to output "00101010" not "0b00101010"
    
    
