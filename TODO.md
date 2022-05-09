
# TODO

- [-] [Installer Module](#installer-module)
    - [ ] [Detect Dependencies](#detect-dependencies)
    - [-] [Install Dependencies](#install-dependencies)
        - [ ] [Windows](#windows)
        - [x] [Linux](#x-linux)
        - [ ] [MacOS](#macos)
        - [x] [Python](#x-python)
        - [-] [Skynet Webportal](#skynet-webportal--ansible-install)
        - [x] [Handshake Daemon](#x-hns-full-node-install)
        - [-] [NGINX](#nginx-install)
        - [-] [PowerDNS](#powerdns-install)
- [ ] [System Configuration Module](#system-configuration-module)
    - [ ] [Skynet Webportal](#sk)

## Installer Module
- ### [ ] **Detect Dependencies**

- ### [-] **Install Dependencies**
    - #### [ ] **Windows**

    - #### [x] **Linux**
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
    - #### [ ] **MacOS**
    - #### [x] **Python**
        - PIP
            - getch
    - #### [-] **Skynet Webportal + Ansible install**
        - GIT
            - https://github.com/SkynetLabs/skynet-webportal.git
            - https://github.com/SkynetLabs/ansible-playbooks.git
            - https://github.com/SkynetLabs/ansible-private-sample.git
    - #### [x] **HNS Daemon Install**
        - GIT
            - https://github.com/handshake-org/hsd.git
    - #### [-] **NGINX install**
        - APT
            - nginx
    - #### [-] **PowerDNS install**
        - [x] Download
            - APT
                - sqlite3
                - pdns-server
                - pdns-backend-sqlite3
            - WGET
                - pdnsmanager-2.1.0.tar.gz

## [ ] Manager Module
- ### [ ] **Skynet Webportal**
- ### [ ] **HNS Node**
- ### [ ] **NGINX**
- ### [ ] **PowerDNS**
 