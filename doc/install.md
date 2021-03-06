This section explains how to install the framework and how to tune its configuration.

## System Requirements

This framework was tested on an **InstantContiki** appliance (that is, an Ubuntu 14.04).

It was tested with **Python 2 and 3**.


## Manual Installation

**This section only applies if did not followed the previous section.**

**Important Note**: For more ease, it is advised to download and deploy [InstantContiki at Sourceforge.net](https://sourceforge.net/projects/contiki/files/Instant%20Contiki/)

1. Clone the repository

 ```
 $ git clone https://github.com/dhondta/rpl-attacks.git
 ```
 
 > **Behind a proxy ?**
 > 
 > Setting: `git config --global http.proxy http://[user]:[pwd]@[host]:[port]`
 > 
 > Unsetting: `git config --global --unset http.proxy`
 > 
 > Getting: `git config --global --get http.proxy`
 
   If not using InstantContiki appliance, also clone the [repository of Contiki](https://github.com/contiki-os/contiki) :

 ```
 $ git clone https://github.com/contiki-os/contiki.git
 ```

2. Install system requirements

 ```
 $ sudo apt-get install gfortran libopenblas-dev liblapack-dev
 $ sudo apt-get install build-essential python-dev libffi-dev libssl-dev
 $ sudo apt-get install python-numpy python-scipy
 $ sudo apt-get install libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev
 $ sudo apt-get install imagemagick libcairo2-dev libffi-dev
 ```

 > **Behind a proxy ?**
 > 
 > Do not forget to configure your Network system settings (or manually edit `/etc/apt/apt.conf`).
 
   If not using InstantContiki appliance, also install :

 ```
 $ sudo apt-get install build-essential binutils-msp430 gcc-msp430 msp430-libc msp430mcu mspdebug binutils-avr gcc-avr gdb-avr avr-libc avrdude openjdk-7-jdk openjdk-7-jre ant libncurses5-dev lib32ncurses5
 ```

3. Install Python requirements

 ```
 $ cd rpl-attacks
 rpl-attacks$ sudo apt-get install python-pip
 rpl-attacks$ sudo pip install -r requirements.txt
 ```

 or

 ```
 $ cd rpl-attacks
 rpl-attacks$ sudo apt-get install python3-pip
 rpl-attacks$ sudo pip3 install -r requirements.txt
 ```

 > **Behind a proxy ?**
 > 
 > Do not forget to add option `--proxy=http://[user]:[pwd]@[host]:[port]` to your pip command.
 
4. Setup dependencies and test the framework

 ```
 rpl-attacks$ fab setup
 rpl-attacks$ fab test
 ```


## Virtual Machine Deployment

**Important Note**: This section is subject to withdrawal

**This section only applies if you want to deploy an appliance. If you want to install on your computer, please go to the next section.**

1. Clone this repository

 ```
 $ git clone https://github.com/dhondta/rpl-attacks.git
 ```
 
 > **Behind a proxy ?**
 > 
 > Setting: `git config --global http.proxy http://[user]:[pwd]@[host]:[port]`
 > 
 > Unsetting: `git config --global --unset http.proxy`
 > 
 > Getting: `git config --global --get http.proxy`

2. Create the VM

 ```
 $ vagrant up
 ```
 
 > **Behind a proxy ?**
 > 
 > Install the plugin: `vagrant plugin install vagrant-proxyconf`
 > 
 > Configure Vagrant: Uncomment the lines starting with `config.proxy` in the `Vagrantfile`

 > **Troubleshooting**:
 > 
 > - Ensure the latest version of Vagrant is installed
 > - If using `virtualbox` provider, ensure Oracle Extension Pack is installed (see [Oracle website](https://www.google.be/#q=virtualbox+oracle+extension+pack+install))


## Non-Standard Configuration

**This section only applies if you want to tune Contiki's source folder and/or your experiments folder.**

Create a default configuration file

 ```
 ../rpl-attacks$ fab config
 ```

 or create a configuration file with your own parameters (respectively, *contiki_folder* and *experiments_folder*)

 ```
 ../rpl-attacks$ fab config:/opt/contiki,~/simulations
 ```

Parameters :

- `contiki_folder`: the path to your contiki installation

>  [default: ~/contiki]

- `experiments_fodler`: the path to your experiments folder

>  [default: ~/Experiments]

These parameters can be later tuned by editing ``~/.rpl-attacks.conf``. These are written in a section named "RPL Attacks Framework Configuration".

Example configuration file :

```
[RPL Attacks Framework Configuration]
contiki_folder = /opt/contiki
experiments_folder = ~/simulations
```

