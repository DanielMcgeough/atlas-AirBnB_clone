# atlas-AirBnB_clone
## atlas-AirBnB_clone- A basically functional clone of the AirBnB program.
## Description
This is the first part of a many part project that will span all of the second trimester with the end goal of creating
a functional approximation of an AirBnB website. This first piece involves laying the groundwork for much of what is
going to come later. Currently, the backend is where most of the work is happening. 
Every component of the website whether it is a user or an amenity or a location will be an 
instance of a class that has been setup here in the backend. Since Python is built on the relationship
between objects and how they interact with each other, we need to build a system that can handle objects.
One of the most important pieces of this back end project is the console that will allow us as developers to interact with the various objects by providing a command line interface for us so that we can test and make sure that the objects that we have created and the instances of these classes work correctly and allow us to create, update, read or delete data that is contained
within each object. We also are constructing a means to transfer and move data between different machines by converting objects
into serialized JSON formatted strings. This will allow the application that we are creating to be able to share data across various machines and operating systems in a quick and easy way. JSON formatted strings are the corner of web applications
and since that is part of what we are creating it is essential for our project. 
The last piece of our project is storage. After we have convereted our objects into JSON formatted strings we need to be able to
have a place to store them so that they can be retrieved when they need to be changed, updated, deleted or read. That is where
the FileStorage comes into play. It will be a location to store all data relevant to the project and be able to handle
the serialization and deserialization of all of our classes.

## Description of the command interpreter:
The command interpreter through the console is a way to manipulate data without a visual interface. Since we do not have a front end Visual interface or UI to use to test our application, a command line interpreter is essential. Without it we would be unsure of how to solve any problems that might crop up and in the tech space, it would mean pushing untested code to production where users would be capable of breaking it with ease if it even works to begin with.
- 'how to start it' - The command line interpreter will start much in the same way someone would start a shell script. The name
of the script is called and a prompt will be displayed for the developer to then interact with. For instance if the script was 
called MyCommandLineInterpreter.py you would start it by entering in "python MyCommandLineInterpreter.py".
- 'how to use it' - After it is running you will receive a prompt and at this stage there are four main commands that can be used
while in the console. You can use the Quit and EOF commands to exit the program. You can use the help command to display a custom help screen. A way to handle nothing when entered is also part of it.
Beyond that there is the commands create, show, destroy, all and update which deals with how the command line interpreter interacts with objects.
- 'examples' -
## Authors
Brad Brown and Danny McGeough