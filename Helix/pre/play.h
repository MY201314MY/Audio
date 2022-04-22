#ifndef HELIX_PLAY_H
#define HELIX_PLAY_H

#include <stdio.h>
#include <stdint.h>

#define MP3_TITSIZE_MAX		40
#define MP3_ARTSIZE_MAX		40

typedef struct
{
    uint32_t totsec ;
    uint32_t cursec ;

    uint32_t bitrate;
    uint32_t samplerate;
    uint16_t outsamples;
    uint32_t datastart;
} MP3MsgCtl;

#endif
