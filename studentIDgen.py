
srcPacket = hex(int('4304'))
dfsPacket = format(8074, 'x')

seq_Numbr = '00000000'
ack_Numbr = '00000000'

d_Offsett = '51020010'

print(srcPacket + dfsPacket + seq_Numbr + ack_Numbr + d_Offsett)