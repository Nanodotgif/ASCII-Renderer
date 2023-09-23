# ASCII-Renderer
The goal of this project is to be a semi-user-friendly ascii/console graphics renderer of sorts and to provide a way to create visually appealing and widely compatable console applications with Python.
The original idea was to print frames to the console as strings of characters slideshow style, but this proved to be inconsistent between computers and environments and too unstable to function properly.  
Once I discovered [windows-curses](https://pypi.org/project/windows-curses/), I rewrote the whole program to use it, and it now runs much better.  


The next steps are to improve getting user input and supporting prompting for text input and support for resizing the window while the program is running.
