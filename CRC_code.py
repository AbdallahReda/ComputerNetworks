import binascii

def generator(message, gen):
    frame = message             # Make frame = message  
    for i in range(len(gen)-1): # for loop to iterate over the frame and append zeros to it 
        frame += '0'            # Appending zeros to frame

    divisor0 = 0                # Divisor0 which used in xor operation with remndr (when remndr = 0)
    divisor1 = int(gen,2)       # Convert gen string into an integer with binary represtantion 
    dividend = frame[:len(gen)] # Take the first n-bits of the frame (where n = gen length)  

    iterations = (len(frame) - len(gen)) + 1  # + 1 is for, after the last bit in frame is used the loop stops
                                              # so to obtain final remainder an extra iteration is added.
    next_bit = len(gen)         # location of the next bit in the frame to be added to the remndr of division in each step
    
    
    return remndr
