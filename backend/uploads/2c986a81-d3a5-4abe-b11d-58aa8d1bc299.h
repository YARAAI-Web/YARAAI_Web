#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
char __fastcall sub_180001000(char a1, char a2);
void *sub_180001051();
__int64 __fastcall sub_18000105E(void *a1, DWORD a2);
__int64 sub_180001083();
__int64 sub_18000130B();
// local variable allocation has failed, the output may be wrong!
BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved);
void __fastcall sub_180001A42();
// attributes: thunk
LSTATUS __stdcall RegOpenUserClassesRoot(HANDLE hToken, DWORD dwOptions, REGSAM samDesired, PHKEY phkResult);
// attributes: thunk
DWORD __stdcall WaitForInputIdle(HANDLE hProcess, DWORD dwMilliseconds);
// attributes: thunk
LPSTR __stdcall CharPrevExA(WORD CodePage, LPCSTR lpStart, LPCSTR lpCurrentChar, DWORD dwFlags);
// attributes: thunk
HDC __stdcall BeginPaint(HWND hWnd, LPPAINTSTRUCT lpPaint);
// attributes: thunk
BOOL __stdcall EnableWindow(HWND hWnd, BOOL bEnable);
// attributes: thunk
BOOL __stdcall EndDialog(HWND hDlg, INT_PTR nResult);
// attributes: thunk
DWORD __stdcall WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds);
// attributes: thunk
DWORD __stdcall GetModuleFileNameA(HMODULE hModule, LPSTR lpFilename, DWORD nSize);
// attributes: thunk
HMODULE __stdcall LoadLibraryExW(LPCWSTR lpLibFileName, HANDLE hFile, DWORD dwFlags);
// attributes: thunk
HMODULE __stdcall GetModuleHandleW(LPCWSTR lpModuleName);
// attributes: thunk
BOOL __stdcall GetStringTypeA(LCID Locale, DWORD dwInfoType, LPCSTR lpSrcStr, int cchSrc, LPWORD lpCharType);
// attributes: thunk
BOOL __stdcall SetConsoleMode(HANDLE hConsoleHandle, DWORD dwMode);
// attributes: thunk
int __stdcall GetThreadPriority(HANDLE hThread);
// attributes: thunk
DWORD __stdcall EraseTape(HANDLE hDevice, DWORD dwEraseType, BOOL bImmediate);
// attributes: thunk
BOOL __stdcall IsValidLocale(LCID Locale, DWORD dwFlags);
// attributes: thunk
int __stdcall SetStretchBltMode(HDC hdc, int mode);
// attributes: thunk
UINT __stdcall SetDIBColorTable(HDC hdc, UINT iStart, UINT cEntries, const RGBQUAD *prgbq);
// attributes: thunk
BOOL __stdcall PaintRgn(HDC hdc, HRGN hrgn);
// attributes: thunk
HGDIOBJ __stdcall GetStockObject(int i);
// attributes: thunk
HDC __stdcall CreateCompatibleDC(HDC hdc);
// attributes: thunk
BOOL __stdcall EndPath(HDC hdc);
unsigned __int64 __fastcall _alloca_probe();
void  sub_18000339E();
struct _TEB *sub_180003520();
struct _PEB *sub_180003546();
__int64 __fastcall sub_180003575(__int64 a1, __int64 a2, unsigned int a3);
unsigned __int64 __fastcall sub_180003708(unsigned int a1);
__int64 __fastcall sub_18000372A(__int64 a1);
__int16 __fastcall sub_180003762(__int16 a1);
__int64 (__fastcall *sub_180003812())();
__int64 __fastcall sub_18000387D(__int64 a1);
__int64 __fastcall sub_18000390E(__int64 a1, __int64 a2, __int64 a3, int a4);
__int64 __fastcall sub_180003AC2(__int64 a1, __int64 a2, int a3);
struct _LIST_ENTRY *__fastcall sub_180003B4B(__int64 a1, struct _LIST_ENTRY *a2);
__int64 __fastcall sub_180003DB7(__int64 a1);
__int64 __fastcall sub_18000401C(__int64 a1, __int64 a2, __int64 a3);
__int64 __fastcall sub_1800040B0(__int64 a1);
__int64 sub_1800040DC();
struct _LIST_ENTRY *sub_180004184();
__int64 __fastcall sub_180004254(_QWORD *a1);
__int64 __fastcall sub_180004569(__int64 a1);
__int64 __fastcall sub_1800045B0(__int64 a1, __int64 a2, int a3);
struct _LIST_ENTRY *sub_180004645();
__int64 __fastcall sub_180004737(__int64 a1, __int64 a2);
void  sub_180004892();
