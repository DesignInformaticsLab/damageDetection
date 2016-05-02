This is the simulated pipe data stored as .gif images. It is the most efficient 
	way of storing the data that I found.

The gif images are stored in the 'pipe_as_gif' folder.

gif2pipe.m is a MATLAB function that translate the gif image into a 3d array of
	dimension 480*640*200. The input is the gif file and output is the 3d 
	array.

The data has noise added.

There are 5 classes: dentxxx.gif  ---- dent damage
		     impixxx.gif  ---- impingement damage
		     ndxxx.gif    ---- Non-damage pipe
		     slitxxx.gif  ---- slit damage
		     squizxxx.gif ---- squeeze damage

Storing all the data as array may require ~20GB of RAM in MATLAB. 


P.S. I wonder if neural network or any classifier could directly use .gif image
	 as input for training and classification.
