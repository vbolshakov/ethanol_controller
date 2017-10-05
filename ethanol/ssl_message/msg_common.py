# -*- coding: utf-8 -*-
""" this modules contains important constants use throught out our implementation

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
import ssl
from socket import socket, AF_INET, SOCK_STREAM

from pox.ethanol.ssl_message.enum import Enum
from pox.ethanol.ssl_message.msg_error import get_error_msg


# #####################################
#
# message version
#
# #####################################
VERSION = "1.0.3"  #: ethanol version

# #####################################
#
# tipos de mensagens
#
# #####################################

MSG_TYPE = Enum(
  'MSG_HELLO_TYPE',
  'MSG_BYE_TYPE',
  # // tipo das mensagens de erro
  'MSG_ERR_TYPE',
  # ping
  'MSG_PING',
  'MSG_PONG',
  # getmac
  'MSG_GET_MAC',
  # returns information about interfaces
  'MSG_GET_ONE_INTF',
  'MSG_GET_ALL_INTF',
  # ap
  'MSG_GET_AP_IN_RANGE_TYPE',
  # association
  'MSG_ENABLE_ASSOC_MSG',
  'MSG_ASSOCIATION',
  'MSG_DISASSOCIATION',
  'MSG_REASSOCIATION',
  'MSG_AUTHORIZATION',
  'MSG_USER_DISCONNECTING',
  'MSG_USER_CONNECTING',
  # ovsctl --> remove these messages
  'MSG_QUEUE_CREATE',
  'MSG_QUEUE_CLEAR',
  'MSG_QUEUE_DESTROY',
  'MSG_QUEUE_DESTROY_ALL',
  'MSG_QUEUE_CONFIG',
  'MSG_SHOW_PORTS',
  # beacon - ap side
  'MSG_INFORM_BEACON',
  'MSG_REQUEST_BEACON',
  # ap
  'MSG_GET_PREAMBLE',
  'MSG_SET_PREAMBLE',
  'MSG_GET_QUEUEDISCIPLINE',
  'MSG_SET_QUEUEDISCIPLINE',
  'MSG_GET_SUPPORTEDINTERFACE',
  'MSG_GET_INTERFERENCEMAP',
  'MSG_GET_AP_SSID',
  # vap
  'MSG_GET_AP_BROADCASTSSID',
  'MSG_SET_AP_BROADCASTSSID',
  'MSG_GET_AP_CAC',
  'MSG_SET_AP_CAC',
  'MSG_GET_AP_FRAMEBURSTENABLED',
  'MSG_SET_AP_FRAMEBURSTENABLED',
  'MSG_GET_AP_GUARDINTERVAL',
  'MSG_SET_AP_GUARDINTERVAL',
  'MSG_GET_AP_DTIMINTERVAL',
  'MSG_SET_AP_DTIMINTERVAL',
  'MSG_GET_AP_CTSPROTECTION_ENABLED',
  'MSG_SET_AP_CTSPROTECTION_ENABLED',
  'MSG_GET_AP_RTSTHRESHOLD',
  'MSG_SET_AP_RTSTHRESHOLD',
  'MSG_SET_AP_SSID',
  'MSG_GET_AP_ENABLED',
  'MSG_SET_AP_ENABLED',
  'MSG_VAP_CREATE',
  'MSG_SET_CONF_SSID_RADIO',
  'MSG_DISCONNECT_USER',
  'MSG_DEAUTHENTICATE_USER',
  'MSG_PROGRAM_PROBE_REQUEST',
  'MSG_PROBERECEIVED',
  'MSG_MGMTFRAME_REGISTER',
  'MSG_MGMTFRAME_UNREGISTER',
  'MSG_MGMTFRAME',
  # network
  'MSG_REQUEST_BEGIN_ASSOCIATION',
  'MSG_REQUEST_STATION_REASSOCIATE',
  'MSG_GET_ROUTES',
  # radio
  'MSG_GET_VALIDCHANNELS',
  'MSG_SET_CURRENTCHANNEL',
  'MSG_GET_CURRENTCHANNEL',
  'MSG_GET_FREQUENCY',
  'MSG_SET_FREQUENCY',
  'MSG_GET_BEACON_INTERVAL',
  'MSG_SET_BEACON_INTERVAL',
  'MSG_GET_TX_BITRATES',
  'MSG_SET_TX_BITRATES',
  'MSG_GET_TX_BITRATE',
  'MSG_GET_POWERSAVEMODE',
  'MSG_SET_POWERSAVEMODE',
  'MSG_GET_FRAGMENTATIONTHRESHOLD',
  'MSG_SET_FRAGMENTATIONTHRESHOLD',
  'MSG_GET_CHANNELBANDWITDH',
  'MSG_SET_CHANNELBANDWITDH',
  'MSG_GET_CHANNELINFO',
  'MSG_WLAN_INFO',
  'MSG_GET_RADIO_WLANS',
  'MSG_GET_RADIO_LINKSTATISTICS',
  # this messages works with station and the AP
  # if a station ID (ip and port addresses) is passed with the function call', then the AP receives the messages
  # relays the message to the station', grabs the station's response and relays this response to the controller
  # but if there is not station ID', then the message's action is performed at the AP
  'MSG_GET_IPV4_ADDRESS',
  'MSG_SET_IPV4_ADDRESS',
  'MSG_GET_IPV6_ADDRESS',
  'MSG_SET_IPV6_ADDRESS',
  'MSG_GET_802_11E_ENABLED',
  'MSG_GET_FASTBSSTRANSITION_COMPATIBLE',
  'MSG_GET_BYTESRECEIVED',
  'MSG_GET_BYTESSENT',
  'MSG_GET_PACKETSRECEIVED',
  'MSG_GET_PACKETSSENT',
  'MSG_GET_PACKETSLOST',
  'MSG_GET_JITTER',
  'MSG_GET_DELAY',
  'MSG_GET_TXPOWER',
  'MSG_SET_TXPOWER',
  'MSG_GET_SNR',
  'MSG_GET_QUALITY',
  'MSG_GET_UPTIME',
  'MSG_GET_RETRIES',
  'MSG_GET_FAILED',
  'MSG_GET_APSINRANGE',
  'MSG_GET_BEACONINFO',
  'MSG_GET_NOISEINFO',
  'MSG_GET_LINKMEASUREMENT',
  'MSG_GET_STATISTICS',
  'MSG_GET_LOCATION',
  'MSG_TRIGGER_TRANSITION',
  'MSG_GET_CPU',
  'MSG_GET_MEMORY',
  'MSG_SCAN',
  'MSG_GET_LINK_INFO',
  'MSG_SET_SNR_THRESHOLD',
  'MSG_SET_SNR_INTERVAL',
  'MSG_GET_ACS',
  'MSG_SET_SNR_THRESHOLD_REACHED',
  'MSG_GET_STA_STATISTICS',
  'MSG_GET_MEAN_STA_STATISTICS',
  'MSG_MEAN_STA_STATISTICS_GET',
  'MSG_MEAN_STA_STATISTICS_SET_INTERFACE',
  'MSG_MEAN_STA_STATISTICS_REMOVE_INTERFACE',
  'MSG_MEAN_STA_STATISTICS_SET_ALPHA',
  'MSG_MEAN_STA_STATISTICS_SET_TIME',
  'MSG_CHANGED_AP',
  'MSG_TOS_CLEANALL',
  'MSG_TOS_ADD',
  'MSG_TOS_REPLACE',
)
""" contains all constants used as message type"""

# #####################################
#
# fim da definição - tipos de mensagens
#
# #####################################

SERVER_ADDR = "localhost"
""" this is the default address our server is going to bind
    for tests, connect only to the loopback interface
    if you want to connect to all available interfaces, use "0.0.0.0"
"""

SERVER_PORT = 22222
""" this is the default port used in the AP
    the port in the station is SERVER_PORT+1 (by default)
"""

BUFFER_SIZE = 65536
""" size of the buffer used by the python socket"""


MSG_ERROR_TYPE = Enum('ERROR_UNKNOWN',
                      'ERROR_VERSION_MISMATCH',
                      'ERROR_PROCESS_NOT_IMPLEMENTED_FOR_THIS_MESSAGE',
                      'ERROR_MSG_WITHOUT_TYPE',
                      'ERROR_FIELD_NOT_FOUND',
                      'ERROR_INTERFACE_NOT_FOUND',
                      )
"""constantes usadas para definição de erro de mensagens usadas no campo error_type in msg_error.py
"""

DEFAULT_WIFI_INTFNAME = 'wlan0'


def hex(s):
    """
      converts a string of bytes to a string of hexa
    """
    return ":".join("{:02x}".format(ord(c)) for c in s)


def connect_ssl_socket(server):
    """ creates a ssl socket to server
        @param server: is a tuple (ip, port)
    """
    # print 'Socket -->: Requerendo um socket '
    sckt = socket(AF_INET, SOCK_STREAM)
    ssl_sock = ssl.wrap_socket(sckt)  # , cert_reqs=ssl.CERT_REQUIRED)
    # print 'Socket -->: conectando '
    try:
       conn = ssl_sock.connect(server)
    except:
        return -1
    # print 'Socket -->: conexao estabelecida '
    return ssl_sock


""" exemplo de uma mensagem MSG_TYPE.MSG_GET_AP_SSID

    Mensagem enviada (em c):
    1e:00:00:00:01:00:00:00:05:00:00:00:31:2e:30:2e:31:00:23:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00
                            ^ver. size  ^version          ^ m_size    ^sta_ip     ^sta_port   ^num_ssid   ^ erro detectado agora


    em C está considerando que as strings nulas tem tamanho como 4 bytes (len) + 1 byte (\0)
    só que na verdade o programa em C envia somente os 4 bytes do tamanho, indicando zero
    assim no caso desta mensagem sta_ip que é nulo, está sendo computado no tamanho da mensagem como tendo 5 bytes, mas é enviado com 4

    em python o tamanho enviado está correto, enviando também somente 4 bytes

    isto não deveria fazer diferença, pois o C e o python decodificam baseado na quantidade de bytes recebidos
    e não considera a informação em m_size
"""


def send_and_receive_msg(server, msg_struct, builder, parser, only_send=False):
    """ generic function to send and receive message

        @param server: (serverIp, serverPort)
        @param msg_struct: Container with message fields
        @param builder: Struct.build
        @param parser: Struc.parse
        this Struct class must be able to interpret Cointainer fields

        @return:
        error : false if something goes wrong
        msg : a Container with the message
    """
    msg = builder(msg_struct)
    ssl_sock = connect_ssl_socket(server)
    if ssl_sock == -1:
        # error
        return True, None

    num_bytes = ssl_sock.write(msg)
    if only_send:
        ssl_sock.close()
        # in this case, just return
        # no return parameters
        return

    received_msg = ssl_sock.read(BUFFER_SIZE)
    ssl_sock.close()
    if received_msg != '':
        from pox.ethanol.ssl_message.msg_error import is_error_msg

        if is_error_msg(received_msg):
            msg = get_error_msg(received_msg)
            return True, msg
        else:
            msg = parser(received_msg)
            # error
            return False, msg
    else:
        return True, None

