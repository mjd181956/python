#include <stdio.h>



const WORD wCRCTalbeAbs[] =
{
0x0000, 0xCC01, 0xD801, 0x1400, 0xF001, 0x3C00, 0x2800, 0xE401, 0xA001, 0x6C00, 0x7800, 0xB401, 0x5000, 0x9C01, 0x8801, 0x4400,
};

WORD CRC16_2(BYTE* pchMsg, WORD wDataLen)
{
WORD wCRC = 0xFFFF;
WORD i;
BYTE chChar;

for (i = 0; i < wDataLen; i++)
{
chChar = *pchMsg++;
wCRC = wCRCTalbeAbs[(chChar ^ wCRC) & 15] ^ (wCRC >> 4);
wCRC = wCRCTalbeAbs[((chChar >> 4) ^ wCRC) & 15] ^ (wCRC >> 4);
}

return wCRC;
}

int main(void)
{
    printf("hello");
    return 0;
}