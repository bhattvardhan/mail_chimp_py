# mail_chimp_py
A small python script which traverses through your defined folder structure and sends emails accordingly with an attachment

The code has been written considering below directory structure:

![alt text](https://github.com/bhattvardhan/mail_chimp_py/blob/master/dir_structure.png)

The sub-folders directly under Assignments are individual student folders and the same are their student IDs. Under them are their respective assignment folders which will contain an assignment file.

The script will prompt the user to supply the assignment number for e.g. 1, 2, n which will decide the assignment to be attached to the email by appending the against the hw folder.

Note: This version of script is only compatible with Python version 3 and above
