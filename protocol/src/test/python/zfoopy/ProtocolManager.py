from .packet import EmptyObject
from .packet import VeryBigObject
from .packet import ComplexObject
from .packet import NormalObject
from .packet import ObjectA
from .packet import ObjectB
from .packet import SimpleObject

protocols = {}

protocols[0] = EmptyObject.EmptyObject
protocols[1] = VeryBigObject.VeryBigObject
protocols[100] = ComplexObject.ComplexObject
protocols[101] = NormalObject.NormalObject
protocols[102] = ObjectA.ObjectA
protocols[103] = ObjectB.ObjectB
protocols[104] = SimpleObject.SimpleObject

def getProtocol(protocolId):
	return protocols[protocolId]

def write(buffer, packet):
	protocolId = packet.protocolId()
	buffer.writeShort(protocolId)
	protocol = protocols[protocolId]
	protocol.write(buffer, packet)

def read(buffer):
	protocolId = buffer.readShort()
	protocol = protocols[protocolId]
	packet = protocol.read(buffer)
	return packet