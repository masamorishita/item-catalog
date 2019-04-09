# Item Catalog
A simple item catalog application build on Flask framework.

## Prerequisite
The program can be run on the virtual machine by using such tools as Vagrant and VirtualBox.
Here are some tips to install these tools and set up for your environment.

### Installing VirtualBox
You can download the latest version of VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads). As of January 2019, you can get VirtualBox 6.0 which is also supported by the current version of Vagrant (2.2.3)

Once you download it, install the platform package on your operating system. You do not need to launch the app itself since it is taken care of by Vagrant.


### Installing Vagrant
You can download the latest version of Vagrant from [here](https://www.vagrantup.com/downloads.html). As of January 2019, you can get Vagrant 2.2.3 which supports the current version of VirtualBox (6.0).

Once you download it, install the platform package on your operating system.

### Configure your Vagrant and access to the virtual machine
After you installed both VirtualBox and Vagrant, you should clone this [repositry](https://github.com/udacity/fullstack-nanodegree-vm) to get the pre-set configuration file for your virtual machine.
Then you use `cd` command to move into **vagrant** directory which is located in the directory you cloned.

You run the command `vagrant up` (it may take a while to initially set up the environment), then run the command `vagrant ssh`.
If you see a shell prompt that starts with the word `vagrant`, it means that you successfully logged in your virtual machine!

Inside your virtual machinde, run the comomand `cd` to move the directory to **/vagrant** where the files can be shared with your local computer.


## Installing
Clone this reporistry in one of the **/vagrant** folder by executing the following command.
```
$ git clone https://github.com/masamorishita/item-catalog
```

## Setup the database
To set up the database for the application, run the following command.
```
$ python database_setup.py
```

## Adding default category and some items
In order to add some default categories, run the following command.
```
$ python addcategories.py
```

You can also add some initail items by running the following command.
```
$ python lotsofitems.py
```

## Run the program
To run the program, execute the following command on your vagrant environment.
```
$ python application.py
```

You can access the applicatioin from [http://localhost:8000/](http://localhost:8000/).
