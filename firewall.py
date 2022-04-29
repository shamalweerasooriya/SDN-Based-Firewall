"""*************************************************************************************
 *
 * Date			: 29-04-2022
 * Author 		: Shamal Weerasooriya
 *
 * Description	: SDN Based Firewall
 *
 *************************************************************************************"""

from pox.core import core

blocked_ips = []

def _handle_IP_PacketIn(event):
    # gets the packet
    tcpPacket = event.parsed.find('tcp')
    # returns, if packet is not tcp
    if tcpPacket is None:
        return
    # gets the source and destination ip
    srcIp = tcpPacket.srcip
    dstIp = tcpPacket.dstip

    # if the (source ip, dst ip) is blocked, drop the packet
    if (srcIp, dstIp) in blocked_ips:
        print("Dropping packet from %s to %s" % (srcIp, dstIp))
        event.halt = True

def block(srcIp, dstIp):
    blocked_ips.append((srcIp, dstIp))

def unblock(srcIp, dstIp):
    blocked_ips.remove((srcIp, dstIp))

def launch(ips = ''):
    # add blocks from CLI
    blocked_ips.append((ip[0], ip[1]) for ip in ips.split(','))

    # add or remove rules when running POX with py
    core.Interactive.variables['block'] = block
    core.Interactive.variables['unblock'] = unblock

    # add the event handler
    core.openflow.addListenerByName("PacketIn", _handle_IP_PacketIn)