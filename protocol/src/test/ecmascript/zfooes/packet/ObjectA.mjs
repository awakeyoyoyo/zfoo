
class ObjectA {
    a = 0; // number
    m = new Map(); // Map<number, string>
    objectB = null; // ObjectB | null
    innerCompatibleValue = 0; // number
}

export class ObjectARegistration {
    protocolId() {
        return 102;
    }

    write(buffer, packet) {
        if (packet === null) {
            buffer.writeInt(0);
            return;
        }
        const beforeWriteIndex = buffer.getWriteOffset();
        buffer.writeInt(201);
        buffer.writeInt(packet.a);
        buffer.writeIntStringMap(packet.m);
        buffer.writePacket(packet.objectB, 103);
        buffer.writeInt(packet.innerCompatibleValue);
        buffer.adjustPadding(201, beforeWriteIndex);
    }

    read(buffer) {
        const length = buffer.readInt();
        if (length === 0) {
            return null;
        }
        const beforeReadIndex = buffer.getReadOffset();
        const packet = new ObjectA();
        const result0 = buffer.readInt();
        packet.a = result0;
        const map1 = buffer.readIntStringMap();
        packet.m = map1;
        const result2 = buffer.readPacket(103);
        packet.objectB = result2;
        if (buffer.compatibleRead(beforeReadIndex, length)) {
            const result3 = buffer.readInt();
            packet.innerCompatibleValue = result3;
        }
        if (length > 0) {
            buffer.setReadOffset(beforeReadIndex + length);
        }
        return packet;
    }
}

export default ObjectA;