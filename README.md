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
    --------------
    * sound1 (dict): a dictionary that represents the sound
    
    * sound2 (dict): a second dictionary that represents another sound. Must have the same rate as sound1
    or the function will return None
    
    * p (float): the mixing parameter where 0 < p < 0
    
    Returns
    ----------------
    A dictionary representing a sound that is the combination of the two sounds 

### Echo
Simulates an echo by starting with our original sound, and adding one or 
more additional copies of the sound, each delayed by some amount and scaled 
down so as to be quieter.

    echo(sound, num_echos, delay, scale)
    
    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound
    * num_echos (int): the number of additional copies of the sound to add
    * delay (float): the amount (in seconds) by which each "echo" should be delayed
    * scale (float): the amount by which each echo's samples should be scaled
    
    Returns
    -------
    A dictionary representing the sound of the echo

### Making a Spatial Sound
Transforms the sound into a spatial sound to simulate movement

    pan(sound)
    
    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound

    Returns
    -------
    A dictionary representing the sound of the spatial sound
    
### Removing vocals from Music
Removes the vocals from the sound by subtracting the left sound by the right sound

    remove_vocals(sound)
    
    Parameters
    ----------
    * sound (dict): a dictionary that represents the original sound

    Returns
    -------
    A dictionary representing the sound of the sound without vocals
