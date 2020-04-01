global crc_tab16


def init_crc16_tab(genPoly):
    global crc_tab16
    crc_tab16 = []
    for i in range(256):
        nData = i << 8
        crc = 0

        for j in range(8):
            if (nData ^ crc) & 0x8000:
                crc = (crc << 1) ^ genPoly
            else:
                crc = crc << 1
            nData = nData << 1

        crc_tab16.append(crc & 0xFFFF)

    return


def crc16(array, start, length):
    crc = 0

    for i in range(start, start + length):
        tmp_data = array[i]

        crc = ((crc << 8) & 0xFFFF) ^ crc_tab16[((crc >> 8) ^ tmp_data) & 0xFF]

    return crc & 0xFFFF
