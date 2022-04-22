#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "../pub/mp3dec.h"

char *array[] = {
        "../Audio/1.mp3", "../Audio/bai.mp3", "../Audio/3.mp3", "../Audio/shi.mp3","../Audio/4.mp3", "../Audio/dian.mp3",
        "../Audio/5.mp3", "../Audio/2.mp3", "../Audio/yuan.mp3"
};
static FILE *pcm = NULL;
#define MAX_PCM_BUFF_SIZE 100*1024U
void MP3_Decode(uint8_t *buffer, uint32_t length)
{
    int offset = 0;
    unsigned char *p = buffer;
    int left = length;
    int k = 0;
    int16_t *output = malloc(MAX_PCM_BUFF_SIZE);
    MP3FrameInfo frameInfo;

    HMP3Decoder hmp3decoder = MP3InitDecoder();
    memset(output, MAX_PCM_BUFF_SIZE, 0);

    while (1) {
        offset = MP3FindSyncWord(p, left);
        if (offset < 0) {
            printf(".");
            break;
        }

        left -= offset;
        p += offset;
        int err = MP3Decode(hmp3decoder, &p, &left, output, 0);
        MP3GetLastFrameInfo(hmp3decoder, &frameInfo);
#if 0
        printf("Output Num:%d\r\n", frameInfo.outputSamps);
#endif

        fwrite(output, frameInfo.outputSamps * 2, 1, pcm);
        k++;
    }
    MP3FreeDecoder(hmp3decoder);
    free(output);
}

int main() {
    static int k = 0;
    uint8_t *buffer = NULL;

    buffer = (uint8_t *)malloc(128*1024);
    printf("This is designed by Apple in Cal.\n");

    pcm = fopen("../audio/maria.pcm", "wb+");

    for(int mteaching=0;mteaching<9;mteaching++) {
        FILE *fp = fopen(array[mteaching], "rb+");
        fseek(fp, 0, SEEK_END);
        int size = ftell(fp);
        fseek(fp, 0, SEEK_SET);
        printf("filename:%s -- size:%d bytes\r\n", array[mteaching], size);
        fread(buffer, size, 1, fp);
        MP3_Decode(buffer, size);
        fclose(fp);
    }

    fclose(pcm);
    free(buffer);

    return 0;
}
