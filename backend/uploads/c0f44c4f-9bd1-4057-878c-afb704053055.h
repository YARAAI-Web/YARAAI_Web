#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
__int64 __fastcall sub_62741010(__int64 a1, int a2, __int64 a3);
__int64 __fastcall sub_62741200(void *a1, unsigned int a2, __int64 a3);
BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved);
__int64 __fastcall StartAddress(HMODULE lpThreadParameter);
void sub_627413F0();
__int64 __fastcall sub_62741420(LPVOID lpParameter, int a2);
HRESULT __stdcall DllRegisterServer();
__int64 DllRegisterServerEx();
HRESULT __stdcall DllGetClassObject(const IID *const rclsid, const IID *const riid, LPVOID *ppv);
HRESULT __stdcall DllUnregisterServer();
void Start();
_BYTE *__fastcall sub_62741530(_BYTE *a1, _BYTE *a2, int a3);
_BYTE *__fastcall sub_62741690(_BYTE *a1, _BYTE *a2, int a3);
int sub_627417F0(wchar_t *a1, size_t a2, const wchar_t *a3, ...);
__int64 __fastcall sub_62741810(__int64 a1);
__int64 sub_62741A50();
__int64 sub_62741B10();
__int64 sub_62741B60();
__int64 sub_62741CD0();
__int64 sub_62741D50();
__int64 __fastcall sub_62741DE0(HMODULE hModule);
char *__fastcall sub_62741F30(
        __int64 a1,
        __int64 a2,
        unsigned __int16 a3,
        int a4,
        __int64 a5,
        WCHAR *String,
        __int64 a7,
        int a8,
        _DWORD *a9,
        int a10);
int sub_62742580(wchar_t *a1, size_t a2, const wchar_t *a3, ...);
CHAR *__fastcall sub_627425A0(LPCWCH lpWideCharStr);
WCHAR *__fastcall sub_62742640(_PROCESS_INFORMATION *lpMultiByteStr);
CHAR *__fastcall sub_627426C0(LPCWCH lpWideCharStr);
WCHAR *__fastcall sub_62742760(_PROCESS_INFORMATION *lpMultiByteStr);
_BYTE *__fastcall sub_62742820(__int64 a1);
WCHAR *__fastcall sub_627428E0(_BYTE *a1, unsigned int a2);
CHAR *__fastcall sub_62742960(
        _DWORD *a1,
        _DWORD *a2,
        const WCHAR *a3,
        const WCHAR *a4,
        const WCHAR *lpWideCharStr,
        const WCHAR *a6,
        const WCHAR *a7,
        const char *a8,
        int a9,
        unsigned int *a10);
int __fastcall sub_62742C40(char *Destination);
_DWORD *__fastcall sub_62742CD0(_DWORD *a1, int a2, const char *a3, int a4, DWORD *a5);
_DWORD *__fastcall sub_62743070(_DWORD *a1, int a2, const char *a3, int a4, _DWORD *a5);
char *__fastcall sub_627431B0(_DWORD *a1);
char *__fastcall sub_62743670(_DWORD *a1, int a2, const char *a3, int a4, _DWORD *a5);
__int64 __fastcall sub_627437A0(__int64 a1, const void *a2, DWORD a3);
_DWORD *__fastcall sub_62743890(
        _DWORD *a1,
        int a2,
        __int64 a3,
        const void *a4,
        DWORD a5,
        const char *a6,
        int a7,
        unsigned int *a8);
void *__fastcall sub_627439E0(__int64 a1, DWORD *a2);
_DWORD *__fastcall sub_62743B20(_DWORD *a1, int a2, __int64 a3, const char *a4, int a5, unsigned int *a6);
__int64 sub_62743D10();
WCHAR *__fastcall sub_62743EA0(_DWORD *a1, int a2, _PROCESS_INFORMATION *a3, const char *a4, int a5, DWORD *a6);
char *__fastcall sub_627444A0(
        _DWORD *a1,
        int a2,
        int a3,
        int a4,
        __int64 a5,
        __int64 a6,
        __int64 a7,
        int a8,
        const char *a9,
        int a10,
        unsigned int *a11);
__int64 __fastcall sub_62744620(HMODULE hModule, __int64 a2, int a3);
__int64 __fastcall sub_62744900(int a1, int a2);
__int64 sub_62744940();
__int64 sub_62744A30();
__int64 __fastcall sub_62744B50(__int64 a1, const wchar_t *a2);
__int64 sub_62745590();
__int64 sub_627455E0();
__int64 __fastcall sub_627458E0(HMODULE a1);
__int64 __fastcall sub_62745A70(HMODULE a1, const wchar_t *a2);
__int64 __fastcall sub_62745AC0(HMODULE a1);
LPVOID __fastcall sub_62745B80(SIZE_T dwBytes);
LPVOID __fastcall sub_62745BB0(LPVOID lpMem, SIZE_T dwBytes);
BOOL __fastcall sub_62745BE0(LPVOID lpMem);
_BOOL8 __fastcall sub_62745C10(_DWORD *a1);
__int64 __fastcall sub_62745FF0(_BYTE *a1, __int64 a2, unsigned __int64 a3);
char __fastcall sub_62746060(unsigned __int8 *a1, __int64 a2, __int64 a3, __int64 a4);
void *__fastcall sub_627460D0(unsigned int *a1);
_DWORD *__fastcall sub_62746B10(unsigned int *a1);
_DWORD *__fastcall sub_62746BA0(unsigned int *a1);
BOOL __fastcall sub_62746C30(__int64 a1);
int sub_62746C70(wchar_t *a1, size_t a2, const wchar_t *a3, ...);
WCHAR *__fastcall sub_62746C90(LPCCH lpMultiByteStr);
__int64 __fastcall sub_62746D10(const WCHAR *a1, const void *a2, DWORD a3);
__int64 __fastcall sub_62746DC0(int a1, const void *a2, DWORD a3, __int64 a4, const CHAR *a5, const CHAR *a6);
void sub_62747270();
__int64 __fastcall sub_62747580(__int64 a1, int a2);
__int64 __fastcall sub_627475F0(_QWORD *a1);
__int64 __fastcall sub_627477A0(WCHAR *String);
__int64 __fastcall sub_62747840(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5);
__int64 __fastcall sub_62747BA0(__int64 a1);
_BOOL8 __fastcall sub_62747CC0(OLECHAR *psz);
__int64 sub_62747EE0();
_BOOL8 sub_62748210();
__int64 __fastcall sub_62748230(WCHAR *String2);
__int64 sub_627483E0();
__int64 __fastcall sub_62748410(__int64 a1);
void (*sub_62748420())(void);
void sub_62748460();
void sub_627484D0();
LONGLONG sub_627484F0();
void __fastcall  sub_627485D0(DWORD64 a1);
__int64 __fastcall TlsCallback_1(__int64 a1, int a2);
__int64 __fastcall TlsCallback_0(__int64 a1, int a2);
void  sub_627487A0(char *Format, ...);
int __fastcall sub_62748810(_QWORD *a1, char *a2, unsigned int a3);
void sub_62748A20();
__int64 __fastcall sub_62748D10(unsigned int *a1);
__int64 sub_62748ED0();
__int64 __fastcall sub_62748FD0(unsigned int **a1);
void sub_62749180();
__int64 __fastcall sub_627491F0(int a1, __int64 a2);
__int64 __fastcall sub_62749270(int a1);
__int64 __fastcall sub_62749300(__int64 a1, unsigned int a2);
const char *__fastcall sub_62749470(char *Str2);
__int64 __fastcall sub_62749510(__int64 a1, __int64 a2);
__int64 __fastcall sub_627495A0(__int64 a1, __int64 a2, __int64 a3, __int64 a4);
__int64 __fastcall sub_627495D0(__int64 a1, __int64 a2);
__int64 __fastcall sub_62749640(__int64 a1, __int64 a2, __int64 a3, __int64 a4);
__int64 __fastcall sub_62749670(__int64 a1, __int64 a2);
__int64 __fastcall sub_62749700(unsigned int a1, __int64 a2);
void sub_627497C0();
void *__fastcall sub_627497D0();
__int64 sub_62749810();
// attributes: thunk
int __cdecl wcsncmp(const wchar_t *String1, const wchar_t *String2, size_t MaxCount);
// attributes: thunk
size_t __cdecl wcslen(const wchar_t *String);
// attributes: thunk
wchar_t *__cdecl wcscpy(wchar_t *Destination, const wchar_t *Source);
// attributes: thunk
int __cdecl wcscmp(const wchar_t *String1, const wchar_t *String2);
// attributes: thunk
wchar_t *__cdecl wcscat(wchar_t *Destination, const wchar_t *Source);
// attributes: thunk
int __cdecl vfprintf(FILE *const Stream, const char *const Format, va_list ArgList);
// attributes: thunk
int __cdecl strncmp(const char *Str1, const char *Str2, size_t MaxCount);
// attributes: thunk
size_t __cdecl strlen(const char *Str);
// attributes: thunk
char *__cdecl strcpy(char *Destination, const char *Source);
// attributes: thunk
char *__cdecl strcat(char *Destination, const char *Source);
// attributes: thunk
void __cdecl srand(unsigned int Seed);
// attributes: thunk
_crt_signal_t __cdecl signal(int Signal, _crt_signal_t Function);
// attributes: thunk
int __cdecl rand();
// attributes: thunk
void *__cdecl memset(void *a1, int Val, size_t Size);
// attributes: thunk
void *__cdecl memcpy(void *a1, const void *Src, size_t Size);
// attributes: thunk
size_t __cdecl fwrite(const void *Buffer, size_t ElementSize, size_t ElementCount, FILE *Stream);
// attributes: thunk
void __cdecl free(void *Block);
// attributes: thunk
void *__cdecl calloc(size_t Count, size_t Size);
// attributes: thunk
void __cdecl  abort();
// attributes: thunk
void __cdecl initterm(_PVFV *First, _PVFV *Last);
// attributes: thunk
__int64 __fastcall amsg_exit(__int64 a1);
__int64 __fastcall sub_62749900(__int64 a1, __int64 a2);
__int64 __fastcall sub_627499E0(__int64 a1);
FILE *__fastcall sub_62749A60(int a1);
// attributes: thunk
void *__cdecl realloc(void *Block, size_t Size);
// attributes: thunk
__int64 __fastcall unlock(__int64 a1, __int64 a2);
// attributes: thunk
__int64 __fastcall lock(__int64 a1);
// attributes: thunk
FILE *__cdecl _iob_func();
