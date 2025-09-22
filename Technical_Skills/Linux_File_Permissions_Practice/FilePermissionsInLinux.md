# File permissions in Linux

## Project description
For the purpose of bringing a better security to file hierarchy in Linux system, a revision of the authorization to manage files in the directory `home/researcher2/projects` from various types of users was made. To achieve this goal, the shell of the Linux system was used to check, add and remove permissions from files and directories. In this task the `chmod` and `ls` play a key role, due to `ls` command enables us to check the permissions of files and directories with the flag `-l` and `-a`, while `chmod` allows us to change the permissions of files and directories, with the options `u`, `g`, `o` and the symbols `+`, `-` and `=`.

## Check file and directory details

First we check that we are in correct directory:

```shell
researcher2@ac0df5bd1d88:~$ pwd
/home/researcher2
```
Next, we navigate to the `projects` directory where we will be working:

```shell
researcher2@ac0df5bd1d88:~$ cd projects
```
Now we can check the current directory:

```shell
researcher2@ac0df5bd1d88:~/projects$ pwd
/home/researcher2/projects
```

Then we list the files and directories including hidden files with the information of permissions assigned to each file and directory:

```shell
researcher2@ac0df5bd1d88:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 14:40 .
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 15:52 ..
-rw--w---- 1 researcher2 research_team   46 Jun 21 14:40 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Jun 21 14:40 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Jun 21 14:40 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Jun 21 14:40 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_t.txt
```

Here the option `-l` is used to show the details of files and directories, including permissions, number of links, owner, group, size and modification date. The option `-a` is used to include hidden files (those starting with a dot).

### Permissions description


In the `/home/researcher2/projects directory`, there are five files with the following names and permissions: 

* **project\_k.txt (-rw-rw-rw-)**  
  * User \= read, write,   
  * Group \= read, write  
  * Other \= read, write  
* **project\_m.txt (-rw-r-----)**  
  * User \= read, write  
  * Group \= read  
  * Other \= none  
* **project\_r.txt (-rw-rw-r--)**  
  * User= read, write  
  * Group \= read, write  
  * Other \= read  
* **project\_t.txt (-rw-rw-r--)**  
  * User \= read, write  
  * Group \= read, write  
  * Other \= read  
* **.project\_x.txt (-rw-r-----)**  
  * User \= read, write  
  * Group \= write  
  * Other \= none


There is also one subdirectory inside the projects directory named drafts. The permissions on drafts are:

* User \= read, write, execute  
* Group \= execute  
* Other \= none
* \- indicates a file.


## Describe the permissions string

The permissions is useful to determine what kind of access have the *User*, *Group* and *Other* to the files and directories. The permissions string is composed of 10 characters, where the first character indicates the type of file or directory, and the next nine characters are divided into three groups of three characters each, representing the permissions for User, Group, and Other. For example, in the string `-rw-rw-r--` asociated with the file `project_r.txt`, the first character `-` indicates that it is a regular file, while the next three characters `rw-` indicate that the User has read and write permissions, but not execute permission. The next three characters `rw-` indicate that the Group has read and write permissions, and the last three characters `r--` indicate that Other has only read permission.


## Change file permissions

Since the organization does not let the Others write any file, then the permissions of the file `project_k.txt` should be changed to `-rw-rw-r--`, because a incorrect permission could lead to unauthorized modifications by Other users. To change the permissions we use the following command:

```shell
researcher2@ac0df5bd1d88:~/projects$ chmod o-w project_k.txt
```

The following instruction after the `chmod` command is `o-w`, which means we are removing the write permission for Others on the file `project_k.txt`,

Now we can check the permissions of the file `project_k.txt`:
```shell
researcher2@ac0df5bd1d88:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 14:40 .
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 15:52 ..
-rw--w---- 1 researcher2 research_team   46 Jun 21 14:40 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Jun 21 14:40 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Jun 21 14:40 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_t.txt
```


## Change file permissions on a hidden file

The file `.project_x.txt` was marked as a hidden file and this should not be modified any user, but can be read by the User and Group. The permissions of the file `.project_x.txt` are currently `-rw--w-----`, which means that the User and Group can write to it, but the Group cannot read it. So we need to change the permissions of the file `.project_x.txt` to `-r-r-------`.

To change the permissions of a hidden file, we can use the same following command:

```shell
researcher2@ac0df5bd1d88:~/projects$ chmod u-w,g-w,g+r .project_x.txt
```
The command `chmod u-w,g-w,g+r .project_x.txt` removes the write permission for the User and Group, and adds the read permission for the Group on the file `.project_x.txt`.
Now we can check the permissions of the file `.project_x.txt`:
```shell
researcher2@ac0df5bd1d88:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 14:40 .
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 15:52 ..
-r-r----- 1 researcher2 research_team   46 Jun 21 14:40 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Jun 21 14:40 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Jun 21 14:40 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_t.txt
```

## Change directory permissions

The directory `drafts` is a subdirectory of the `projects` that only must be accessed by the User, so the permissions of the directory `drafts` should be changed to `drwx------`. So we need to remove the execute permission for the User to ensure the proper access control. To change the permissions of the directory `drafts`, we can use the following command:

```shell
researcher2@ac0df5bd1d88:~/projects$ chmod g-x drafts
```

The command `chmod g-x drafts` removes the execute permission for the Group on the directory `drafts`.

Now we can check the permissions of the directory `drafts`:
```shell
researcher2@ac0df5bd1d88:~/projects$ ls -la
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 14:40 .
drwxr-xr-x 3 researcher2 research_team 4096 Jun 21 15:52 ..
drwx------- 2 researcher2 research_team 4096 Jun 21 14:40 drafts
-r-r----- 1 researcher2 research_team   46 Jun 21 14:40 .project_x.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Jun 21 14:40 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Jun 21 14:40 project_t.txt
```

## Summary

In this task, we have successfully changed the permissions of files and directories in the `/home/researcher2/projects` directory to ensure that the User has the necessary permissions to read and write files, while the Group has limited access, and Other only has read access to some files. 
