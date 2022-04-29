# SDN Based Firewall
## Introduction to Traditional Firewalls
It's a combination of hardware and software that isolates an organization's network from the public Internet (allowing selected traffic to flow in and out). It has 3 main goals.

 1. All traffic from inside to outside and vice versa should pass through the firewall.
 2. Only authorized traffic, as defined by the security policy will be allowed to pass.
 3. Should be immune to penetration.

![enter image description here](https://i.pinimg.com/originals/00/39/c8/0039c8d193ab4109250d4211bf7b266a.jpg)

There are three firewall categories; traditional packet filters, stateful packet filters, gateway applications. This implmentation is based on traditional packet filtering. Later versions will be improved to perform stateful filtering and application gateways as well.

### Traditional Packet Filters
Organizations typically have a gateway router connecting to its ISP provider. Packet filtering occurs within this router. Packets can be filtered based on,

 - IP src/dst addresses
 - Protocol type in IP datagram field (TCP, UDP ...)
 - TCP/UDP src/dst ports
 - TCP flag bits
 - ICMP message types
 - Router interface

![enter image description here](https://www.researchgate.net/profile/Vic-Grout/publication/255564632/figure/fig1/AS:669574659833862@1536650447503/An-Access-Control-List-ACL.png)

Firewall rules are implemented using access control lists (similar to the one shown above). Rukes are applied to each datagram from top to bottom.

## Initialization

### POX Installation

The controller is implemented using the POX framework. Following are the commands to install POX.

```
$ git clone http://github.com/noxrepo/pox
$ cd pox
```

POX is implemented to run well on PyPy. Download the latest PyPy tarball from [here](https://www.pypy.org/download.html). Decompress the tarball onto a directory named pypy inside the pox directory.
