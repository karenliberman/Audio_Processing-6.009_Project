# No Imports Allowed!


def backwards(sound):
    '''
    Inverts a sound, making it play backwards

    Parameters
    ----------
    * sound (dict): a dictionary that represents that sound

    Returns
    -------
    A dictionary with the same rate as the parameter, but with reversed left and right as the parameter

    '''

    return {'rate': sound['rate'], 'left': sound['left'][::-1], 'right': sound['right'][::-1]}


def mix(sound1, sound2, p):
    '''
    Mixes two sounds together using a mixing parameter. If they are of different length, 
    the combination will have the length of the shortest one. 

    Parameters
    ----------
    * sound1 (dict): a dictionary that represents the sound
    
    * sound2 (dict): a second dictionary that represents another sound. Must have the same rate as sound1
    or the function will return None
    
    * p (float): the mixing parameter where 0 < p < 0

    Returns
    -------
    A dictionary representing a sound that is the combination of the two sounds

    '''
    
    if sound1['rate'] != sound2['rate']: #ensures the sounds have the same rate
        return None
    
    #saves the length of smallest dictionary
    if len(sound1['right']) > len(sound2['right']): 
        length = len(sound2['right']) 
    else:
        length = len(sound1['right'])
    
    rightL = []
    leftL = []
    for i in range(length): 
        #adds the sum of the samples of both sounds after they are multiplied by their corresponding mixing parameter  
        rightL.append(sound1['right'][i]*p + sound2['right'][i]*(1-p))
        leftL.append(sound1['left'][i]*p + sound2['left'][i]*(1-p))
    
    #combined the new lists of samples into a dictionary and returns it
    new_sound = { 'rate' : sound1['rate'], 'right': rightL, 'left' : leftL}
    return new_sound


def echo(sound, num_echos, delay, scale):
    '''
    Simulates an echo by starting with our original sound, and adding one or 
    more additional copies of the sound, each delayed by some amount and scaled 
    down so as to be quieter.

    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound
    * num_echos (int): the number of additional copies of the sound to add
    * delay (float): the amount (in seconds) by which each "echo" should be delayed
    * scale (float): the amount by which each echo's samples should be scaled
    Returns
    -------
    A dictionary representing the sound of the echo

    '''
    
    sample_delay = round(delay * sound['rate']) #in samples delayed, not time
    
    length = len(sound['right']) + sample_delay * num_echos #final length of the sound + the echo
   
    #makes lists of the length of 'length'filled with 0 so 'append' can be used to add the sound samples
    rightL = [0 for _ in range(length) ]
    leftL = [0 for _ in range(length)]
    
    #appends the echoes + the original sound 'rightL' and 'leftL'
    for n in range(num_echos+1):
        scaling = scale**n #changes the scaling that will be used based on which echo it is
        
        #iterates for each echo, adding each of their samples to the corresponding position
        for i in range(len(sound['right'])):
            rightL[i + n*sample_delay] += sound['right'][i] * scaling
            leftL[i + n*sample_delay] += sound['left'][i] * scaling
            
    #combined the new lists of samples into a dictionary and returns it        
    new_sound = { 'rate' : sound['rate'], 'right': rightL, 'left' : leftL}
    return new_sound

def pan(sound):
    '''
    Transforms the sound into a spatial sound to simulate movement

    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound

    Returns
    -------
    A dictionary representing the sound of the spatial sound

    '''
    #copies the sound lists so they can be modified
    newRight = sound['right'][:]
    newLeft = sound['left'][:]
    
    length = len(newRight)
    
    
    for i in range(length):
        newRight[i] *= i/(length-1) #multiplied each sample by i/(N-1)
        newLeft[i] *= 1- i/(length-1) #multiplied each sample by 1 - i/(N-1)
        
    new_sound = { 'rate' : sound['rate'], 'right': newRight, 'left' : newLeft}
    return new_sound    


def remove_vocals(sound):
    '''
    Removes the vocals from the sound by subtracting the left sound by the right sound

    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound

    Returns
    -------
    A dictionary representing the sound of the sound without vocals

    '''
    combined = sound['left'][:]
    
    #subtracts each sample from the left by the matching one from the right
    for i in range(len(combined)):
        combined[i] -= sound['right'][i]
    
    #combined the new lists of samples into a dictionary and returns it  
    new_sound = { 'rate' : sound['rate'], 'right': combined, 'left' : combined}
    return new_sound



# below are helper functions for converting back-and-forth between WAV files
# and our internal dictionary representation for sounds

import io
import wave
import struct

def load_wav(filename):
    """
    Given the filename of a WAV file, load the data from that file and return a
    Python dictionary representing that sound
    """
    f = wave.open(filename, 'r')
    chan, bd, sr, count, _, _ = f.getparams()

    assert bd == 2, "only 16-bit WAV files are supported"

    left = []
    right = []
    for i in range(count):
        frame = f.readframes(1)
        if chan == 2:
            left.append(struct.unpack('<h', frame[:2])[0])
            right.append(struct.unpack('<h', frame[2:])[0])
        else:
            datum = struct.unpack('<h', frame)[0]
            left.append(datum)
            right.append(datum)

    left = [i/(2**15) for i in left]
    right = [i/(2**15) for i in right]

    return {'rate': sr, 'left': left, 'right': right}


def write_wav(sound, filename):
    """
    Given a dictionary representing a sound, and a filename, convert the given
    sound into WAV format and save it as a file with the given filename (which
    can then be opened by most audio players)
    """
    outfile = wave.open(filename, 'w')
    outfile.setparams((2, 2, sound['rate'], 0, 'NONE', 'not compressed'))

    out = []
    for l, r in zip(sound['left'], sound['right']):
        l = int(max(-1, min(1, l)) * (2**15-1))
        r = int(max(-1, min(1, r)) * (2**15-1))
        out.append(l)
        out.append(r)

    outfile.writeframes(b''.join(struct.pack('<h', frame) for frame in out))
    outfile.close()


if __name__ == '__main__':
    # code in this block will only be run when you explicitly run your script,
    # and not when the tests are being run.  this is a good place to put your
    # code for generating and saving sounds, or any other code you write for
    # testing, etc.

    # here is an example of loading a file (note that this is specified as
    # sounds/hello.wav, rather than just as hello.wav, to account for the
    # sound files being in a different directory than this file)
    
    chord = load_wav('sounds/coffee.wav')

    
    write_wav(remove_vocals(chord), 'careed.wav')
    
    