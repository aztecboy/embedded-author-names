# Embedded Author Names



## Signature

The signature is 3 bytes 0x41,0x52 and 0x4c. 

## Format

The first 3 bytes is the signature, then followed by the Names. Each name has to be 8 bytes(64 bits), There
is no seperator between names. The names are ended by a null byte. The author names should be in the data segment
of the file, however they dont have to.

> Format example in the nasm assembly langauge

```
Authors:
db 0x41,0x52,0x4C
db "TestName"
db "TestName"
db 0x00
```

> Format example in the C programming language

```
char Authors[] = {0x41,0x52,0x4c,'T','e','s','t','N','a','m','e','T','e','s','t','N','a','m','e','\0'};
```

