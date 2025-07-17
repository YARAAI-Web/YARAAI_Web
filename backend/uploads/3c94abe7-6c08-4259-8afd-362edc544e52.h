#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
BOOL __stdcall DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved);
void *__cdecl LibClassDesc(int a1);
int LibVersion();
int LibDescription();
_DWORD *__thiscall sub_100012D0(_DWORD *Block, char a2);
void *__thiscall sub_10001640(void *Block, char a2);
// attributes: thunk
void __cdecl j__free(void *Block);
int __onexitinit();
int __stdcall sub_1000226D(int a1, int a2, int a3);
BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved);
_DWORD *__cdecl _SEH_prolog(int a1, int a2);
// positive sp value has been detected, the output may be wrong!
void _SEH_epilog();
int __cdecl _initptd(int a1);
void __usercall sub_1000400C(int a1@<ebp>);
int __cdecl _except_handler3(int a1, int a2, int a3, int a4);
int sub_100050DB();
void  report_failure();
int __cdecl sub_100055A6(int a1, int __return_address, int a3, int a4, int a5, int a6, int a7, int a8, int a9);
int __usercall _NLG_Notify@<eax>(int result@<eax>, int a2@<ebp>);
int sub_100068D0();
// Microsoft VisualC 2-14/net runtime
int sub_100068F0();
