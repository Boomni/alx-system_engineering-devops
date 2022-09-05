# Shell redirections
**_This is a project on shell redirections. The files below are scripts i craeted that performs the following functions:_**

1.  0-hello_world prints “Hello, World”, followed by a new line to the standard output.
2.  1-confused_smiley Write a script that displays a confused smiley "(Ôo)'.
3.  ./2-hellofile Display the content of the /etc/passwd file.
4.  ./3-twofiles Display the content of /etc/passwd and /etc/hosts
5.  ./4-lastlines Display the last 10 lines of /etc/passwd
6.  ./5-firstlines Display the first 10 lines of /etc/passwd
7.  6-third_line Write a script that displays the third line of the file iacta.(The file iacta will be in the working directory, You’re not allowed to use sed)

   
7. It is a good file that cuts iron without making a noise
mandatory
Write a shell script that creates a file named exactly \*\\'"Best School"\'\\*$\?\*\*\*\*\*:) containing the text Best School ending by a new line.

File: 7-file
   
8. Save current state of directory
mandatory
Write a script that writes into the file ls_cwd_content the result of the command ls -la. If the file ls_cwd_content already exists, it should be overwritten. If the file ls_cwd_content does not exist, create it.


File: 8-cwd_state
   
9. Duplicate last line
mandatory
Write a script that duplicates the last line of the file iacta

T
File: 9-duplicate_last_line
   
10. No more javascript
mandatory
Write a script that deletes all the regular files (not the directories) with a .js extension that are present in the current directory and all its subfolders.


File: 10-no_more_js
   
11. Don't just count your directories, make your directories count
mandatory
Write a script that counts the number of directories and sub-directories in the current directory.

The current and parent directories should not be taken into account
Hidden directories should be counted

File: 11-directories
   
12. What’s new
mandatory
Create a script that displays the 10 newest files in the current directory.

Requirements:

One file per line
Sorted from the newest to the oldest

File: 12-newest_files
   
13. Being unique is better than being perfect
mandatory
Create a script that takes a list of words as input and prints only words that appear exactly once.

Input format: One line, one word
Output format: One line, one word
Words should be sorted

File: 13-unique
   
14. It must be in that file
mandatory
Display lines containing the pattern “root” from the file /etc/passwd


File: 15-countthatword
   
16. What's next?
mandatory
Display lines containing the pattern “root” and 3 lines after them in the file /etc/passwd.


File: 16-whatsnext
   
17. I hate bins
mandatory
Display all the lines in the file /etc/passwd that do not contain the pattern “bin”.


File: 17-hidethisword
   
18. Letters only please
mandatory
Display all lines of the file /etc/ssh/sshd_config starting with a letter.

include capital letters as well

File: 18-letteronly
   
19. A to Z
mandatory
Replace all characters A and c from input to Z and e respectively.


File: 19-AZ
   
20. Without C, you would live in hiago
mandatory
Create a script that removes all letters c and C from input.


File: 20-hiago
   
21. esreveR
mandatory
Write a script that reverse its input.


File: 21-reverse
   
22. DJ Cut Killer
mandatory
Write a script that displays all users and their home directories, sorted by users.

Based on the the /etc/passwd file

File: 22-users_and_homes
   
23. Empty casks make the most noise
#advanced
Write a command that finds all empty files and directories in the current directory and all sub-directories.

Only the names of the files and directories should be displayed (not the entire path)
Hidden files should be listed
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

File: 100-empty_casks
   
24. A gif is worth ten thousand words
#advanced
Write a script that lists all the files with a .gif extension in the current directory and all its sub-directories.

Hidden files should be listed
Only regular files (not directories) should be listed
The names of the files should be displayed without their extensions
The files should be sorted by byte values, but case-insensitive (file aaa should be listed before file bbb, file .b should be listed before file a, and file Rona should be listed after file jay)
One file name per line
The listing should end with a new line
You are not allowed to use basename, grep, egrep, fgrep or rgrep

File: 101-gifs
   
25. Acrostic
#advanced
An acrostic is a poem (or other form of writing) in which the first letter (or syllable, or word) of each line (or paragraph, or other recurring feature in the text) spells out a word, message or the alphabet. The word comes from the French acrostiche from post-classical Latin acrostichis). As a form of constrained writing, an acrostic can be used as a mnemonic device to aid memory retrieval. Read more.

Create a script that decodes acrostics that use the first letter of each line.

The ‘decoded’ message has to end with a new line
You are not allowed to use grep, egrep, fgrep or rgrep
julien@ubuntu:/tmp/0x02$ cat An\ Acrostic 
Elizabeth it is in vain you say
Love not"—thou sayest it in so sweet a way:
In vain those words from thee or L.E.L.
Zantippe's talents had enforced so well:
Ah! if that language from thy heart arise,
Breath it less gently forth—and veil thine eyes.
Endymion, recollect, when Luna tried
To cure his love—was cured of all beside—
His follie—pride—and passion—for he died.


File: 102-acrostic
   
26. The biggest fan
#advanced
Write a script that parses web servers logs in TSV format as input and displays the 11 hosts or IP addresses which did the most requests.

Order by number of requests, most active host or IP at the top
You are not allowed to use grep, egrep, fgrep or rgrep
Format:

host    When possible, the hostname making the request. Uses the IP address if the hostname was unavailable.
logname Unused, always -
time    In seconds, since 1970
method  HTTP method: GET, HEAD, or POST
url Requested path
response    HTTP response code
bytes   Number of bytes in the reply
Here is an example with one day of logs of the NASA website (1995).


File: 103-the_biggest_fan
