
# A.D.A.M.S. TODO
- [ ] [Binary Builder Script]
    - [ ] Windows
    - [x] Linux
    - [ ] MacOS
- [ ] [Installer Module](#installer-module)
    - [ ] [Detect Dependencies](#detect-dependencies)
    - [ ] [Install Dependencies](#install-dependencies)
        - [ ] [Windows](#windows)
            - [ ] Download
            - [ ] Install
        - [x] [Linux](#x-linux)
            - [x] Download
            - [x] Install
        - [ ] [MacOS](#macos)
            - [ ] Download
            - [ ] Install
        - [x] [Python](#x-python)
            - [x] Download
            - [x] Install
        - [ ] [Skynet Webportal](#skynet-webportal--ansible-install)
            - [x] Download
            - [ ] Install
        - [x] [Handshake Daemon](#x-hns-full-node-install)
            - [x] Download
            - [x] Install
        - [ ] [NGINX](#nginx-install)
            - [x] Download
            - [ ] Install
        - [ ] [PowerDNS](#powerdns-install)
            - [x] Download
            - [ ] Install
- [ ] [Manager Module](#system-configuration-module)
    - [ ] [Skynet Webportal](#skynet-webportal)
    - [ ] [Handshake Daemon](#handshake-daemon)
    - [ ] [NGINX Webserver](#nginx)
    - [ ] [PowerDNS Server](#powerdns-server)

# Binary Builder Script
- ### Windows
- ### Linux
- ### MacOS

# Installer Module
- ### **Detect Dependencies**

- ### **Install Dependencies**
    - #### **Windows**

    - #### **Linux**
        - APT
            - npm
            - python3-pip
            - g++
            - libboost-all-dev
            - libtool
            - make
            - pkg-config
            - default-libmysqlclient-dev
            - libssl-dev
            - libluajit-5.1-dev
            - python3-venv
            - autoconf
            - automake
            - ragel
            - bison
            - flex
            - zip
            - unzip
    - #### **MacOS**
    - #### **Python**
        - PIP
            - getch
    - #### **Skynet Webportal + Ansible install**
        - GIT
            - https://github.com/SkynetLabs/skynet-webportal.git
            - https://github.com/SkynetLabs/ansible-playbooks.git
            - https://github.com/SkynetLabs/ansible-private-sample.git
    - #### **HNS Daemon Install**
        - GIT
            - https://github.com/handshake-org/hsd.git
    - #### **NGINX install**
        - APT
            - nginx
    - #### **PowerDNS install**
        - APT
            - sqlite3
            - pdns-server
            - pdns-backend-sqlite3
        - WGET
            - pdnsmanager-2.1.0.tar.gz

# Manager Module
- ### **Skynet Webportal**
- ### **Handshake Daemon**
- ### **NGINX Webserver**
- ### **PowerDNS Server**
 