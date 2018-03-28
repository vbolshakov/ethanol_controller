#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
implements the following MLME messages:

* qos_map_request
* scan_request
* channel_measurement
* channel_switch
* neighbor_report
* link_measurement
* bss_transition

no process is implemented: the controller is not supposed to respond to these message

@author: Henrique Duarte Moura
@organization: WINET/DCC/UFMG
@copyright: h3dema (c) 2017
@contact: henriquemoura@hotmail.com
@licence: GNU General Public License v2.0
(https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
@since: July 2015
@status: in development

@requires: construct 2.5.2
"""


def qos_map_request(server, id=0, intf_name=None, bssid=None, mac_station=None, mappings=None):
    """ MLME-QOS-MAP.request
        AP to transmit an unsolicited QoS Map Configure frame to a specified STA
    """
    if intf_name is None or bssid is None or mappings is None or mac_station is None:
        return


def scan_request(server, id=0, intf_name=None, bssid=None, mac_station=None, configs=None):
    """ MLME-SCAN.request
        This primitive requests a survey of potential BSSs that the STA can later elect to try to join.

        config is a dictionary with the following fields (optional):
        BSSType, BSSID, SSID, ScanType, ProbeDelay, ChannelList, MinChannelTime, MaxChannelTime,
        RequestInformation, SSID List, ChannelUsage, AccessNetworkType,
        HESSID, MeshID, DiscoveryMode
    """
    if intf_name is None or bssid is None or configs is None or mac_station is None:
        return


def channel_measurement(server, id=0, intf_name=None, bssid=None, mac_station=None,):
    """MLME-MEASURE.request
    """
    if intf_name is None or bssid is None or mac_station is None:
        return


def channel_switch(server, id=0, intf_name=None, bssid=None, mac_station=None, configs=None):
    """MLME-CHANNELSWITCH.request
        requests a switch to a new operating channel.
        waits the response or timeout

        config is a dictionary with the following fields. All optional, except "Channel Number"
        Mode, Channel Number, Secondary Channel Offset, Channel Switch Count,
        Mesh Channel Switch Parameters, Wide Bandwidth Channel Switch, New Transmit Power Envelope
    """
    if intf_name is None or bssid is None or mac_station is None or configs is None:
        return


def neighbor_report(server, id=0, intf_name=None, bssid=None, mac_station=None):
    """ start with MLME-NEIGHBORREPREQ.request
        and manages the whole process, until MLME-NEIGHBORRESP.indication

        requests that a Neighbor Report Request frame be sent to the AP with which the STA is
        associated.

        waits the response or timeout
    """
    if intf_name is None or bssid is None or mac_station is None:
        return


def link_measurement(server, id=0, intf_name=None, bssid=None, mac_station=None, configs=None):
    """ start with MLME-LINKMEASURE.request

        supports the measurement of link path loss and
        the estimation of link margin between peer entities.
        waits the response or timeout

        configs is a dictionary with the following fields
        Transmit Power, Max Transmit Power
    """
    if intf_name is None or bssid is None or mac_station is None or configs is None:
        return


def bss_transition(server, id=0, intf_name=None, bssid=None, mac_station=None, new_ap=None):
    """ start with MLME-BTM.request

        requests transmission of a BSS Transition Management Request frame to a non-AP STA.
        waits the response or timeout.
        generated by the SME to request that a BSS Transition Management Request frame be sent
        to an associated non-AP STA. This request is sent autonomously.
    """
    if intf_name is None or bssid is None or mac_station is None or new_ap is None:
        return
