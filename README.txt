Running the program-
Take all the uplaoded files to a common folder.
Then open the terminal from this folder where the files are present and type <python main.py> to run the program.

Execution Packages-
In this program, I have used the following packages-
1)Modules like kivy.uix.Label,kivy.uix.Button,kivy.uix.Widget,kivy.uix.TextInput, kivy.graphics and datetime module.
2)I have used the eval() function for modifying str to dictionary.
3)I have used dictionary and tuples in my whole program majorly.

Program Structure-
My program starts with the login page where the user signs in.
if its a new user so he makes a new account and then enters it.
here i have used a txt file for saving passwords of usernames with their last updated entry date, 
that is I have stored a dictionary in the form of string to extract it again in the form of dictionary of form({"":{"":""}})
by eval() function ,at times of login.

In the second page , a page with two buttons will open which will take us to further two task- writing or reading the diary.

After that I have created two separate pages for writing a new entry or editing a previous entry and the other for reading the entries.

In writing page I have used the text box for writing content and searching bar for searching for dates and their content for editing.
Most of the functions are depended on the dictionary of the diary content which was of the form({"":{"":{"":{"":""}}}}) and the properties
of dictionaries and tuples and str indexing helped me a lot.
I have also created features option for the text that is added in the dairy like font, font size, font color .
this can be changed by clicking on a "Set" button.

In reading page , I have created readonly text box where you can just see the content but cant edit it.
Here you can search for the entry from the date search box and even read nearby diary entries by next and previous buttons which uses a method of sorting
, that was required and was the reason for creating such complex dictionary.
I have created a font resizer in this page to change the font size according to you.

I have also created a "i" button for 'how to use' rules or the program which explains the whole program in detail,
which the user can access anytime in the program from the top left corner of the page.

Learning Outcomes-
1)I learned a lot by searching on google about different ways of execution ad different types of modules that can be used to make the program easier to make.
2)I learned different types of functions like eval() which changes a string to dictionary if it is in a format of dictionary. 
This was the most frequently used technique that i used for storing new updates of user data.
3)I understood features of dictionary and tuples in a more good way and found dictionary as a very good tool in any program.
4)I also became creative because due to this program , i was contantly thinking that how should i work upon it and what else new feature can be made and all and how can we implement it.
I searched for many new things like date access where i got to learn about datetime module which is a very good module that can help a lot.
5)At many places, i was unable to figure out smart methods to do them , but tried my best to complete it any possible way atleast if no option remains.
I worked with patience ,at times when i use to repetedly get errors while running the code, but slowly I was able to clear those errors by repeated anylysis.
6)I found python very easy and useful and making a program like this was a very good explerience because it was fascinating and even i learny about a lot of basics of app development.  
