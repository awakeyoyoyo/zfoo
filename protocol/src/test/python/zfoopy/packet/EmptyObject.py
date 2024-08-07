
class EmptyObject:
    
    pass

class EmptyObjectRegistration:
    @classmethod
    def protocolId(cls, self):
        return 0

    @classmethod
    def write(cls, buffer, packet):
        if packet is None:
            buffer.writeInt(0)
            return
        buffer.writeInt(-1)
        pass

    @classmethod
    def read(cls, buffer):
        length = buffer.readInt()
        if length == 0:
            return None
        beforeReadIndex = buffer.getReadOffset()
        packet = EmptyObject()
        
        if length > 0:
            buffer.setReadOffset(beforeReadIndex + length)
        return packet