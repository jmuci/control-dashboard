Control Dashboard Project
=========================

Author: Jose M Mucientes - jm.mucientes.fayos@gmail.com


This project is a pet project of mine to practice and improve my python skills.
The idea is too create a simple dashboard that can monitor and restart services by
simply pushing a button. 

The dashboard will initially simply allow a restart of services, such as TC buildserver. 

Architecture
-----------

There should be a HTTP server running in a host. Users will have to login with LDAP to 
restart the service. 
The service will then restart the given application running a couple of ssh commands.
Alternatively the hosts where the monitored services run could have a server listening 
to restart commands.
