#include "5c7ccde8-6e4c-4109-8c7f-85e54f748eb3.h"

__int64 __fastcall start(__int64 a1, __int64 a2)
{
  return sub_140053160(0, a2);
}


int *__fastcall sub_140053122(unsigned int a1)
{
  unsigned __int64 v1; // rbp
  _DWORD *v2; // rdi
  int *result; // rax
  char v4; // dl
  unsigned int v5; // ecx
  int v6; // edx
  bool v7; // cf
  bool v8; // zf

  result = (_DWORD *)((char *)v2 + v1);
  v4 = *((_BYTE *)v2 + v1);
  if ( a1 <= 5 )
    goto LABEL_9;
  if ( v1 > 0xFFFFFFFFFFFFFFFCuLL )
    goto LABEL_9;
  v5 = a1 - 4;
  do
  {
    v6 = *result++;
    v7 = v5 < 4;
    v5 -= 4;
    *v2++ = v6;
  }
  while ( !v7 );
  v8 = v5 == -4;
  a1 = v5 + 4;
  v4 = *(_BYTE *)result;
  if ( !v8 )
  {
LABEL_9:
    do
    {
      result = (int *)((char *)result + 1);
      *(_BYTE *)v2 = v4;
      --a1;
      v4 = *(_BYTE *)result;
      v2 = (_DWORD *)((char *)v2 + 1);
    }
    while ( a1 );
  }
  return result;
}


// positive sp value has been detected, the output may be wrong!
__int64 __fastcall sub_140053160(__int64 a1, __int64 a2)
{
}