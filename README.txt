Important lines for forking:

23: 
	from subprocess import call

194:
	call (["python", "life-generator.py", "1", "2")]

	-this is how our programs will communicate
	-my program will call this to run your program, vice verca
	-it's basically typing into the command line:

		python life-generator.py 1 2
 
	-I added 2 extra arguments, that way our program knows that if it receives
         extra arguments from the command line, it'll automatically produce an output file
	 for the other program to consume

	-for example, your program will call
	
	call (["python", "person-generator.py", "1", "2")]

	-we can edit the other arguments if we want to, depending on if we want to add
	 more customizability for the user.

270:    
	-this else block executes if more than 2 arguments are passed
	-so this will execute when your program forks mine
	-then your program will use my output.csv that's produced
	-you'll have to add in an else block like this for when my program forks yours
	
My output.csv headers:
	input_state
	input_number_to_generate
	output_content_type
	output_content_value             ( this is the actual address, this is what you'll use )

So, we'll both have to import each other's programs into our own folders,
then when one of them gets forked, it'll produce an output file, and the original 
program will use that. We'll also have to import the required input csv files. I put up my ak.csv
for when your program forks mine.
