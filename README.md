# Audio_Processing-6.009_Project

## Description
Coded in python. It is a finished class project that has some basic functions to deal with audio processing. 

## Functionalities

### Reversing Audio - 
Inverts a sound, making it play backwards

backwards(sound)
Parameters
    ----------
    sound (dict): a dictionary that represents that sound

Returns
    -------
    A dictionary with the same rate as the parameter, but with reversed left and right as the parameter
   
   
### Mixing Sounds
 Mixes two sounds together using a mixing parameter. If they are of different length, 
 the combination will have the length of the shortest one. 

mix(sound1, sound2, p)
    Parameters
    
    * sound1 (dict): a dictionary that represents the sound
    
    * sound2 (dict): a second dictionary that represents another sound. Must have the same rate as sound1
    or the function will return None
    
    * p (float): the mixing parameter where 0 < p < 0

    Returns

    A dictionary representing a sound that is the combination of the two sounds
