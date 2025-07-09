#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
// attributes: thunk
BOOL __stdcall CloseHandle(HANDLE hObject);
// attributes: thunk
HANDLE __stdcall MEMORY[0x404AE8](DWORD nStdHandle);
// attributes: thunk
BOOL __stdcall MEMORY[0x404AF0](
        HANDLE hFile,
        LPCVOID lpBuffer,
        DWORD nNumberOfBytesToWrite,
        LPDWORD lpNumberOfBytesWritten,
        LPOVERLAPPED lpOverlapped);
// attributes: thunk
BOOL __stdcall MEMORY[0x404AF8](HANDLE hFindFile);
// attributes: thunk
HANDLE __stdcall MEMORY[0x404B00](LPCWSTR lpFileName, LPWIN32_FIND_DATAW lpFindFileData);
// attributes: thunk
void __stdcall InitializeCriticalSection(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
void __stdcall MEMORY[0x404B10](LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
void __stdcall LeaveCriticalSection(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
void __stdcall DeleteCriticalSection(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
HANDLE __stdcall MEMORY[0x404B28](
        LPSECURITY_ATTRIBUTES lpThreadAttributes,
        SIZE_T dwStackSize,
        LPTHREAD_START_ROUTINE lpStartAddress,
        LPVOID lpParameter,
        DWORD dwCreationFlags,
        LPDWORD lpThreadId);
// attributes: thunk
DWORD __stdcall MEMORY[0x404B30]();
// attributes: thunk
BOOL __stdcall MEMORY[0x404B38]();
// attributes: thunk
void __stdcall  MEMORY[0x404B40](DWORD dwExitCode);
// attributes: thunk
void __stdcall  MEMORY[0x404B48](UINT uExitCode);
// attributes: thunk
void __stdcall RaiseException(
        DWORD dwExceptionCode,
        DWORD dwExceptionFlags,
        DWORD nNumberOfArguments,
        const ULONG_PTR *lpArguments);
// attributes: thunk
void __stdcall RtlUnwind(PVOID TargetFrame, PVOID TargetIp, PEXCEPTION_RECORD ExceptionRecord, PVOID ReturnValue);
// attributes: thunk
LONG __stdcall UnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo);
// attributes: thunk
DWORD __stdcall MEMORY[0x404B68]();
// attributes: thunk
BOOL __stdcall MEMORY[0x404B70](HMODULE hLibModule);
// attributes: thunk
int __stdcall LoadStringW(HINSTANCE hInstance, UINT uID, LPWSTR lpBuffer, int cchBufferMax);
// attributes: thunk
LPWSTR __stdcall MEMORY[0x404B80]();
// attributes: thunk
DWORD __stdcall MEMORY[0x404B88](HMODULE hModule, LPWSTR lpFilename, DWORD nSize);
// attributes: thunk
HMODULE __stdcall MEMORY[0x404B90](LPCWSTR lpModuleName);
// attributes: thunk
FARPROC __stdcall MEMORY[0x404B98](HMODULE hModule, LPCSTR lpProcName);
// attributes: thunk
void __stdcall GetStartupInfoW(LPSTARTUPINFOW lpStartupInfo);
// attributes: thunk
HMODULE __stdcall LoadLibraryExW(LPCWSTR lpLibFileName, HANDLE hFile, DWORD dwFlags);
// attributes: thunk
UINT __stdcall GetACP();
// attributes: thunk
int __stdcall MultiByteToWideChar(
        UINT CodePage,
        DWORD dwFlags,
        LPCCH lpMultiByteStr,
        int cbMultiByte,
        LPWSTR lpWideCharStr,
        int cchWideChar);
// attributes: thunk
int __stdcall MEMORY[0x404BC0](
        UINT CodePage,
        DWORD dwFlags,
        LPCWCH lpWideCharStr,
        int cchWideChar,
        LPSTR lpMultiByteStr,
        int cbMultiByte,
        LPCCH lpDefaultChar,
        LPBOOL lpUsedDefaultChar);
// attributes: thunk
int __stdcall MEMORY[0x404BC8](LCID Locale, LCTYPE LCType, LPWSTR lpLCData, int cchData);
// attributes: thunk
LANGID __stdcall MEMORY[0x404BD0]();
// attributes: thunk
LANGID __stdcall MEMORY[0x404BD8]();
// attributes: thunk
BOOL __stdcall SetThreadLocale(LCID Locale);
// attributes: thunk
BOOL __stdcall IsValidLocale(LCID Locale, DWORD dwFlags);
// attributes: thunk
LPWSTR __stdcall MEMORY[0x404BF0](LPCWSTR lpsz);
// attributes: thunk
int __stdcall MEMORY[0x404BF8](
        LCID Locale,
        DWORD dwCmpFlags,
        PCNZWCH lpString1,
        int cchCount1,
        PCNZWCH lpString2,
        int cchCount2);
// attributes: thunk
int __stdcall MessageBoxA(HWND hWnd, LPCSTR lpText, LPCSTR lpCaption, UINT uType);
// attributes: thunk
LSTATUS __stdcall RegCloseKey(HKEY hKey);
// attributes: thunk
LSTATUS __stdcall RegOpenKeyExW(HKEY hKey, LPCWSTR lpSubKey, DWORD ulOptions, REGSAM samDesired, PHKEY phkResult);
// attributes: thunk
LSTATUS __stdcall RegQueryValueExW(
        HKEY hKey,
        LPCWSTR lpValueName,
        LPDWORD lpReserved,
        LPDWORD lpType,
        LPBYTE lpData,
        LPDWORD lpcbData);
// attributes: thunk
DWORD __stdcall GetVersion();
// attributes: thunk
void __stdcall GetSystemInfo(LPSYSTEM_INFO lpSystemInfo);
// attributes: thunk
DWORD __stdcall MEMORY[0x404C30]();
// attributes: thunk
BOOL __stdcall QueryPerformanceCounter(LARGE_INTEGER *lpPerformanceCount);
// attributes: thunk
SIZE_T __stdcall MEMORY[0x404C40](LPCVOID lpAddress, PMEMORY_BASIC_INFORMATION lpBuffer, SIZE_T dwLength);
// attributes: thunk
BSTR __stdcall MEMORY[0x404C48](const OLECHAR *strIn, UINT ui);
// attributes: thunk
INT __stdcall MEMORY[0x404C50](BSTR *pbstr, const OLECHAR *psz, unsigned int len);
// attributes: thunk
void __stdcall MEMORY[0x404C58](BSTR bstrString);
// attributes: thunk
int __stdcall lstrlenW(LPCWSTR lpString);
int __usercall sub_404C78@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall MEMORY[0x404C88](PSYSTEM_LOGICAL_PROCESSOR_INFORMATION Buffer, PDWORD ReturnedLength);
int sub_404C90();
// attributes: thunk
LPVOID __stdcall MEMORY[0x404CBC](LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
// attributes: thunk
BOOL __stdcall MEMORY[0x404CC4](LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);
// attributes: thunk
void __stdcall MEMORY[0x404CCC](DWORD dwMilliseconds);
signed __int8 __usercall sub_404DB4@<al>(
        signed __int8 a1@<al>,
        signed __int8 a2@<dl>,
        volatile signed __int8 *a3@<ecx>);
int __usercall sub_404DBC@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_404DD0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_404DF0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_404E1C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_404E3C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_404E60@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_404E8C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_404EBC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_404EF4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_404F24@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
unsigned int __usercall sub_404F40@<eax>(unsigned int result@<eax>);
_DWORD *__usercall sub_404F80@<eax>(_DWORD *result@<eax>, int a2@<edx>);
void sub_404FE0();
void nullsub_88();
int __usercall sub_40504C@<eax>(int a1@<eax>);
void sub_4050C8();
_DWORD *__usercall sub_405110@<eax>(int a1@<eax>);
int __usercall sub_405174@<eax>(int a1@<eax>);
int __usercall sub_405218@<eax>(int a1@<eax>, unsigned int a2@<edx>);
volatile signed __int8 **__usercall sub_405368@<eax>(int a1@<eax>);
int __usercall sub_4056EC@<eax>(int a1@<eax>);
volatile signed __int8 **__usercall sub_4058E4@<eax>(volatile signed __int8 **result@<eax>, unsigned int a2@<edx>);
volatile signed __int8 **__usercall sub_405BFC@<eax>(int a1@<eax>);
int __usercall sub_405C30@<eax>(int a1@<eax>);
int __usercall sub_405C54@<eax>(unsigned int a1@<eax>);
int __usercall sub_405C94@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int *a3@<ecx>);
int __usercall sub_405CD0@<eax>(unsigned int a1@<eax>, int a2@<edx>);
int __fastcall sub_405D20(int a1, int a2);
int __usercall sub_405D38@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_405D6C@<al>(unsigned int a1@<eax>, int a2);
bool __usercall sub_405DE4@<al>(int a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_405E64@<eax>(int *a1@<eax>);
bool sub_405E8C();
char __usercall sub_405F00@<al>(int a1@<eax>);
int __usercall sub_405F40@<eax>(int a1@<eax>);
int *__usercall sub_405F98@<eax>(int *a1@<eax>, int a2);
int sub_406154();
unsigned int sub_406554();
_DWORD *sub_406598();
BOOL sub_4066C0();
BOOL sub_406770();
volatile signed __int8 **__usercall sub_4067C4@<eax>(volatile signed __int8 **result@<eax>);
void nullsub_89();
bool __usercall sub_4067DC@<al>(int a1@<eax>);
volatile signed __int8 **__usercall sub_4067F8@<eax>(int a1@<eax>);
int __usercall sub_406814@<eax>(int result@<eax>);
void nullsub_90();
volatile signed __int8 **__usercall sub_40682C@<eax>(volatile signed __int8 **result@<eax>, unsigned int a2@<edx>);
int sub_40687C();
int sub_40689C();
int sub_4068BC();
int sub_4068F0();
void __fastcall  sub_4068FC(int a1, int a2);
void nullsub_91();
void __usercall  sub_406908(char a1@<al>, int a2@<edx>, int a3@<ecx>);
void __usercall  sub_406954(char a1@<al>, int a2@<ecx>);
int __usercall sub_40696C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void nullsub_92();
__int64 *__usercall sub_4069BC@<eax>(__int64 *result@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int16 *__usercall sub_406ABC@<eax>(__int16 *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
__int16 *__usercall sub_406B78@<eax>(int a1@<eax>, int *a2@<edx>);
DWORD sub_406BD8();
__int16 __usercall sub_406C00@<ax>(__int16 result@<ax>);
int __cdecl sub_406C10();
int __cdecl sub_406C18();
int __usercall sub_406C2C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_406C34@<eax>(int a1@<eax>, unsigned int a2@<edx>, int a3@<ecx>);
int __usercall sub_406C54@<eax>(int result@<eax>, unsigned int a2@<edx>, char a3@<cl>);
int __usercall sub_406C74@<eax>(int a1@<eax>, char a2@<dl>);
__int16 __userpurge sub_406C98@<ax>(int a1@<eax>, __int16 a2, int a3);
double __usercall sub_406CCC@<st0>(unsigned __int64 *a1@<eax>);
int __usercall sub_406DA0@<eax>(int a1@<eax>);
int __usercall sub_406DC4@<eax>(__int64 *a1@<eax>);
char __usercall sub_406E7C@<al>(int *a1@<eax>);
int __userpurge sub_406F44@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_406F8C@<eax>(int result@<eax>, int a2, int a3, __int16 a4);
double __usercall sub_406FA8@<st0>(int a1@<eax>);
long double __stdcall sub_406FC4(_TBYTE a1);
long double __stdcall sub_406FD4(_TBYTE a1);
__int64 __usercall sub_406FE4@<edx:eax>(double a1@<st0>);
__int64 __usercall sub_406FF0@<edx:eax>(double a1@<st0>);
void __thiscall  sub_407014(void *this);
int __usercall sub_407038@<eax>(int a1@<eax>, int (__thiscall *a2)(int)@<edx>);
int __usercall sub_407080@<eax>(int a1@<eax>);
int __usercall sub_40708C@<eax>(int a1@<eax>);
int __usercall sub_4070E4@<eax>(_WORD *a1@<eax>, int a2@<edx>, __int16 a3@<cx>);
_WORD *__usercall sub_407142@<eax>(_WORD *result@<eax>, __int16 a2@<cx>);
void nullsub_76();
int __usercall sub_407180@<eax>(int result@<eax>, unsigned int *a2@<edx>);
char __usercall sub_407284@<al>(void *a1@<eax>, unsigned __int8 a2@<dl>, unsigned __int8 a3@<cl>);
char __usercall sub_4072A8@<al>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
void nullsub_93();
_BYTE *__usercall sub_4072DC@<eax>(_BYTE *result@<eax>, char *a2@<edx>, char a3@<cl>);
int __usercall sub_4072E8@<eax>(const void *a1@<eax>, char *a2@<edx>, __int16 a3@<cx>);
// attributes: thunk
int sub_407308();
void nullsub_94();
double __usercall sub_407310@<st0>(int a1@<eax>, double result@<st0>);
void nullsub_95();
int sub_4073C4();
int sub_4073F8();
void sub_407414();
void __thiscall  sub_407420(void *this);
void nullsub_96();
void __thiscall  sub_407428(void *this);
void nullsub_97();
int __usercall sub_407430@<eax>(int a1@<eax>);
int __fastcall sub_407438(int a1, int a2);
int __fastcall sub_407450(int a1, int a2);
int __usercall sub_4074E0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_40755C@<eax>(int a1@<eax>);
int sub_407568();
int __usercall sub_407584@<eax>(int a1@<eax>);
int __usercall sub_407658@<eax>(int a1@<eax>);
int __fastcall sub_407660(int a1, char a2);
int sub_407680();
_DWORD *__usercall sub_407690@<eax>(_DWORD *result@<eax>);
// attributes: thunk
_DWORD *__usercall sub_40769C@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_4076A4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4076FC@<eax>(int *a1@<eax>);
int __usercall sub_407724@<eax>(_DWORD *a1@<eax>, unsigned int a2@<edx>);
void nullsub_98();
bool __usercall sub_407754@<al>(int a1@<eax>, int a2@<edx>);
void nullsub_99();
int __usercall sub_407760@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_40780C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_407850@<eax>(int a1@<eax>);
int __fastcall sub_407858(int a1, int a2);
int __fastcall sub_4078DC(int a1, int a2);
bool __usercall sub_407960@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_407984@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4079B4@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>);
// positive sp value has been detected, the output may be wrong!
void __usercall sub_4079E4(int *a1@<eax>, unsigned __int16 a2@<si>);
void nullsub_100();
// positive sp value has been detected, the output may be wrong!
int __usercall sub_407A04@<eax>(int *a1@<eax>, unsigned __int16 a2@<dx>);
char __usercall sub_407A18@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_407A2C@<eax>(int a1@<eax>);
int sub_407A34();
int __fastcall sub_407A3C(int a1, int a2);
void nullsub_101();
void nullsub_102();
void nullsub_103();
int __usercall sub_407A5C@<eax>(int *a1@<eax>, unsigned __int16 *a2@<edx>);
void nullsub_104();
bool __usercall sub_407A88@<al>(const CHAR *a1@<eax>, const CHAR *a2@<edx>);
int *__usercall sub_407B00@<eax>(int a1@<eax>, const CHAR *a2@<edx>);
int __fastcall sub_407B70(int a1, int a2);
int *__usercall sub_407B84@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_407BAC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void nullsub_105();
_DWORD *__usercall sub_407BF8@<eax>(_DWORD *result@<eax>, const CHAR *a2@<edx>);
_DWORD *__usercall sub_407C6C@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
int __usercall sub_407C94@<eax>(int result@<eax>, char a2@<dl>, char a3);
// attributes: thunk
int __cdecl sub_407CBD(
        int a1,
        int __return_address,
        __int64 ExceptionInfo,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9);
int __usercall sub_407CE4@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_407CEC@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_407D3C@<eax>(_DWORD *result@<eax>, char a2@<dl>);
void __usercall sub_407D4C(int *a1@<eax>);
signed __int32 __usercall sub_407DC4@<eax>(volatile signed __int32 *a1@<eax>);
volatile __int32 *__usercall sub_407DF0@<eax>(volatile __int32 *result@<eax>);
int __usercall sub_407DF8@<eax>(int result@<eax>);
int sub_407E08();
void __thiscall sub_407F04(void *this);
int __usercall sub_407F18@<eax>(int a1@<eax>);
volatile signed __int8 **sub_407F30();
_DWORD *sub_407F8C();
int __usercall sub_407FA4@<eax>(int a1@<eax>);
int __thiscall sub_407FD0(void *this);
_DWORD *__usercall sub_407FEC@<eax>(int a1@<eax>);
int __usercall sub_40806C@<eax>(int a1@<eax>, unsigned int a2@<edx>);
int __usercall sub_408204@<eax>(int a1@<eax>);
int __thiscall sub_40824C(void *this);
signed __int32 __usercall sub_408264@<eax>(int a1@<eax>);
int __usercall sub_4082C4@<eax>(_DWORD *a1@<eax>);
volatile signed __int8 **__usercall sub_4082D4@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_408308@<eax>(int a1@<eax>);
_DWORD *__usercall sub_408324@<eax>(_DWORD *a1@<eax>, void *a2@<ecx>);
volatile __int32 *__usercall sub_40833C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
volatile __int32 *__usercall sub_4083AC@<eax>(volatile __int32 *result@<eax>, _DWORD *a2@<edx>);
char __usercall sub_408450@<al>(int a1@<eax>);
int __usercall sub_408490@<eax>(volatile __int32 *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_408544@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, void *a3@<ecx>);
int sub_408570();
void __usercall __spoils<edx,ecx> sub_40858C(int a1@<eax>, int a2@<edx>);
void __usercall __spoils<edx,ecx> sub_4085C8(int a1@<ebx>);
void __usercall __spoils<edx,ecx> sub_4085DC(int a1@<ebx>);
void sub_4085F0();
void __thiscall __spoils<edx,ecx> sub_408610(void *this);
void __fastcall sub_408638(int a1, int a2);
void __spoils<ecx> sub_408654();
// attributes: thunk
int __cdecl sub_408900(int a1, int a2);
int __usercall sub_408928@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __cdecl sub_4089A8(int a1, int a2);
int __cdecl sub_4089D0(int a1, int a2);
// positive sp value has been detected, the output may be wrong!
int __usercall sub_408A08@<eax>(int a1@<eax>, int a2, int a3, int a4, int a5);
void nullsub_106();
// positive sp value has been detected, the output may be wrong!
int __cdecl sub_408A78(int a1, int a2);
void nullsub_107();
int __stdcall sub_408AFC(unsigned int a1, int a2, int a3);
void nullsub_108();
struct _EXCEPTION_REGISTRATION_RECORD **__usercall sub_408C54@<eax>(
        int a1@<eax>,
        struct _EXCEPTION_REGISTRATION_RECORD *a2@<ebp>);
struct _EXCEPTION_REGISTRATION_RECORD *__usercall sub_408C74@<eax>(int a1@<eax>);
int sub_408C9C();
int sub_408D04();
int __userpurge sub_408D70@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        _DWORD *a3@<ecx>,
        int a4@<ebx>,
        int a5@<ebp>,
        int a6@<edi>,
        int a7@<esi>,
        void (__cdecl *a8)(_DWORD *));
void nullsub_109();
int __thiscall sub_408E38(void *this);
int __thiscall sub_408E8C(void *this);
int __fastcall sub_408EDC(int a1, int a2);
int __usercall sub_408EF0@<eax>(int *a1@<eax>);
int __usercall sub_408F34@<eax>(int *a1@<eax>);
int __usercall sub_408F58@<eax>(int *a1@<eax>);
unsigned int __usercall sub_408F94@<eax>(int a1@<ebx>);
// positive sp value has been detected, the output may be wrong!
BOOL __userpurge sub_408FF0@<eax>(const void **a1@<eax>, int a2, int a3, int a4);
void nullsub_110();
void __thiscall sub_40901C(void *this);
// positive sp value has been detected, the output may be wrong!
void __usercall  sub_4090B4(int a1@<ebx>);
void __usercall  sub_4091EC(UINT a1@<eax>, int a2@<ebx>);
void nullsub_111();
int __stdcall StartAddress(int (**lpThreadParameter)(void));
HANDLE __userpurge sub_40924C@<eax>(
        struct _SECURITY_ATTRIBUTES *a1@<eax>,
        SIZE_T a2@<edx>,
        volatile signed __int8 *a3@<ecx>,
        LPDWORD lpThreadId,
        DWORD dwCreationFlags,
        volatile signed __int8 *a6);
void __usercall  sub_4092C4(DWORD a1@<eax>);
volatile signed __int8 **__usercall sub_4092E0@<eax>(int a1@<eax>, void *a2@<ecx>);
volatile signed __int8 **__usercall sub_409320@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
void nullsub_112();
BSTR __usercall sub_409374@<eax>(BSTR result@<eax>);
_DWORD *__usercall sub_40938C@<eax>(_DWORD *result@<eax>);
_DWORD *__usercall sub_4093B0@<eax>(_DWORD *result@<eax>);
OLECHAR **__usercall sub_4093D4@<eax>(OLECHAR **result@<eax>);
int __usercall sub_4093EC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_40941C@<eax>(int result@<eax>, int a2@<edx>);
void __usercall sub_40944C(OLECHAR **a1@<eax>, int a2@<edx>);
int __usercall sub_409470@<eax>(int result@<eax>);
int __usercall sub_409480@<eax>(int result@<eax>);
const OLECHAR **__usercall sub_409490@<eax>(const OLECHAR **result@<eax>);
int __userpurge sub_4094B0@<eax>(CHAR *a1@<eax>, int a2@<edx>, const WCHAR *a3@<ecx>, int a4, int cchWideChar);
int __userpurge sub_4094DC@<eax>(CHAR *a1@<eax>, int a2@<edx>, const WCHAR *a3@<ecx>, int a4);
int __userpurge sub_4094F8@<eax>(WCHAR *a1@<eax>, int a2@<edx>, const CHAR *a3@<ecx>, int a4, int cbMultiByte);
_DWORD *__usercall sub_409514@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>, void *a3@<ecx>);
void __usercall sub_409544(UINT ui@<ecx>, OLECHAR *strIn@<edx>, OLECHAR **a3@<eax>);
_DWORD *__userpurge sub_409568@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>, void *a3@<ecx>, unsigned __int16 a4);
_DWORD *__userpurge sub_4095A0@<eax>(__int64 **a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>, int __saved_registers);
_DWORD *__usercall sub_409634@<eax>(__int64 **a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>);
void __userpurge sub_409644(WCHAR **a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>, int __saved_registers);
void __usercall sub_4096D8(WCHAR **a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>);
CHAR *__userpurge sub_4096E8@<eax>(CHAR **a1@<eax>, const WCHAR *a2@<edx>, int a3@<ecx>, unsigned __int16 a4);
volatile __int32 *__usercall sub_40976C@<eax>(volatile __int32 *result@<eax>, __int32 a2@<edx>);
volatile __int32 *__usercall sub_4097B4@<eax>(volatile __int32 *result@<eax>, __int32 a2@<edx>);
OLECHAR **__usercall sub_4097E0@<eax>(OLECHAR **result@<eax>, const OLECHAR *a2@<edx>);
volatile __int32 *__usercall sub_409808@<eax>(volatile __int32 *result@<eax>, __int32 a2@<edx>);
volatile __int32 *__usercall sub_409850@<eax>(volatile __int32 *result@<eax>, __int32 a2@<edx>);
int __usercall sub_40987C@<eax>(int result@<eax>);
int __usercall sub_409888@<eax>(int a1@<eax>);
int __usercall sub_40989C@<eax>(int a1@<eax>);
__int32 __usercall sub_4098B0@<eax>(volatile __int32 *a1@<eax>);
__int32 __usercall sub_4098F4@<eax>(volatile __int32 *a1@<eax>);
// attributes: thunk
__int32 __usercall sub_409938@<eax>(volatile __int32 *a1@<eax>);
void nullsub_113();
// attributes: thunk
__int32 __usercall sub_409940@<eax>(volatile __int32 *a1@<eax>);
void nullsub_114();
// attributes: thunk
__int32 __usercall sub_409948@<eax>(volatile __int32 *a1@<eax>);
void nullsub_115();
unsigned int __usercall sub_409950@<eax>(unsigned __int8 *a1@<eax>, unsigned __int8 *a2@<edx>);
int __usercall sub_4099D4@<eax>(int result@<eax>, int a2@<edx>, unsigned int a3@<ecx>);
__int64 *__usercall sub_409A44@<eax>(__int64 *a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_409A50@<eax>(int a1@<eax>, char *a2@<edx>, unsigned __int8 a3@<cl>);
int __userpurge sub_409A6C@<eax>(unsigned __int8 *a1@<eax>, int a2@<edx>, signed int a3@<ecx>, _BYTE *a4);
_DWORD *__usercall sub_409AB0@<eax>(__int64 **a1@<eax>, unsigned __int16 a2@<cx>);
_DWORD *__userpurge sub_409AC0@<eax>(__int64 **a1@<eax>, int a2@<edx>, unsigned __int16 a3);
void nullsub_116();
CHAR *__userpurge sub_409AF4@<eax>(CHAR **a1@<eax>, int a2@<edx>, unsigned __int16 a3);
void nullsub_117();
_DWORD *__userpurge sub_409B34@<eax>(__int64 **a1@<eax>, unsigned __int8 *a2@<edx>, unsigned __int16 a3);
void nullsub_118();
CHAR *__userpurge sub_409B48@<eax>(CHAR **a1@<eax>, const WCHAR *a2@<edx>, unsigned __int16 a3);
void nullsub_119();
__int64 *__usercall sub_409B60@<eax>(__int64 *result@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __usercall sub_409B84@<eax>(int result@<eax>, int a2@<edx>);
void nullsub_120();
int __usercall sub_409C04@<eax>(int result@<eax>);
volatile signed __int8 *__usercall sub_409C1C@<eax>(__int64 **a1@<eax>, int a2@<edx>, void *a3@<ecx>);
CHAR *__userpurge sub_409C94@<eax>(CHAR **a1@<eax>, const WCHAR *a2@<edx>, unsigned __int16 a3);
void nullsub_121();
void __usercall sub_409CAC(volatile __int32 *a1@<eax>, __int32 a2@<edx>);
void __usercall sub_409CBC(WCHAR **a1@<eax>);
void __usercall sub_409CD4(OLECHAR **a1@<eax>);
void __usercall sub_409CE4(WCHAR **a1@<eax>, int a2@<edx>);
void nullsub_122();
void __usercall sub_409D14(OLECHAR **a1@<eax>, OLECHAR *a2@<edx>);
void nullsub_123();
void __usercall sub_409D50(WCHAR **a1@<eax>, const CHAR *a2@<edx>, int a3);
void nullsub_124();
int *__usercall sub_409D70@<eax>(int *result@<eax>);
int __usercall sub_409D84@<eax>(int result@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int __usercall sub_409E08@<eax>(int result@<eax>, _DWORD *a2@<edx>);
void nullsub_125();
void __userpurge sub_409E10(int a1@<eax>, int a2@<edx>, int a3@<ecx>, OLECHAR **a4);
void __usercall sub_409E5C(__int64 **a1@<eax>, OLECHAR *a2@<edx>);
__int64 *__usercall sub_409EA4@<eax>(int a1@<eax>, WCHAR a2@<dx>, int a3@<ecx>);
int __usercall sub_409F00@<eax>(int result@<eax>);
_DWORD *__usercall sub_409F18@<eax>(__int64 **a1@<eax>);
_DWORD *__usercall sub_409F28@<eax>(__int64 **a1@<eax>);
_DWORD *__usercall sub_409F38@<eax>(__int64 **a1@<eax>, int a2@<edx>);
void nullsub_126();
_DWORD *__usercall sub_409F68@<eax>(__int64 **a1@<eax>, int a2@<edx>);
void nullsub_127();
_DWORD *__usercall sub_409FA4@<eax>(__int64 **a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>);
void nullsub_128();
_DWORD *__usercall sub_409FBC@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
void nullsub_129();
_DWORD *__usercall sub_409FD8@<eax>(__int64 **a1@<eax>, const CHAR *a2@<edx>, int a3);
void nullsub_130();
_DWORD *__usercall sub_409FF8@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>);
void nullsub_131();
void __usercall sub_40A00C(OLECHAR **a1@<eax>, OLECHAR *a2@<edx>);
void nullsub_132();
__int64 *__usercall sub_40A01C@<eax>(int a1@<eax>, const WCHAR *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_40A088@<eax>(__int64 **a1@<eax>, const CHAR *a2@<edx>);
void nullsub_133();
volatile signed __int8 *__usercall sub_40A094@<eax>(__int64 **a1@<eax>, int a2@<edx>, void *a3@<ecx>);
__int64 **__usercall sub_40A114@<eax>(__int64 **result@<eax>, __int32 a2@<edx>);
volatile __int32 *__usercall sub_40A16C@<eax>(volatile __int32 *a1@<eax>, __int64 *a2@<edx>, _DWORD *a3@<ecx>);
void nullsub_134();
// positive sp value has been detected, the output may be wrong!
int __usercall sub_40A1F4@<eax>(__int64 **a1@<eax>, int a2@<edx>);
void nullsub_135();
int __usercall sub_40A2A4@<eax>(int result@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_40A2DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4);
volatile signed __int8 *__usercall sub_40A324@<eax>(volatile __int32 *a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_40A380@<eax>(__int64 *result@<eax>, __int64 **a2@<edx>, int a3@<ecx>);
_BYTE *__usercall sub_40A438@<eax>(unsigned __int8 *a1@<eax>, unsigned __int8 *a2@<edx>, int a3@<ecx>);
unsigned int __usercall sub_40A4EC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_40A5BC@<eax>(__int16 a1@<ax>, void *a2@<edx>, __int64 **a3@<ecx>);
CHAR *__userpurge sub_40A5E4@<eax>(CHAR **a1@<eax>, const WCHAR *a2@<edx>, int a3@<ecx>, unsigned __int16 a4);
_DWORD *__usercall sub_40A5F8@<eax>(const CHAR **a1@<eax>, unsigned __int16 a2@<dx>, char a3@<cl>);
int __fastcall sub_40A748(int a1, int a2);
char __usercall sub_40A77C@<al>(_DWORD *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
char __usercall sub_40A814@<al>(_DWORD *a1@<eax>, _BYTE *a2@<edx>);
void nullsub_136();
int __usercall sub_40A820@<eax>(int a1@<eax>, int a2@<edx>);
int __thiscall sub_40A858(void *this);
void nullsub_137();
OLECHAR **__usercall sub_40A870@<eax>(OLECHAR **result@<eax>, char *a2@<edx>, int a3@<ecx>, int a4@<edi>);
OLECHAR **__usercall sub_40A980@<eax>(OLECHAR **a1@<eax>, char *a2@<edx>, int a3@<edi>);
void nullsub_138();
int __fastcall sub_40A98C(int a1, int a2);
int __thiscall sub_40A9C0(void *this);
void nullsub_139();
const OLECHAR **__usercall sub_40A9D8@<eax>(const OLECHAR **result@<eax>, char *a2@<edx>, void *a3@<ecx>);
int __thiscall sub_40AA9C(void *this);
void nullsub_140();
__int64 *__usercall sub_40AAB4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_40ABFC@<eax>(volatile __int32 *a1@<eax>, __int32 *a2@<edx>, _BYTE *a3@<ecx>, int a4);
void nullsub_141();
volatile signed __int8 **__usercall sub_40AD14@<eax>(int a1@<eax>, _BYTE *a2@<edx>);
int __usercall sub_40AD28@<eax>(OLECHAR **a1@<eax>, char *a2@<edx>, int a3@<edi>);
volatile __int32 *__userpurge sub_40AD38@<eax>(
        volatile __int32 *result@<eax>,
        __int32 *a2@<edx>,
        _BYTE *a3@<ecx>,
        int a4);
// attributes: thunk
OLECHAR **__usercall sub_40AD50@<eax>(OLECHAR **result@<eax>, char *a2@<edx>, int a3@<ecx>, int a4@<edi>);
void nullsub_142();
WCHAR *__usercall sub_40AD58@<eax>(const CHAR *a1@<eax>);
OLECHAR *__usercall sub_40AD78@<eax>(OLECHAR *a1@<eax>);
void __thiscall  sub_40AD98(void *this);
void nullsub_143();
int __userpurge sub_40ADA0@<eax>(int a1@<eax>, int a2, int a3);
void nullsub_144();
int __userpurge sub_40ADC4@<eax>(int a1@<eax>, int a2, int a3);
void nullsub_145();
__int64 __userpurge sub_40ADE8@<edx:eax>(int a1@<eax>, int a2@<edx>, __int64 a3);
void nullsub_146();
int __userpurge sub_40AE7C@<eax>(unsigned __int64 _RAX@<edx:eax>, unsigned __int64 a2);
void nullsub_147();
int __userpurge sub_40AEC8@<eax>(__int64 _RAX@<edx:eax>, unsigned int a2, int a3);
void nullsub_148();
__int64 __usercall sub_40AF44@<edx:eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_40B1C0@<eax>(int result@<eax>);
int __userpurge sub_40B1CC@<eax>(volatile signed __int8 ***a1@<eax>, int a2@<edx>, int a3@<ecx>, int *a4);
int __usercall sub_40B3D8@<eax>(volatile signed __int8 ***a1@<eax>, int a2@<edx>, int a3@<ecx>, int __return_address);
int __usercall sub_40B3E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
volatile __int32 **__userpurge sub_40B408@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        volatile __int32 **a4,
        int a5);
OLECHAR ***__usercall sub_40B4FC@<eax>(OLECHAR ***result@<eax>, int a2@<edx>, int a3@<edi>);
OLECHAR ***__usercall sub_40B540@<eax>(OLECHAR ***result@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
void nullsub_149();
int __usercall sub_40B57C@<eax>(int result@<eax>);
PVOID __usercall sub_40B58C@<eax>(const void *a1@<eax>);
// attributes: thunk
PVOID __usercall sub_40B5B4@<eax>(const void *a1@<eax>);
int __usercall sub_40B5BC@<eax>(int a1@<eax>);
int __usercall sub_40B604@<eax>(int a1@<eax>);
unsigned int sub_40B868();
void sub_40B958();
__int16 *__usercall sub_40B964@<eax>(__int16 *result@<eax>, int a2@<edx>, __int16 *a3@<ecx>);
int __usercall sub_40B998@<eax>(int a1@<eax>);
int __usercall sub_40BA04@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_40BAE4@<eax>(unsigned __int16 a1@<ax>, __int64 **a2@<edx>);
int __usercall sub_40BC78@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
volatile signed __int8 **__usercall sub_40BC9C@<eax>(ULONG *a1@<eax>);
volatile signed __int8 **__usercall sub_40BCE0@<eax>(__int16 a1@<ax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_40BDFC@<eax>(unsigned __int16 a1@<ax>, __int64 **a2@<edx>);
const WCHAR *__usercall sub_40BF1C@<eax>(const WCHAR *a1@<eax>);
__int16 *__usercall sub_40BF40@<eax>(__int16 *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_40C130@<eax>(int a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_40C44C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
__int64 *__usercall sub_40C4B0@<eax>(int a1@<eax>);
int __usercall sub_40C50C@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_40C578@<eax>(__int64 *a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
_DWORD *__usercall sub_40C644@<eax>(__int64 *a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_40C710@<eax>(int a1@<eax>, __int32 a2@<edx>, volatile __int32 *a3@<ecx>, int a4@<ebx>, int a5@<esi>);
HMODULE __usercall sub_40C834@<eax>(int a1@<eax>);
// attributes: thunk
int sub_40C900();
int __usercall sub_40C908@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_40C930@<eax>(int result@<eax>);
// attributes: thunk
int sub_40C95C();
// attributes: thunk
int sub_40C964();
volatile signed __int8 **__usercall sub_40C96C@<eax>(volatile signed __int8 *a1@<eax>);
int __usercall sub_40C98C@<eax>(int result@<eax>);
int __usercall sub_40C9E8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_40CA44@<eax>(_DWORD *result@<eax>);
_DWORD *__usercall sub_40CA54@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_40CAC4@<eax>(_DWORD *result@<eax>);
_DWORD *__usercall sub_40CADC@<eax>(_DWORD *result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_40CB08@<eax>(
        _DWORD *a1@<eax>,
        int (__stdcall ***a2)(_DWORD, int, _DWORD **)@<edx>,
        int a3@<ecx>);
int __usercall sub_40CB38@<eax>(int result@<eax>);
int __usercall sub_40CB50@<eax>(int result@<eax>);
int __usercall sub_40CB5C@<eax>(int result@<eax>, int a2@<ecx>);
int sub_40CB70();
int __stdcall sub_40CB80(_DWORD *a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_40CBA8(int a1);
signed __int32 __stdcall sub_40CBC4(int a1);
volatile signed __int8 **__cdecl sub_40CC08(int a1);
int __cdecl sub_40CC18(int a1);
volatile signed __int8 **__cdecl sub_40CC30(volatile signed __int8 **a1, unsigned int a2);
unsigned int __userpurge sub_40CC50@<eax>(
        LPCWCH lpWideCharStr@<ecx>,
        CHAR *a2@<eax>,
        unsigned int a3@<edx>,
        int cchWideChar);
unsigned int __userpurge sub_40CCF0@<eax>(
        WCHAR *a1@<eax>,
        unsigned int a2@<edx>,
        const CHAR *a3@<ecx>,
        int cbMultiByte);
_DWORD *__usercall sub_40CD80@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
signed int __usercall sub_40CE5C@<eax>(int a1@<eax>, _BYTE *a2@<edx>);
OLECHAR **__usercall sub_40CE94@<eax>(int a1@<eax>, OLECHAR **a2@<edx>);
_DWORD *__usercall sub_40CF3C@<eax>(const CHAR *a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_40CFCC@<eax>(const CHAR *a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_40CFE0@<eax>(const CHAR *a1@<eax>, __int64 **a2@<ecx>);
int **__usercall sub_40D018@<eax>(int **result@<eax>, __int64 **a2@<edx>);
int __userpurge sub_40D084@<eax>(
        LPCWCH lpWideCharStr@<ecx>,
        DWORD dwFlags@<edx>,
        UINT a3@<eax>,
        LPBOOL lpUsedDefaultChar,
        LPCCH lpDefaultChar,
        int cbMultiByte,
        LPSTR lpMultiByteStr,
        int cchWideChar);
int __userpurge sub_40D0AC@<eax>(
        LPCCH lpMultiByteStr@<ecx>,
        DWORD dwFlags@<edx>,
        UINT a3@<eax>,
        int cchWideChar,
        LPWSTR lpWideCharStr,
        int cbMultiByte);
DWORD sub_40D0CC();
int sub_40D0E0();
bool __usercall sub_40D11C@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_40D140@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_40D154@<eax>(_WORD *a1@<eax>);
_DWORD *__usercall sub_40D164@<eax>(_DWORD *result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_40D168@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_40D16C@<eax>(int a1@<eax>);
int __usercall sub_40D170@<eax>(int a1@<eax>);
bool __usercall sub_40D174@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_40D18C@<al>(int a1@<eax>, int a2@<edx>);
void __usercall  sub_40D1A4(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_40D1D8@<eax>(int a1@<eax>);
int __usercall sub_40D1E4@<eax>(int a1@<eax>);
int __usercall sub_40D1F0@<eax>(int a1@<eax>);
// positive sp value has been detected, the output may be wrong!
CHAR *__usercall sub_40D1FC@<eax>(const WCHAR *a1@<eax>, CHAR **a2@<edx>, unsigned __int16 a3@<si>);
// positive sp value has been detected, the output may be wrong!
CHAR *__usercall sub_40D214@<eax>(int a1@<eax>, CHAR **a2@<edx>, unsigned __int16 a3@<si>);
volatile signed __int8 **__fastcall sub_40D22C(int a1, volatile signed __int8 **a2);
volatile signed __int8 *__thiscall sub_40D240(void *this);
int __fastcall sub_40D260(int a1, int a2);
OLECHAR ***__userpurge sub_40D270@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D2CC@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D32C@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D388@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D3EC@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D448@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D4AC@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D508@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D568@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D5C4@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D628@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D688@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D6EC@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D74C@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_40D7B4@<eax>(OLECHAR **a1@<edx>, int a2@<ecx>, int a3@<edi>, int a4, __int64 *a5);
OLECHAR ***__userpurge sub_40D814@<eax>(__int64 *a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4, int a5);
__int64 __fastcall sub_40D89C(int a1, int a2);
int __fastcall sub_40D8C0(int a1, int a2);
_BYTE *__fastcall sub_40D8D8(char a1, _BYTE *a2);
int __fastcall sub_40D8E4(int a1, int a2, unsigned __int8 a3);
_WORD *__fastcall sub_40D8FC(__int16 a1, _WORD *a2);
int __fastcall sub_40D908(int a1, int a2, unsigned __int16 a3);
_DWORD *__fastcall sub_40D920(int a1, _DWORD *a2);
int __fastcall sub_40D92C(int a1, int a2, int a3);
_DWORD *__fastcall sub_40D940(int a1, _DWORD *a2, int a3, int a4);
int __fastcall sub_40D95C(int a1, int a2, int a3, int a4);
_DWORD *__fastcall sub_40D978(int a1, _DWORD *a2);
int __fastcall sub_40D990(int a1, int a2, int a3);
__int64 *__fastcall sub_40D9A4(__int64 *a1, __int64 *a2, int a3);
void *__fastcall sub_40D9C4(int a1, volatile __int32 *a2);
void *__fastcall sub_40D9F0(__int32 a1, __int32 a2);
_DWORD *__fastcall sub_40DA10(int a1, void *a2);
int __fastcall sub_40DA28(int a1, int a2);
int __thiscall sub_40DA34(void *this);
volatile signed __int8 **__fastcall sub_40DA58(unsigned __int16 __return_address, int a2);
__int64 *__fastcall sub_40DAD8(int __return_address, int a2);
int __fastcall sub_40DB28(int a1, const WCHAR *a2);
CHAR *__fastcall sub_40DB4C(unsigned __int16 __return_address, LPCWCH lpWideCharStr);
volatile signed __int8 **__fastcall sub_40DBBC(int a1, int a2);
CHAR *__fastcall sub_40DBDC(int a1, const WCHAR *a2);
int __thiscall sub_40DBFC(void *cbMultiByte, int a2);
volatile signed __int8 *__fastcall sub_40DC28(const CHAR *a1, unsigned __int16 a2, __int64 **a3, int cbMultiByte);
__int64 *__fastcall sub_40DCB0(void *a1, __int64 *a2, __int64 **a3);
volatile signed __int8 *__fastcall sub_40DCF0(int cbMultiByte, const CHAR *a2, __int64 **a3);
volatile signed __int8 *__fastcall sub_40DD18(const CHAR *a1, unsigned __int16 a2, __int64 **a3, int a4);
__int64 *__fastcall sub_40DD5C(int a1, __int64 *a2, __int64 **a3);
volatile signed __int8 *__fastcall sub_40DD9C(int a1, const CHAR *a2, __int64 **a3);
int __stdcall sub_40DDC4(int cbMultiByte);
int __fastcall sub_40DDE4(int a1, CHAR *a2, unsigned __int16 a3, int cbMultiByte);
int __stdcall sub_40DE54(int cbMultiByte, int a2);
int __fastcall sub_40DE78(int a1, int a2, unsigned __int16 a3, int cbMultiByte, int a5);
__int64 *__fastcall sub_40DEF4(int a1, __int64 *a2, int a3);
__int64 *__fastcall sub_40DF30(int a1, int a2, int a3, int a4);
int __fastcall sub_40DF74(int a1, CHAR *a2, int cbMultiByte);
int __fastcall sub_40DF94(int a1, int a2, int cbMultiByte, int a4);
BOOL sub_40DFB8();
__int32 __stdcall sub_40DFFC(volatile __int32 *a1, __int32 a2);
// attributes: thunk
BOOL __stdcall MEMORY[0x40E010](HMODULE hLibModule);
// attributes: thunk
HLOCAL __stdcall LocalAlloc(UINT uFlags, SIZE_T uBytes);
// attributes: thunk
HLOCAL __stdcall LocalFree(HLOCAL hMem);
// attributes: thunk
DWORD __stdcall TlsAlloc();
// attributes: thunk
BOOL __stdcall TlsFree(DWORD dwTlsIndex);
// attributes: thunk
LPVOID __stdcall MEMORY[0x40E038](DWORD dwTlsIndex);
// attributes: thunk
BOOL __stdcall MEMORY[0x40E040](DWORD dwTlsIndex, LPVOID lpTlsValue);
// attributes: thunk
DWORD __stdcall MEMORY[0x40E048]();
// attributes: thunk
HMODULE __stdcall LoadLibraryA(LPCSTR lpLibFileName);
// attributes: thunk
void __stdcall RaiseException_0(
        DWORD dwExceptionCode,
        DWORD dwExceptionFlags,
        DWORD nNumberOfArguments,
        const ULONG_PTR *lpArguments);
// attributes: thunk
FARPROC __stdcall MEMORY[0x40E060](HMODULE hModule, LPCSTR lpProcName);
// attributes: thunk
int __stdcall sub_40E068(int a1, int a2);
void nullsub_150();
HLOCAL __usercall sub_40E070@<eax>(SIZE_T a1@<eax>);
int sub_40E07C();
SIZE_T sub_40E084();
LPVOID sub_40E0C8();
int sub_40E0F4();
LPVOID sub_40E150();
_DWORD *sub_40E190();
int __usercall sub_40E19C@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<ebp>, int a4@<edi>, int a5@<esi>);
FARPROC __stdcall sub_40E1E8(_DWORD *a1, FARPROC *a2);
int __stdcall sub_40E4C8(int a1);
int sub_40E690();
char *__cdecl sub_40E698(int a1);
char *__cdecl sub_40E6A8(int a1);
char *__cdecl sub_40E6B8(int a1);
char *__cdecl sub_40E6C8(int a1);
char *__cdecl sub_40E6D8(int a1);
unsigned int __cdecl sub_40E6E8(const char *a1);
int __cdecl sub_40E6FC(_BYTE *a1, _BYTE *a2, int a3);
int __cdecl sub_40E72C(_DWORD *a1);
_BYTE *__cdecl sub_40E744(_BYTE *a1, _BYTE *a2, int a3);
HLOCAL *__cdecl sub_40E76C(HLOCAL *a1);
char *__cdecl sub_40E790(int a1);
char *__cdecl sub_40E7A0(int a1);
int sub_40E7B0();
double __stdcall sub_40F528(int a1, int __saved_registers);
bool __usercall sub_40F5C4@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_40F5D8@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_40F5EC@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_40F600@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_40F628@<eax>(int *a1@<eax>);
_DWORD *__usercall sub_40F69C@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_40F6BC@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
long double __usercall sub_40F6C4@<st0>(int *a1@<eax>, int *a2@<edx>);
_DWORD *__usercall sub_40F704@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_40F70C@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_40F718@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_40F720@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
int __usercall sub_40F72C@<eax>(int a1@<ecx>, int *a2@<eax>, int *a3@<edx>);
_DWORD *__usercall sub_40F754@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
double __usercall sub_40F770@<st0>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_40F7B0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int sub_40F7E0();
int __usercall sub_40F7F4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_40F814@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__userpurge sub_40F840@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__userpurge sub_40F858@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, char a4);
_DWORD *__usercall sub_40F88C@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, char a3@<cl>);
int __usercall sub_40F8B8@<eax>(_DWORD *a1@<eax>);
int __usercall sub_40F8C0@<eax>(int a1@<eax>);
bool __usercall sub_40F8CC@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_40F8F0@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __fastcall sub_40F904(int a1, int a2);
int __fastcall sub_40F91C(int a1, int a2);
_DWORD *__usercall sub_40F934@<eax>(_DWORD *result@<eax>);
bool __usercall sub_40F968@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
bool __usercall sub_40F98C@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_40F994@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_40F9E4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_40F9F0@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_40FA14@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_40FA20@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_40FA44@<eax>(int *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_40FAE0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_40FB04@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
_DWORD *__usercall sub_40FB20@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_40FB3C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_40FB64@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_40FB88@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
_DWORD *__userpurge sub_40FBB4@<eax>(_DWORD *result@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4);
_DWORD *__userpurge sub_40FC0C@<eax>(_DWORD *result@<eax>, char a2@<dl>, _DWORD *a3@<ecx>, double a4);
_DWORD *__userpurge sub_40FCB0@<eax>(_DWORD *result@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4);
_DWORD *__userpurge sub_40FD08@<eax>(_DWORD *result@<eax>, char a2@<dl>, _DWORD *a3@<ecx>, double a4);
int __usercall sub_40FDAC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_40FE28@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_40FE4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, int a5);
int __usercall sub_40FE68@<eax>(_DWORD *a1@<eax>);
int __usercall sub_40FE70@<eax>(int a1@<eax>);
void __cdecl sub_40FE7C();
int __usercall sub_40FE94@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, int *a3@<ecx>);
int __usercall sub_40FF08@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, int *a3@<ecx>);
_DWORD *__usercall sub_40FF88@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_40FF94@<al>(_DWORD *a1@<eax>);
char __usercall sub_40FFAC@<al>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_40FFC4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, int a5);
_DWORD *__usercall sub_40FFE0@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_410000@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_410008@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_41001C@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
// positive sp value has been detected, the output may be wrong!
long double __usercall sub_410032@<st0>(int *a1@<eax>, int *a2@<edx>);
bool __usercall sub_410084@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_410098@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4100AC@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_4100C0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
_WORD *__usercall sub_4100EC@<eax>(_WORD *result@<eax>, __int16 a2@<dx>, __int16 a3@<cx>);
_WORD *__usercall sub_4100F4@<eax>(_WORD *result@<eax>, __int16 a2@<dx>, __int16 a3@<cx>);
int __usercall sub_4100FC@<eax>(_WORD *a1@<eax>, int a2@<edx>);
int __usercall sub_410124@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_410154@<eax>(_WORD *a1@<eax>, int a2@<edx>);
int __usercall sub_41017C@<eax>(int a1@<eax>, int a2@<edx>);
double __usercall sub_4101AC@<st0>(__int16 *a1@<eax>, int a2@<edx>);
bool __usercall sub_4101F0@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_41021C@<al>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
LSTATUS __stdcall RegCloseKey_0(HKEY hKey);
// attributes: thunk
LSTATUS __stdcall RegConnectRegistryW(LPCWSTR lpMachineName, HKEY hKey, PHKEY phkResult);
// attributes: thunk
LSTATUS __stdcall RegCreateKeyExW(
        HKEY hKey,
        LPCWSTR lpSubKey,
        DWORD Reserved,
        LPWSTR lpClass,
        DWORD dwOptions,
        REGSAM samDesired,
        const LPSECURITY_ATTRIBUTES lpSecurityAttributes,
        PHKEY phkResult,
        LPDWORD lpdwDisposition);
// attributes: thunk
LSTATUS __stdcall RegDeleteKeyW(HKEY hKey, LPCWSTR lpSubKey);
int __usercall sub_4115C4@<eax>(__int32 a1@<eax>);
// attributes: thunk
LSTATUS __stdcall RegDeleteKeyExW(HKEY hKey, LPCWSTR lpSubKey, REGSAM samDesired, DWORD Reserved);
// attributes: thunk
LSTATUS __stdcall RegDeleteValueW(HKEY hKey, LPCWSTR lpValueName);
// attributes: thunk
LSTATUS __stdcall RegEnumKeyExW(
        HKEY hKey,
        DWORD dwIndex,
        LPWSTR lpName,
        LPDWORD lpcchName,
        LPDWORD lpReserved,
        LPWSTR lpClass,
        LPDWORD lpcchClass,
        PFILETIME lpftLastWriteTime);
// attributes: thunk
LSTATUS __stdcall RegEnumValueW(
        HKEY hKey,
        DWORD dwIndex,
        LPWSTR lpValueName,
        LPDWORD lpcchValueName,
        LPDWORD lpReserved,
        LPDWORD lpType,
        LPBYTE lpData,
        LPDWORD lpcbData);
// attributes: thunk
LSTATUS __stdcall RegFlushKey(HKEY hKey);
// attributes: thunk
LSTATUS __stdcall RegLoadKeyW(HKEY hKey, LPCWSTR lpSubKey, LPCWSTR lpFile);
// attributes: thunk
LSTATUS __stdcall RegOpenKeyExW_0(HKEY hKey, LPCWSTR lpSubKey, DWORD ulOptions, REGSAM samDesired, PHKEY phkResult);
// attributes: thunk
LSTATUS __stdcall RegQueryInfoKeyW(
        HKEY hKey,
        LPWSTR lpClass,
        LPDWORD lpcchClass,
        LPDWORD lpReserved,
        LPDWORD lpcSubKeys,
        LPDWORD lpcbMaxSubKeyLen,
        LPDWORD lpcbMaxClassLen,
        LPDWORD lpcValues,
        LPDWORD lpcbMaxValueNameLen,
        LPDWORD lpcbMaxValueLen,
        LPDWORD lpcbSecurityDescriptor,
        PFILETIME lpftLastWriteTime);
// attributes: thunk
LSTATUS __stdcall RegQueryValueExW_0(
        HKEY hKey,
        LPCWSTR lpValueName,
        LPDWORD lpReserved,
        LPDWORD lpType,
        LPBYTE lpData,
        LPDWORD lpcbData);
// attributes: thunk
LSTATUS __stdcall RegReplaceKeyW(HKEY hKey, LPCWSTR lpSubKey, LPCWSTR lpNewFile, LPCWSTR lpOldFile);
// attributes: thunk
LSTATUS __stdcall RegRestoreKeyW(HKEY hKey, LPCWSTR lpFile, DWORD dwFlags);
// attributes: thunk
LSTATUS __stdcall RegSaveKeyW(HKEY hKey, LPCWSTR lpFile, const LPSECURITY_ATTRIBUTES lpSecurityAttributes);
// attributes: thunk
LSTATUS __stdcall RegSetValueExW(
        HKEY hKey,
        LPCWSTR lpValueName,
        DWORD Reserved,
        DWORD dwType,
        const BYTE *lpData,
        DWORD cbData);
// attributes: thunk
LSTATUS __stdcall RegUnLoadKeyW(HKEY hKey, LPCWSTR lpSubKey);
// attributes: thunk
BOOL __stdcall MEMORY[0x411644](HANDLE hObject);
// attributes: thunk
int __stdcall MEMORY[0x41164C](
        LCID Locale,
        DWORD dwCmpFlags,
        PCNZWCH lpString1,
        int cchCount1,
        PCNZWCH lpString2,
        int cchCount2);
// attributes: thunk
int __stdcall MEMORY[0x411654](
        LCID Locale,
        DWORD dwCmpFlags,
        PCNZWCH lpString1,
        int cchCount1,
        PCNZWCH lpString2,
        int cchCount2);
// attributes: thunk
HANDLE __stdcall MEMORY[0x41166C](
        LPSECURITY_ATTRIBUTES lpEventAttributes,
        BOOL bManualReset,
        BOOL bInitialState,
        LPCWSTR lpName);
// attributes: thunk
HANDLE __stdcall MEMORY[0x411674](
        LPCWSTR lpFileName,
        DWORD dwDesiredAccess,
        DWORD dwShareMode,
        LPSECURITY_ATTRIBUTES lpSecurityAttributes,
        DWORD dwCreationDisposition,
        DWORD dwFlagsAndAttributes,
        HANDLE hTemplateFile);
// attributes: thunk
HANDLE __stdcall MEMORY[0x41167C](
        LPSECURITY_ATTRIBUTES lpThreadAttributes,
        SIZE_T dwStackSize,
        LPTHREAD_START_ROUTINE lpStartAddress,
        LPVOID lpParameter,
        DWORD dwCreationFlags,
        LPDWORD lpThreadId);
// attributes: thunk
void __stdcall MEMORY[0x411684](LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
void __stdcall MEMORY[0x41168C](LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
BOOL __stdcall MEMORY[0x411694](CALINFO_ENUMPROCW lpCalInfoEnumProc, LCID Locale, CALID Calendar, CALTYPE CalType);
// attributes: thunk
BOOL __stdcall MEMORY[0x41169C](HMODULE hModule, LPCWSTR lpType, ENUMRESNAMEPROCW lpEnumFunc, LONG_PTR lParam);
// attributes: thunk
BOOL __stdcall MEMORY[0x4116A4](LOCALE_ENUMPROCW lpLocaleEnumProc, DWORD dwFlags);
// attributes: thunk
BOOL __stdcall MEMORY[0x4116AC](HANDLE hFindFile);
// attributes: thunk
HANDLE __stdcall MEMORY[0x4116B4](LPCWSTR lpFileName, LPWIN32_FIND_DATAW lpFindFileData);
// attributes: thunk
HRSRC __stdcall MEMORY[0x4116BC](HMODULE hModule, LPCWSTR lpName, LPCWSTR lpType);
// attributes: thunk
DWORD __stdcall MEMORY[0x4116C4](
        DWORD dwFlags,
        LPCVOID lpSource,
        DWORD dwMessageId,
        DWORD dwLanguageId,
        LPWSTR lpBuffer,
        DWORD nSize,
        va_list *Arguments);
// attributes: thunk
BOOL __stdcall MEMORY[0x4116CC](HMODULE hLibModule);
// attributes: thunk
LONG __stdcall InterlockedCompareExchange(volatile LONG *Destination, LONG Exchange, LONG Comperand);
// attributes: thunk
LONG __stdcall InterlockedExchange(volatile LONG *Target, LONG Value);
// attributes: thunk
BOOL __stdcall FreeResource(HGLOBAL hResData);
// attributes: thunk
UINT __stdcall MEMORY[0x4116EC]();
// attributes: thunk
BOOL __stdcall MEMORY[0x4116F4](UINT CodePage, LPCPINFO lpCPInfo);
// attributes: thunk
BOOL __stdcall GetCPInfoExW(UINT CodePage, DWORD dwFlags, LPCPINFOEXW lpCPInfoEx);
// attributes: thunk
HANDLE __stdcall MEMORY[0x411704]();
// attributes: thunk
DWORD __stdcall MEMORY[0x41170C]();
// attributes: thunk
HANDLE __stdcall MEMORY[0x411714]();
// attributes: thunk
DWORD __stdcall MEMORY[0x41171C]();
// attributes: thunk
int __stdcall MEMORY[0x411724](
        LCID Locale,
        DWORD dwFlags,
        const SYSTEMTIME *lpDate,
        LPCWSTR lpFormat,
        LPWSTR lpDateStr,
        int cchDate);
// attributes: thunk
BOOL __stdcall MEMORY[0x41172C](
        LPCWSTR lpRootPathName,
        LPDWORD lpSectorsPerCluster,
        LPDWORD lpBytesPerSector,
        LPDWORD lpNumberOfFreeClusters,
        LPDWORD lpTotalNumberOfClusters);
// attributes: thunk
BOOL __stdcall MEMORY[0x411734](HANDLE hThread, LPDWORD lpExitCode);
// attributes: thunk
DWORD __stdcall MEMORY[0x41173C](LPCWSTR lpFileName);
// attributes: thunk
DWORD __stdcall MEMORY[0x411744](HANDLE hFile, LPDWORD lpFileSizeHigh);
// attributes: thunk
DWORD __stdcall MEMORY[0x41174C](LPCWSTR lpFileName, DWORD nBufferLength, LPWSTR lpBuffer, LPWSTR *lpFilePart);
// attributes: thunk
DWORD __stdcall MEMORY[0x411754]();
// attributes: thunk
void __stdcall MEMORY[0x41175C](LPSYSTEMTIME lpSystemTime);
// attributes: thunk
int __stdcall MEMORY[0x411764](LCID Locale, LCTYPE LCType, LPWSTR lpLCData, int cchData);
// attributes: thunk
int __stdcall MEMORY[0x41176C](LCID Locale, LCTYPE LCType, LPWSTR lpLCData, int cchData);
// attributes: thunk
DWORD __stdcall MEMORY[0x411774](HMODULE hModule, LPWSTR lpFilename, DWORD nSize);
// attributes: thunk
HMODULE __stdcall MEMORY[0x41177C](LPCWSTR lpModuleName);
// attributes: thunk
FARPROC __stdcall MEMORY[0x411784](HMODULE hModule, LPCSTR lpProcName);
FARPROC __stdcall sub_41178C(HMODULE hModule, LPCSTR lpProcName);
// attributes: thunk
HANDLE __stdcall MEMORY[0x411800]();
// attributes: thunk
HANDLE __stdcall MEMORY[0x411808](DWORD nStdHandle);
// attributes: thunk
BOOL __stdcall GetSystemTimes(PFILETIME lpIdleTime, PFILETIME lpKernelTime, PFILETIME lpUserTime);
__int32 __usercall sub_411818@<eax>(__int32 a1@<eax>);
// attributes: thunk
void __stdcall GetNativeSystemInfo(LPSYSTEM_INFO lpSystemInfo);
// attributes: thunk
DWORD __stdcall MEMORY[0x411830](DWORD nBufferLength, LPWSTR lpBuffer);
// attributes: thunk
LCID __stdcall MEMORY[0x411838]();
// attributes: thunk
int __stdcall GetThreadPriority(HANDLE hThread);
// attributes: thunk
DWORD __stdcall MEMORY[0x411848]();
__int32 __usercall sub_411850@<eax>(__int32 a1@<eax>);
// attributes: thunk
LCID __stdcall LocaleNameToLCID(LPCWSTR lpName, DWORD dwFlags);
// attributes: thunk
DWORD __stdcall MEMORY[0x411868]();
// attributes: thunk
BOOL __stdcall MEMORY[0x411870](LPOSVERSIONINFOW lpVersionInformation);
// attributes: thunk
BOOL __stdcall GetVersionExW_0(LPOSVERSIONINFOW lpVersionInformation);
// attributes: thunk
ATOM __stdcall MEMORY[0x411880](LPCWSTR lpString);
// attributes: thunk
HGLOBAL __stdcall MEMORY[0x411888](UINT uFlags, SIZE_T dwBytes);
// attributes: thunk
ATOM __stdcall MEMORY[0x411890](ATOM nAtom);
// attributes: thunk
ATOM __stdcall MEMORY[0x411898](LPCWSTR lpString);
// attributes: thunk
HGLOBAL __stdcall MEMORY[0x4118A0](HGLOBAL hMem);
// attributes: thunk
LPVOID __stdcall MEMORY[0x4118A8](HGLOBAL hMem);
// attributes: thunk
BOOL __stdcall MEMORY[0x4118B0](HGLOBAL hMem);
// attributes: thunk
LPVOID __stdcall MEMORY[0x4118B8](HANDLE hHeap, DWORD dwFlags, SIZE_T dwBytes);
// attributes: thunk
HANDLE __stdcall HeapCreate(DWORD flOptions, SIZE_T dwInitialSize, SIZE_T dwMaximumSize);
// attributes: thunk
BOOL __stdcall HeapDestroy(HANDLE hHeap);
// attributes: thunk
BOOL __stdcall HeapFree(HANDLE hHeap, DWORD dwFlags, LPVOID lpMem);
// attributes: thunk
SIZE_T __stdcall HeapSize(HANDLE hHeap, DWORD dwFlags, LPCVOID lpMem);
// attributes: thunk
void __stdcall InitializeCriticalSection_0(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
BOOL __stdcall IsBadReadPtr(const void *lp, UINT_PTR ucb);
// attributes: thunk
BOOL __stdcall IsValidLocale_0(LCID Locale, DWORD dwFlags);
// attributes: thunk
void __stdcall LeaveCriticalSection_0(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
HMODULE __stdcall LoadLibraryW(LPCWSTR lpLibFileName);
// attributes: thunk
HGLOBAL __stdcall LoadResource(HMODULE hModule, HRSRC hResInfo);
// attributes: thunk
HLOCAL __stdcall LocalFree_0(HLOCAL hMem);
// attributes: thunk
LPVOID __stdcall LockResource(HGLOBAL hResData);
// attributes: thunk
int __stdcall MulDiv(int nNumber, int nNumerator, int nDenominator);
// attributes: thunk
BOOL __stdcall IsDebuggerPresent();
// attributes: thunk
void __stdcall RaiseException_1(
        DWORD dwExceptionCode,
        DWORD dwExceptionFlags,
        DWORD nNumberOfArguments,
        const ULONG_PTR *lpArguments);
// attributes: thunk
BOOL __stdcall ReadFile(
        HANDLE hFile,
        LPVOID lpBuffer,
        DWORD nNumberOfBytesToRead,
        LPDWORD lpNumberOfBytesRead,
        LPOVERLAPPED lpOverlapped);
// attributes: thunk
BOOL __stdcall ResetEvent(HANDLE hEvent);
// attributes: thunk
DWORD __stdcall ResumeThread(HANDLE hThread);
// attributes: thunk
BOOL __stdcall SetEndOfFile(HANDLE hFile);
// attributes: thunk
UINT __stdcall SetErrorMode(UINT uMode);
// attributes: thunk
BOOL __stdcall SetEvent(HANDLE hEvent);
// attributes: thunk
DWORD __stdcall SetFilePointer(HANDLE hFile, LONG lDistanceToMove, PLONG lpDistanceToMoveHigh, DWORD dwMoveMethod);
// attributes: thunk
void __stdcall SetLastError(DWORD dwErrCode);
// attributes: thunk
BOOL __stdcall SetThreadLocale_0(LCID Locale);
// attributes: thunk
BOOL __stdcall SetThreadPriority(HANDLE hThread, int nPriority);
// attributes: thunk
DWORD __stdcall MEMORY[0x411988](HMODULE hModule, HRSRC hResInfo);
// attributes: thunk
void __stdcall MEMORY[0x411990](DWORD dwMilliseconds);
// attributes: thunk
DWORD __stdcall MEMORY[0x411998](HANDLE hThread);
// attributes: thunk
BOOL __stdcall MEMORY[0x4119A0]();
// attributes: thunk
BOOL __stdcall TryEnterCriticalSection(LPCRITICAL_SECTION lpCriticalSection);
// attributes: thunk
BOOL __stdcall MEMORY[0x4119B0](LPOSVERSIONINFOEXW lpVersionInformation, DWORD dwTypeMask, DWORDLONG dwlConditionMask);
// attributes: thunk
ULONGLONG __stdcall MEMORY[0x4119B8](ULONGLONG ConditionMask, DWORD TypeMask, BYTE Condition);
// attributes: thunk
LPVOID __stdcall MEMORY[0x4119C0](LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect);
// attributes: thunk
BOOL __stdcall MEMORY[0x4119C8](LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType);
// attributes: thunk
BOOL __stdcall MEMORY[0x4119D0](LPVOID lpAddress, SIZE_T dwSize, DWORD flNewProtect, PDWORD lpflOldProtect);
// attributes: thunk
SIZE_T __stdcall MEMORY[0x4119D8](LPCVOID lpAddress, PMEMORY_BASIC_INFORMATION lpBuffer, SIZE_T dwLength);
// attributes: thunk
SIZE_T __stdcall MEMORY[0x4119E0](
        HANDLE hProcess,
        LPCVOID lpAddress,
        PMEMORY_BASIC_INFORMATION lpBuffer,
        SIZE_T dwLength);
// attributes: thunk
DWORD __stdcall MEMORY[0x4119E8](
        DWORD nCount,
        const HANDLE *lpHandles,
        BOOL bWaitAll,
        DWORD dwMilliseconds,
        BOOL bAlertable);
// attributes: thunk
DWORD __stdcall MEMORY[0x4119F0](HANDLE hHandle, DWORD dwMilliseconds);
// attributes: thunk
int __stdcall MEMORY[0x4119F8](
        UINT CodePage,
        DWORD dwFlags,
        LPCWCH lpWideCharStr,
        int cchWideChar,
        LPSTR lpMultiByteStr,
        int cbMultiByte,
        LPCCH lpDefaultChar,
        LPBOOL lpUsedDefaultChar);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A00](
        HANDLE hFile,
        LPCVOID lpBuffer,
        DWORD nNumberOfBytesToWrite,
        LPDWORD lpNumberOfBytesWritten,
        LPOVERLAPPED lpOverlapped);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A08](LPCWSTR lptstrFilename, DWORD dwHandle, DWORD dwLen, LPVOID lpData);
// attributes: thunk
DWORD __stdcall MEMORY[0x411A10](LPCWSTR lptstrFilename, LPDWORD lpdwHandle);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A18](LPCVOID pBlock, LPCWSTR lpSubBlock, LPVOID *lplpBuffer, PUINT puLen);
// attributes: thunk
int __stdcall AbortDoc(HDC hdc);
__int32 __usercall sub_411A38@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A48](
        HDC hdcDest,
        int xoriginDest,
        int yoriginDest,
        int wDest,
        int hDest,
        HDC hdcSrc,
        int xoriginSrc,
        int yoriginSrc,
        int wSrc,
        int hSrc,
        BLENDFUNCTION ftn);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A50](HDC hdc, int x, int y, DWORD r, FLOAT StartAngle, FLOAT SweepAngle);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A58](HDC hdc, int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A60](HDC hdc, int left, int top, int right, int bottom, int xr1, int yr1, int xr2, int yr2);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A68](HDC hdc, int x, int y, int cx, int cy, HDC hdcSrc, int x1, int y1, DWORD rop);
// attributes: thunk
BOOL __stdcall MEMORY[0x411A70](HDC hdc, int x1, int y1, int x2, int y2, int x3, int y3, int x4, int y4);
// attributes: thunk
HENHMETAFILE __stdcall MEMORY[0x411A78](HENHMETAFILE hEnh, LPCWSTR lpFileName);
// attributes: thunk
HBITMAP __stdcall MEMORY[0x411A80](int nWidth, int nHeight, UINT nPlanes, UINT nBitCount, const void *lpBits);
// attributes: thunk
HBRUSH __stdcall MEMORY[0x411A88](const LOGBRUSH *plbrush);
// attributes: thunk
HBITMAP __stdcall MEMORY[0x411A90](HDC hdc, int cx, int cy);
// attributes: thunk
HDC __stdcall MEMORY[0x411A98](HDC hdc);
// attributes: thunk
HDC __stdcall MEMORY[0x411AA0](LPCWSTR pwszDriver, LPCWSTR pwszDevice, LPCWSTR pszPort, const DEVMODEW *pdm);
// attributes: thunk
HBITMAP __stdcall MEMORY[0x411AA8](
        HDC hdc,
        const BITMAPINFO *pbmi,
        UINT usage,
        void **ppvBits,
        HANDLE hSection,
        DWORD offset);
// attributes: thunk
HBITMAP __stdcall MEMORY[0x411AB0](
        HDC hdc,
        const BITMAPINFOHEADER *pbmih,
        DWORD flInit,
        const void *pjBits,
        const BITMAPINFO *pbmi,
        UINT iUsage);
// attributes: thunk
HFONT __stdcall MEMORY[0x411AB8](const LOGFONTW *lplf);
// attributes: thunk
HPALETTE __stdcall MEMORY[0x411AC0](HDC hdc);
// attributes: thunk
HDC __stdcall MEMORY[0x411AC8](LPCWSTR pszDriver, LPCWSTR pszDevice, LPCWSTR pszPort, const DEVMODEW *pdm);
// attributes: thunk
HPALETTE __stdcall MEMORY[0x411AD0](const LOGPALETTE *plpal);
// attributes: thunk
HPEN __stdcall MEMORY[0x411AD8](const LOGPEN *plpen);
// attributes: thunk
HRGN __stdcall MEMORY[0x411AE0](int x1, int y1, int x2, int y2);
// attributes: thunk
HBRUSH __stdcall MEMORY[0x411AE8](COLORREF color);
// attributes: thunk
BOOL __stdcall MEMORY[0x411AF0](HDC hdc);
// attributes: thunk
BOOL __stdcall MEMORY[0x411AF8](HENHMETAFILE hmf);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B00](HGDIOBJ ho);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B08](HDC hdc, int left, int top, int right, int bottom);
// attributes: thunk
int __stdcall MEMORY[0x411B10](HDC hdc);
// attributes: thunk
int __stdcall MEMORY[0x411B18](HDC hdc);
// attributes: thunk
int __stdcall MEMORY[0x411B20](HDC hdc, LPLOGFONTW lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam, DWORD dwFlags);
// attributes: thunk
int __stdcall MEMORY[0x411B28](HDC hdc, LPCWSTR lpLogfont, FONTENUMPROCW lpProc, LPARAM lParam);
// attributes: thunk
int __stdcall MEMORY[0x411B30](HDC hdc, int left, int top, int right, int bottom);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B38](HDC hdc, int x, int y, COLORREF color, UINT type);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B40](
        HDC hdc,
        int x,
        int y,
        UINT options,
        const RECT *lprect,
        LPCWSTR lpString,
        UINT c,
        const INT *lpDx);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B48](HDC hdc, HRGN hrgn, HBRUSH hbr, int w, int h);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B50]();
// attributes: thunk
LONG __stdcall GetBitmapBits(HBITMAP hbit, LONG cb, LPVOID lpvBits);
// attributes: thunk
BOOL __stdcall MEMORY[0x411B60](HDC hdc, LPPOINT lppt);
// attributes: thunk
int __stdcall GetClipBox(HDC hdc, LPRECT lprect);
// attributes: thunk
BOOL __stdcall GetCurrentPositionEx(HDC hdc, LPPOINT lppt);
// attributes: thunk
UINT __stdcall MEMORY[0x411B78](HDC hdc, UINT iStart, UINT cEntries, RGBQUAD *prgbq);
// attributes: thunk
int __stdcall MEMORY[0x411B80](
        HDC hdc,
        HBITMAP hbm,
        UINT start,
        UINT cLines,
        LPVOID lpvBits,
        LPBITMAPINFO lpbmi,
        UINT usage);
// attributes: thunk
int __stdcall MEMORY[0x411B88](HDC hdc, int index);
// attributes: thunk
UINT __stdcall MEMORY[0x411B90](HENHMETAFILE hEMF, UINT nSize, LPBYTE lpData);
// attributes: thunk
UINT __stdcall GetEnhMetaFileDescriptionW(HENHMETAFILE hemf, UINT cchBuffer, LPWSTR lpDescription);
// attributes: thunk
UINT __stdcall MEMORY[0x411BA0](HENHMETAFILE hemf, UINT nSize, LPENHMETAHEADER lpEnhMetaHeader);
// attributes: thunk
UINT __stdcall GetEnhMetaFilePaletteEntries(HENHMETAFILE hemf, UINT nNumEntries, LPPALETTEENTRY lpPaletteEntries);
// attributes: thunk
int __stdcall MEMORY[0x411BB0](HANDLE h, int c, LPVOID pv);
// attributes: thunk
UINT __stdcall MEMORY[0x411BB8](HPALETTE hpal, UINT iStart, UINT cEntries, LPPALETTEENTRY pPalEntries);
// attributes: thunk
COLORREF __stdcall GetPixel(HDC hdc, int x, int y);
// attributes: thunk
int __stdcall MEMORY[0x411BC8](HRGN hrgn, LPRECT lprc);
// attributes: thunk
HGDIOBJ __stdcall MEMORY[0x411BD0](int i);
// attributes: thunk
UINT __stdcall MEMORY[0x411BD8](HDC hdc, UINT iStart, UINT cEntries, LPPALETTEENTRY pPalEntries);
// attributes: thunk
BOOL __stdcall GetTextExtentPoint32W(HDC hdc, LPCWSTR lpString, int c, LPSIZE psizl);
// attributes: thunk
BOOL __stdcall MEMORY[0x411BE8](HDC hdc, LPCWSTR lpString, int c, LPSIZE lpsz);
// attributes: thunk
BOOL __stdcall MEMORY[0x411BF0](HDC hdc, LPTEXTMETRICW lptm);
// attributes: thunk
UINT __stdcall MEMORY[0x411BF8](HENHMETAFILE hemf, UINT cbData16, LPBYTE pData16, INT iMapMode, HDC hdcRef);
// attributes: thunk
BOOL __stdcall MEMORY[0x411C00](HDC hdc, LPPOINT lppoint);
int __usercall sub_411C08@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall MEMORY[0x411C18](HDC hdc, PTRIVERTEX pVertex, ULONG nVertex, PVOID pMesh, ULONG nMesh, ULONG ulMode);
// attributes: thunk
int __stdcall IntersectClipRect(HDC hdc, int left, int top, int right, int bottom);
// attributes: thunk
BOOL __stdcall LineTo(HDC hdc, int x, int y);
// attributes: thunk
BOOL __stdcall MaskBlt(
        HDC hdcDest,
        int xDest,
        int yDest,
        int width,
        int height,
        HDC hdcSrc,
        int xSrc,
        int ySrc,
        HBITMAP hbmMask,
        int xMask,
        int yMask,
        DWORD rop);
// attributes: thunk
BOOL __stdcall MoveToEx(HDC hdc, int x, int y, LPPOINT lppt);
// attributes: thunk
BOOL __stdcall PatBlt(HDC hdc, int x, int y, int w, int h, DWORD rop);
// attributes: thunk
BOOL __stdcall Pie(HDC hdc, int left, int top, int right, int bottom, int xr1, int yr1, int xr2, int yr2);
// attributes: thunk
BOOL __stdcall PlayEnhMetaFile(HDC hdc, HENHMETAFILE hmf, const RECT *lprect);
// attributes: thunk
BOOL __stdcall PolyBezier(HDC hdc, const POINT *apt, DWORD cpt);
// attributes: thunk
BOOL __stdcall PolyBezierTo(HDC hdc, const POINT *apt, DWORD cpt);
// attributes: thunk
BOOL __stdcall Polygon(HDC hdc, const POINT *apt, int cpt);
// attributes: thunk
BOOL __stdcall Polyline(HDC hdc, const POINT *apt, int cpt);
// attributes: thunk
UINT __stdcall RealizePalette(HDC hdc);
// attributes: thunk
BOOL __stdcall RectVisible(HDC hdc, const RECT *lprect);
// attributes: thunk
BOOL __stdcall Rectangle(HDC hdc, int left, int top, int right, int bottom);
// attributes: thunk
BOOL __stdcall RestoreDC(HDC hdc, int nSavedDC);
// attributes: thunk
BOOL __stdcall RoundRect(HDC hdc, int left, int top, int right, int bottom, int width, int height);
// attributes: thunk
int __stdcall SaveDC(HDC hdc);
// attributes: thunk
HGDIOBJ __stdcall SelectObject(HDC hdc, HGDIOBJ h);
// attributes: thunk
HPALETTE __stdcall SelectPalette(HDC hdc, HPALETTE hPal, BOOL bForceBkgd);
// attributes: thunk
int __stdcall SetAbortProc(HDC hdc, ABORTPROC proc);
// attributes: thunk
COLORREF __stdcall SetBkColor(HDC hdc, COLORREF color);
// attributes: thunk
int __stdcall SetBkMode(HDC hdc, int mode);
// attributes: thunk
BOOL __stdcall SetBrushOrgEx(HDC hdc, int x, int y, LPPOINT lppt);
// attributes: thunk
UINT __stdcall SetDIBColorTable(HDC hdc, UINT iStart, UINT cEntries, const RGBQUAD *prgbq);
// attributes: thunk
int __stdcall SetDIBits(
        HDC hdc,
        HBITMAP hbm,
        UINT start,
        UINT cLines,
        const void *lpBits,
        const BITMAPINFO *lpbmi,
        UINT ColorUse);
// attributes: thunk
HENHMETAFILE __stdcall SetEnhMetaFileBits(UINT nSize, const BYTE *pb);
// attributes: thunk
COLORREF __stdcall SetPixel(HDC hdc, int x, int y, COLORREF color);
// attributes: thunk
int __stdcall SetROP2(HDC hdc, int rop2);
// attributes: thunk
int __stdcall SetStretchBltMode(HDC hdc, int mode);
// attributes: thunk
COLORREF __stdcall SetTextColor(HDC hdc, COLORREF color);
// attributes: thunk
BOOL __stdcall SetViewportOrgEx(HDC hdc, int x, int y, LPPOINT lppt);
// attributes: thunk
HENHMETAFILE __stdcall SetWinMetaFileBits(UINT nSize, const BYTE *lpMeta16Data, HDC hdcRef, const METAFILEPICT *lpMFP);
// attributes: thunk
BOOL __stdcall SetWindowOrgEx(HDC hdc, int x, int y, LPPOINT lppt);
// attributes: thunk
int __stdcall MEMORY[0x411D28](HDC hdc, const DOCINFOW *lpdi);
// attributes: thunk
int __stdcall MEMORY[0x411D30](HDC hdc);
// attributes: thunk
BOOL __stdcall MEMORY[0x411D38](
        HDC hdcDest,
        int xDest,
        int yDest,
        int wDest,
        int hDest,
        HDC hdcSrc,
        int xSrc,
        int ySrc,
        int wSrc,
        int hSrc,
        DWORD rop);
// attributes: thunk
int __stdcall MEMORY[0x411D40](
        HDC hdc,
        int xDest,
        int yDest,
        int DestWidth,
        int DestHeight,
        int xSrc,
        int ySrc,
        int SrcWidth,
        int SrcHeight,
        const void *lpBits,
        const BITMAPINFO *lpbmi,
        UINT iUsage,
        DWORD rop);
// attributes: thunk
BOOL __stdcall UnrealizeObject(HGDIOBJ h);
// attributes: thunk
HKL __stdcall MEMORY[0x411D50](HKL hkl, UINT Flags);
// attributes: thunk
BOOL __stdcall AdjustWindowRectEx(LPRECT lpRect, DWORD dwStyle, BOOL bMenu, DWORD dwExStyle);
// attributes: thunk
HDC __stdcall MEMORY[0x411D60](HWND hWnd, LPPAINTSTRUCT lpPaint);
// attributes: thunk
LRESULT __stdcall MEMORY[0x411D78](HHOOK hhk, int nCode, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall MEMORY[0x411D80](WNDPROC lpPrevWndFunc, HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LPWSTR __stdcall MEMORY[0x411D88](LPWSTR lpsz);
// attributes: thunk
DWORD __stdcall MEMORY[0x411D90](LPWSTR lpsz, DWORD cchLength);
// attributes: thunk
LPWSTR __stdcall MEMORY[0x411D98](LPCWSTR lpsz);
// attributes: thunk
LPWSTR __stdcall MEMORY[0x411DA0](LPWSTR lpsz);
// attributes: thunk
DWORD __stdcall MEMORY[0x411DA8](LPWSTR lpsz, DWORD cchLength);
// attributes: thunk
DWORD __stdcall CheckMenuItem(HMENU hMenu, UINT uIDCheckItem, UINT uCheck);
// attributes: thunk
BOOL __stdcall MEMORY[0x411DB8](HWND hWnd, LPPOINT lpPoint);
// attributes: thunk
BOOL __stdcall MEMORY[0x411DC0]();
// attributes: thunk
HICON __stdcall CopyIcon(HICON hIcon);
// attributes: thunk
HANDLE __stdcall MEMORY[0x411DD0](HANDLE h, UINT type, int cx, int cy, UINT flags);
// attributes: thunk
HACCEL __stdcall MEMORY[0x411DD8](LPACCEL paccel, int cAccel);
// attributes: thunk
HICON __stdcall CreateIcon(
        HINSTANCE hInstance,
        int nWidth,
        int nHeight,
        BYTE cPlanes,
        BYTE cBitsPixel,
        const BYTE *lpbANDbits,
        const BYTE *lpbXORbits);
// attributes: thunk
HMENU __stdcall CreateMenu();
// attributes: thunk
HMENU __stdcall CreatePopupMenu();
// attributes: thunk
LRESULT __stdcall DefFrameProcW(HWND hWnd, HWND hWndMDIClient, UINT uMsg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall DefMDIChildProcW(HWND hWnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall DefWindowProcW(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
BOOL __stdcall DeleteMenu(HMENU hMenu, UINT uPosition, UINT uFlags);
// attributes: thunk
BOOL __stdcall DestroyCursor(HCURSOR hCursor);
// attributes: thunk
BOOL __stdcall DestroyIcon(HICON hIcon);
// attributes: thunk
BOOL __stdcall DestroyMenu(HMENU hMenu);
// attributes: thunk
BOOL __stdcall DestroyWindow(HWND hWnd);
// attributes: thunk
LRESULT __stdcall DispatchMessageW(const MSG *lpMsg);
// attributes: thunk
LRESULT __stdcall DispatchMessageA(const MSG *lpMsg);
// attributes: thunk
LRESULT __stdcall DispatchMessageW_0(const MSG *lpMsg);
// attributes: thunk
BOOL __stdcall DrawEdge(HDC hdc, LPRECT qrc, UINT edge, UINT grfFlags);
// attributes: thunk
BOOL __stdcall DrawFocusRect(HDC hDC, const RECT *lprc);
// attributes: thunk
BOOL __stdcall DrawFrameControl(HDC a1, LPRECT a2, UINT a3, UINT a4);
// attributes: thunk
BOOL __stdcall DrawIcon(HDC hDC, int X, int Y, HICON hIcon);
// attributes: thunk
BOOL __stdcall DrawIconEx(
        HDC hdc,
        int xLeft,
        int yTop,
        HICON hIcon,
        int cxWidth,
        int cyWidth,
        UINT istepIfAniCur,
        HBRUSH hbrFlickerFreeDraw,
        UINT diFlags);
// attributes: thunk
BOOL __stdcall DrawMenuBar(HWND hWnd);
// attributes: thunk
int __stdcall DrawTextW(HDC hdc, LPCWSTR lpchText, int cchText, LPRECT lprc, UINT format);
// attributes: thunk
int __stdcall DrawTextW_0(HDC hdc, LPCWSTR lpchText, int cchText, LPRECT lprc, UINT format);
// attributes: thunk
int __stdcall DrawTextExW(HDC hdc, LPWSTR lpchText, int cchText, LPRECT lprc, UINT format, LPDRAWTEXTPARAMS lpdtp);
// attributes: thunk
BOOL __stdcall EmptyClipboard();
// attributes: thunk
BOOL __stdcall EnableMenuItem(HMENU hMenu, UINT uIDEnableItem, UINT uEnable);
// attributes: thunk
BOOL __stdcall EnableScrollBar(HWND hWnd, UINT wSBflags, UINT wArrows);
// attributes: thunk
BOOL __stdcall EnableWindow(HWND hWnd, BOOL bEnable);
// attributes: thunk
BOOL __stdcall EndMenu();
// attributes: thunk
BOOL __stdcall EndPaint(HWND hWnd, const PAINTSTRUCT *lpPaint);
// attributes: thunk
BOOL __stdcall EnumChildWindows(HWND hWndParent, WNDENUMPROC lpEnumFunc, LPARAM lParam);
// attributes: thunk
BOOL __stdcall EnumThreadWindows(DWORD dwThreadId, WNDENUMPROC lpfn, LPARAM lParam);
// attributes: thunk
BOOL __stdcall EnumWindows(WNDENUMPROC lpEnumFunc, LPARAM lParam);
// attributes: thunk
int __stdcall FillRect(HDC hDC, const RECT *lprc, HBRUSH hbr);
// attributes: thunk
HWND __stdcall FindWindowW(LPCWSTR lpClassName, LPCWSTR lpWindowName);
// attributes: thunk
HWND __stdcall FindWindowExW(HWND hWndParent, HWND hWndChildAfter, LPCWSTR lpszClass, LPCWSTR lpszWindow);
// attributes: thunk
int __stdcall FrameRect(HDC hDC, const RECT *lprc, HBRUSH hbr);
// attributes: thunk
HWND __stdcall GetActiveWindow();
// attributes: thunk
HWND __stdcall GetCapture();
// attributes: thunk
BOOL __stdcall GetClassInfoW(HINSTANCE hInstance, LPCWSTR lpClassName, LPWNDCLASSW lpWndClass);
// attributes: thunk
BOOL __stdcall GetClassInfoExW(HINSTANCE hInstance, LPCWSTR lpszClass, LPWNDCLASSEXW lpwcx);
// attributes: thunk
int __stdcall GetClassNameW(HWND hWnd, LPWSTR lpClassName, int nMaxCount);
// attributes: thunk
BOOL __stdcall GetClientRect(HWND hWnd, LPRECT lpRect);
// attributes: thunk
HANDLE __stdcall GetClipboardData(UINT uFormat);
// attributes: thunk
HCURSOR __stdcall GetCursor();
// attributes: thunk
BOOL __stdcall GetCursorPos(LPPOINT lpPoint);
// attributes: thunk
HDC __stdcall GetDC(HWND hWnd);
// attributes: thunk
HDC __stdcall GetDCEx(HWND hWnd, HRGN hrgnClip, DWORD flags);
// attributes: thunk
HWND __stdcall GetDesktopWindow();
// attributes: thunk
int __stdcall GetDlgCtrlID(HWND hWnd);
// attributes: thunk
HWND __stdcall GetFocus();
// attributes: thunk
HWND __stdcall GetForegroundWindow();
// attributes: thunk
BOOL __stdcall GetIconInfo(HICON hIcon, PICONINFO piconinfo);
// attributes: thunk
int __stdcall GetKeyNameTextW(LONG lParam, LPWSTR lpString, int cchSize);
// attributes: thunk
SHORT __stdcall GetKeyState(int nVirtKey);
// attributes: thunk
HKL __stdcall GetKeyboardLayout(DWORD idThread);
// attributes: thunk
int __stdcall GetKeyboardLayoutList(int nBuff, HKL *lpList);
// attributes: thunk
BOOL __stdcall GetKeyboardLayoutNameW(LPWSTR pwszKLID);
// attributes: thunk
BOOL __stdcall GetKeyboardState(PBYTE lpKeyState);
// attributes: thunk
HWND __stdcall GetLastActivePopup(HWND hWnd);
// attributes: thunk
HMENU __stdcall GetMenu(HWND hWnd);
// attributes: thunk
int __stdcall GetMenuItemCount(HMENU hMenu);
// attributes: thunk
UINT __stdcall GetMenuItemID(HMENU hMenu, int nPos);
// attributes: thunk
BOOL __stdcall GetMenuItemInfoW(HMENU hmenu, UINT item, BOOL fByPosition, LPMENUITEMINFOW lpmii);
// attributes: thunk
UINT __stdcall GetMenuState(HMENU hMenu, UINT uId, UINT uFlags);
// attributes: thunk
int __stdcall GetMenuStringW(HMENU hMenu, UINT uIDItem, LPWSTR lpString, int cchMax, UINT flags);
// attributes: thunk
LPARAM __stdcall GetMessageExtraInfo();
// attributes: thunk
DWORD __stdcall GetMessagePos();
// attributes: thunk
HWND __stdcall GetWindow(HWND hWnd, UINT uCmd);
// attributes: thunk
HWND __stdcall GetParent(HWND hWnd);
// attributes: thunk
HANDLE __stdcall GetPropW(HWND hWnd, LPCWSTR lpString);
// attributes: thunk
BOOL __stdcall GetScrollInfo(HWND hwnd, int nBar, LPSCROLLINFO lpsi);
// attributes: thunk
int __stdcall GetScrollPos(HWND hWnd, int nBar);
// attributes: thunk
BOOL __stdcall GetScrollRange(HWND hWnd, int nBar, LPINT lpMinPos, LPINT lpMaxPos);
// attributes: thunk
HMENU __stdcall GetSubMenu(HMENU hMenu, int nPos);
// attributes: thunk
DWORD __stdcall GetSysColor(int nIndex);
// attributes: thunk
HBRUSH __stdcall GetSysColorBrush(int nIndex);
// attributes: thunk
HMENU __stdcall GetSystemMenu(HWND hWnd, BOOL bRevert);
// attributes: thunk
int __stdcall GetSystemMetrics(int nIndex);
// attributes: thunk
HWND __stdcall GetTopWindow(HWND hWnd);
// attributes: thunk
HWND __stdcall GetWindow(HWND hWnd, UINT uCmd);
// attributes: thunk
HDC __stdcall GetWindowDC(HWND hWnd);
LONG __usercall sub_412068@<eax>(HWND a1@<eax>, int a2@<edx>);
// attributes: thunk
BOOL __stdcall GetWindowPlacement(HWND hWnd, WINDOWPLACEMENT *lpwndpl);
// attributes: thunk
BOOL __stdcall GetWindowRect(HWND hWnd, LPRECT lpRect);
// attributes: thunk
int __stdcall GetWindowTextW(HWND hWnd, LPWSTR lpString, int nMaxCount);
// attributes: thunk
DWORD __stdcall GetWindowThreadProcessId(HWND hWnd, LPDWORD lpdwProcessId);
// attributes: thunk
DWORD __stdcall GetWindowThreadProcessId(HWND hWnd, LPDWORD lpdwProcessId);
// attributes: thunk
BOOL __stdcall HideCaret(HWND hWnd);
// attributes: thunk
BOOL __stdcall InsertMenuW(HMENU hMenu, UINT uPosition, UINT uFlags, UINT_PTR uIDNewItem, LPCWSTR lpNewItem);
// attributes: thunk
BOOL __stdcall InsertMenuItemW(HMENU hmenu, UINT item, BOOL fByPosition, LPCMENUITEMINFOW lpmi);
// attributes: thunk
BOOL __stdcall InvalidateRect(HWND hWnd, const RECT *lpRect, BOOL bErase);
// attributes: thunk
BOOL __stdcall InvalidateRect(HWND hWnd, const RECT *lpRect, BOOL bErase);
// attributes: thunk
BOOL __stdcall IsChild(HWND hWndParent, HWND hWnd);
// attributes: thunk
BOOL __stdcall IsDialogMessageA(HWND hDlg, LPMSG lpMsg);
// attributes: thunk
BOOL __stdcall IsDialogMessageW(HWND hDlg, LPMSG lpMsg);
// attributes: thunk
BOOL __stdcall IsIconic(HWND hWnd);
// attributes: thunk
BOOL __stdcall IsWindow(HWND hWnd);
// attributes: thunk
BOOL __stdcall IsWindowEnabled(HWND hWnd);
// attributes: thunk
BOOL __stdcall IsWindowUnicode(HWND hWnd);
// attributes: thunk
BOOL __stdcall IsWindowVisible(HWND hWnd);
// attributes: thunk
BOOL __stdcall IsZoomed(HWND hWnd);
// attributes: thunk
BOOL __stdcall KillTimer(HWND hWnd, UINT_PTR uIDEvent);
// attributes: thunk
HBITMAP __stdcall LoadBitmapW(HINSTANCE hInstance, LPCWSTR lpBitmapName);
// attributes: thunk
HCURSOR __stdcall LoadCursorW(HINSTANCE hInstance, LPCWSTR lpCursorName);
// attributes: thunk
HICON __stdcall LoadIconW(HINSTANCE hInstance, LPCWSTR lpIconName);
// attributes: thunk
HKL __stdcall LoadKeyboardLayoutW(LPCWSTR pwszKLID, UINT Flags);
// attributes: thunk
int __stdcall LoadStringW_0(HINSTANCE hInstance, UINT uID, LPWSTR lpBuffer, int cchBufferMax);
// attributes: thunk
UINT __stdcall MapVirtualKeyW(UINT uCode, UINT uMapType);
// attributes: thunk
int __stdcall MapWindowPoints(HWND hWndFrom, HWND hWndTo, LPPOINT lpPoints, UINT cPoints);
// attributes: thunk
BOOL __stdcall MessageBeep(UINT uType);
// attributes: thunk
int __stdcall MessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, UINT uType);
// attributes: thunk
DWORD __stdcall MsgWaitForMultipleObjects(
        DWORD nCount,
        const HANDLE *pHandles,
        BOOL fWaitAll,
        DWORD dwMilliseconds,
        DWORD dwWakeMask);
// attributes: thunk
DWORD __stdcall MsgWaitForMultipleObjectsEx(
        DWORD nCount,
        const HANDLE *pHandles,
        DWORD dwMilliseconds,
        DWORD dwWakeMask,
        DWORD dwFlags);
// attributes: thunk
BOOL __stdcall OpenClipboard(HWND hWndNewOwner);
// attributes: thunk
BOOL __stdcall PeekMessageW(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg);
// attributes: thunk
BOOL __stdcall PeekMessageA(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg);
// attributes: thunk
BOOL __stdcall PeekMessageW_0(LPMSG lpMsg, HWND hWnd, UINT wMsgFilterMin, UINT wMsgFilterMax, UINT wRemoveMsg);
// attributes: thunk
BOOL __stdcall PostMessageW(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
void __stdcall PostQuitMessage(int nExitCode);
// attributes: thunk
BOOL __stdcall RedrawWindow(HWND hWnd, const RECT *lprcUpdate, HRGN hrgnUpdate, UINT flags);
// attributes: thunk
ATOM __stdcall RegisterClassW(const WNDCLASSW *lpWndClass);
// attributes: thunk
UINT __stdcall RegisterClipboardFormatW(LPCWSTR lpszFormat);
// attributes: thunk
UINT __stdcall RegisterWindowMessageW(LPCWSTR lpString);
// attributes: thunk
BOOL __stdcall ReleaseCapture();
// attributes: thunk
int __stdcall ReleaseDC(HWND hWnd, HDC hDC);
// attributes: thunk
BOOL __stdcall RemoveMenu(HMENU hMenu, UINT uPosition, UINT uFlags);
// attributes: thunk
HANDLE __stdcall RemovePropW(HWND hWnd, LPCWSTR lpString);
// attributes: thunk
BOOL __stdcall ScreenToClient(HWND hWnd, LPPOINT lpPoint);
__int32 __usercall sub_4121E0@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall PhysicalToLogicalPoint(HWND hWnd, LPPOINT lpPoint);
// attributes: thunk
BOOL __stdcall ScrollWindow(HWND hWnd, int XAmount, int YAmount, const RECT *lpRect, const RECT *lpClipRect);
// attributes: thunk
LRESULT __stdcall SendMessageW(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall SendMessageW_0(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall SendMessageA(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
LRESULT __stdcall SendMessageW_0(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
// attributes: thunk
HWND __stdcall SetActiveWindow(HWND hWnd);
// attributes: thunk
HWND __stdcall SetCapture(HWND hWnd);
// attributes: thunk
HANDLE __stdcall SetClipboardData(UINT uFormat, HANDLE hMem);
// attributes: thunk
HCURSOR __stdcall SetCursor(HCURSOR hCursor);
// attributes: thunk
BOOL __stdcall SetCursorPos(int X, int Y);
// attributes: thunk
HWND __stdcall SetFocus(HWND hWnd);
// attributes: thunk
BOOL __stdcall SetForegroundWindow(HWND hWnd);
// attributes: thunk
BOOL __stdcall SetMenu(HWND hWnd, HMENU hMenu);
// attributes: thunk
BOOL __stdcall SetMenuItemInfoW(HMENU hmenu, UINT item, BOOL fByPositon, LPCMENUITEMINFOW lpmii);
// attributes: thunk
HWND __stdcall SetParent(HWND hWndChild, HWND hWndNewParent);
// attributes: thunk
BOOL __stdcall SetPropW(HWND hWnd, LPCWSTR lpString, HANDLE hData);
// attributes: thunk
BOOL __stdcall SetRect(LPRECT lprc, int xLeft, int yTop, int xRight, int yBottom);
// attributes: thunk
int __stdcall SetScrollInfo(HWND hwnd, int nBar, LPCSCROLLINFO lpsi, BOOL redraw);
// attributes: thunk
int __stdcall SetScrollPos(HWND hWnd, int nBar, int nPos, BOOL bRedraw);
// attributes: thunk
BOOL __stdcall SetScrollRange(HWND hWnd, int nBar, int nMinPos, int nMaxPos, BOOL bRedraw);
// attributes: thunk
UINT_PTR __stdcall SetTimer(HWND hWnd, UINT_PTR nIDEvent, UINT uElapse, TIMERPROC lpTimerFunc);
// attributes: thunk
BOOL __stdcall SetWindowPlacement(HWND hWnd, const WINDOWPLACEMENT *lpwndpl);
// attributes: thunk
BOOL __stdcall SetWindowPos(HWND hWnd, HWND hWndInsertAfter, int X, int Y, int cx, int cy, UINT uFlags);
// attributes: thunk
BOOL __stdcall SetWindowTextW(HWND hWnd, LPCWSTR lpString);
// attributes: thunk
HHOOK __stdcall SetWindowsHookExW(int idHook, HOOKPROC lpfn, HINSTANCE hmod, DWORD dwThreadId);
// attributes: thunk
int __stdcall sub_4122C0(HWND hWnd, HRGN hRgn, BOOL bRedraw);
// attributes: thunk
BOOL __stdcall ShowCaret(HWND hWnd);
// attributes: thunk
BOOL __stdcall ShowOwnedPopups(HWND hWnd, BOOL fShow);
// attributes: thunk
BOOL __stdcall ShowScrollBar(HWND hWnd, int wBar, BOOL bShow);
// attributes: thunk
BOOL __stdcall ShowWindow(HWND hWnd, int nCmdShow);
// attributes: thunk
BOOL __stdcall SystemParametersInfoW(UINT uiAction, UINT uiParam, PVOID pvParam, UINT fWinIni);
// attributes: thunk
BOOL __stdcall SystemParametersInfoW_0(UINT uiAction, UINT uiParam, PVOID pvParam, UINT fWinIni);
// attributes: thunk
BOOL __stdcall SystemParametersInfoW_0(UINT uiAction, UINT uiParam, PVOID pvParam, UINT fWinIni);
// attributes: thunk
BOOL __stdcall TrackPopupMenu(HMENU hMenu, UINT uFlags, int x, int y, int nReserved, HWND hWnd, const RECT *prcRect);
// attributes: thunk
BOOL __stdcall TranslateMDISysAccel(HWND hWndClient, LPMSG lpMsg);
// attributes: thunk
BOOL __stdcall TranslateMessage(const MSG *lpMsg);
// attributes: thunk
BOOL __stdcall UnhookWindowsHookEx(HHOOK hhk);
// attributes: thunk
BOOL __stdcall UnregisterClassW(LPCWSTR lpClassName, HINSTANCE hInstance);
// attributes: thunk
BOOL __stdcall UpdateWindow(HWND hWnd);
// attributes: thunk
BOOL __stdcall WaitMessage();
// attributes: thunk
HWND __stdcall WindowFromPoint(POINT Point);
__int32 __usercall sub_412350@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall WTSRegisterSessionNotification(HWND hWnd, DWORD dwFlags);
int __usercall sub_412368@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall WTSUnRegisterSessionNotification(HWND hWnd);
// attributes: thunk
HWND __stdcall CreateWindowExW(
        DWORD dwExStyle,
        LPCWSTR lpClassName,
        LPCWSTR lpWindowName,
        DWORD dwStyle,
        int X,
        int Y,
        int nWidth,
        int nHeight,
        HWND hWndParent,
        HMENU hMenu,
        HINSTANCE hInstance,
        LPVOID lpParam);
HWND __userpurge sub_412388@<eax>(
        DWORD a1@<eax>,
        const WCHAR *a2@<edx>,
        const WCHAR *a3@<ecx>,
        void *lpParam,
        HINSTANCE hInstance,
        HMENU hMenu,
        HWND hWndParent,
        int nHeight,
        int nWidth,
        int Y,
        int X,
        DWORD dwStyle);
HWND __userpurge sub_4123E0@<eax>(UINT *a1@<eax>, UINT *a2@<edx>, UINT *a3@<ecx>, LRESULT *a4, LRESULT *a5);
// attributes: thunk
LONG __stdcall GetWindowLongW(HWND hWnd, int nIndex);
// attributes: thunk
LONG __stdcall SetWindowLongW(HWND hWnd, int nIndex, LONG dwNewLong);
// attributes: thunk
DWORD __stdcall GetClassLongW(HWND hWnd, int nIndex);
// attributes: thunk
DWORD __stdcall SetClassLongW(HWND hWnd, int nIndex, LONG dwNewLong);
__int32 __usercall sub_412548@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall GetGestureInfo(HGESTUREINFO hGestureInfo, PGESTUREINFO pGestureInfo);
__int32 __usercall sub_412560@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall MEMORY[0x412570](HGESTUREINFO hGestureInfo);
int __usercall sub_412578@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall SetGestureConfig(HWND hwnd, DWORD dwReserved, UINT cIDs, PGESTURECONFIG pGestureConfig, UINT cbSize);
DWORD sub_412590();
int sub_4125CC();
int __usercall sub_4125E4@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall IsWow64Process(HANDLE hProcess, PBOOL Wow64Process);
BOOL sub_4125FC();
LRESULT __userpurge sub_4128D8@<eax>(WPARAM wParam@<ecx>, UINT Msg@<edx>, HWND a3@<eax>, int a4);
LRESULT __userpurge sub_412934@<eax>(WPARAM wParam@<ecx>, UINT Msg@<edx>, HWND a3@<eax>, LPARAM lParam);
// attributes: thunk
BOOL __stdcall Shell_NotifyIconW(DWORD dwMessage, PNOTIFYICONDATAW lpData);
// attributes: thunk
HINSTANCE __stdcall ShellExecuteW(
        HWND hwnd,
        LPCWSTR lpOperation,
        LPCWSTR lpFile,
        LPCWSTR lpParameters,
        LPCWSTR lpDirectory,
        INT nShowCmd);
DWORD sub_412AFC();
int sub_412B38();
void __userpurge nullsub_151(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
void nullsub_152();
int __userpurge nullsub_153@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_154();
__int16 *sub_4131F8();
_DWORD *sub_419F38();
bool __usercall sub_419F8C@<al>(_WORD *a1@<eax>);
bool __usercall sub_41A048@<al>(unsigned __int8 *a1@<eax>);
bool __usercall sub_41A0E0@<al>(unsigned __int16 *a1@<eax>);
int __usercall sub_41A0EC@<eax>(unsigned __int8 *a1@<eax>);
bool __usercall sub_41A164@<al>(_WORD *a1@<eax>);
int __usercall sub_41A218@<eax>(unsigned __int16 *a1@<eax>);
int sub_41A458();
void nullsub_155();
void sub_420DB4();
unsigned int __userpurge sub_420DBC@<eax>(
        unsigned int result@<eax>,
        unsigned __int16 a2@<dx>,
        _WORD *a3@<ecx>,
        _WORD *a4);
int __cdecl sub_420E14(int a1);
char __usercall sub_420E3C@<al>(__int16 a1@<ax>, int a2);
char __usercall sub_420E7C@<al>(__int16 *a1@<eax>, int a2);
char __usercall sub_420EAC@<al>(_WORD *a1@<eax>, int a2@<edx>);
bool __usercall sub_420FA8@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int sub_420FCC();
int *__usercall sub_420FF4@<eax>(volatile signed __int8 *a1@<eax>);
unsigned __int8 __usercall sub_42102C@<al>(unsigned __int16 a1@<ax>, const signed __int32 *a2@<edx>);
unsigned __int16 __usercall sub_42103C@<ax>(int a1@<eax>, __int64 **a2@<edx>, void *a3@<ecx>);
unsigned __int16 __usercall sub_42108C@<ax>(int a1@<eax>, __int64 **a2@<edx>, void *a3@<ecx>);
int __usercall sub_4210DC@<eax>(unsigned int a1@<eax>, unsigned int a2@<edx>);
BOOL __usercall sub_421148@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4211DC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_42128C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
char __usercall sub_4212A0@<al>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
volatile __int32 *__usercall sub_4212DC@<eax>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_421310@<eax>(_DWORD *a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_42134C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_421390@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_4213D4@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4213EC@<eax>(int cchCount2@<ecx>, PCNZWCH lpString2@<edx>, const WCHAR *a3@<eax>);
volatile __int32 *__usercall sub_42140C@<eax>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_42149C@<eax>(int a1@<eax>, __int16 a2@<dx>, __int64 **a3@<ecx>);
__int64 *__usercall sub_421610@<eax>(__int64 **a1@<eax>, __int16 a2@<dx>, __int64 **a3@<ecx>);
int __usercall sub_421770@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_421870@<eax>(unsigned int a1@<eax>, unsigned __int8 a2@<dl>, __int64 **a3@<ecx>);
int __userpurge sub_42196C@<eax>(unsigned __int8 a1@<al>, __int64 **a2@<edx>, void *a3@<ecx>, unsigned __int64 a4);
int __usercall sub_421C7C@<eax>(signed int a1@<eax>, __int64 **a2@<edx>);
int __userpurge sub_421CA4@<eax>(__int64 **a1@<eax>, void *a2@<ecx>, signed __int64 a3);
int __usercall sub_421CE8@<eax>(unsigned int a1@<eax>, __int64 **a2@<edx>);
int __userpurge sub_421CFC@<eax>(__int64 **a1@<eax>, void *a2@<ecx>, unsigned __int64 a3);
OLECHAR ***__userpurge sub_421D18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>, unsigned __int64 a4);
OLECHAR ***__usercall sub_421EB0@<eax>(unsigned int a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR ***__userpurge sub_421ECC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>, unsigned __int64 a4);
int __usercall sub_421EEC@<eax>(int a1@<eax>);
int __usercall sub_421F28@<eax>(int a1@<eax>, int a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_421F40@<eax>(int a1@<eax>, int *a2@<edx>, unsigned int a3@<ecx>);
__int64 __usercall sub_421F60@<edx:eax>(int a1@<eax>);
int __usercall sub_421FA4@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
volatile __int32 *sub_421FC4();
int __usercall sub_42206C@<eax>(int *a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_4220BC@<eax>(int a1@<eax>, bool *a2@<edx>, int a3@<ecx>);
volatile __int32 *__usercall sub_422168@<eax>(unsigned __int8 a1@<al>, char a2@<dl>, volatile __int32 *a3@<ecx>);
bool __usercall sub_4221FC@<al>(HINSTANCE a1@<eax>, int a2@<edx>);
int __usercall sub_42223C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_4222B0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_4222C4@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_42231C@<eax>(int a1@<eax>, char a2@<dl>);
DWORD __usercall sub_422370@<eax>(DWORD nNumberOfBytesToRead@<ecx>, LPVOID lpBuffer@<edx>, void *a3@<eax>);
DWORD __usercall sub_42239C@<eax>(DWORD nNumberOfBytesToWrite@<ecx>, LPCVOID lpBuffer@<edx>, void *a3@<eax>);
HDC __userpurge sub_4223C8@<eax>(void *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, DWORD nNumberOfBytesToRead);
HDC __userpurge sub_422400@<eax>(void *a1@<eax>, int a2@<edx>, int a3@<ecx>, DWORD nNumberOfBytesToWrite);
__int64 __userpurge sub_422438@<edx:eax>(void *a1@<eax>, DWORD a2@<edx>, LONG a3, int a4);
bool __usercall sub_422488@<al>(int a1@<eax>);
char __usercall sub_4224C8@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_422560@<eax>(int a1@<eax>, char a2@<dl>);
_WORD *__usercall sub_422640@<eax>(int a1@<eax>);
int __usercall sub_422684@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4226D8@<eax>(__int64 *a1@<eax>, _DWORD *a2@<edx>, volatile __int32 *a3@<ecx>);
int __fastcall sub_422778(int a1, int a2);
int __fastcall sub_4227B8(int a1, int a2);
int __fastcall sub_422830(int a1, int a2);
_DWORD *__fastcall sub_42286C(int a1, _DWORD *a2);
__int64 *__usercall sub_4228C4@<eax>(int a1@<eax>, __int64 **a2@<edx>);
BOOL __stdcall sub_422948(LPCWSTR lpRootPathName, int *a2, int *a3, int a4);
_WORD *__usercall sub_4229BC@<eax>(_WORD *result@<eax>);
__int64 *__usercall sub_4229D8@<eax>(__int64 *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
_WORD *__usercall sub_4229E8@<eax>(_WORD *a1@<eax>, int a2@<edx>);
__int64 *__usercall sub_422A20@<eax>(__int64 *a1@<eax>, __int64 *a2@<edx>, unsigned int a3@<ecx>);
__int64 *__usercall sub_422A5C@<eax>(__int64 *a1@<eax>, int a2@<edx>);
__int64 *__usercall sub_422A84@<eax>(__int64 *a1@<eax>, int a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_422AA4@<eax>(unsigned __int16 *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_422AD0@<eax>(unsigned __int16 *a1@<eax>, _WORD *a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_422B18@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>, unsigned int a3@<ecx>);
_WORD *__usercall sub_422B90@<eax>(_WORD *result@<eax>, __int16 a2@<dx>);
_WORD *__usercall sub_422BAC@<eax>(_WORD *a1@<eax>, __int16 a2@<dx>);
_WORD *__usercall sub_422BDC@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>);
int __userpurge sub_422C34@<eax>(int a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>, unsigned int a4);
_DWORD *__usercall sub_422C94@<eax>(int a1@<eax>, __int64 **a2@<edx>);
volatile signed __int8 **__usercall sub_422CA8@<eax>(int a1@<eax>);
// attributes: thunk
volatile signed __int8 **__usercall sub_422CC0@<eax>(int a1@<eax>);
unsigned int __usercall sub_422CC8@<eax>(int a1@<eax>);
__int64 *__usercall sub_422CD4@<eax>(__int64 *a1@<eax>);
int __usercall sub_422D00@<eax>(int result@<eax>);
int __fastcall sub_422D10(unsigned int a1, __int64 *a2);
int __stdcall sub_422D6C(int a1, int a2, int a3);
int __stdcall sub_422D8C(int a1, int a2, int a3, int a4);
int __stdcall sub_422DAC(int a1);
int __userpurge sub_422DC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __stdcall sub_422E14(int a1, int a2);
int __userpurge sub_422E30@<eax>(int a1@<eax>, int a2@<ecx>, int a3, int a4, int a5);
int __stdcall sub_422E7C(int a1);
int __thiscall sub_422EA4(void *this, int a2, int a3);
int __stdcall sub_422EBC(int a1);
volatile signed __int8 *__userpurge sub_422ED4@<eax>(
        __int64 **a1@<eax>,
        _DWORD *a2@<edx>,
        void *a3@<ecx>,
        int a4,
        int a5);
int __usercall sub_422FCC@<eax>(int a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_423040@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4231C0@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_42320C@<eax>(
        _WORD *a1@<eax>,
        unsigned int a2@<edx>,
        __int64 *a3@<ecx>,
        int a4,
        int a5,
        int a6,
        unsigned int a7);
int __usercall sub_423BE8@<eax>(__int16 a1@<ax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, _BYTE *a5@<edi>);
unsigned int __userpurge sub_423C4C@<eax>(char *a1@<eax>, char a2@<cl>, int a3, int a4, int a5, unsigned __int8 a6);
char __usercall sub_423D5E@<al>(char *a1@<esi>);
__int16 __usercall sub_423D69@<ax>(int a1@<ebp>, _WORD *a2@<edi>);
char __usercall sub_423D76@<al>(int a1@<ebp>, _WORD *a2@<edi>, unsigned __int8 *a3@<esi>);
char __usercall sub_423E23@<al>(int a1@<ebp>, _WORD *a2@<edi>, char *a3@<esi>);
unsigned __int8 __usercall sub_423E9B@<al>(int a1@<ebp>, _WORD *a2@<edi>);
void __usercall sub_423EF2(int a1@<ebp>, _WORD *a2@<edi>);
void __usercall sub_423F02(int a1@<eax>, _BYTE *a2@<edx>, _BYTE *a3@<ecx>, int a4@<ebp>);
int __fastcall sub_423F6C(char a1, int a2, int a3, int a4);
int __usercall sub_423F99@<eax>(int a1@<ebx>, int a2@<ebp>, int a3@<esi>);
_BYTE *__usercall sub_4240BB@<eax>(int a1@<ebx>, int a2@<ebp>, int a3@<esi>);
char __userpurge sub_424198@<al>(__int16 *a1@<eax>, double *a2@<edx>, char a3@<cl>, int a4);
__int16 __usercall sub_42426A@<ax>(__int16 *a1@<esi>);
double __usercall sub_42427B@<st0>(int a1@<ebp>, __int16 *a2@<esi>, double result@<st0>);
__int16 __usercall sub_42429E@<ax>(_WORD *a1@<esi>);
char __usercall sub_4242E4@<al>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
char __usercall sub_424304@<al>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_424324@<eax>(int a1@<eax>, __int64 **a2@<edx>, char a3, int a4, int a5);
_DWORD *__userpurge sub_424358@<eax>(int a1@<eax>, __int64 **a2@<edx>, char a3, int a4);
int sub_42438C();
// attributes: thunk
char __usercall sub_424398@<al>(int a1@<ecx>, int a2@<eax>, double *a3@<edx>);
int __usercall sub_4243A0@<eax>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
int __usercall sub_424400@<eax>(int a1@<eax>, float *a2@<edx>, int a3@<ecx>);
// attributes: thunk
char __usercall sub_424460@<al>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
int __userpurge sub_424468@<eax>(_DWORD *a1@<eax>, double a2);
int *__usercall sub_4244AC@<eax>(int *result@<eax>);
void __stdcall sub_4244F4(__int64 a1);
double __usercall sub_424534@<st0>(int *a1@<eax>);
int __stdcall sub_424570(unsigned __int64 a1);
double __usercall sub_42459C@<st0>(int *a1@<eax>);
int __userpurge sub_4245B4@<eax>(
        unsigned __int16 a1@<ax>,
        unsigned __int16 a2@<dx>,
        unsigned __int16 a3@<cx>,
        double *a4,
        unsigned __int16 a5);
double __userpurge sub_42462C@<st0>(
        unsigned __int16 a1@<ax>,
        unsigned __int16 a2@<dx>,
        unsigned __int16 a3@<cx>,
        unsigned __int16 a4);
unsigned int __userpurge sub_42466C@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>, _WORD *a3@<ecx>, _WORD *a4, double a5);
bool __usercall sub_4246C8@<al>(unsigned __int16 a1@<ax>);
int __userpurge sub_424704@<eax>(
        unsigned __int16 a1@<ax>,
        unsigned __int16 a2@<dx>,
        unsigned __int16 a3@<cx>,
        double *a4);
double __usercall sub_4247D0@<st0>(unsigned __int16 a1@<ax>, unsigned __int16 a2@<dx>, unsigned __int16 a3@<cx>);
int __userpurge sub_424800@<eax>(
        unsigned __int16 *a1@<eax>,
        unsigned __int16 *a2@<edx>,
        _WORD *a3@<ecx>,
        _WORD *a4,
        double a5);
int __userpurge sub_42494C@<eax>(unsigned __int16 *a1@<eax>, unsigned __int16 *a2@<edx>, _WORD *a3@<ecx>, double a4);
int __stdcall sub_42496C(double a1);
double sub_424994();
int sub_4249E4();
int __usercall sub_424A28@<eax>(__int64 *a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_424B14@<eax>(__int64 *a1@<eax>, int a2);
int __usercall sub_424B30@<eax>(int a1@<eax>, int a2@<edx>, int a3);
int __cdecl sub_424B7C(int a1);
int __cdecl sub_424BB0(int a1);
int __cdecl sub_424BE8(int a1);
_DWORD *__usercall sub_424C28@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3);
_DWORD *__usercall sub_424DA4@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3);
int __usercall sub_424EC0@<eax>(int a1@<eax>, int a2);
OLECHAR ***__userpurge sub_425794@<eax>(
        volatile __int32 *a1@<eax>,
        int a2@<edx>,
        OLECHAR **a3@<ecx>,
        int a4@<edi>,
        int a5,
        int a6);
OLECHAR ***__userpurge sub_425938@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_425950@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<edi>, int a4, int a5);
OLECHAR ***__userpurge sub_425968@<eax>(OLECHAR **a1@<eax>, volatile __int32 *a2@<edx>, int a3@<edi>, int a4, int a5);
int __usercall sub_425980@<eax>(int a1@<eax>, int *a2@<edx>);
int __userpurge sub_4259A8@<eax>(int a1@<eax>, int *a2@<edx>, _WORD *a3@<ecx>, _BYTE *a4);
int __usercall sub_425A40@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
int __usercall sub_425AD0@<eax>(int a1@<eax>, int *a2@<edx>, __int16 a3@<cx>);
int __usercall sub_425B08@<eax>(int a1@<eax>);
__int16 __usercall sub_425B5C@<ax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_425BB4@<eax>(int a1@<eax>, int a2);
int __userpurge sub_425C10@<eax>(int a1@<eax>, int *a2@<edx>, double *a3@<ecx>, int a4);
int __userpurge sub_425FAC@<eax>(int a1@<eax>, int *a2@<edx>, double *a3@<ecx>, int a4);
int __usercall sub_4261D4@<eax>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
int __usercall sub_426214@<eax>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>);
int __usercall sub_426254@<eax>(int a1@<eax>, double *a2@<edx>, int a3@<ecx>, int a4@<ebx>);
HLOCAL __usercall sub_426474@<eax>(DWORD a1@<eax>, __int64 **a2@<edx>);
// attributes: thunk
int __usercall sub_4264E3@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
volatile __int32 *__userpurge sub_426510@<eax>(LCID a1@<eax>, LCTYPE a2@<edx>, __int32 a3@<ecx>, volatile __int32 *a4);
int __usercall sub_42655C@<eax>(LCID a1@<eax>, LCTYPE a2@<edx>, int a3@<ecx>);
int __usercall sub_426588@<eax>(LCID a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_4269CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
int __usercall sub_426A74@<eax>(int a1@<eax>, int a2@<ecx>, int a3@<edi>);
_WORD *__usercall sub_426A84@<eax>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_426AB8@<eax>(__int32 a1@<eax>, __int32 a2@<edx>);
int __usercall sub_426B74@<eax>(__int32 a1@<edx>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
BOOL __stdcall CalInfoEnumProc(LPWSTR a1);
BOOL __stdcall sub_426D60(LPWSTR a1);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_426DF8@<eax>(LCID a1@<eax>, int a2@<edx>);
int **__userpurge sub_4270D4@<eax>(LCID a1@<eax>, LCTYPE a2@<edx>, int a3@<ecx>, volatile __int32 *a4, int a5, int a6);
_WORD *__usercall sub_427110@<eax>(int *a1@<eax>, int a2);
_DWORD *__userpurge sub_427154@<eax>(
        LCID a1@<eax>,
        LCTYPE a2@<edx>,
        __int32 a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        __int64 **a7,
        int a8);
int __usercall sub_427440@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4274CC@<eax>(int result@<eax>);
int __userpurge sub_4274D8@<eax>(int a1@<eax>, const void *a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_4276D0@<eax>(int a1@<eax>, const void *a2@<edx>, int a3@<edi>);
int __cdecl sub_427814(int a1, int a2, int a3, int a4);
_DWORD *__usercall sub_427840@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3@<ecx>);
int __userpurge sub_42787C@<eax>(int a1@<eax>, char a2@<dl>, int a3, int a4);
int __usercall sub_4278FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_427974@<eax>(int a1@<eax>, char a2@<dl>, int **a3@<ecx>);
int __userpurge sub_4279B0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_427A44@<eax>(int a1@<eax>, char a2@<dl>, int **a3@<ecx>, int a4, int a5);
_DWORD *__userpurge sub_427AD8@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3@<ecx>, int a4);
int __userpurge sub_427B20@<eax>(int a1@<eax>, char a2@<dl>, int a3, int a4, int a5);
int __userpurge sub_427BA8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__userpurge sub_427C28@<eax>(int a1@<eax>, char a2@<dl>, int **a3@<ecx>, int a4);
int __userpurge sub_427C70@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5, int a6);
int __userpurge sub_427D0C@<eax>(int a1@<eax>, char a2@<dl>, int **a3@<ecx>, int a4, int a5, int a6);
int __usercall sub_427DA8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_427DEC@<eax>(int result@<eax>);
_DWORD *__fastcall sub_427DF8(int a1, _DWORD *a2);
void nullsub_156();
void nullsub_157();
int sub_427E48();
char __usercall sub_427E74@<al>(int a1@<eax>);
int __usercall sub_427E9C@<eax>(int result@<eax>, int a2@<edx>);
void *__usercall sub_427EA0@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_427EF8@<eax>(int result@<eax>);
// attributes: thunk
char __usercall sub_427F04@<al>(int a1@<eax>);
_DWORD *sub_427F0C();
int __usercall sub_427FDC@<eax>(
        __int64 *a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        int a7,
        int a8,
        int a9,
        int a10);
// attributes: thunk
int __usercall sub_4280B3@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
char __usercall sub_4280DC@<al>(int *a1@<eax>);
int (**__usercall sub_42815C@<eax>(int *a1@<eax>))();
int __cdecl sub_428180(int a1);
void (__stdcall ***__usercall sub_428398@<eax>(int *a1@<eax>))(struct _EXCEPTION_REGISTRATION_RECORD *);
char __usercall sub_42847C@<al>(int a1@<eax>, int a2@<ecx>);
void __usercall  sub_4284A0(int a1@<eax>, const void *a2@<edx>, int a3@<ebx>, int a4@<edi>);
void nullsub_158();
_DWORD (*sub_4284B0())();
void *sub_428540();
void *sub_4285C0();
DWORD __usercall sub_4285D0@<eax>(void *a1@<eax>, DWORD a2@<edx>);
signed __int32 __usercall sub_4285D8@<eax>(volatile signed __int32 *a1@<eax>, volatile signed __int32 *a2@<edx>);
signed __int32 *__usercall sub_4285EC@<eax>(volatile signed __int32 *a1@<eax>);
HANDLE sub_428608();
__int32 __usercall sub_42866C@<eax>(void *a1@<eax>);
HANDLE sub_428690();
signed __int32 __usercall sub_4286D0@<eax>(int a1@<eax>);
DWORD __usercall sub_4286FC@<eax>(void *a1@<eax>, void *a2@<edx>, DWORD a3@<ecx>);
int *sub_428730();
int __usercall sub_42873C@<eax>(int result@<eax>);
int __usercall sub_42876C@<eax>(int result@<eax>, int a2@<edx>);
int sub_4287D0();
int __userpurge sub_4287FC@<eax>(DWORD *a1@<eax>, DWORD *a2@<edx>, WORD *a3@<ecx>, DWORD *a4, WORD *a5);
_DWORD *sub_428A60();
bool __usercall sub_428AB8@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_428AD8@<eax>(__int32 a1@<eax>);
char __usercall sub_428BC4@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_428C1C@<eax>(int a1@<eax>, int a2@<edx>);
int sub_428C5C();
int __usercall sub_428C80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int *__userpurge sub_428CF0@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, int *a4);
__int64 __usercall sub_428D90@<edx:eax>(int a1@<eax>, int a2@<edx>);
__int64 __usercall sub_428E24@<edx:eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_428E88@<eax>(_WORD *a1@<eax>);
unsigned __int16 *__usercall sub_428EB8@<eax>(unsigned __int16 *result@<eax>);
int __usercall sub_428EE8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_428F2C@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_428F78@<al>(int a1@<eax>, int a2@<edx>);
unsigned __int8 __usercall sub_428FC4@<al>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
unsigned __int8 __usercall sub_42900C@<al>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_42904C@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4290AC@<eax>(_DWORD *a1@<eax>, __int64 **a2@<edx>);
// attributes: thunk
_WORD *__usercall sub_4290C0@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>);
// attributes: thunk
_WORD *__usercall sub_4290C8@<eax>(_WORD *a1@<eax>, __int16 a2@<dx>);
// attributes: thunk
_WORD *__usercall sub_4290D0@<eax>(_WORD *a1@<eax>, __int16 a2@<dx>);
int __cdecl sub_4290D8(int a1);
int sub_429134();
int __usercall sub_4291C8@<eax>(int a1@<ecx>, int a2@<edi>);
int __userpurge sub_42923C@<eax>(__int32 a1@<eax>, __int32 a2@<edx>, __int32 a3@<ecx>, __int64 **a4, char a5);
unsigned int __usercall sub_42959C@<eax>(const CHAR *a1@<eax>);
unsigned int __usercall sub_429630@<eax>(const CHAR *a1@<eax>);
void nullsub_159();
int __usercall sub_429668@<eax>(int a1@<edi>);
_DWORD *__usercall sub_429698@<eax>(_DWORD *result@<eax>, int a2@<edi>);
// attributes: thunk
void __stdcall Sleep_1(DWORD dwMilliseconds);
_DWORD *__usercall sub_4297B0@<eax>(HMODULE a1@<eax>, __int64 **a2@<edx>);
int sub_4297E0();
_DWORD *__usercall sub_4297F0@<eax>(DWORD a1@<eax>, int a2@<edx>);
int __usercall sub_429894@<eax>(int a1@<eax>);
int __usercall sub_4298A4@<eax>(int a1@<ebx>);
int sub_4298C4();
HMODULE sub_4298E4();
int __usercall sub_429960@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
char sub_4299B8();
volatile signed __int8 **__usercall sub_4299D4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __fastcall sub_429A44(int a1, int *a2);
int *__usercall sub_429A54@<eax>(int a1@<eax>);
_DWORD *__usercall sub_429A90@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_429B04@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
BOOL __usercall sub_429B4C@<eax>(int a1@<eax>);
BOOL __usercall sub_429B58@<eax>(int a1@<eax>);
BOOL __usercall sub_429B64@<eax>(int a1@<eax>);
DWORD __usercall sub_429B70@<eax>(int a1@<eax>);
DWORD __usercall sub_429B80@<eax>(int a1@<eax>);
signed __int32 __usercall sub_429B90@<eax>(volatile signed __int32 *a1@<eax>, unsigned int a2@<edx>);
int __usercall sub_429BA0@<eax>(int a1@<eax>, int a2@<ebx>);
volatile signed __int8 **__usercall sub_429C58@<eax>(int a1@<eax>, volatile signed __int8 **a2@<ecx>);
int __usercall sub_429CA8@<eax>(int a1@<eax>, volatile signed __int8 **a2@<ecx>);
int __usercall sub_429D20@<eax>(int a1@<eax>, volatile signed __int8 **a2@<ecx>);
_DWORD *__usercall sub_429D8C@<eax>(_DWORD **a1@<eax>);
BOOL __usercall sub_429D9C@<eax>(int (__stdcall ***a1)(_DWORD, int, int)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_429DC0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
BOOL __usercall sub_429E58@<eax>(int (__stdcall ***a1)(_DWORD, int, int)@<eax>, int a2@<edx>);
_RTL_CRITICAL_SECTION_DEBUG *__stdcall LocaleEnumProc(_RTL_CRITICAL_SECTION_DEBUG *__return_ptr retstr, UINT a2);
_DWORD *__usercall sub_429EC8@<eax>(LCID a1@<eax>, LCTYPE a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_429F00@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_42A104@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_42A150@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_42A174@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_42A18C@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
_DWORD *__usercall sub_42A1AC@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
int __usercall sub_42A218@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_42A224@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
volatile __int32 *__usercall sub_42A244@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
int **__usercall sub_42A264@<eax>(int a1@<eax>, __int64 **a2@<ecx>);
LCID __usercall sub_42A2AC@<eax>(int a1@<eax>, int a2@<ecx>);
int **__usercall sub_42A334@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_42A358@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42A3CC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42A408@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *sub_42A454();
int __thiscall sub_42A470(void *this);
HMODULE __usercall sub_42A490@<eax>(int a1@<eax>, UINT a2@<edx>);
// attributes: thunk
int __usercall sub_42A502@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_42A514@<eax>(int a1@<eax>);
int __userpurge sub_42A518@<eax>(int a1@<eax>, void *a2@<ecx>, unsigned int __return_address, unsigned int a4);
int __userpurge sub_42A5A0@<eax>(int a1@<eax>, float a2);
int __usercall sub_42A5FC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42A654@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>);
int __userpurge sub_42A6A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_42A74C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_42A7F0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42A844@<eax>(int a1@<eax>, const CHAR *a2@<edx>);
int __usercall sub_42A898@<eax>(int a1@<eax>, unsigned int a2@<edx>);
int __usercall sub_42A8EC@<eax>(int a1@<eax>, __int16 a2@<dx>, void *a3@<ecx>);
int __usercall sub_42A944@<eax>(int a1@<eax>, char a2@<dl>);
int __userpurge sub_42A9BC@<eax>(int a1@<eax>, char __return_address, int a3);
int __usercall sub_42AA14@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_42AA6C@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __userpurge sub_42AAC0@<eax>(int a1@<eax>, __int64 a2);
int __userpurge sub_42AB1C@<eax>(int a1@<eax>, void *a2@<ecx>, unsigned int __return_address, unsigned int a4);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_42AB70@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<esi>);
int __usercall sub_42ABC4@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_42AC18@<eax>(int a1@<eax>, signed int a2@<edx>);
int __userpurge sub_42AC6C@<eax>(int a1@<eax>, int __return_address);
int __usercall sub_42ACCC@<eax>(int a1@<eax>);
int __usercall sub_42ACF0@<eax>(int a1@<eax>, int a2@<edx>);
__int64 *__userpurge sub_42AD58@<eax>(int a1@<eax>, int a2@<edx>, __int64 *a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_42AEEC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_42AF3C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__userpurge sub_42AF9C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5, int a6);
_DWORD *__userpurge sub_42B028@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_42B06C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_42B0BC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __fastcall sub_42B100(int a1, int a2);
BOOL __usercall sub_42B158@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42B1AC@<eax>(int a1@<eax>);
int __usercall sub_42B1F0@<eax>(int a1@<eax>);
int __usercall sub_42B208@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_42B26C@<eax>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_42B270@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __userpurge sub_42B2C8@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>, signed __int64 a4);
int __userpurge sub_42B324@<eax>(int a1@<eax>, int a2@<edx>, float a3);
int __usercall sub_42B388@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_42B474@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, unsigned __int16 a3@<cx>);
int __usercall sub_42B4CC@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, char a3@<cl>);
int __usercall sub_42B528@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, __int64 *a3@<ecx>);
int __userpurge sub_42B608@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, char __return_address, int a4);
int __usercall sub_42B668@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, __int16 a3@<cx>);
int __usercall sub_42B714@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __userpurge sub_42B770@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, __int64 a3);
int __usercall sub_42B7D4@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, signed int a3@<ecx>);
int __usercall sub_42B82C@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, __int16 a3@<cx>);
int __usercall sub_42B884@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __userpurge sub_42B8E0@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_42B910@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_42BB08@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, void *a3@<ecx>);
int __userpurge sub_42BB64@<eax>(int a1@<eax>, EXCEPTION_RECORD *a2@<edx>, void *a3@<ecx>, unsigned __int64 a4);
int __usercall sub_42BBC0@<eax>(int a1@<eax>);
int __usercall sub_42BBFC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_42BCFC@<eax>(int a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_42BF08@<eax>(int a1@<eax>, __int16 a2@<dx>, __int16 a3@<cx>, int a4, int a5);
int __usercall sub_42C008@<eax>(int result@<eax>, __int16 a2@<dx>, __int16 a3@<cx>);
int __usercall sub_42C030@<eax>(int a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_42C044@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42C0B8@<eax>(int a1@<eax>, int a2@<edx>, __int16 a3@<cx>);
int __usercall sub_42C120@<eax>(int a1@<eax>, const wchar_t *a2@<edx>);
_DWORD *__usercall sub_42C20C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
_DWORD *__userpurge sub_42C21C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4);
int __userpurge sub_42C328@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_42C450@<eax>(int *a1@<eax>);
int __stdcall sub_42C45C(char a1, int cchCount2, int a3);
int __stdcall sub_42C480(LCID Locale, char a2, int cchCount2, int cchCount1, int a5);
int __usercall sub_42C4D4@<eax>(signed __int16 a1@<ax>, int a2@<ecx>);
int __userpurge sub_42C534@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        LCID Locale,
        __int16 a5,
        int cchCount2,
        int cchCount1,
        int a8);
int __stdcall sub_42C5D8(LCID Locale, char a2, int cchCount2, int a4);
int __usercall sub_42C5FC@<eax>(int *a1@<eax>, int a2@<edx>);
bool __usercall sub_42C61C@<al>(int *a1@<eax>, int a2@<edx>);
__int64 *__userpurge sub_42C638@<eax>(int a1@<eax>, void *a2@<ecx>, __int64 **a3, int a4);
__int64 *__usercall sub_42C674@<eax>(__int64 *a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_42C6A4@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
volatile __int32 *__userpurge sub_42C6AC@<eax>(
        __int64 **a1@<eax>,
        int a2@<edx>,
        __int64 *a3@<ecx>,
        volatile __int32 *a4);
int __usercall sub_42C6CC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_42C72C@<eax>(int *a1@<eax>, int a2@<edx>);
int __userpurge sub_42C790@<eax>(__int32 *a1@<eax>, __int64 **a2);
int sub_42C80C();
int __usercall sub_42C814@<eax>(int *a1@<eax>, int a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_42C878@<eax>(int *a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
_DWORD *__userpurge sub_42C8A8@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4);
volatile __int32 *__usercall sub_42C8CC@<eax>(__int32 *a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_42C954@<eax>(int a1@<eax>, unsigned int a2@<edx>, int a3@<ecx>);
int __usercall sub_42C974@<eax>(int result@<eax>, unsigned int a2@<edx>, char a3@<cl>);
int __usercall sub_42C994@<eax>(int a1@<eax>, unsigned int a2@<edx>, int a3@<ecx>);
int __usercall sub_42C9B4@<eax>(int result@<eax>, unsigned int a2@<edx>, char a3@<cl>);
char __usercall sub_42C9D4@<al>(int *a1@<eax>);
int __usercall sub_42CA8C@<eax>(int result@<eax>, unsigned int a2@<edx>, char a3@<cl>);
int __usercall sub_42CAAC@<eax>(bool a1@<zf>, int a2@<eax>);
void nullsub_160();
int __usercall sub_42CAD4@<eax>(int a1@<eax>, unsigned int *a2@<edx>);
int sub_42CC14();
OLECHAR ***__userpurge sub_42CC18@<eax>(int a1@<edi>, int a2, int a3, int a4);
OLECHAR ***__userpurge sub_42CC7C@<eax>(int a1@<edi>, int a2, int a3);
OLECHAR ***__userpurge sub_42CCDC@<eax>(int a1@<edi>, int a2, int a3, int a4, int a5, int a6);
OLECHAR ***__userpurge sub_42CD48@<eax>(int a1@<edi>, int a2, int a3, int a4, int a5);
int sub_42CDB0();
_DWORD *sub_42CDC4();
int sub_42CE34();
int __thiscall sub_42CE74(void *this);
int __fastcall sub_42CEA8(int a1, int a2);
_BYTE *__userpurge sub_42CEC4@<eax>(_BYTE *a1@<eax>, int a2@<edx>, _BYTE *a3@<ecx>, int a4);
void *__usercall sub_42CF0C@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_42D0FC(int a1, __int16 a2);
int __thiscall sub_42D16C(char *this);
int __fastcall sub_42D17C(int a1, int a2);
int __userpurge sub_42D190@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_42D238@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_42D2E4@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>);
int __userpurge sub_42D30C@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_42D3BC@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        volatile signed __int8 ***a4,
        int a5,
        int a6);
int __userpurge sub_42D41C@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        volatile signed __int8 ***a4,
        int a5);
int __thiscall sub_42D474(void *this);
int __thiscall sub_42D498(char *this, volatile signed __int8 ***a2);
int __fastcall sub_42D4F0(volatile signed __int8 ***a1, int a2);
int __userpurge sub_42D53C@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4,
        int a5,
        int a6,
        int a7);
int __userpurge sub_42D6AC@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4,
        int a5,
        int a6);
int __usercall sub_42D81C@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        volatile signed __int8 ***a3@<ecx>);
int __userpurge sub_42D86C@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4,
        int a5,
        int a6);
int __thiscall sub_42D9BC(char *this);
int __userpurge sub_42D9E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_42DAA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __thiscall sub_42DB74(char *this, int a2);
int __fastcall sub_42DB9C(int a1, int a2);
int __userpurge sub_42DBC4@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        volatile signed __int8 ***a4,
        int a5,
        int a6);
int __userpurge sub_42DCDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, volatile signed __int8 ***a4, int a5);
int __userpurge sub_42DE00@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int a7, int a8);
int __userpurge sub_42DF5C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6);
int sub_42E0DC();
// attributes: thunk
int sub_42E0E0(void);
int __usercall sub_42E0E8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_42E148@<eax>(int a1@<eax>, void *a2@<ecx>);
_DWORD *__fastcall sub_42E1C4(int a1, _DWORD *a2);
int __fastcall sub_42E1D0(int a1, int a2);
int __userpurge sub_42E1F8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4, int a5);
int __thiscall sub_42E31C(void *this);
int __thiscall sub_42E350(void *this);
bool __usercall sub_42E384@<al>(int a1@<eax>);
_DWORD *__usercall sub_42E3C0@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_42E404@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __userpurge sub_42E44C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __usercall sub_42E4D8@<eax>(_DWORD *a1@<eax>);
int __usercall sub_42E4FC@<eax>(int cchWideChar@<ecx>, int a2@<eax>, const WCHAR *a3@<edx>);
int __userpurge sub_42E514@<eax>(
        int cchWideChar@<ecx>,
        int a2@<eax>,
        const WCHAR *a3@<edx>,
        int cbMultiByte,
        LPSTR lpMultiByteStr);
int __usercall sub_42E538@<eax>(int cbMultiByte@<ecx>, int a2@<eax>, const CHAR *a3@<edx>);
int __userpurge sub_42E54C@<eax>(
        int cbMultiByte@<ecx>,
        int a2@<eax>,
        const CHAR *a3@<edx>,
        int cchWideChar,
        LPWSTR lpWideCharStr);
int __usercall sub_42E56C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_42E570@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_42E5B0@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_42E5B8(int a1, int a2);
// bad sp value at call has been detected, the output may be wrong!
OLECHAR **__usercall sub_42E5BC@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<ebx>, int a4@<edi>);
_DWORD *__usercall sub_42E708@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *sub_42E748();
int __fastcall sub_42E758(int a1, int a2);
int __fastcall sub_42E760(int a1, int a2);
int __usercall sub_42E764@<eax>(int a1@<eax>, char a2@<dl>);
int sub_42E7A8();
int __fastcall sub_42E7B8(int a1, int a2);
int __fastcall sub_42E7C0(int a1, int a2);
OLECHAR ***__usercall sub_42E7C4@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
_DWORD *__usercall sub_42E84C@<eax>(_DWORD *result@<eax>, char a2@<dl>);
_DWORD *sub_42E878();
int __fastcall sub_42E888(int a1);
int __fastcall sub_42E890(int a1, __int64 *a2, int a3, __int64 *a4);
int __fastcall sub_42E8AC(int a1);
int __fastcall sub_42E8B8(int a1, __int64 *a2, int a3, __int64 *a4);
int sub_42E8D8();
volatile __int32 *__fastcall sub_42E8E0(int a1, volatile __int32 *a2);
int __fastcall sub_42E920(int a1, int a2);
int __fastcall sub_42E928(int a1, int a2);
OLECHAR ***__usercall sub_42E938@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
_DWORD *sub_42E9B8();
int __fastcall sub_42E9C8(int a1, _WORD *a2, int a3, _BYTE *a4);
int __fastcall sub_42E9FC(int a1, _BYTE *a2, int a3, _WORD *a4);
int sub_42EA48();
volatile __int32 *__fastcall sub_42EA50(int a1, volatile __int32 *a2);
OLECHAR ***__usercall sub_42EAAC@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
_DWORD *__usercall sub_42EB2C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_42EB3C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_42EB6C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_42EB8C@<eax>(_DWORD *a1@<eax>, int a2@<ebx>, int a3@<esi>);
_DWORD *__userpurge sub_42EC30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4);
int __usercall sub_42EC54@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
volatile signed __int8 **__usercall sub_42EC98@<eax>(_DWORD *a1@<eax>, volatile signed __int8 **a2@<edx>, int a3@<ecx>);
int __usercall sub_42ECD0@<eax>(_DWORD *a1@<eax>, void *a2@<ecx>);
int sub_42ED08();
volatile signed __int8 **__usercall sub_42ED28@<eax>(
        unsigned __int16 __return_address@<cx>,
        _DWORD *a2@<eax>,
        int a3@<edx>);
__int64 *__usercall sub_42ED68@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
volatile signed __int8 **__usercall sub_42EDA0@<eax>(
        unsigned __int16 __return_address@<cx>,
        _DWORD *a2@<eax>,
        int a3@<edx>);
volatile signed __int8 **__usercall sub_42EDE0@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
CHAR *__usercall sub_42EE00@<eax>(unsigned __int16 __return_address@<cx>, LPCWCH lpWideCharStr@<edx>, _DWORD *a3@<eax>);
int __usercall sub_42EE40@<eax>(_DWORD *a1@<eax>, const WCHAR *a2@<edx>, int a3@<ecx>);
CHAR *__usercall sub_42EE78@<eax>(_DWORD *a1@<eax>, const WCHAR *a2@<edx>);
int __usercall sub_42EE98@<eax>(_DWORD *a1@<eax>, void *a2@<ecx>);
void *__usercall sub_42EED0@<eax>(_DWORD *a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
void *__usercall sub_42EF08@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>, __int32 a3@<ecx>);
__int64 *__usercall sub_42EF50@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
volatile signed __int8 **__usercall sub_42F010@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
void *__usercall sub_42F058@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>);
int __usercall sub_42F0CC@<eax>(_DWORD *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
volatile signed __int8 *__usercall sub_42F134@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __usercall sub_42F1A4@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_42F26C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
OLECHAR ***__usercall sub_42F298@<eax>(int a1@<eax>);
_DWORD *__usercall sub_42F318@<eax>(_DWORD *result@<eax>);
bool __usercall sub_42F324@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_42F348@<al>(int a1@<eax>, _DWORD *a2@<edx>);
bool sub_42F420();
bool __usercall sub_42F47C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_42F708@<eax>(int a1@<edi>);
// attributes: thunk
void __stdcall VariantInit(VARIANTARG *pvarg);
// attributes: thunk
HRESULT __stdcall VariantClear(VARIANTARG *pvarg);
// attributes: thunk
HRESULT __stdcall VariantCopy(VARIANTARG *pvargDest, const VARIANTARG *pvargSrc);
// attributes: thunk
HRESULT __stdcall VariantChangeType(VARIANTARG *pvargDest, const VARIANTARG *pvarSrc, USHORT wFlags, VARTYPE vt);
HRESULT __stdcall sub_42F820(VARIANTARG *pvargDest, VARIANTARG *pvarSrc, int a3, USHORT a4, VARTYPE vt);
int __stdcall sub_42F868(int a1, int a2);
int __stdcall sub_42F874(int a1, int a2, int a3);
int __stdcall sub_42F880(int a1, int a2, int a3, int a4);
int __stdcall sub_42F88C(int __return_address, int a2, int a3, int *a4);
int __stdcall sub_42F8F8(int __return_address, int a2, int a3, float *a4);
int __stdcall sub_42F968(int __return_address, int a2, int a3, double *a4);
int __userpurge sub_42F9D8@<eax>(int a1@<ebx>, int __return_address, int a3, int a4, double *a5);
int __stdcall sub_42FA48(int __return_address, int a2, int a3, double *a4);
int __stdcall sub_42FAB8(int a1, int a2, int a3, _WORD *a4);
int __stdcall sub_42FB38(char a1, int a2, int a3, int a4, OLECHAR **a5);
int __userpurge sub_42FBAC@<eax>(int a1@<edi>, int a2, int a3, int a4, int a5, OLECHAR **a6);
int __stdcall sub_42FC20(__int16 a1, int a2, int a3, OLECHAR **a4);
// attributes: thunk
SAFEARRAY *__stdcall SafeArrayCreate(VARTYPE vt, UINT cDims, SAFEARRAYBOUND *rgsabound);
// attributes: thunk
HRESULT __stdcall SafeArrayGetLBound(SAFEARRAY *psa, UINT nDim, LONG *plLbound);
// attributes: thunk
HRESULT __stdcall SafeArrayGetUBound(SAFEARRAY *psa, UINT nDim, LONG *plUbound);
// attributes: thunk
HRESULT __stdcall SafeArrayPtrOfIndex(SAFEARRAY *psa, LONG *rgIndices, void **ppvData);
FARPROC __usercall sub_42FCB4@<eax>(const CHAR *a1@<eax>, FARPROC a2@<edx>, int a3);
FARPROC sub_42FCE0();
void sub_42FFF8();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_431050();
int sub_4310A4();
// attributes: thunk
_DWORD *sub_431140();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_431148();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_43119C();
int sub_4311F0();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_43128C();
int __usercall sub_4312E0@<eax>(signed int a1@<eax>);
signed int __usercall sub_431534@<eax>(signed int result@<eax>);
signed int __usercall sub_431540@<eax>(signed int result@<eax>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_4315F8();
int __usercall sub_43164C@<eax>(_WORD *a1@<eax>);
int __usercall sub_431660@<eax>(SAFEARRAY *a1@<eax>, UINT a2@<edx>);
signed int __usercall sub_43169C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_431738@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>);
VARIANTARG *__usercall sub_4317D0@<eax>(VARIANTARG *result@<eax>, int a2@<ecx>);
void __usercall __spoils<edx,ecx> sub_4317E4(VARIANTARG *a1@<eax>, int a2@<ecx>);
int __usercall sub_4317EC@<eax>(int a1@<eax>, const CHAR **a2@<edx>);
int __usercall sub_431808@<eax>(int a1@<eax>, OLECHAR **a2@<edx>);
void sub_431824();
int __userpurge sub_43183C@<eax>(
        int a1@<eax>,
        const CHAR **a2@<edx>,
        int a3@<ecx>,
        volatile signed __int8 ***a4,
        char a5);
int __usercall sub_431CA8@<eax>(int a1@<eax>, int a2);
int __usercall sub_431CD8@<eax>(int a1@<eax>, int a2@<edx>, int a3);
signed int __usercall sub_431D30@<eax>(VARIANTARG *a1@<eax>, int a2@<edx>, void (*a3)(void)@<ecx>);
volatile __int32 *__usercall sub_431F04@<eax>(VARIANTARG *a1@<eax>, const VARIANTARG *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_431FF4@<eax>(__int64 *result@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
VARIANTARG *__fastcall sub_432030(unsigned __int16 a1, VARIANTARG *a2);
OLECHAR **sub_43209C();
_DWORD *sub_4320E8();
_DWORD *sub_432134();
_DWORD *sub_432180();
_DWORD *sub_4321CC();
int __usercall sub_432218@<eax>(int a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
VARIANTARG *__usercall sub_432298@<eax>(int a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_432304@<eax>(__int64 *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
unsigned int __usercall sub_432558@<eax>(int a1@<ebx>, int a2@<esi>);
LONG __usercall sub_432640@<eax>(int a1@<eax>);
int __usercall sub_43267C@<eax>(VARIANTARG *a1@<eax>);
int __usercall sub_4326E0@<eax>(int a1@<eax>, LONG *a2@<edx>, int a3@<ecx>);
LONG __usercall sub_432724@<eax>(VARIANTARG *a1@<eax>, void *a2@<ecx>, int a3@<ebx>, int a4@<esi>);
LONG __usercall sub_432BC8@<eax>(VARIANTARG *a1@<eax>, void *a2@<ecx>, int a3@<ebx>, int a4@<esi>);
unsigned int __usercall sub_432C7C@<eax>(VARIANTARG *a1@<eax>, void *a2@<ecx>, int a3@<ebx>, int a4@<esi>);
int __usercall sub_432D24@<eax>(VARIANTARG *a1@<eax>, void *a2@<ecx>, int a3@<ebx>, int a4@<esi>);
unsigned int __usercall sub_432E1C@<eax>(VARIANTARG *a1@<eax>, void *a2@<ecx>, int a3@<ebx>, int a4@<esi>);
int __usercall sub_432EF8@<eax>(_WORD *a1@<eax>);
__int64 __usercall sub_432FE4@<edx:eax>(int a1@<eax>);
__int64 sub_433090();
__int64 __usercall sub_4331D4@<edx:eax>(VARIANTARG *a1@<eax>);
int __usercall sub_433240@<eax>(int a1@<eax>, LONGLONG *a2@<edx>, int a3@<ecx>);
LONGLONG __usercall sub_43328C@<edx:eax>(VARIANTARG *a1@<eax>, int a2@<ecx>);
LONGLONG __usercall sub_433714@<edx:eax>(VARIANTARG *a1@<eax>, int a2@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_433884@<eax>(int a1@<ebx>);
BOOL __usercall sub_43394C@<eax>(int a1@<eax>);
int __usercall sub_43398C@<eax>(VARIANTARG *a1@<eax>);
int __usercall sub_4339F0@<eax>(int a1@<eax>, bool *a2@<edx>, int a3@<ecx>);
int __usercall sub_433A3C@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>);
BOOL __usercall sub_433DB8@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>);
double sub_433DC4();
DOUBLE __usercall sub_433E94@<st0>(int a1@<eax>);
double __usercall sub_433EE0@<st0>(VARIANTARG *a1@<eax>);
int __usercall sub_433F44@<eax>(int a1@<eax>, LONGLONG *a2@<edx>, int a3@<ecx>);
double __usercall sub_433F90@<st0>(VARIANTARG *a1@<eax>, int a2@<ecx>);
double __usercall sub_434380@<st0>(VARIANTARG *a1@<eax>, int a2@<ecx>);
double __usercall sub_43439C@<st0>(VARIANTARG *a1@<eax>, int a2@<ecx>);
double sub_434560();
double __stdcall sub_43465C(LONGLONG a1);
DOUBLE __usercall sub_4346BC@<st0>(int a1@<eax>);
double __usercall sub_434708@<st0>(VARIANTARG *a1@<eax>);
int __usercall sub_43476C@<eax>(int a1@<eax>, LONGLONG *a2@<edx>, int a3@<ecx>);
double __usercall sub_4347B8@<st0>(VARIANTARG *a1@<eax>, int a2@<ecx>);
double sub_434BB4();
double __stdcall sub_434C7C(LONGLONG a1);
double __usercall sub_434CDC@<st0>(int a1@<eax>);
double __usercall sub_434D28@<st0>(VARIANTARG *a1@<eax>);
int __usercall sub_434D8C@<eax>(int a1@<eax>, LONGLONG *a2@<edx>, int a3@<ecx>);
double __usercall sub_434DD8@<st0>(VARIANTARG *a1@<eax>, int a2@<ecx>);
signed int __userpurge sub_43524C@<eax>(OLECHAR **a1@<eax>, int a2, int a3);
signed int __userpurge sub_435284@<eax>(OLECHAR **a1@<eax>, int a2, int a3);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_4352BC@<eax>(int a1@<eax>, OLECHAR **a2@<edx>, int a3@<ebx>, int a4@<esi>);
_DWORD *__usercall sub_435384@<eax>(int a1@<eax>, __int64 **a2@<edx>);
VARIANTARG *__usercall sub_43543C@<eax>(VARIANTARG *a1@<eax>);
int __usercall sub_4354A0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_435528@<eax>(CHAR **a1@<eax>, VARIANTARG *a2@<edx>, void *a3@<ecx>);
int __usercall sub_435C7C@<eax>(int a1@<eax>, OLECHAR **a2@<edx>);
VARIANTARG *__usercall sub_435D48@<eax>(VARIANTARG *a1@<eax>);
int __usercall sub_435DAC@<eax>(int a1@<eax>, OLECHAR **a2@<edx>);
int __usercall sub_435E88@<eax>(OLECHAR **a1@<eax>, VARIANTARG *a2@<edx>, void *a3@<ecx>);
VARIANTARG *__usercall sub_43652C@<eax>(VARIANTARG *a1@<eax>);
int __usercall sub_436590@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_436618@<eax>(volatile __int32 *a1@<eax>, VARIANTARG *a2@<edx>, void *a3@<ecx>);
VARIANTARG *__usercall sub_436C98@<eax>(_DWORD *a1@<eax>, VARIANTARG *a2@<edx>);
VARIANTARG *__usercall sub_436D10@<eax>(_DWORD *a1@<eax>, VARIANTARG *a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_436DDC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
VARIANTARG *__usercall sub_436E88@<eax>(VARIANTARG *result@<eax>, LONG a2@<edx>, char a3@<cl>);
VARIANTARG *__usercall sub_436EC4@<eax>(VARIANTARG *result@<eax>, LONG a2@<edx>, int a3@<ecx>);
VARIANTARG *__usercall sub_436EE4@<eax>(VARIANTARG *result@<eax>, BYTE a2@<dl>, int a3@<ecx>);
VARIANTARG *__usercall sub_436F04@<eax>(VARIANTARG *result@<eax>, SHORT a2@<dx>, int a3@<ecx>);
VARIANTARG *__usercall sub_436F24@<eax>(VARIANTARG *result@<eax>, LONG a2@<edx>, int a3@<ecx>);
LONG __userpurge sub_436F44@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3, LONG a4);
VARIANTARG *__usercall sub_436F70@<eax>(VARIANTARG *result@<eax>, BYTE a2@<dl>, int a3@<ecx>);
VARIANTARG *__usercall sub_436F90@<eax>(VARIANTARG *result@<eax>, SHORT a2@<dx>, int a3@<ecx>);
LONG __userpurge sub_436FB0@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3, LONG a4);
LONG __userpurge sub_436FDC@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3);
LONG __userpurge sub_437000@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3, LONG a4);
LONG __userpurge sub_43702C@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3, LONG a4);
LONG __userpurge sub_437058@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, LONG a3, LONG a4);
int __usercall sub_437084@<eax>(VARIANTARG *a1@<eax>, char a2@<dl>, int a3@<ecx>);
VARIANTARG *__usercall sub_4370AC@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, DOUBLE a3@<st0>);
VARIANTARG *__usercall sub_4370CC@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, DOUBLE a3@<st0>);
VARIANTARG *__usercall sub_4370EC@<eax>(VARIANTARG *a1@<eax>, int a2@<ecx>, double a3@<st0>);
volatile __int32 *__usercall sub_43710C@<eax>(VARIANTARG *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_437138@<eax>(VARIANTARG *a1@<eax>, unsigned __int8 *a2@<edx>);
void __usercall sub_43718C(VARIANTARG *a1@<eax>, int a2@<edx>, int a3@<ecx>);
volatile __int32 *__usercall sub_4371C4@<eax>(VARIANTARG *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4371F0@<eax>(VARIANTARG *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_43721C@<eax>(VARIANTARG *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_437248@<eax>(__int16 a1@<ax>, int a2@<ebx>);
int __usercall sub_437274@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>);
char __usercall sub_43734C@<al>(char a1@<al>, char a2@<dl>);
int __usercall sub_437360@<eax>(char a1@<al>, char a2@<dl>, int a3@<ecx>, int a4@<ebx>);
char __usercall sub_437454@<al>(int a1@<eax>, int a2@<edx>);
char __stdcall sub_437468(__int64 a1, __int64 a2);
char __stdcall sub_4374A4(unsigned __int64 a1, unsigned __int64 a2);
char __stdcall sub_4374D8(double a1, double a2);
char __stdcall sub_437504(double a1, double a2);
char __stdcall sub_437530(__int64 a1, __int64 a2);
int __usercall sub_437560@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>, void *a3@<ecx>);
_DWORD *__usercall sub_4375CC@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>, int a4@<ebx>);
int __usercall sub_437784@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_437BA4@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_437C30@<eax>(__int64 *result@<eax>, int a2@<ecx>);
int __usercall sub_437EAC@<eax>(
        __int16 a1@<ax>,
        volatile __int32 *a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
int __usercall sub_438060@<eax>(int result@<eax>);
char __usercall sub_438070@<al>(int a1@<eax>);
bool __usercall sub_4380E4@<al>(int a1@<eax>);
bool __usercall sub_4380F8@<al>(int a1@<eax>);
bool __usercall sub_43810C@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_438184@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_438224@<eax>(unsigned __int16 *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __thiscall sub_438268(void *this);
char __usercall sub_438270@<al>(unsigned __int16 *a1@<eax>, char a2@<dl>);
int __usercall sub_4382C8@<eax>(void *a1@<ecx>, int a2@<edi>);
_DWORD *__usercall sub_438360@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4383A4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_438628@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __stdcall sub_4386CC(int a1);
int __usercall sub_4386D8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_438710@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __stdcall sub_438758(int a1);
int __userpurge sub_438764@<eax>(int a1@<eax>, int a2);
int __usercall sub_438794@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int sub_4387D0();
char __userpurge sub_4387D4@<al>(int a1@<eax>, _WORD *a2);
char __thiscall sub_4387E8(_WORD *this);
// attributes: thunk
_DWORD *sub_4387F0(void);
// attributes: thunk
_DWORD *sub_4387F8(void);
// attributes: thunk
_DWORD *sub_438800();
char __userpurge sub_438808@<al>(int a1@<eax>, _WORD *a2);
// attributes: thunk
_DWORD *sub_43881C();
_DWORD *__stdcall sub_438824(int a1, int a2);
int __stdcall sub_438848(_DWORD *a1, int a2, _DWORD *a3);
BOOL __usercall sub_438870@<eax>(unsigned __int16 a1@<ax>, _DWORD *a2@<edx>, void *a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_438934@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int __usercall sub_438A3C@<eax>(_WORD *a1@<eax>);
_DWORD *__usercall sub_438A44@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>);
_DWORD *__usercall sub_438A54@<eax>(VARIANTARG *a1@<eax>, VARIANTARG *a2@<edx>);
int __usercall sub_438A64@<eax>(void *a1@<ecx>, int a2@<edi>);
void nullsub_161();
// attributes: thunk
int __stdcall IsEqualGUID(int a1, int a2);
// attributes: thunk
HRESULT __stdcall CoInitialize(LPVOID pvReserved);
// attributes: thunk
void __stdcall CoUninitialize();
// attributes: thunk
HRESULT __stdcall MEMORY[0x438DA4](
        const IID *const rclsid,
        LPUNKNOWN pUnkOuter,
        DWORD dwClsContext,
        const IID *const riid,
        LPVOID *ppv);
// attributes: thunk
LPVOID __stdcall MEMORY[0x438DAC](SIZE_T cb);
// attributes: thunk
void __stdcall MEMORY[0x438DB4](LPVOID pv);
// attributes: thunk
HRESULT __stdcall OleInitialize(LPVOID pvReserved);
// attributes: thunk
void __stdcall OleUninitialize();
// attributes: thunk
void __stdcall SysFreeString_0(BSTR bstrString);
// attributes: thunk
HRESULT __stdcall GetErrorInfo(ULONG dwReserved, IErrorInfo **pperrinfo);
int __usercall sub_438DDC@<eax>(unsigned int a1@<eax>, unsigned int a2@<edx>);
void sub_438E60();
double *__userpurge sub_438E68@<eax>(double *result@<eax>, _DWORD *a2@<edx>, double _ST6@<st1>, _TBYTE a4);
bool __stdcall sub_438E98(int a1, int a2);
int sub_438EAC();
int *sub_438F20();
void sub_438F38();
volatile signed __int8 **__usercall sub_43953C@<eax>(
        volatile signed __int8 *a1@<eax>,
        volatile signed __int8 *a2@<edx>);
int __stdcall sub_43955C(int a1);
int __stdcall sub_439568(int a1);
int __stdcall sub_439574(int a1, int a2, int a3);
signed __int32 __stdcall sub_439580(int a1);
signed __int32 __stdcall sub_439598(int a1);
int __fastcall sub_4395BC(char a1, char a2);
bool __fastcall sub_4395C8(char a1, char a2);
int sub_4395D0();
int __fastcall sub_4395E4(__int16 a1, __int16 a2);
bool __fastcall sub_4395F0(__int16 a1, __int16 a2);
int sub_4395F8();
int __fastcall sub_439610(int a1, int a2);
bool __fastcall sub_439628(int a1, int a2);
int sub_439630();
int __fastcall sub_439644(unsigned __int8 a1, unsigned __int8 a2);
int __fastcall sub_439650(unsigned __int16 a1, unsigned __int16 a2);
int __fastcall sub_43965C(unsigned int a1, unsigned int a2);
int (__stdcall **sub_439674())(int, int, int);
int (__stdcall **sub_4396DC())(int, int, int);
bool __stdcall sub_439718(__int64 a1, __int64 a2);
int __stdcall sub_439730(char a1, int a2);
int __stdcall sub_439748(__int64 a1, __int64 a2);
int __stdcall sub_439788(unsigned __int64 a1, unsigned __int64 a2);
int (__stdcall **sub_4397C0())(int, int, int);
int __stdcall sub_439800(float a1, float a2);
bool __stdcall sub_439830(float a1, float a2);
int __userpurge sub_439844@<eax>(double a1@<st1>, float a2);
int __stdcall sub_43989C(double a1, double a2);
bool __stdcall sub_4398CC(double a1, double a2);
int __userpurge sub_4398E0@<eax>(double a1@<st1>, double a2);
int __stdcall sub_439938(_TBYTE a1, _TBYTE a2);
bool __stdcall sub_43996C(_TBYTE a1, _TBYTE a2);
int __userpurge sub_439984@<eax>(double a1@<st1>, _TBYTE a2);
int __stdcall sub_4399DC(__int64 a1, __int64 a2);
bool __stdcall sub_439A10(__int64 a1, __int64 a2);
int __stdcall sub_439A28(char a1, int a2);
int __stdcall sub_439A40(__int64 a1, __int64 a2);
bool __stdcall sub_439A74(__int64 a1, __int64 a2);
int __stdcall sub_439A8C(char a1, int a2);
int (__stdcall **sub_439AA4())(int, int, int);
int (__stdcall **sub_439B00())(int, int, int);
int __usercall sub_439B5C@<eax>(unsigned __int8 *a1@<eax>, unsigned __int8 *a2@<edx>, int a3@<ecx>);
int __usercall sub_439B7C@<eax>(int a1@<eax>, unsigned __int8 *a2@<edx>, unsigned __int8 *a3@<ecx>);
BOOL __usercall sub_439B88@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_439B94@<eax>(int a1@<eax>);
int (__stdcall **__fastcall sub_439BA0(int a1, volatile signed __int8 *a2))(int, int, int);
int (__stdcall **__fastcall sub_439BCC(int a1, volatile signed __int8 *a2))(int, int, int);
char __fastcall sub_439BF8(int a1, _DWORD *a2);
int __fastcall sub_439C0C(int a1, _DWORD *a2);
int __usercall sub_439C20@<eax>(int a1@<eax>, unsigned __int8 *a2@<edx>, unsigned __int8 *a3@<ecx>);
BOOL __usercall sub_439C64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_439CA4@<eax>(int a1@<eax>, int a2@<edx>);
volatile signed __int8 **sub_439CC4();
volatile signed __int8 **sub_439CDC();
int __fastcall sub_439CF4(_BYTE *a1, _BYTE *a2);
int __fastcall sub_439D50(unsigned __int8 *a1, unsigned __int8 *a2);
int __fastcall sub_439DB0(unsigned __int8 *a1, unsigned __int8 *a2);
int __fastcall sub_439E10(unsigned __int8 *a1, unsigned __int8 *a2);
int __fastcall sub_439E40(_BYTE *a1, _BYTE *a2);
int __fastcall sub_439E84(unsigned __int8 *a1, unsigned __int8 *a2);
int __fastcall sub_439ECC(unsigned __int8 *a1, unsigned __int8 *a2);
char __fastcall sub_439F14(int a1, unsigned __int8 *a2);
int __fastcall sub_439F30(int a1, _BYTE *a2);
int __fastcall sub_439F5C(int a1, unsigned __int8 *a2);
int __fastcall sub_439F88(int a1, unsigned __int8 *a2);
int __fastcall sub_439FB4(int a1, unsigned __int8 *a2);
int (__stdcall **__fastcall sub_439FC4(int a1, int a2))(int, int, int);
int (__stdcall **__fastcall sub_439FEC(int a1, int a2))(int, int, int);
int __fastcall sub_43A014(unsigned int a1, unsigned int a2);
char __fastcall sub_43A020(int a1, int a2);
int __fastcall sub_43A038(int a1, int a2);
int __fastcall sub_43A05C(unsigned int a1, unsigned int a2);
char __fastcall sub_43A068(int a1, int a2);
int __fastcall sub_43A080(int a1, int a2);
int __stdcall sub_43A0A4(int a1, int a2, int a3, int a4);
bool __stdcall sub_43A108(int a1, int a2, int a3, int a4);
int __stdcall sub_43A144(char a1, int a2);
int __fastcall sub_43A15C(_DWORD *a1, int a2);
char __fastcall sub_43A18C(_DWORD *a1, int a2);
int __fastcall sub_43A1A4(int a1, int *a2);
int __usercall sub_43A1CC@<eax>(VARIANTARG *a1@<edx>, __int32 a2@<ecx>, int a3@<edi>);
VARIANTARG *__usercall sub_43A348@<eax>(
        VARIANTARG *a1@<edx>,
        VARIANTARG *a2@<ecx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __fastcall sub_43A3C4(int a1, VARIANTARG *a2);
int __fastcall sub_43A454(unsigned int a1, unsigned int a2);
bool __fastcall sub_43A46C(int a1, int a2);
int sub_43A474();
int (__stdcall **__usercall sub_43A488@<eax>(
        char a1@<al>,
        unsigned __int8 *a2@<edx>,
        volatile signed __int8 *a3@<ecx>))(int, int, int);
int __fastcall sub_43A6D4(int a1, int a2);
BOOL __fastcall sub_43A73C(int a1, int a2);
int __fastcall sub_43A784(int a1, int a2);
_DWORD *sub_43A7A8();
int __fastcall sub_43A7E4(_DWORD *a1, _DWORD *a2);
BOOL __fastcall sub_43A89C(_DWORD *a1, _DWORD *a2);
int __fastcall sub_43A938(int a1, _DWORD *a2);
int __usercall sub_43A99C@<eax>(unsigned __int8 *a1@<eax>, int a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_43AE58@<eax>(int a1@<ecx>, int a2@<edx>, unsigned __int8 *a3@<eax>);
int nullsub_162();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_163(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_164@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// attributes: thunk
int sub_4433B0();
int __thiscall sub_443C7C(void *this);
_DWORD *__usercall sub_443CB4@<eax>(_DWORD *result@<eax>, char a2@<dl>);
int __usercall sub_443CD4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_443D18(int a1, void *a2);
int __usercall sub_443D3C@<eax>(int a1@<eax>);
int __usercall sub_443D68@<eax>(SIZE_T dwSize@<ecx>, int a2@<eax>, LPVOID *a3@<edx>);
SIZE_T __usercall sub_443DAC@<eax>(int a1@<eax>, const void *a2@<edx>);
int sub_443DCC();
signed __int32 sub_443DDC();
int __usercall sub_443FC4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_444008@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *sub_444074();
int __usercall sub_444138@<eax>(int result@<eax>);
int __stdcall sub_444140(int a1);
int __stdcall sub_44414C(int a1, int a2, int a3);
int sub_444158();
bool __usercall sub_44415C@<al>(_BYTE *a1@<eax>);
int __usercall sub_4441D4@<eax>(_BYTE *a1@<eax>);
char __usercall sub_444334@<al>(_BYTE *a1@<eax>);
bool __usercall sub_4443C4@<al>(_BYTE *a1@<eax>, char a2@<dl>, char a3@<cl>);
OLECHAR **__userpurge sub_444448@<eax>(int a1@<eax>, __int32 a2@<ecx>, char a3);
int __usercall sub_444620@<eax>(_DWORD *a1@<eax>);
unsigned int __usercall sub_444640@<eax>(int a1@<eax>);
int __userpurge sub_444A04@<eax>(int a1@<eax>, char a2@<dl>, __int32 *a3@<ecx>, _BYTE *a4, int a5);
_DWORD *__userpurge sub_444A7C@<eax>(int __return_address@<ecx>, int a2@<eax>, char a3@<dl>, int a4);
int __userpurge sub_444AD0@<eax>(int a1@<eax>, char a2@<dl>, __int64 *a3@<ecx>, int a4, int a5);
int __usercall sub_444B30@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<edi>);
__int64 *__usercall sub_444B88@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_444BF4@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_444C1C@<al>(int a1@<eax>);
int __usercall sub_444C74@<eax>(int a1@<eax>);
int __usercall sub_444C78@<eax>(unsigned __int8 **a1@<eax>);
int __usercall sub_444C94@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
int __usercall sub_444CA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
unsigned int __usercall sub_444DEC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_444E00@<eax>(int a1@<eax>);
_DWORD *__usercall sub_444E10@<eax>(__int32 a1@<eax>, int a2@<edx>);
int __usercall sub_444E50@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_444E6C@<eax>(int a1@<eax>, int a2);
int __userpurge sub_444E8C@<eax>(int a1@<eax>, int a2, int a3);
__int16 __userpurge sub_444EB0@<ax>(int a1@<eax>, int a2, int a3, __int16 a4);
int __userpurge sub_444EDC@<eax>(int a1@<eax>, int a2, int a3);
int __userpurge sub_444F00@<eax>(int a1@<eax>, int a2, int a3);
int __userpurge sub_444F24@<eax>(int a1@<eax>, int a2, int a3);
int __usercall sub_444F48@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_444F98@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_444FC0@<eax>(char a1@<al>, int a2@<edx>);
int __usercall sub_444FDC@<eax>(unsigned __int16 *a1@<eax>, int a2@<edx>);
bool __usercall sub_44521C@<al>(_BYTE **a1@<eax>);
bool __usercall sub_445278@<al>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_445300(int a1, int a2);
OLECHAR ***__usercall sub_44531C@<eax>(int a1@<eax>, int a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>, int a6);
int __usercall sub_445458@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
OLECHAR **__userpurge sub_445594@<eax>(
        _BYTE *a1@<eax>,
        int a2@<edx>,
        __int32 a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        int a7);
// attributes: thunk
int sub_44567C();
bool __usercall sub_445684@<al>(int a1@<eax>);
int __usercall sub_4456F4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __fastcall sub_4457DC(int a1, int a2);
int __usercall sub_44588C@<eax>(int a1@<eax>);
char __usercall sub_4458EC@<al>(int a1@<eax>);
double __usercall sub_445918@<st0>(int a1@<eax>);
__int64 __usercall sub_4459A8@<edx:eax>(int a1@<eax>);
__int64 __usercall sub_445A18@<edx:eax>(int a1@<eax>);
int __usercall sub_445A88@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_445ABC@<eax>(_BYTE **a1@<eax>, __int64 **a2@<edx>);
int __fastcall sub_445B3C(int a1, int a2);
double sub_445B50();
bool __usercall sub_445B64@<al>(int a1@<eax>);
int __usercall sub_445BEC@<eax>(char *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_445CBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_445DA0@<eax>(int a1@<eax>, int a2);
char __usercall sub_445DB8@<al>(__int32 *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_445E6C@<eax>(__int32 a1@<eax>, _BYTE *a2@<edx>, _DWORD *a3@<ecx>);
char __usercall sub_445ED4@<al>(__int64 *a1@<eax>, _BYTE *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_44609C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
char __usercall sub_446828@<al>(int a1@<eax>, int a2@<ecx>);
int sub_446854();
char __usercall sub_44685C@<al>(int a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_4468D0@<eax>(int a1@<eax>, __int32 a2@<ecx>, int a3@<edi>);
char __usercall sub_446AA0@<al>(int a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_446B28@<eax>(int a1@<eax>, _BYTE *a2@<edx>, __int32 a3@<ecx>);
int __usercall sub_446D08@<eax>(int a1@<eax>, _BYTE *a2@<edx>, __int32 a3@<ecx>);
_BYTE *__usercall sub_446F40@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_446F74@<eax>(_BYTE *a1@<eax>, int a2@<ecx>, int a3@<ebx>);
BOOL __usercall sub_447044@<eax>(_BYTE **a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_44710C@<eax>(int a1@<eax>, __int32 a2@<ecx>, int a3@<edi>);
_BYTE *__usercall sub_44775C@<eax>(_BYTE **a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __fastcall sub_4479E4(int a1, _BYTE *a2);
int *__fastcall sub_447A44(int a1, _BYTE *a2);
int __usercall sub_447ABC@<eax>(int a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
char __fastcall sub_447B3C(int a1, int *a2);
char __usercall sub_447B90@<al>(int a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_447DD8@<eax>(int a1@<eax>, __int32 a2@<ecx>, int a3@<edi>);
int __usercall sub_447F70@<eax>(int a1@<eax>, __int32 a2@<ecx>, int a3@<edi>);
int __usercall sub_4482F0@<eax>(int a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>, int a4@<ebx>);
int __fastcall sub_44846C(int a1, int a2);
int __usercall sub_44871C@<eax>(int a1@<eax>, __int32 a2@<ecx>);
int *__usercall sub_44896C@<eax>(
        int **a1@<eax>,
        int *a2@<edx>,
        __int32 a3@<ecx>,
        int (__fastcall *a4)(int, int *)@<edi>);
__int64 *__usercall sub_448AB0@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_448AB8@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __usercall sub_448ACC@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
int __usercall sub_448AE0@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
int __usercall sub_448AF4@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
int __usercall sub_448B08@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
OLECHAR ***__usercall sub_448B48@<eax>(__int64 *a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_448BDC@<eax>(__int64 **a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_448BFC@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
int __usercall sub_448C10@<eax>(unsigned __int8 *a1@<eax>);
int __usercall sub_448C1C@<eax>(unsigned int a1@<eax>, char a2@<dl>, char a3@<cl>);
int (__stdcall **__usercall sub_448C34@<eax>(unsigned __int8 *a1@<eax>))(int, int);
_DWORD *__usercall sub_44C4A4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_44C4E0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int nullsub_165();
int __usercall sub_44C960@<eax>(int a1@<eax>, int a2);
_DWORD *__usercall sub_44CA84@<eax>(OLECHAR ***a1@<eax>, int a2@<ecx>, int a3);
OLECHAR ***__usercall sub_44CCC8@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
OLECHAR *__usercall sub_44CD4C@<eax>(int a1@<eax>, unsigned int a2@<edx>, int a3@<edi>);
int __userpurge sub_44CDF8@<eax>(int a1@<eax>, int a2@<edx>, unsigned int *a3);
int __userpurge sub_44CE28@<eax>(int a1@<eax>, int a2@<edx>, unsigned int a3);
int __usercall sub_44CE44@<eax>(int a1@<eax>, unsigned int a2@<edx>);
int __usercall sub_44CE68@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_44CE80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
OLECHAR ***__usercall sub_44CF68@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_44CFC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, OLECHAR *a4@<edi>, int a5@<esi>);
int __usercall sub_44D068@<eax>(int a1@<eax>, unsigned int *a2@<edx>);
_DWORD *__usercall sub_44D1C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, void *a3@<ecx>);
int __usercall sub_44D268@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__cdecl sub_44D300(int __return_address);
_DWORD *__usercall sub_44D388@<eax>(_DWORD *a1@<eax>);
int __usercall sub_44D3AC@<eax>(__int64 **a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_44D3E8@<eax>(unsigned __int8 *a1@<eax>, int a2@<ecx>, int a3);
OLECHAR **__fastcall sub_44D424(__int32 a1, __int32 *a2, volatile signed __int8 ***a3, int a4);
int __usercall sub_44D800@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_44D8E4@<eax>(__int64 **a1@<eax>, int a2@<ecx>, int a3);
OLECHAR ***__usercall sub_44DA20@<eax>(__int64 *a1@<eax>, OLECHAR ***a2@<edx>, int a3@<ecx>);
int nullsub_166();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_167(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_168@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
_DWORD *__usercall sub_44F3E4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_44F45C@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
_DWORD *__usercall sub_44F484@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_44F48C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_44F498@<eax>(_DWORD *a1@<eax>, unsigned int a2@<edx>);
_DWORD *__thiscall sub_44F4B0(void *this);
int __usercall sub_44F4EC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, OLECHAR *a3@<edi>, int a4@<esi>);
int __usercall sub_44F504@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_44F51C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<edi>, int a4@<esi>);
signed __int32 sub_44F534();
OLECHAR ***__usercall sub_44F550@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_44F568@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_44F5B0@<eax>(int a1@<eax>);
_DWORD *__thiscall sub_44F5B4(_DWORD *this);
int __userpurge sub_44F5C0@<eax>(
        int a1@<eax>,
        int (__stdcall **a2)(int, int)@<edx>,
        void *a3@<ecx>,
        unsigned __int8 **a4);
int __userpurge sub_44F680@<eax>(
        int a1@<eax>,
        int (__stdcall **a2)(int, int)@<edx>,
        void *a3@<ecx>,
        unsigned __int8 *a4);
_DWORD *__userpurge sub_44F69C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
int __usercall sub_44F6F4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
OLECHAR ***__usercall sub_44F79C@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
_DWORD *__userpurge sub_44F7C8@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_44F86C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_44F880@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_44F894@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_44F8A8@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR *__usercall sub_44F8BC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_44F994@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_44FA68@<eax>(int a1@<eax>);
OLECHAR ***__usercall sub_44FA6C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
OLECHAR *__usercall sub_44FB40@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_44FC18@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_44FC2C@<al>(int a1@<eax>);
bool __usercall sub_44FC40@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_44FC54@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_44FC68@<al>(int a1@<eax>, int a2@<ecx>);
OLECHAR *__usercall sub_44FC7C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_44FD54@<eax>(int a1@<eax>, int a2@<edx>, OLECHAR ***a3@<ecx>, int a4@<edi>);
OLECHAR ***__usercall sub_44FF10@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_44FFE4@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR ***__usercall sub_450008@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
OLECHAR *__usercall sub_4500DC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4501B4@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
OLECHAR ***__usercall sub_4501C8@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
OLECHAR ***__usercall sub_4501DC@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
OLECHAR ***__usercall sub_4501F0@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
int __usercall sub_450204@<eax>(int a1@<eax>);
int __usercall sub_450218@<eax>(int a1@<eax>);
int sub_450228();
int __usercall sub_450230@<eax>(int a1@<eax>);
_DWORD *__usercall sub_450244@<eax>(_DWORD **a1@<eax>, _DWORD *a2@<edx>);
int sub_4502CC();
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_4502D0@<eax>(int a1@<eax>);
volatile signed __int8 ***__userpurge sub_4507AC@<eax>(
        volatile signed __int8 ***a1@<eax>,
        char a2@<dl>,
        int a3@<ecx>,
        unsigned __int8 **a4,
        int a5);
volatile __int32 **__usercall sub_45094C@<eax>(int a1@<eax>, volatile __int32 **a2@<edx>);
OLECHAR ***__userpurge sub_450984@<eax>(int a1@<eax>, const void *a2@<edx>, int a3@<ecx>, int a4, int a5);
bool __usercall sub_450E58@<al>(int a1@<eax>);
int sub_450E80();
int __usercall sub_450E90@<eax>(int a1@<eax>);
bool __usercall sub_450EAC@<al>(int a1@<eax>);
int __thiscall sub_450EB4(void *this);
int __usercall sub_450ED8@<eax>(int a1@<eax>);
int __usercall sub_450EDC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_450EEC@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_4510C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
int sub_451140();
int __usercall sub_451160@<eax>(int a1@<eax>);
int __usercall sub_4511E8@<eax>(int a1@<eax>);
int __usercall sub_4511F8@<eax>(int a1@<eax>);
int __usercall sub_45120C@<eax>(int a1@<eax>);
int __usercall sub_451218@<eax>(int a1@<eax>);
int sub_451224();
int sub_451234();
bool __usercall sub_451254@<al>(int a1@<eax>);
bool sub_451278();
int __usercall sub_4512B8@<eax>(int a1@<eax>);
int __usercall sub_4512C4@<eax>(int a1@<eax>);
int __usercall sub_4512D8@<eax>(int a1@<eax>);
OLECHAR ***__userpurge sub_4512DC@<eax>(int a1@<eax>, const void *a2@<edx>, __int32 a3@<ecx>, int a4, int a5);
int __usercall sub_451A4C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_451EC4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
OLECHAR ***__usercall sub_451F20@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
// attributes: thunk
int sub_451F40();
int __usercall sub_451F48@<eax>(int a1@<eax>);
int __usercall sub_451F6C@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_451F7C@<eax>(OLECHAR ***a1@<eax>, int a2@<ecx>, int a3);
OLECHAR **__usercall sub_452010@<eax>(OLECHAR ***a1@<eax>, int a2@<ecx>, int a3);
char __usercall sub_4520A4@<al>(int a1@<eax>, int a2@<ecx>, int a3);
_DWORD *__usercall sub_4520FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
volatile signed __int8 **__usercall sub_4521AC@<eax>(volatile signed __int8 ***a1@<eax>, int a2@<ecx>, int a3);
OLECHAR **__usercall sub_452228@<eax>(int a1@<eax>, int a2@<edi>);
int __usercall sub_4523A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_4523CC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_4523F4@<eax>(OLECHAR ***a1@<eax>, int a2@<ecx>, int a3@<edi>, OLECHAR **a4);
OLECHAR **__usercall sub_4524B4@<eax>(OLECHAR ***a1@<eax>, int a2@<ecx>, int a3);
char __usercall sub_452548@<al>(int a1@<eax>, int a2@<ecx>, int a3);
_DWORD *__usercall sub_4525A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR **__usercall sub_452650@<eax>(int a1@<eax>, int a2@<edi>);
OLECHAR ***__usercall sub_45279C@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, __int64 *a3@<ecx>);
OLECHAR ***__usercall sub_45282C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
volatile signed __int8 **__usercall sub_452900@<eax>(volatile signed __int8 ***a1@<eax>, int a2);
volatile signed __int8 **__usercall sub_452980@<eax>(volatile signed __int8 ***a1@<eax>, int a2@<ecx>, int a3);
char __usercall sub_4529FC@<al>(int a1@<eax>, int a2@<ecx>, int a3);
_DWORD *__usercall sub_452A54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR **__usercall sub_452B04@<eax>(OLECHAR **a1@<eax>, OLECHAR ***a2@<edx>, int a3@<ebx>, int a4@<edi>);
OLECHAR ***__usercall sub_452BCC@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_452BF4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_452C18@<eax>(int a1@<eax>, int a2@<edi>);
_DWORD *__usercall sub_452C38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_452D28@<eax>(int a1@<eax>);
int __usercall sub_452D38@<eax>(int a1@<eax>);
int __usercall sub_452D48@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_452D6C@<eax>(int a1@<eax>);
int __usercall sub_452D7C@<eax>(int a1@<eax>);
bool __usercall sub_452D94@<al>(int a1@<eax>);
bool __usercall sub_452DA8@<al>(int a1@<eax>);
OLECHAR ***__usercall sub_452DBC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, __int32 a3@<ecx>);
OLECHAR ***__usercall sub_452F60@<eax>(int a1@<eax>, _DWORD *a2@<edx>, __int32 a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_453180@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3@<ebx>, int a4@<esi>);
_DWORD *__userpurge sub_45322C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
int __usercall sub_453284@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_453288@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_453290@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int sub_45332C();
int __usercall sub_45333C@<eax>(int a1@<eax>);
int __usercall sub_453340@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_45335C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_4533FC@<eax>(int a1@<eax>);
int __usercall sub_45340C@<eax>(int a1@<eax>);
int __usercall sub_45341C@<eax>(int a1@<eax>);
int __usercall sub_45342C@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_453444@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int sub_4534E0();
int __usercall sub_4534E8@<eax>(int a1@<eax>);
int __usercall sub_453510@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_453534@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_4535D0@<eax>(int a1@<eax>);
int __usercall sub_4535F4@<eax>(int a1@<eax>);
unsigned __int8 *__usercall sub_453618@<eax>(unsigned __int8 *a1@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_453638@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
_DWORD *__usercall sub_453714@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4537F4@<eax>(int a1@<eax>);
int __usercall sub_453810@<eax>(int a1@<eax>);
int __usercall sub_453838@<eax>(int a1@<eax>);
int nullsub_169();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_170(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_171@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_172();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_173(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_174@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_175();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_176(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_177@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
_DWORD *__userpurge sub_457CA0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
bool sub_457D3C();
OLECHAR ***__usercall sub_457D50@<eax>(
        int a1@<eax>,
        volatile __int32 *a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_457ED0@<eax>(int a1@<eax>);
int __usercall sub_457ED4@<eax>(int a1@<eax>);
OLECHAR ***__usercall sub_457EFC@<eax>(int *a1@<eax>, OLECHAR ***a2@<edx>, unsigned __int8 *a3@<ecx>, int a4@<edi>);
_DWORD *__userpurge sub_457F90@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_458030@<eax>(int a1@<eax>);
int __usercall sub_458034@<eax>(int a1@<eax>);
int __usercall sub_458048@<eax>(int a1@<eax>);
int __usercall sub_458064@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_458088@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_45818C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int sub_45822C();
int __usercall sub_458248@<eax>(int a1@<eax>);
int __usercall sub_45824C@<eax>(int a1@<eax>);
int __usercall sub_458264@<eax>(int a1@<eax>);
int __usercall sub_458274@<eax>(int a1@<eax>, int a2@<ecx>);
int *__userpurge sub_4583FC@<eax>(int *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_4584B8@<eax>(int a1@<eax>);
int __usercall sub_4584CC@<eax>(int a1@<eax>);
int sub_4584D8();
bool sub_4584DC();
int __usercall sub_4584E8@<eax>(int a1@<eax>);
bool __usercall sub_4584F0@<al>(int a1@<eax>);
bool __usercall sub_45850C@<al>(int a1@<eax>);
OLECHAR ***__userpurge sub_458520@<eax>(int a1@<eax>, const void *a2@<edx>, int a3@<ecx>, int a4, int a5);
OLECHAR ***__usercall sub_4587AC@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, unsigned __int8 *a3@<ecx>, int a4@<edi>);
char __usercall sub_4587C0@<al>(int a1@<eax>);
OLECHAR ***__usercall sub_458820@<eax>(int a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_458838@<eax>(int *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4588E0@<eax>(_DWORD *a1@<eax>, volatile signed __int8 ***a2@<edx>);
OLECHAR ***__usercall sub_458A34@<eax>(int *a1@<eax>, volatile signed __int8 ***a2@<edx>, int a3@<edi>);
OLECHAR ***__usercall sub_458AF0@<eax>(_DWORD *a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_458B4C@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_458B5C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_458C08@<eax>(int a1@<eax>);
int __usercall sub_458C18@<eax>(int a1@<eax>);
int __usercall sub_458C28@<eax>(int a1@<eax>);
int __usercall sub_458C44@<eax>(int a1@<eax>);
int __usercall sub_458C54@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_458C74@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_458D14@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_458D38@<eax>(int a1@<eax>);
int __usercall sub_458D48@<eax>(int a1@<eax>);
int __usercall sub_458D68@<eax>(int a1@<eax>);
int __usercall sub_458D78@<eax>(int a1@<eax>);
_DWORD *__usercall sub_458D90@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_458E6C@<eax>(int a1@<eax>);
int __usercall sub_458E80@<eax>(int a1@<eax>);
OLECHAR ***__usercall sub_458E9C@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, unsigned __int8 *a3@<ecx>, int a4@<edi>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_458EC8@<eax>(_DWORD **a1@<eax>, __int64 **a2@<edx>, int a3@<ebx>, int a4@<esi>);
int *__userpurge sub_458FC4@<eax>(int *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
OLECHAR ***__userpurge sub_4590D8@<eax>(
        int a1@<eax>,
        int a2@<ecx>,
        int a3@<edi>,
        struct _EXCEPTION_REGISTRATION_RECORD *a4,
        int a5);
_DWORD *__usercall sub_459358@<eax>(_DWORD **a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_4593D0@<eax>(int a1@<eax>);
int *__userpurge sub_4593E0@<eax>(int *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
OLECHAR ***__userpurge sub_45944C@<eax>(int a1@<eax>, __int32 a2@<ecx>, int a3@<edi>, int a4, int a5);
_DWORD *__usercall sub_4596B0@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_45978C@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_45979C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
char __usercall sub_459868@<al>(int a1@<eax>);
int __usercall sub_459890@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_4598B4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_459950@<eax>(int a1@<eax>);
int __usercall sub_459960@<eax>(int a1@<eax>);
void __thiscall  sub_459978(void *this);
int nullsub_178();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_179(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_180@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
char __fastcall sub_45AFD8(int a1, int a2);
int __usercall sub_45B054@<eax>(char a1@<al>, int a2);
int __usercall sub_45B0D0@<eax>(unsigned __int8 **a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_45B164@<eax>(int a1@<eax>, _DWORD *a2);
OLECHAR ***__userpurge sub_45B1B4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>, int a4, char a5, char a6, _BYTE *a7);
int __usercall sub_45B4AC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __thiscall sub_45B4DC(void *this);
int sub_45B500();
int sub_45B504();
int sub_45B508();
int __usercall sub_45B50C@<eax>(volatile signed __int32 *a1@<eax>);
bool __usercall sub_45B6F8@<al>(int a1@<eax>);
bool __usercall sub_45B71C@<al>(int a1@<eax>);
bool __usercall sub_45B740@<al>(int a1@<eax>);
int sub_45B764();
int sub_45B768();
// bad sp value at call has been detected, the output may be wrong!
int __userpurge sub_45B76C@<eax>(
        int a1@<eax>,
        _DWORD *a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<esi>,
        int a6,
        int a7);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge sub_45B7E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<esi>, int a6, int a7);
int __userpurge sub_45B854@<eax>(int a1@<eax>, const void *a2@<edx>, int a3@<ecx>, int a4, int a5);
OLECHAR ***__usercall sub_45B910@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3@<edi>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_45BC38@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ebx>, int a4@<esi>);
_DWORD *__userpurge sub_45BD74@<eax>(
        _DWORD *a1@<eax>,
        char a2@<dl>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<esi>,
        __int64 **a6,
        int a7);
volatile __int32 *__usercall sub_45BE44@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_45BE58@<eax>(int a1@<eax>);
int __usercall sub_45BE60@<eax>(int a1@<eax>);
int __usercall sub_45BE70@<eax>(int a1@<eax>);
char sub_45BE74();
int sub_45BE78();
unsigned int sub_45BE7C();
char __usercall sub_45BE84@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45BED4@<eax>(int a1@<eax>, int a2@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_45BF6C@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
_DWORD *__userpurge sub_45C07C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
int __thiscall sub_45C0D4(void *this);
int __usercall sub_45C0F8@<eax>(int a1@<eax>);
int __usercall sub_45C0FC@<eax>(int a1@<eax>);
int __usercall sub_45C128@<eax>(int a1@<eax>);
int __usercall sub_45C138@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_45C144@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __thiscall sub_45C1E4(void *this);
int __usercall sub_45C208@<eax>(int a1@<eax>);
int __usercall sub_45C20C@<eax>(int a1@<eax>);
int __usercall sub_45C21C@<eax>(int a1@<eax>);
int __usercall sub_45C238@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_45C254@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
int __usercall sub_45C2F4@<eax>(int a1@<eax>);
int __usercall sub_45C310@<eax>(int a1@<eax>);
int __usercall sub_45C624@<eax>(__int64 **a1@<eax>, int a2);
_DWORD *__userpurge sub_45C6F0@<eax>(
        _DWORD *a1@<eax>,
        char a2@<dl>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<esi>,
        int *a6,
        int __saved_registers);
int __usercall sub_45C7AC@<eax>(int a1@<eax>);
int __usercall sub_45C7C0@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_45C7E4();
int __usercall sub_45C7EC@<eax>(int a1@<eax>);
int __usercall sub_45C810@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __fastcall sub_45C82C(int a1, int a2);
_DWORD *__userpurge sub_45C848@<eax>(
        _DWORD *a1@<eax>,
        char a2@<dl>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<esi>,
        __int64 **a6,
        int a7);
volatile __int32 *__usercall sub_45C918@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_45C92C@<eax>(int a1@<eax>);
int __usercall sub_45C934@<eax>(int a1@<eax>);
volatile signed __int8 ***__userpurge sub_45C944@<eax>(
        volatile signed __int8 ***a1@<eax>,
        char a2@<dl>,
        int a3@<ecx>,
        int *a4,
        int a5);
int __usercall sub_45CA94@<eax>(int a1@<eax>);
int __usercall sub_45CA98@<eax>(int a1@<eax>);
int __usercall sub_45CA9C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_45CAC0@<al>(int a1@<eax>);
int __usercall sub_45CAD0@<eax>(int a1@<eax>);
int __usercall sub_45CAD8@<eax>(int a1@<eax>);
char sub_45CAE8();
int __usercall sub_45CAEC@<eax>(int a1@<eax>);
char sub_45CAF4();
OLECHAR ***__userpurge sub_45CAF8@<eax>(_DWORD *a1@<eax>, const void *a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_45CCEC@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_45CD08@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int sub_45CD70();
volatile __int32 *__fastcall sub_45CD74(int a1, volatile __int32 *a2);
OLECHAR ***__usercall sub_45CDB8@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
_DWORD *__userpurge sub_45CDCC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, _DWORD *a4, int a5);
int __usercall sub_45CE9C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_45CED0@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_45CFA0@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_45CFB8@<eax>(unsigned __int8 *a1@<eax>, int a2);
volatile signed __int8 *__usercall sub_45CFE0@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __fastcall sub_45D0B8(_DWORD *a1, int a2);
_DWORD *__usercall sub_45D0E8@<eax>(volatile signed __int8 ***a1@<eax>, int a2);
OLECHAR ***__usercall sub_45D18C@<eax>(void *a1@<ecx>, int a2@<edi>, int a3);
OLECHAR ***__usercall sub_45D370@<eax>(OLECHAR ***result@<eax>, void *a2@<ecx>, int a3@<edi>);
int __userpurge sub_45D38C@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>, char a4);
int __usercall sub_45D3E0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_45D40C(int a1, int a2);
void nullsub_77();
OLECHAR ***__usercall sub_45D440@<eax>(int a1@<edx>, volatile signed __int8 ***a2@<ecx>, int a3@<edi>);
OLECHAR ***__userpurge sub_45D4FC@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, int a4@<edi>, int a5);
int __usercall sub_45D5E0@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_45D744@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_45D760@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_45D818@<eax>(int a1@<eax>, int a2);
int __usercall sub_45D86C@<eax>(int a1@<eax>);
void __usercall sub_45DBD8(int a1@<eax>, int a2@<edx>);
int __usercall sub_45DBEC@<eax>(int result@<eax>, int a2@<edx>, char a3@<cl>);
char __usercall sub_45DBF8@<al>(_BYTE **a1@<eax>, int a2@<ecx>);
int __usercall sub_45DC64@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_45DC98@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45DD28@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int (*a10)(void));
void nullsub_181();
char *__usercall sub_45DFC8@<eax>(int a1@<eax>, int a2@<edx>, char *a3@<ecx>);
int __usercall sub_45E02C@<eax>(void *a1@<eax>, void *a2@<ecx>);
_DWORD *__userpurge sub_45E078@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __usercall sub_45E0EC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_45E11C@<eax>(int a1@<eax>);
OLECHAR ***__usercall sub_45E130@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
_DWORD *__userpurge sub_45E20C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int *a4, int a5);
OLECHAR ***__usercall sub_45E2AC@<eax>(int a1@<eax>, int a2@<edi>);
int __usercall sub_45E3A0@<eax>(int a1@<eax>, int a2@<edi>);
int __usercall sub_45E3C8@<eax>(int a1@<eax>, int a2@<edi>);
int __usercall sub_45E3F0@<eax>(int a1@<eax>);
bool __usercall sub_45E3F4@<al>(int a1@<eax>);
bool __usercall sub_45E408@<al>(int a1@<eax>);
bool __usercall sub_45E420@<al>(int a1@<eax>);
int __usercall sub_45E438@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_45E45C@<eax>(int a1@<eax>, int a2@<edi>);
_DWORD *__userpurge sub_45E4E4@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_45E598@<eax>(int a1@<eax>);
OLECHAR ***__userpurge sub_45E5B8@<eax>(int a1@<eax>, _DWORD *a2@<edx>, __int32 a3@<ecx>, int a4@<edi>, int a5, int a6);
OLECHAR ***__usercall sub_45E714@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3@<edi>);
int sub_45E980();
int __usercall sub_45E9E4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_45EA08@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_45EA10@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_45EAC8@<eax>(int a1@<eax>);
int __usercall sub_45EAD0@<eax>(int a1@<eax>);
int __usercall sub_45EAE8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45EBA8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_45EC24@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45EC68@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_45ED40();
int __usercall sub_45ED48@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_45ED60@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_45EDD8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_45EE7C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_45EF1C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_45EF54(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_45EF8C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_45EFF4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_45F000@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_45F06C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45F098@<eax>(_DWORD *__return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_45F180@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_45F2BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45F33C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_45F3B0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_45F41C@<eax>(int result@<eax>, int a2@<edx>);
int sub_45F500();
int sub_45F520();
int __usercall sub_45F540@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_45F548@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __fastcall sub_45F6DC(int a1, int a2);
int __userpurge sub_45F6F8@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_45F748@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_45F7B0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_45F8C4(int a1, int a2);
int __usercall sub_45F8D8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_45F8F0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_45F908@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_45F958();
int __usercall sub_45F970@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_45F9B0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_45FA08@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_45FA44@<eax>(int result@<eax>);
int __usercall sub_45FABC@<eax>(int a1@<eax>);
int __usercall sub_45FAE4@<eax>(int a1@<eax>);
int __usercall sub_45FB10@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_45FB4C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_45FB98@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_45FC00@<eax>(int a1@<eax>);
int __usercall sub_45FC10@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_45FC28@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_45FC3C();
_DWORD *__usercall sub_45FC44@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_45FC88@<al>(int a1@<eax>);
_DWORD *__usercall sub_45FCA8@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_45FCB0(volatile signed __int8 ***a1, int a2);
int __usercall sub_45FD48@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_45FD6C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_45FD74@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_45FE2C@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_45FE74@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_45FFA4@<eax>(int a1@<eax>);
int __usercall sub_45FFCC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_460078@<eax>(int a1@<eax>);
int __userpurge sub_460144@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_46018C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_4601DC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_460210@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
// attributes: thunk
int sub_460364();
int __usercall sub_46036C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_460384@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46039C@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4603D4@<eax>(int __return_address@<ecx>, int a2@<eax>, char a3@<dl>);
_DWORD *__userpurge sub_46040C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int __return_address);
_DWORD *__usercall sub_4604C4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>);
_DWORD *__userpurge sub_460574@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>, int a4);
int __usercall sub_460628@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_460664@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
int __usercall sub_4606C8@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4606E8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_460738@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_460810@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_460850@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
bool __usercall sub_4608B8@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4608DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46097C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_460994@<eax>(int a1@<eax>);
int __usercall sub_4609B4@<eax>(int a1@<eax>);
int __usercall sub_4609D4@<eax>(int a1@<eax>);
int __fastcall sub_4609E4(volatile signed __int8 ***a1, int a2);
int __usercall sub_460A70@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_460A94@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_460A9C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_460B50@<eax>(int a1@<eax>);
int __usercall sub_460B58@<eax>(int a1@<eax>);
// attributes: thunk
int sub_460B60();
_DWORD *__usercall sub_460B68@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_460BA4@<eax>(int a1@<eax>);
int __usercall sub_460BB4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_460BCC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_460BF0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_460C34@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_460C6C(volatile signed __int8 ***a1, int a2);
int __usercall sub_460CF8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_460D1C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_460D24@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_460DD8@<eax>(int a1@<eax>);
int __usercall sub_460DE0@<eax>(int a1@<eax>);
// attributes: thunk
int sub_460DE8();
_DWORD *__usercall sub_460DF0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_460E2C@<eax>(int a1@<eax>);
int __usercall sub_460E3C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_460E54@<eax>(int a1@<eax>);
_DWORD *__usercall sub_460E78@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_460EBC@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_460EF4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_460F1C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_460F30();
_DWORD *__usercall sub_460F38@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_460F7C@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_460FB4@<eax>(_DWORD *a1@<eax>);
char __usercall sub_460FD4@<al>(__int32 a1@<eax>, int a2@<edx>);
char __usercall sub_461000@<al>(__int32 *a1@<eax>, int a2@<edx>);
char __usercall sub_46102C@<al>(__int32 a1@<eax>, int a2@<edx>);
char __userpurge sub_461058@<al>(int a1@<eax>, __int32 a2, int a3);
char __usercall sub_461084@<al>(__int32 a1@<eax>, int a2@<edx>);
char __usercall sub_4610B0@<al>(__int32 a1@<eax>, int a2@<edx>);
char __usercall sub_4610DC@<al>(__int32 a1@<eax>, int a2@<edx>);
int __thiscall sub_461108(void *this);
double __usercall sub_4611BC@<st0>(int a1@<eax>, int a2@<ecx>);
__int64 __usercall sub_4611F4@<edx:eax>(int a1@<eax>, int a2@<ecx>);
__int64 __usercall sub_461230@<edx:eax>(int a1@<eax>, int a2@<ecx>);
double __usercall sub_461320@<st0>(int a1@<eax>, int a2@<ecx>);
char __userpurge sub_4613C8@<al>(int a1@<eax>, __int32 a2);
char __userpurge sub_4613F4@<al>(int a1@<eax>, __int32 a2, int a3);
char __userpurge sub_461420@<al>(int a1@<eax>, __int32 a2, int a3, int a4);
char __userpurge sub_46144C@<al>(int a1@<eax>, __int32 a2, int a3);
char __userpurge sub_461478@<al>(int a1@<eax>, __int32 a2, int a3);
char __usercall sub_4614A4@<al>(__int32 *a1@<eax>, int a2@<edx>);
char __usercall sub_4614D0@<al>(__int32 a1@<eax>, int a2@<edx>);
char __usercall sub_4614FC@<al>(__int32 a1@<eax>, int a2@<edx>);
char __usercall sub_461528@<al>(__int32 a1@<eax>, int a2@<edx>);
char __userpurge sub_461554@<al>(int a1@<eax>, __int32 a2, int a3);
char __userpurge sub_461580@<al>(int a1@<eax>, __int32 a2, int a3);
char __usercall sub_4615AC@<al>(__int32 *a1@<eax>, int a2@<edx>);
int __usercall sub_4615D8@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
int __fastcall sub_4615F0(volatile signed __int8 ***a1, int a2);
int __usercall sub_4616CC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4616F0@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_4616F8@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4617F0@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_461838@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_461968@<eax>(int a1@<eax>);
int __usercall sub_461990@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_461A3C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_461AAC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
volatile __int32 *__userpurge sub_461B60@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int32 a4);
int __userpurge sub_461BB0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, __int32 a4, int a5);
_DWORD *__usercall sub_461C00@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
_DWORD *__userpurge sub_461C80@<eax>(
        _DWORD *a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        volatile __int32 *a4,
        unsigned __int8 a5);
// attributes: thunk
int sub_461DD8();
int __usercall sub_461DE0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_461DF8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_461E10@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_461E48@<eax>(int __return_address@<ecx>, int a2@<eax>, char a3@<dl>);
_DWORD *__userpurge sub_461E80@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int __return_address);
_DWORD *__usercall sub_461F38@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_462024@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_462114@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_462150@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
_DWORD *__usercall sub_4621B4@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_46220C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_46229C@<eax>(int *a1@<eax>, int a2@<edi>);
BOOL __usercall sub_462374@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
_DWORD *__usercall sub_4623D0@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
bool __usercall sub_462438@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46245C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4624FC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_462514@<eax>(int a1@<eax>);
int __usercall sub_462534@<eax>(int a1@<eax>);
int __usercall sub_462554@<eax>(int a1@<eax>);
int __fastcall sub_462564(volatile signed __int8 ***a1, int a2);
int __usercall sub_4625F0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_462614@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_46261C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_4626D0@<eax>(int a1@<eax>);
int __usercall sub_4626D8@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4626E0();
_DWORD *__usercall sub_4626E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_462724@<eax>(int a1@<eax>);
int __usercall sub_462734@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_46274C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_462770@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4627B4@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_4627EC@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4627F4();
_DWORD *__usercall sub_4627FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_462838@<eax>(int a1@<eax>);
int __usercall sub_462848@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_462860@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_462880@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int sub_462894();
_DWORD *__usercall sub_46289C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4628E0@<eax>(int a1@<eax>, int a2@<ebx>);
volatile __int32 *__usercall sub_462918@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_46294C@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_462960();
_DWORD *__usercall sub_462968@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4629AC@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_4629E4@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __fastcall sub_462A00(volatile signed __int8 ***a1, int a2);
int __usercall sub_462ADC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_462B00@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_462B08@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_462C00@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_462C48@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_462D78@<eax>(int a1@<eax>);
int __usercall sub_462DA0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_462E4C@<eax>(int a1@<eax>);
int __userpurge sub_462F18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_462F68@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, __int32 a5);
int __usercall sub_462FB8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_462FEC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
// attributes: thunk
int sub_463140();
int __usercall sub_463148@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_463160@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_463178@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4631B0@<eax>(int __return_address@<ecx>, int a2@<eax>, char a3@<dl>);
_DWORD *__userpurge sub_4631E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int __return_address);
_DWORD *__usercall sub_4632A0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_46338C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_46347C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4634B8@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
int __usercall sub_46351C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_46353C@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_46358C@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_463664@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_4636A4@<eax>(int __return_address@<ecx>, _DWORD *a2@<eax>, int a3@<edx>);
bool __usercall sub_46370C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_463730@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4637D0@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4637E8@<eax>(int a1@<eax>);
int __usercall sub_463808@<eax>(int a1@<eax>);
int __usercall sub_463828@<eax>(int a1@<eax>);
int __usercall sub_463838@<eax>(int a1@<eax>);
// attributes: thunk
int sub_463840();
_DWORD *__usercall sub_463848@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_463884@<eax>(int a1@<eax>);
int __usercall sub_463894@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_4638AC@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_4638CC@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int sub_4638E0();
_DWORD *__usercall sub_4638E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46392C@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_463964@<eax>(int a1@<eax>);
// attributes: thunk
int sub_46396C();
_DWORD *__usercall sub_463974@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4639B0@<eax>(int a1@<eax>);
int __usercall sub_4639C0@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4639D8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4639FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_463A40@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_463A78@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_463AAC@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_463AC0();
_DWORD *__usercall sub_463AC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_463B0C@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_463B44(int a1, int a2);
_DWORD *__fastcall sub_463B60(int a1, _DWORD *a2);
_DWORD *__fastcall sub_463B80(_DWORD *a1, int a2);
int *__usercall sub_463BA8@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
char __usercall sub_463C40@<al>(__int32 a1@<eax>, int a2@<edx>);
int __usercall sub_463CA0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_463CC4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_463CCC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_463D80@<eax>(int a1@<eax>);
int __usercall sub_463D88@<eax>(int a1@<eax>);
int __usercall sub_463DA0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_463E98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_463EDC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_463F90();
int __usercall sub_463F98@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_463FB0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_464028@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4640CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46416C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4641A4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4641DC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_464244@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_464250@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4642A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4642D0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_4643A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4644D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_464548@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4645C0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46462C@<eax>(int result@<eax>, int a2@<edx>);
int sub_4646E8();
int sub_464708();
int __usercall sub_464728@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_464730@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4648CC@<eax>(int a1@<eax>);
int __usercall sub_4648F8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_464918@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_464A04@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_464A1C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_464A6C(int a1, int a2);
int __usercall sub_464A84@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_464AC0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_464B14@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_464B4C@<eax>(int result@<eax>);
int __usercall sub_464B7C@<eax>(int a1@<eax>);
int __usercall sub_464BA4@<eax>(int a1@<eax>);
int __usercall sub_464BD0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_464C0C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_464C58@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_464CA4@<eax>(int a1@<eax>);
int __usercall sub_464CB4@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_464CD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_464D14@<al>(int a1@<eax>);
int __fastcall sub_464D34(volatile signed __int8 ***a1, int a2);
int *__usercall sub_464D80@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
int *__usercall sub_464E18@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
int *__usercall sub_464EB0@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
int *__usercall sub_464F48@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
int *__usercall sub_464FE0@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int __usercall sub_465064@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_465088@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_465090@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_465144@<eax>(int a1@<eax>);
int __usercall sub_46514C@<eax>(int a1@<eax>);
int __usercall sub_465164@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46525C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4652A0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_465354();
int __usercall sub_46535C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_465374@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4653EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_465490@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_465530@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_465568(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4655A0@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_465608@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_465614@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_465668@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_465694@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_465768@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_465894@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_46590C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_465984@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4659F0@<eax>(int result@<eax>, int a2@<edx>);
int sub_465AAC();
int sub_465ACC();
int __usercall sub_465AEC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_465AF4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_465C90@<eax>(int a1@<eax>);
int __usercall sub_465CBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_465CDC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_465DC8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_465DE0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_465E30(int a1, int a2);
int __usercall sub_465E48@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_465E84@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_465ED8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_465F10@<eax>(int result@<eax>);
int __usercall sub_465F40@<eax>(int a1@<eax>);
int __usercall sub_465F68@<eax>(int a1@<eax>);
int __usercall sub_465F94@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_465FD0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46601C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_466068@<eax>(int a1@<eax>);
int __usercall sub_466078@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_466094@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4660D8@<al>(int a1@<eax>);
int __fastcall sub_4660F8(volatile signed __int8 ***a1, int a2);
int __usercall sub_466144@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_466168@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_466170@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_466224@<eax>(int a1@<eax>);
int __usercall sub_46622C@<eax>(int a1@<eax>);
int __usercall sub_466244@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46633C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_466380@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_466434();
int __usercall sub_46643C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_466454@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4664CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_466570@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_466610@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_466648(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_466680@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4666E8@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4666F4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_466748@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_466774@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_466848@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_466974@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4669EC@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_466A64@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_466AD0@<eax>(int result@<eax>, int a2@<edx>);
int sub_466B8C();
int sub_466BAC();
int __usercall sub_466BCC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_466BD4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_466D70@<eax>(int a1@<eax>);
int __usercall sub_466D9C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_466DBC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_466EA8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_466EC0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_466F10(int a1, int a2);
int __usercall sub_466F28@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_466F64@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_466FB8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_466FF0@<eax>(int result@<eax>);
int __usercall sub_467020@<eax>(int a1@<eax>);
int __usercall sub_467048@<eax>(int a1@<eax>);
int __usercall sub_467074@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4670B0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4670FC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_467148@<eax>(int a1@<eax>);
int __usercall sub_467158@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_467174@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4671B8@<al>(int a1@<eax>);
int __fastcall sub_4671D8(volatile signed __int8 ***a1, int a2);
int *__usercall sub_467224@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
int __usercall sub_4672BC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4672E0@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4672E8@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_46739C@<eax>(int a1@<eax>);
int __usercall sub_4673A4@<eax>(int a1@<eax>);
int __usercall sub_4673BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4674B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4674F8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4675AC();
int __usercall sub_4675B4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4675CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_467644@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4676E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_467788@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4677C0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4677F8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_467860@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46786C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4678C0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4678EC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_4679C0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_467AEC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_467B64@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_467BDC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_467C48@<eax>(int result@<eax>, int a2@<edx>);
int sub_467D04();
int sub_467D24();
int __usercall sub_467D44@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_467D4C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_467EE8@<eax>(int a1@<eax>);
int __usercall sub_467F14@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_467F34@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_468020@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_468038@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_468088(int a1, int a2);
int __usercall sub_4680A0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4680DC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_468130@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_468168@<eax>(int result@<eax>);
int __usercall sub_468198@<eax>(int a1@<eax>);
int __usercall sub_4681C0@<eax>(int a1@<eax>);
int __usercall sub_4681EC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_468228@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_468274@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4682C0@<eax>(int a1@<eax>);
int __usercall sub_4682D0@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4682EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_468330@<al>(int a1@<eax>);
int __fastcall sub_468350(volatile signed __int8 ***a1, int a2);
int __usercall sub_46839C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4683C0@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4683C8@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_46847C@<eax>(int a1@<eax>);
int __usercall sub_468484@<eax>(int a1@<eax>);
int __usercall sub_46849C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_468594@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4685D8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_46868C();
int __usercall sub_468694@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4686AC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_468724@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4687C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_468868@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4688A0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4688D8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_468940@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46894C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4689A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4689CC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_468AA0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_468BCC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_468C44@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_468CBC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_468D28@<eax>(int result@<eax>, int a2@<edx>);
int sub_468DE4();
int sub_468E04();
int __usercall sub_468E24@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_468E2C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_468FC8@<eax>(int a1@<eax>);
int __usercall sub_468FF4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_469014@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_469100@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_469118@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_469168(int a1, int a2);
int __usercall sub_469180@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4691BC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_469210@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_469248@<eax>(int result@<eax>);
int __usercall sub_469278@<eax>(int a1@<eax>);
int __usercall sub_4692A0@<eax>(int a1@<eax>);
int __usercall sub_4692CC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_469308@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_469354@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4693A0@<eax>(int a1@<eax>);
int __usercall sub_4693B0@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4693CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_469410@<al>(int a1@<eax>);
int __fastcall sub_469430(volatile signed __int8 ***a1, int a2);
int *__usercall sub_46947C@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_469500@<eax>(int *a1@<eax>, int a2@<edx>, volatile signed __int8 ***a3@<ecx>);
_DWORD *__usercall sub_469598@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4695C8@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4695F8@<eax>(int a1@<eax>, char a2@<dl>, int a3);
_DWORD *__userpurge sub_469644@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __userpurge sub_469690@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>, int a4, int a5);
_DWORD *__fastcall sub_469734(int a1, _DWORD *a2);
_DWORD *__fastcall sub_469754(_DWORD *a1, int a2);
__int64 *__fastcall sub_46977C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4697B0(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4697E4(int a1, int a2, int a3, int a4);
bool __usercall sub_469810@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_469834@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_469894@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_469950@<eax>(int a1@<eax>);
int __usercall sub_469968@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_469A1C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_469A84@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_469AC8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_469B94@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_469BAC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_469C24@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_469CC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_469D68@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_469DA0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_469DD8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_469E40@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_469E4C@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_469EB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_469EC4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_469ED0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_469EDC@<eax>(_DWORD *__return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_469FBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_46A0F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46A170@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_46A1E4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46A250@<eax>(int result@<eax>, int a2@<edx>);
int sub_46A324();
int sub_46A344();
int __usercall sub_46A364@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46A36C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __fastcall sub_46A500(int a1, int a2);
int __userpurge sub_46A51C@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_46A560@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46A5A4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_46A698(int a1, int a2);
int __usercall sub_46A6AC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46A6C4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46A6DC@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_46A72C();
int __usercall sub_46A744@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46A780@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46A7D4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46A80C@<eax>(int result@<eax>);
int __usercall sub_46A860@<eax>(int a1@<eax>);
int __usercall sub_46A888@<eax>(int a1@<eax>);
int __usercall sub_46A8B4@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_46A8F0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46A930@<eax>(int a1@<eax>, int a2@<ecx>);
volatile signed __int8 **__usercall sub_46A93C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_46A99C@<eax>(int a1@<eax>);
int __usercall sub_46A9AC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46A9C4@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_46A9D8();
_DWORD *__usercall sub_46A9E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_46AA24@<al>(int a1@<eax>);
_DWORD *__usercall sub_46AA44@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_46AA64@<eax>(_DWORD *a1@<eax>);
int __usercall sub_46AA84@<eax>(int a1@<eax>);
int __usercall sub_46AA9C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46AB94@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46ABD8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46AC94@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46ACAC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46AD24@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46ADC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46AE68@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_46AEA0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_46AED8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_46AF40@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46AF4C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46AFA0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46AFB4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46AFC0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46AFCC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_46B0A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_46B1CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_46B244@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_46B2BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46B328@<eax>(int result@<eax>, int a2@<edx>);
int sub_46B3E4();
int sub_46B404();
int __usercall sub_46B424@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46B42C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_46B5C0();
int __usercall sub_46B5C8@<eax>(int a1@<eax>);
int __usercall sub_46B5F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46B614@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_46B6EC(void *this);
int __usercall sub_46B6F4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46B700@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46B718@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_46B768(int a1, int a2);
int __usercall sub_46B780@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46B7BC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46B810@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46B848@<eax>(int result@<eax>);
int __usercall sub_46B878@<eax>(int a1@<eax>);
int __usercall sub_46B8A0@<eax>(int a1@<eax>);
int __usercall sub_46B8CC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_46B908@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46B948@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46B954@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_46B9A0@<eax>(int a1@<eax>);
int __usercall sub_46B9B0@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_46B9C4();
_DWORD *__usercall sub_46B9CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_46BA10@<al>(int a1@<eax>);
int __usercall sub_46BA30@<eax>(int a1@<eax>);
int __usercall sub_46BA48@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46BB40@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46BB84@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46BC40@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46BC58@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46BCD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46BD74@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46BE14@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_46BE4C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_46BE84@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_46BEEC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46BEF8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46BF4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46BF60@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46BF6C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46BF78@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_46C04C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_46C178@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_46C1F0@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_46C268@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46C2D4@<eax>(int result@<eax>, int a2@<edx>);
int sub_46C390();
int sub_46C3B0();
int __usercall sub_46C3D0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46C3D8@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_46C56C();
int __usercall sub_46C574@<eax>(int a1@<eax>);
int __usercall sub_46C5A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46C5C0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_46C698(void *this);
int __usercall sub_46C6A0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46C6AC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46C6C4@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_46C714(int a1, int a2);
int __usercall sub_46C72C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46C768@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46C7BC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46C7F4@<eax>(int result@<eax>);
int __usercall sub_46C824@<eax>(int a1@<eax>);
int __usercall sub_46C84C@<eax>(int a1@<eax>);
int __usercall sub_46C878@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_46C8B4@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46C8F4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46C900@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_46C94C@<eax>(int a1@<eax>);
int __usercall sub_46C95C@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_46C970();
_DWORD *__usercall sub_46C978@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_46C9BC@<al>(int a1@<eax>);
int *__usercall sub_46C9DC@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CA60@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CAE4@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CB68@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CBEC@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CC70@<eax>(
        int **a1@<eax>,
        _DWORD *a2@<edx>,
        int a3@<ecx>,
        int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CD04@<eax>(
        int **a1@<eax>,
        _DWORD *a2@<edx>,
        int a3@<ecx>,
        int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CD98@<eax>(
        int **a1@<eax>,
        VARIANTARG *a2@<edx>,
        int a3@<ecx>,
        int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CE38@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CEBC@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int *__usercall sub_46CF40@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
int __usercall sub_46CFC4@<eax>(int a1@<eax>);
int __usercall sub_46CFDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D09C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D150@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D194@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D2A8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46D2C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46D338@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46D3DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46D47C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_46D4B4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_46D4EC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_46D554@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46D560@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D5C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D5D8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46D5E4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46D5F0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_46D6D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_46D7F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46D890@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_46D948@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_46D9B4@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_46DAE8();
int sub_46DB08();
int __usercall sub_46DB28@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46DB30@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_46DCC4(void *this);
_DWORD *__userpurge sub_46DCE0@<eax>(int a1@<eax>, int a2);
int __usercall sub_46DD30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46DDC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_46DF04(int a1, int a2);
int __usercall sub_46DF18@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46DF30@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46DF48@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_46DF98();
int __usercall sub_46DFB0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46DFEC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46E070@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46E0A8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46E148@<eax>(int a1@<eax>);
int __usercall sub_46E170@<eax>(int a1@<eax>);
int __usercall sub_46E19C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_46E1D8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46E218@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46E224@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_46E2B8@<eax>(int a1@<eax>);
int __usercall sub_46E2C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46E2E0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_46E2F4();
_DWORD *__usercall sub_46E2FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_46E340@<al>(int a1@<eax>);
_DWORD *__usercall sub_46E360@<eax>(_DWORD *a1@<eax>);
int __usercall sub_46E380@<eax>(int a1@<eax>);
int __usercall sub_46E398@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46E490@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46E4D4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46E590@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46E5A8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46E620@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46E6C4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46E764@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_46E79C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_46E7D4@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_46E83C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46E848@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46E89C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46E8B0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46E8BC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46E8C8@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>);
int __userpurge sub_46E99C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_46EAC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_46EB40@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_46EBB8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46EC24@<eax>(int result@<eax>, int a2@<edx>);
int sub_46ECE0();
int sub_46ED00();
int __usercall sub_46ED20@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46ED28@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_46EEBC();
int __usercall sub_46EEC4@<eax>(int a1@<eax>);
int __usercall sub_46EEF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_46EF10@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_46EFE8(void *this);
int __usercall sub_46EFF0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46EFFC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46F014@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_46F064(int a1, int a2);
int __usercall sub_46F07C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46F0B8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_46F10C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46F144@<eax>(int result@<eax>);
int __usercall sub_46F174@<eax>(int a1@<eax>);
int __usercall sub_46F19C@<eax>(int a1@<eax>);
int __usercall sub_46F1C8@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_46F204@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_46F244@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46F250@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_46F29C@<eax>(int a1@<eax>);
int __usercall sub_46F2AC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_46F2C0();
_DWORD *__usercall sub_46F2C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_46F30C@<al>(int a1@<eax>);
int __usercall sub_46F32C@<eax>(int a1@<eax>);
int __usercall sub_46F344@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46F400@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
int __usercall sub_46F49C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46F4E0@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>);
// attributes: thunk
int sub_46F5C8();
int __usercall sub_46F5D0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_46F5E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46F660@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_46F704@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_46F7A4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_46F7DC(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_46F814@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_46F87C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_46F888@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __thiscall sub_46F8E8(void *this);
int __usercall sub_46F8FC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46F908@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_46F914@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_46F9F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_46FB10@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>, int a6@<esi>);
_DWORD *__usercall sub_46FB94@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_46FC38@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_46FCA4@<eax>(int result@<eax>, int a2@<edx>);
int sub_46FD60();
int sub_46FD80();
_DWORD *__usercall sub_46FDA0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_46FDA8@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_46FF3C(void *this);
_DWORD *__userpurge sub_46FF58@<eax>(int a1@<eax>, volatile __int32 *a2);
_DWORD *__usercall sub_46FF98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_470004@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_47011C(int a1, int a2);
int __usercall sub_470130@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_470148@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_470160@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_4701B0();
int __usercall sub_4701C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_470204@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_470280@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4702B8@<eax>(int a1@<eax>);
int __usercall sub_470330@<eax>(int a1@<eax>);
int __usercall sub_470358@<eax>(int a1@<eax>);
int __usercall sub_470384@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4703C0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_470400@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_47040C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_470498@<eax>(int a1@<eax>);
int __usercall sub_4704A8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4704C0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4704D4();
_DWORD *__usercall sub_4704DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_470520@<al>(int a1@<eax>);
int __usercall sub_470540@<eax>(int a1@<eax>);
int __usercall sub_470558@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_470618@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4706CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_470710@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_470824@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_47083C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4708B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_470958@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4709F8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_470A30(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_470A68@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_470AD0@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_470ADC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_470B40(void *this);
int __usercall sub_470B54@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_470B60@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_470B6C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_470C4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_470D70@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_470E0C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_470EC4@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_470F30@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_471064();
int sub_471084();
int __usercall sub_4710A4@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4710AC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_471240(void *this);
_DWORD *__userpurge sub_47125C@<eax>(int a1@<eax>, int a2);
int __usercall sub_4712AC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_471340@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_471480(int a1, int a2);
int __usercall sub_471494@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4714AC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4714C4@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_471514();
int __usercall sub_47152C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_471568@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4715EC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_471624@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4716C4@<eax>(int a1@<eax>);
int __usercall sub_4716EC@<eax>(int a1@<eax>);
int __usercall sub_471718@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_471754@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_471794@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4717A0@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_471834@<eax>(int a1@<eax>);
int __usercall sub_471844@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_47185C@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_471870();
_DWORD *__usercall sub_471878@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4718BC@<al>(int a1@<eax>);
int __userpurge sub_4718DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4719A8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4719E4@<eax>(int a1@<eax>);
int *__usercall sub_4719F0@<eax>(int **a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(int, int *)@<edi>);
_DWORD *__fastcall sub_471A74(int a1, _DWORD *a2);
_DWORD *__fastcall sub_471A94(_DWORD *a1, int a2);
__int64 *__fastcall sub_471ABC(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_471AE8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_471B14(int a1, int a2, int a3, int a4);
bool __usercall sub_471B38@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_471B5C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_471BBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_471C74@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
_DWORD *__fastcall sub_471CA8(int a1, _DWORD *a2);
_DWORD *__fastcall sub_471CC8(_DWORD *a1, int a2);
__int64 *__fastcall sub_471CF0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_471D1C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_471D48(int a1, int a2, int a3, int a4);
bool __usercall sub_471D6C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_471D90@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_471DF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_471EA8(int a1, _DWORD *a2);
_DWORD *__fastcall sub_471EC8(_DWORD *a1, int a2);
__int64 *__fastcall sub_471EF0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_471F1C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_471F48(int a1, int a2, int a3, int a4);
bool __usercall sub_471F6C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_471F90@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_471FF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4720A8(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4720C8(_DWORD *a1, int a2);
__int64 *__fastcall sub_4720F0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_47211C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_472148(int a1, int a2, int a3, int a4);
bool __usercall sub_47216C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_472190@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4721F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4722A8(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4722C8(_DWORD *a1, int a2);
__int64 *__fastcall sub_4722F0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_47231C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_472348(int a1, int a2, int a3, int a4);
bool __usercall sub_47236C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_472390@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4723F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_4724A8@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
_DWORD *__usercall sub_4724DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_472518@<eax>(int a1@<eax>);
int __userpurge sub_472528@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__fastcall sub_472648(int a1, _DWORD *a2);
_DWORD *__fastcall sub_472668(_DWORD *a1, int a2);
__int64 *__fastcall sub_472690(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4726C0(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4726F0(int a1, int a2, int a3, int a4);
bool __usercall sub_472718@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_47273C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_47279C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_472854(int a1, _DWORD *a2);
_DWORD *__fastcall sub_472874(_DWORD *a1, int a2);
__int64 *__fastcall sub_47289C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4728C8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4728F4(int a1, int a2, int a3, int a4);
bool __usercall sub_472918@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_47293C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_47299C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_472A54(int a1, _DWORD *a2);
_DWORD *__fastcall sub_472A74(_DWORD *a1, int a2);
__int64 *__fastcall sub_472A9C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_472AC8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_472AF4(int a1, int a2, int a3, int a4);
bool __usercall sub_472B18@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_472B3C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_472B9C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_472C54@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472C88@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472CBC@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472CF0@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472D24@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472D58@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472D98@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472DD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_472E24@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472E58@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
int __usercall sub_472E8C@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
_DWORD *__fastcall sub_472EC0(int a1, _DWORD *a2);
_DWORD *__fastcall sub_472EE0(_DWORD *a1, int a2);
__int64 *__fastcall sub_472F08(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_472F38(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_472F68(int a1, int a2, int a3, int a4);
bool __usercall sub_472F90@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_472FB4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_473014@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4730CC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4730EC(_DWORD *a1, int a2);
__int64 *__fastcall sub_473114(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_473140(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_47316C(int a1, int a2, int a3, int a4);
bool __usercall sub_473190@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4731B4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_473214@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4732CC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4732EC(_DWORD *a1, int a2);
__int64 *__fastcall sub_473314(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_473340(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_47336C(int a1, int a2, int a3, int a4);
bool __usercall sub_473390@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4733B4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_473414@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4734CC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4734EC(_DWORD *a1, int a2);
__int64 *__fastcall sub_473514(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_473544(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_473574(int a1, int a2, int a3, int a4);
bool __usercall sub_47359C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4735C0@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_473620@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_4736D8@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>);
_DWORD *__usercall sub_47370C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473748@<eax>(int a1@<eax>);
int __userpurge sub_473754@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473820@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_47385C@<eax>(int a1@<eax>);
int __userpurge sub_473868@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473934@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473970@<eax>(int a1@<eax>);
int __userpurge sub_47397C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473A48@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473A84@<eax>(int a1@<eax>);
int __userpurge sub_473A90@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473B5C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473B98@<eax>(int a1@<eax>);
int __userpurge sub_473BA4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473C70@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473CAC@<eax>(int a1@<eax>);
int __userpurge sub_473CBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473DA8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473DE4@<eax>(int a1@<eax>);
int __userpurge sub_473DF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473EBC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_473EF8@<eax>(int a1@<eax>);
int __userpurge sub_473F04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_473FD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_47400C@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_47401C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_47416C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4741A8@<eax>(int a1@<eax>);
int __userpurge sub_4741B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_474280@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4742BC@<eax>(int a1@<eax>);
int __userpurge sub_4742C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4743E4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_474420@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_474430@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
int nullsub_182();
int nullsub_183();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_184(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_185@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_186();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_187(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_188@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_189();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_190(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_191@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_192();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_193(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_194@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_195();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_196(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_197@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_198();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_199(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_200@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_201();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_202(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_203@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_204();
int nullsub_205();
int nullsub_206();
__int32 __usercall sub_47EC1D@<eax>(int a1@<eax>);
int __stdcall sub_47EC29(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_47EC33(int a1);
signed __int32 __stdcall sub_47EC3D(int a1);
int nullsub_207();
int nullsub_208();
int nullsub_209();
__int32 __usercall sub_48051D@<eax>(int a1@<eax>);
int __stdcall sub_480529(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_480533(int a1);
signed __int32 __stdcall sub_48053D(int a1);
int nullsub_210();
int nullsub_211();
int nullsub_212();
int nullsub_213();
int nullsub_214();
_DWORD *__usercall sub_485AF4@<eax>(_DWORD *result@<eax>, int a2@<edx>);
bool __usercall sub_485AF8@<al>(_BYTE *a1@<eax>, _BYTE *a2@<edx>);
_DWORD *__usercall sub_485B38@<eax>(unsigned __int8 **a1@<eax>, __int64 **a2@<edx>);
__int64 *__usercall sub_485B88@<eax>(__int64 **a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_485B9C@<eax>(unsigned __int8 **a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_485BE4@<eax>(int a1@<eax>);
int __usercall sub_485BFC@<eax>(int a1@<eax>);
int __usercall sub_485C24@<eax>(int a1@<eax>);
int __usercall sub_485C3C@<eax>(int a1@<eax>);
int __usercall sub_485C64@<eax>(int a1@<eax>);
int __usercall sub_485C7C@<eax>(int a1@<eax>);
int __usercall sub_485CA4@<eax>(int a1@<eax>);
int __usercall sub_485CBC@<eax>(int a1@<eax>);
int __usercall sub_485CE4@<eax>(int a1@<eax>);
int __usercall sub_485CFC@<eax>(int a1@<eax>);
int __usercall sub_485D24@<eax>(int a1@<eax>);
int __usercall sub_485D3C@<eax>(int a1@<eax>);
void sub_485D64();
int __usercall sub_485D70@<eax>(unsigned __int8 *a1@<eax>);
int __usercall sub_485D98@<eax>(int a1@<eax>);
int __usercall sub_485DB0@<eax>(int a1@<eax>);
int __usercall sub_485DD8@<eax>(int a1@<eax>);
int __usercall sub_485DF0@<eax>(int a1@<eax>);
int __usercall sub_485E08@<eax>(int a1@<eax>);
int __usercall sub_485E20@<eax>(int a1@<eax>);
int __usercall sub_485E38@<eax>(int a1@<eax>);
int __usercall sub_485E60@<eax>(int a1@<eax>);
int __usercall sub_485E88@<eax>(int a1@<eax>);
int __usercall sub_485EB0@<eax>(int a1@<eax>);
int __usercall sub_485EDC@<eax>(int a1@<eax>);
int __usercall sub_485EF4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_485F1C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_485F40@<eax>(int a1@<eax>);
OLECHAR ***__usercall sub_485F7C@<eax>(__int64 *a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_486010@<eax>(int *a1@<eax>, signed int a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_48628C@<eax>(unsigned int a1@<eax>, int a2@<edx>);
unsigned int *__usercall sub_4862AC@<eax>(unsigned int a1@<eax>, int a2@<edx>);
int __usercall sub_486398@<eax>(unsigned int a1@<eax>, int a2@<edx>);
bool __usercall sub_48641C@<al>(const CHAR *a1@<eax>, const CHAR *a2@<edx>);
int __usercall sub_48647C@<eax>(int a1@<eax>, const CHAR *a2@<edx>);
int __usercall sub_4864F4@<eax>(unsigned int a1@<eax>, int a2@<edx>);
int __usercall sub_48655C@<eax>(_BYTE *a1@<eax>, wchar_t *a2@<edx>);
int __usercall sub_486604@<eax>(int result@<eax>, const CHAR *a2@<edx>);
int __usercall sub_4866B8@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_48670C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_486714@<eax>(int a1@<eax>, void *a2@<edx>);
char __usercall sub_486768@<al>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_486798@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
OLECHAR *__usercall sub_486910@<eax>(int a1@<eax>, int a2@<edx>, OLECHAR *a3@<edi>);
OLECHAR *__usercall sub_486A2C@<eax>(int a1@<eax>, int a2@<edi>, int a3);
OLECHAR *__usercall sub_486B0C@<eax>(__int32 a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>, int a5);
int __usercall sub_486BD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, OLECHAR *a3@<edi>);
int __usercall sub_486E38@<eax>(OLECHAR *a1@<eax>, int a2@<edx>);
char __usercall sub_486E6C@<al>(_DWORD *a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_486EE0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_486F3C@<eax>(int *a1@<eax>, signed int a2@<edx>, volatile __int32 *a3@<ecx>);
int __usercall sub_486FD0@<eax>(_BYTE *a1@<eax>, wchar_t *a2@<edx>);
_DWORD *__userpurge sub_487070@<eax>(int *a1@<eax>, int a2@<edx>, char a3@<cl>, __int64 **a4);
__int64 *__userpurge sub_487160@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int64 *a3@<ecx>, int a4);
unsigned __int8 __usercall sub_4871A4@<al>(_DWORD *a1@<eax>, int **a2@<edx>, unsigned __int8 *a3@<ecx>);
// positive sp value has been detected, the output may be wrong!
_DWORD *__usercall sub_4871F8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
unsigned __int8 __usercall sub_487228@<al>(_DWORD *a1@<eax>, int **a2@<edx>, __int64 *a3@<ecx>);
volatile __int32 *__usercall sub_48725C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
volatile __int32 *__usercall sub_48729C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
OLECHAR **__fastcall sub_4872DC(CHAR **a1, int a2);
OLECHAR **__fastcall sub_487338(const CHAR *a1, int a2);
_DWORD *__fastcall sub_487390(CHAR **a1, int a2);
_DWORD *__fastcall sub_4873EC(const CHAR *a1, int a2);
_DWORD *__fastcall sub_487444(__int64 **a1, _BYTE ***a2);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4874F0@<eax>(const WCHAR *cchWideChar@<ecx>, int a2@<eax>, int **a3@<edx>);
OLECHAR **__usercall sub_4875FC@<eax>(WCHAR *cchWideChar@<ecx>, _DWORD *a2@<eax>, int **a3@<edx>);
OLECHAR **__usercall sub_4876C4@<eax>(_DWORD *a1@<eax>, _BYTE ***a2@<edx>, __int64 **a3@<ecx>);
char __usercall sub_487710@<al>(_DWORD *a1@<eax>, int **a2@<edx>, __int64 *a3@<ecx>);
int __fastcall sub_48774C(OLECHAR **a1, _BYTE ***a2);
int __usercall sub_4877F4@<eax>(_DWORD *a1@<eax>, int **a2@<edx>, __int64 *a3@<ecx>);
// attributes: thunk
OLECHAR **__usercall sub_487894@<eax>(WCHAR *a1@<ecx>, int **a2@<edx>, _DWORD *a3@<eax>);
double __usercall sub_48789C@<st0>(int a1@<eax>, int **a2@<edx>);
int __fastcall sub_48795C(int a1, int **a2, _TBYTE a3);
__int64 *__usercall sub_487A34@<eax>(__int64 *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_487A48@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int64 *a3@<ecx>);
__int64 *__usercall sub_487A88@<eax>(_DWORD *a1@<eax>, int a2@<edx>, VARIANTARG *a3@<ecx>);
_DWORD *__usercall sub_4884E0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_488520@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_488558@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_488580@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3, int a4);
int __thiscall sub_4885BC(void *this);
int __thiscall sub_4885D8(void *this);
int __usercall sub_4885E8@<eax>(int a1@<edi>);
volatile __int32 *__fastcall sub_4887CC(int a1, _DWORD *a2, volatile __int32 *a3);
volatile __int32 *__fastcall sub_488854(int a1, _DWORD *a2, __int32 a3);
OLECHAR **__fastcall sub_4888D8(int a1, _DWORD *a2, OLECHAR **a3);
OLECHAR **__fastcall sub_488960(int a1, _DWORD *a2, const OLECHAR *a3);
double __fastcall sub_4889E4(int a1, _DWORD *a2);
_DWORD *__fastcall sub_488A68(int a1, _DWORD *a2, int a3);
double __fastcall sub_488AE4(int a1, _DWORD *a2);
_DWORD *__fastcall sub_488B70(int a1, _DWORD *a2, int a3, int a4);
double __fastcall sub_488BF8(int a1, _DWORD *a2);
int __fastcall sub_488C8C(int a1, _DWORD *a2, int a3, int a4, unsigned __int16 a5);
double __fastcall sub_488D28(int a1, _DWORD *a2);
_DWORD *__fastcall sub_488DB4(int a1, _DWORD *a2, int a3, int a4);
double __fastcall sub_488E3C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_488EC8(int a1, _DWORD *a2, int a3, int a4);
_DWORD *__fastcall sub_488F50(int a1, _DWORD *a2, _DWORD *a3);
_DWORD *__fastcall sub_488FD8(int a1, _DWORD *a2, int a3);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_225@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_226@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
void sub_49626C();
int nullsub_236();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_237(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_238@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// attributes: thunk
int sub_498238();
int nullsub_239();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_240(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_241@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_242();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_243(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_244@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_245();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_246(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_247@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_248();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_249(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_250@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_251();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_252(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_253@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_254@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
bool __usercall sub_4A1BB8@<al>(_DWORD *a1@<eax>);
unsigned __int8 *__usercall sub_4A1BCC@<eax>(unsigned __int8 *a1@<eax>);
int nullsub_255();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_256(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_257@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_258();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_259(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_260@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int sub_4A6BF8();
int __usercall sub_4A6C04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4A6C64(int a1, int a2, int a3);
_DWORD *__usercall sub_4A6CD4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4A6D30@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4A6D6C@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4A6DA8@<eax>(int result@<eax>, void (*a2)(void), int a3);
int __usercall sub_4A6E20@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4A6E64@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4A6F1C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_4A6F60@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A6F88@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A70E4@<eax>(_DWORD *a1@<eax>, void *a2@<edx>, int a3@<ecx>);
int __usercall sub_4A7398@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4A73E4(int a1, int a2);
_DWORD *__usercall sub_4A7404@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4A7470@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4A749C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A74E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A7530@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4A754C(void *this);
int __usercall sub_4A75D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4A777C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A7794@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A77B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A77F8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A7850@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A7880@<eax>(int a1@<eax>, void *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4A78C8@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, char a4);
int __usercall sub_4A7A00@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4A7A2C@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __userpurge sub_4A7AB8@<eax>(int a1@<eax>, void *a2@<ecx>, void (*a3)(void), int a4);
int __usercall sub_4A7B28@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4A7B34@<eax>(int a1@<eax>);
int __usercall sub_4A7BA0@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4A7BF8@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4A7C18@<eax>(int (**a1)()@<eax>, void *a2@<ecx>);
int __usercall sub_4A7C8C@<eax>(void *a1@<eax>, void *a2@<ecx>);
int __usercall sub_4A7CDC@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4A7D2C@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __usercall sub_4A7D84@<eax>(int a1@<eax>, void *a2@<ecx>);
int nullsub_261();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_262(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_263@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
_DWORD *__userpurge sub_4A9860@<eax>(_DWORD *result@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __usercall sub_4A9898@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4A98C4@<eax>(int a1@<eax>);
int __usercall sub_4A9944@<eax>(int a1@<eax>);
char __userpurge sub_4A99C4@<al>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4A9A2C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, _DWORD *a3@<ecx>, int a4);
int nullsub_264();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_265(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_266@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int __usercall sub_4AB188@<eax>(int result@<eax>, int a2@<ecx>);
int __thiscall sub_4AB1A0(void *this);
char __thiscall sub_4AB1E0(void *this);
bool __usercall sub_4AB204@<al>(int a1@<eax>, HMODULE a2@<edx>, _DWORD *a3@<ecx>);
int nullsub_267();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_268(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_269@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// attributes: thunk
int sub_4ABE78();
_DWORD *sub_4ACA9C();
_DWORD *sub_4ACAF8();
_DWORD *sub_4ACB28();
int __usercall sub_4ACB88@<eax>(int (**a1)()@<eax>, int a2);
int __usercall sub_4ACC14@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4, int a5, int a6, int a7, __int16 a8);
_DWORD *__thiscall sub_4ACCE8(void (__stdcall **this)(int *));
BOOL __userpurge sub_4ACD54@<eax>(
        _DWORD *a1@<eax>,
        _DWORD *a2@<edx>,
        void (__stdcall **a3)(int *)@<ecx>,
        void (__stdcall **a4)(int *));
_DWORD *__usercall sub_4ACE70@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4ACED8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4ACEF8@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __thiscall sub_4ACF38(void *this);
__int64 *__usercall sub_4ACF50@<eax>(__int64 **a1@<eax>, int a2@<edx>);
int __fastcall sub_4ACFB8(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4ACFF0@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4AD058@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4AD0BC@<eax>(int a1@<eax>);
int __usercall sub_4AD110@<eax>(int a1@<eax>);
int __usercall sub_4AD144@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AD168@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4AD238@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AD2F8@<eax>(__int64 **a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4AD318@<eax>(int result@<eax>);
int __usercall sub_4AD3C8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4AD464@<eax>(OLECHAR **a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4AD6D4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4AD750@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_4AD770@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
void nullsub_215();
int __userpurge sub_4AD7C4@<eax>(__int64 **a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>, int a4);
int __usercall sub_4ADA90@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4ADAE8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4ADB64@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4ADBEC@<eax>(int a1@<eax>);
int __usercall sub_4ADC34@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4ADC64@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __thiscall sub_4ADCB8(void *this);
_DWORD *__usercall sub_4ADCC4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4ADD08@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_4ADD20@<al>(int a1@<eax>);
_DWORD *__usercall sub_4ADD3C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4ADD80@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4ADDC4@<eax>(int a1@<eax>);
int __usercall sub_4ADE38@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4ADE9C@<eax>(int a1@<eax>);
int __fastcall sub_4ADEF4(int a1, int a2);
_DWORD *__usercall sub_4ADF08@<eax>(__int64 *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_4ADFBC@<eax>(int a1@<eax>);
int __usercall sub_4AE010@<eax>(int a1@<eax>);
int __usercall sub_4AE07C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AE0DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AE14C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AE1B8@<eax>(__int64 *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4AE214@<eax>(__int64 *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AE2D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AE354@<eax>(int a1@<eax>);
int __usercall sub_4AE3A8@<eax>(int a1@<eax>);
int __usercall sub_4AE3FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AE46C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4AE4B4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AE4C0@<eax>(int result@<eax>, int a2@<edx>);
signed __int32 *__usercall sub_4AE59C@<eax>(int a1@<eax>, signed int a2@<edx>, char a3@<cl>);
void nullsub_270();
int __usercall sub_4AE5E0@<eax>(int a1@<eax>);
int __usercall sub_4AE658@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4AE684(int a1, int (***a2)(void));
_DWORD *__fastcall sub_4AE698(int a1, int a2);
_DWORD *__usercall sub_4AE754@<eax>(int a1@<eax>, int a2@<ecx>);
void nullsub_216();
_DWORD *__usercall sub_4AE760@<eax>(
        int *a1@<eax>,
        __int64 **a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
void __usercall sub_4AE7FC(int *a1@<eax>);
int __stdcall sub_4AE84C(int a1);
int __stdcall sub_4AE86C(int a1);
int __stdcall sub_4AE88C(_DWORD *a1, int a2, _DWORD *a3);
unsigned __int8 __usercall sub_4AE8B4@<al>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4AE954@<eax>(_BYTE *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4AE9A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4AEA04@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_4AEA3C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4AEA70@<eax>(int a1@<eax>);
int __usercall sub_4AEA78@<eax>(int result@<eax>);
int __usercall sub_4AEA98@<eax>(int a1@<eax>, int a2@<ecx>);
int __fastcall sub_4AEAB0(int a1, int a2);
_DWORD *__usercall sub_4AEAC4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AEB70@<eax>(int a1@<eax>);
int __usercall sub_4AEB74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AEB9C@<eax>(int a1@<eax>);
int __usercall sub_4AEBA4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4AEBD4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4AEC24@<al>(int a1@<eax>);
_DWORD *__usercall sub_4AEC40@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4AEC8C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4AECD8@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
int __usercall sub_4AECF8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AEDA4@<eax>(int result@<eax>);
_DWORD *__usercall sub_4AEDA8@<eax>(_DWORD *result@<eax>);
int __usercall sub_4AEDB8@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_4AEE24@<eax>(_DWORD *a1@<eax>);
int __usercall sub_4AEE30@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__thiscall sub_4AEE64(_DWORD *this);
_DWORD *__usercall sub_4AEE70@<eax>(int a1@<eax>);
int __stdcall sub_4AEE8C(int a1);
int __usercall sub_4AEEAC@<eax>(int a1@<eax>);
int __usercall sub_4AEEC0@<eax>(
        int *a1@<eax>,
        __int64 **a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
_DWORD *__usercall sub_4AEF74@<eax>(int *a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_4AF0C0@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4AF144@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __fastcall sub_4AF198(int a1, int a2);
int sub_4AF1B8();
void nullsub_219();
void nullsub_220();
_DWORD *__usercall sub_4AF1E0@<eax>(int a1@<eax>);
void __usercall sub_4AF210(int *a1@<eax>);
void nullsub_217();
void nullsub_218();
int __usercall sub_4AF224@<eax>(int result@<eax>, char a2@<cl>);
_DWORD *__userpurge sub_4AF248@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_4AF28C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4AF290@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4AF2D4@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_4AF2EC@<al>(int a1@<eax>);
int __usercall sub_4AF308@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4AF350@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4AF3D4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AF3F8@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4AF428@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AF4E0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AF54C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4AF5FC@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4AF6D8@<eax>(_DWORD *result@<eax>);
int __usercall sub_4AF6F0@<eax>(int a1@<ecx>, int a2@<ebx>, int a3);
int __usercall sub_4AF740@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>);
_DWORD *__usercall sub_4AF798@<eax>(_DWORD *result@<eax>);
int __usercall sub_4AF7AC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4AF854@<eax>(
        int a1@<eax>,
        int **a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5,
        int a6,
        int a7,
        int a8);
// attributes: thunk
int __usercall sub_4AF8CA@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_DWORD *__usercall sub_4AF8D8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__fastcall sub_4AF9C4(volatile __int32 *a1, __int32 a2);
int __usercall sub_4AFA40@<eax>(int a1@<eax>);
int __usercall sub_4AFA48@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4AFAE0@<eax>(struct _EXCEPTION_REGISTRATION_RECORD *a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_4AFD8C@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>);
int sub_4AFDEC();
// bad sp value at call has been detected, the output may be wrong!
__int64 *__usercall sub_4AFDF0@<eax>(int a1@<eax>);
int __usercall sub_4AFE44@<eax>(int a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_4AFF80@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_4B000C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4B0098@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4B016C@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4B01A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4B01D0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B0224@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B0280@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4B0298@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
_DWORD *__usercall sub_4B03A0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B0460@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void nullsub_221();
_DWORD *__usercall sub_4B0498@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4B0548@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4B0564@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B05C8@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
OLECHAR **__usercall sub_4B05E4@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int (__fastcall ***a3)(int, int)@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
void nullsub_222();
int __usercall sub_4B06B4@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4B074C@<eax>(int a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4B0780@<eax>(int a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4B07D0@<eax>(_DWORD *a1@<eax>, __int64 *a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
void nullsub_223();
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_4B096C@<eax>(
        int a1@<eax>,
        __int64 *a2@<edx>,
        int a3@<ecx>,
        __int64 *a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
_DWORD *__usercall sub_4B0A18@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4B0A9C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4B0C54@<eax>(int a1@<eax>, int a2@<ecx>);
volatile __int32 *__usercall sub_4B0C70@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B0CAC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B0CC8@<eax>(int a1@<eax>, int a2@<ecx>);
char __usercall sub_4B0CE0@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4B0D28@<eax>(int result@<eax>, __int16 a2@<dx>);
char __usercall sub_4B0D48@<al>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_4B0D90@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4B0DBC@<eax>(int result@<eax>, __int16 a2@<dx>);
int __usercall sub_4B0DDC@<eax>(int result@<eax>, char a2@<dl>);
int __fastcall sub_4B0DF8(int a1, int a2);
int __usercall sub_4B0E04@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B0E20@<eax>(int result@<eax>, __int16 a2@<dx>);
_DWORD *__usercall sub_4B0E40@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>);
int __usercall sub_4B0EDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>, int a6@<esi>);
_DWORD *__usercall sub_4B0F84@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4B101C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
OLECHAR ***__usercall sub_4B106C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4B1168@<eax>(int a1@<eax>);
int __usercall sub_4B1174@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B11D8@<eax>(_BYTE *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1214@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_4B1230@<eax>(int result@<eax>, int a2@<ecx>);
OLECHAR ***__usercall sub_4B124C@<eax>(_DWORD *a1@<eax>, int a2@<edi>);
int *__usercall sub_4B1430@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1454@<eax>(int a1@<eax>, int a2@<edx>, signed int *a3@<ecx>);
int __usercall sub_4B1508@<eax>(int a1@<eax>);
int __usercall sub_4B150C@<eax>(int a1@<eax>);
int __usercall sub_4B1534@<eax>(int a1@<eax>);
int __usercall sub_4B1568@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B15A4@<eax>(int a1@<eax>);
int __userpurge sub_4B15B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4B1608@<eax>(_DWORD *a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, int a4);
int *__userpurge sub_4B1724@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int (__fastcall *a4)(unsigned int, int));
_BYTE *__usercall sub_4B17F8@<eax>(_BYTE *result@<eax>, char a2@<dl>);
int __usercall sub_4B1818@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_4B1830@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1844@<eax>(int a1@<eax>);
int __usercall sub_4B1854@<eax>(int result@<eax>, int (__fastcall *a2)(unsigned int, int)@<edx>);
int __usercall sub_4B188C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B18A8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B18E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_BYTE *__usercall sub_4B1924@<eax>(_BYTE *result@<eax>, char a2@<dl>);
__int64 __usercall sub_4B194C@<edx:eax>(int a1@<eax>);
int __userpurge sub_4B1974@<eax>(int a1@<eax>, int a2, int a3);
__int64 __usercall sub_4B1990@<edx:eax>(int a1@<eax>);
void nullsub_224();
int __userpurge sub_4B19E0@<eax>(int a1@<eax>, int a2, int a3);
_DWORD *__thiscall sub_4B1A48(void *this);
int __usercall sub_4B1ABC@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>);
__int64 __userpurge sub_4B1B40@<edx:eax>(int a1@<eax>, unsigned __int8 a2@<dl>, __int64 a3);
__int64 __userpurge sub_4B1BB0@<edx:eax>(int a1@<eax>, int a2, int a3);
int sub_4B1BE0();
int sub_4B1BE4();
int __userpurge sub_4B1BE8@<eax>(int a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5);
int __userpurge sub_4B1C4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_4B1C60@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1C70@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B1C7C@<eax>(int a1@<eax>);
int __usercall sub_4B1C8C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B1C98@<eax>(int a1@<eax>);
int __usercall sub_4B1CA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1CE8@<eax>(int a1@<eax>);
int __usercall sub_4B1CF8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1D38@<eax>(int a1@<eax>);
int __usercall sub_4B1D48@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1D88@<eax>(int a1@<eax>);
int __usercall sub_4B1D98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1DD8@<eax>(int a1@<eax>);
int __usercall sub_4B1DE8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1E28@<eax>(int a1@<eax>);
int __usercall sub_4B1E38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1E78@<eax>(int a1@<eax>);
int __usercall sub_4B1E88@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1EC8@<eax>(int a1@<eax>);
int __usercall sub_4B1ED8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1F18@<eax>(int a1@<eax>);
int __usercall sub_4B1F28@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1F68@<eax>(int a1@<eax>);
int __usercall sub_4B1F78@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B1FB8@<eax>(int a1@<eax>);
int __usercall sub_4B1FC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B2008@<eax>(int a1@<eax>);
int __usercall sub_4B2018@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B2038@<eax>(int a1@<eax>);
int __usercall sub_4B2048@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B206C@<eax>(int a1@<eax>);
int __usercall sub_4B207C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B20A4@<eax>(int a1@<eax>);
int __usercall sub_4B20B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B20EC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B2100@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B2114@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B2154@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B2168@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B21A8@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B21C0@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B2204@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B2218@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B2258@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B226C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4B22AC@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B22C4@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B2308@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B2320@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4B2364@<eax>(int a1@<eax>);
int __usercall sub_4B2378@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B23BC@<eax>(int a1@<eax>);
int __usercall sub_4B23D0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4B2414@<eax>(int a1@<eax>, char a2, int a3);
int __userpurge sub_4B242C@<eax>(int a1@<eax>, int a2@<edx>, char a3, int a4);
int __userpurge sub_4B2474@<eax>(int a1@<eax>, char a2, int a3);
int __userpurge sub_4B248C@<eax>(int a1@<eax>, int a2@<edx>, char a3, int a4);
int __userpurge sub_4B24D4@<eax>(int a1@<eax>, char a2);
int __userpurge sub_4B24EC@<eax>(int a1@<eax>, int a2@<edx>, char a3);
int __userpurge sub_4B2534@<eax>(int a1@<eax>, char a2, int a3);
int __userpurge sub_4B254C@<eax>(int a1@<eax>, int a2@<edx>, char a3, int a4);
int __userpurge sub_4B2594@<eax>(int a1@<eax>, char a2, int a3, int a4);
int __userpurge sub_4B25AC@<eax>(int a1@<eax>, int a2@<edx>, char a3, int a4, int a5);
int __usercall sub_4B25F4@<eax>(int a1@<eax>);
int __usercall sub_4B2604@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4B2644(void *this);
int __userpurge sub_4B2650@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_4B26E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B275C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B27C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2838@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B28A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2914@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2980@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B29F4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2A5C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2AD0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2B38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2BAC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2C18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2C8C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2CF8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2D6C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2DD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2E4C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2EB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B2F2C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B2F98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B300C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B3078@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B30EC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B3158@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B31CC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B3238@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B32AC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B3318@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B338C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B33F8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B346C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4B34E8(void *this);
int __userpurge sub_4B34F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_4B3580@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 __userpurge sub_4B35BC@<edx:eax>(
        int a1@<eax>,
        __int64 (__cdecl ***a2)(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *)@<edx>,
        __int64 a3);
int sub_4B36F0();
_DWORD *__fastcall sub_4B3758(int a1, int a2);
int sub_4B37B4();
OLECHAR **__usercall sub_4B37D8@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4@<ebx>, int a5@<edi>);
int __usercall sub_4B3A4C@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4B3B08@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5);
int __usercall sub_4B3B3C@<eax>(int *a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4@<edi>);
OLECHAR ***__usercall sub_4B3C08@<eax>(int a1@<eax>);
int __usercall sub_4B3DCC@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4B3DF0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
HDC __userpurge sub_4B3E2C@<eax>(int a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4@<edi>, DWORD a5);
DWORD __usercall sub_4B3E98@<eax>(int a1@<eax>, void *a2@<edx>, DWORD a3@<ecx>);
DWORD __usercall sub_4B3EA8@<eax>(int a1@<eax>, const void *a2@<edx>, DWORD a3@<ecx>);
HDC __userpurge sub_4B3EB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, DWORD a4);
__int64 __userpurge sub_4B3ED4@<edx:eax>(int a1@<eax>, char a2@<dl>, LONG a3, int a4);
int __usercall sub_4B3F00@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4B3F14@<eax>(HANDLE *a1@<eax>, int a2, int a3);
_DWORD *__userpurge sub_4B3F3C@<eax>(int a1@<eax>, char a2@<dl>, unsigned __int16 a3);
int __userpurge sub_4B3F80@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, __int16 a5);
int __usercall sub_4B40F8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4B412C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4B4134@<eax>(_DWORD *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __userpurge sub_4B416C@<eax>(_DWORD *a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4);
__int64 __userpurge sub_4B41FC@<edx:eax>(int a1@<eax>, char a2@<dl>, int a3, int a4);
int __usercall sub_4B4240@<eax>(int result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4B4258@<eax>(int a1@<eax>);
int __usercall sub_4B42B0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4B42DC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B42F4@<eax>(int *a1@<eax>, int (***a2)(void)@<edx>);
_DWORD *__usercall sub_4B432C@<eax>(int *a1@<eax>);
int __usercall sub_4B4380@<eax>(int *a1@<eax>);
int __usercall sub_4B43A8@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_4B4454@<eax>(int *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __userpurge sub_4B44A4@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__userpurge sub_4B4508@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
_DWORD *__userpurge sub_4B4560@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
_DWORD *__cdecl sub_4B45B4(int a1);
int __userpurge sub_4B4654@<eax>(int a1@<eax>, HMODULE a2@<edx>, const WCHAR *a3@<ecx>, int a4, const WCHAR *lpType);
int __usercall sub_4B46C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __userpurge sub_4B4728@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_4B478C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<edi>);
int __usercall sub_4B47B4@<eax>(int result@<eax>, int a2@<edx>);
int nullsub_271();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_272(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_273@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int __userpurge sub_4B641C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, __int32 a4, __int32 a5, int a6, int a7);
int __usercall sub_4B6474@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B64E4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4B6568@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4B66C8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B6700@<eax>(int a1@<eax>, int a2@<ecx>);
int sub_4B6748();
int __usercall sub_4B6918@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_4B69EC@<eax>(int result@<eax>);
int sub_4B6A8C();
int __usercall sub_4B6AC4@<eax>(_BYTE *a1@<eax>, wchar_t *a2@<edx>);
OLECHAR ***__usercall sub_4B6ADC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<edi>);
int __usercall sub_4B6B14@<eax>(int a1@<eax>);
int __usercall sub_4B6B7C@<eax>(int a1@<eax>, char a2@<dl>);
unsigned __int8 __userpurge sub_4B6BA0@<al>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4,
        int a5,
        void (__fastcall *a6)(int, int),
        int a7);
unsigned __int8 __userpurge sub_4B6C08@<al>(int a1@<eax>, int a2@<edx>, int a3, int a4, void (*a5)(void), int a6);
bool __usercall sub_4B6D10@<al>(int a1@<eax>);
int __usercall sub_4B6D24@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B6D40@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_4B6DFC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4B6E20@<eax>(int result@<eax>, int *a2@<edx>, int a3@<ecx>, _DWORD *a4);
__int64 __usercall sub_4B6E90@<edx:eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B6EE0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4B6F60@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B70A4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B70DC@<eax>(int *a1@<eax>);
int __usercall sub_4B7100@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4B713C@<eax>(int a1@<eax>, int (***a2)()@<edx>, void *a3@<ecx>);
int __usercall sub_4B71D0@<eax>(int *a1@<eax>);
int __usercall sub_4B71E8@<eax>(int a1@<eax>);
int sub_4B71F8();
__int64 *__usercall sub_4B720C@<eax>(__int64 *result@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR ***__userpurge sub_4B7260@<eax>(_DWORD *a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_4B72FC@<eax>(_DWORD *a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4@<edi>);
_DWORD *__usercall sub_4B7354@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_4B7428@<eax>(int *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B7458@<eax>(int *a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B74AC@<eax>(int *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B74DC@<eax>(int *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B750C@<eax>(int *a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B7550@<eax>(int *a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B7594@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B75F8@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B765C@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4B77D0@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B7944@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B7988@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B79CC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B7A14@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool sub_4B7A64();
int __thiscall sub_4B7A90(void *this);
int __usercall sub_4B7AF8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __cdecl sub_4B7BDC(int a1);
int __cdecl sub_4B7C24(int a1);
int __usercall sub_4B7CB8@<eax>(unsigned __int16 a1@<ax>, char a2@<dl>, int a3);
bool __cdecl sub_4B7D3C(int a1);
int __usercall sub_4B7D5C@<eax>(_DWORD **a1@<eax>, int a2);
int __cdecl sub_4B7DBC(int a1);
int __cdecl sub_4B7ECC(int a1);
int __cdecl sub_4B7F6C(int a1);
int __usercall sub_4B800C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_4B824C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4B82BC@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
double __usercall sub_4B838C@<st0>(int a1@<eax>);
double __usercall sub_4B83C4@<st0>(int a1@<eax>);
double __usercall sub_4B8408@<st0>(int a1@<eax>);
double __usercall sub_4B844C@<st0>(int a1@<eax>);
double __usercall sub_4B84AC@<st0>(int a1@<eax>);
OLECHAR ***__usercall sub_4B8500@<eax>(
        __int64 *a1@<eax>,
        volatile __int32 *a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
__int64 __usercall sub_4B8698@<edx:eax>(__int64 *a1@<eax>);
__int64 __usercall sub_4B8704@<edx:eax>(__int64 *a1@<eax>);
int __usercall sub_4B8748@<eax>(int a1@<eax>);
int __usercall sub_4B8750@<eax>(int a1@<eax>);
char __usercall sub_4B8758@<al>(__int64 *a1@<eax>, _BYTE *a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_4B8798@<eax>(int a1@<eax>, int a2);
int sub_4B8868();
_DWORD *__usercall sub_4B8884@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_BYTE *__usercall sub_4B8AF8@<eax>(_DWORD *a1@<eax>, int **a2@<edx>);
int __usercall sub_4B8B40@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, int a4);
VARIANTARG *__cdecl sub_4B8B80(int a1);
_DWORD *__usercall sub_4B8BDC@<eax>(int a1@<ebx>, int a2@<edi>, int a3@<esi>, int __saved_registers);
int __usercall sub_4B8C9C@<eax>(__int64 *a1@<eax>, _DWORD *a2@<edx>, __int32 a3@<ecx>, int a4@<edi>, int a5@<esi>);
char __usercall sub_4B8FC0@<al>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int *__usercall sub_4B9028@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
int __userpurge sub_4B935C@<eax>(
        void (__stdcall ***a1)(int *, struct _EXCEPTION_REGISTRATION_RECORD *, _DWORD, int)@<eax>,
        int *a2@<edx>,
        int a3@<ecx>,
        int a4@<edi>,
        void (*a5)(void),
        int a6);
int __usercall sub_4B944C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4B952C@<eax>(
        __int64 *a1@<eax>,
        volatile __int32 *a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
OLECHAR ***__usercall sub_4B95E4@<eax>(
        __int64 *a1@<eax>,
        volatile __int32 *a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
OLECHAR ***__usercall sub_4B980C@<eax>(__int64 *a1@<eax>, volatile __int32 *a2@<edx>, int a3@<edi>);
int __usercall sub_4B9820@<eax>(__int64 *a1@<eax>, int a2@<ecx>);
int __usercall sub_4B9834@<eax>(int *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4B9854@<eax>(__int64 *a1@<eax>, int a2@<edi>, int a3@<esi>);
int __cdecl sub_4B989C(int a1);
int __cdecl sub_4B98C8(int a1);
int __cdecl sub_4B98F8(int a1);
_DWORD *__usercall sub_4B995C@<eax>(__int64 *a1@<eax>, int a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
_DWORD *__usercall sub_4B9B0C@<eax>(int a1@<ecx>, int a2@<ebx>, int a3@<edi>, int a4@<esi>, int __return_address);
OLECHAR ***__usercall sub_4B9BC8@<eax>(int a1@<eax>, int a2@<edi>, int __return_address);
OLECHAR ***__usercall sub_4B9C80@<eax>(int a1@<eax>, int a2@<ecx>, int a3@<edi>, int a4);
int __usercall sub_4B9CD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
_DWORD *__usercall sub_4B9EC0@<eax>(__int64 *a1@<eax>, int a2@<edi>, int a3@<esi>);
int __usercall sub_4B9F08@<eax>(__int64 *a1@<eax>, char a2@<dl>, int a3@<edi>);
int __usercall sub_4B9FB4@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __usercall sub_4BA06C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_4BA084@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4BA0AC@<eax>(int a1@<eax>, void *a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_4BA120@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<edi>);
_DWORD *__usercall sub_4BA1B4@<eax>(_WORD *a1@<eax>, int a2@<edi>, int a3@<esi>, int a4);
int __usercall sub_4BA37C@<eax>(__int64 *a1@<eax>, VARIANTARG *a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
OLECHAR ***__usercall sub_4BA598@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<edi>);
int __fastcall sub_4BA5C4(int a1, int a2);
int __usercall sub_4BA5D0@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_4BA5F4(char a1, int a2, int (*a3)(void), int a4, int a5, int a6);
int __fastcall sub_4BA61C(char a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4BA648@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4BA658@<eax>(int a1@<eax>, int *a2@<edx>, _DWORD *a3@<ecx>);
// attributes: thunk
int sub_4BA6A0();
int __usercall sub_4BA6A8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4BA6E4@<eax>(int a1@<eax>, int a2@<edx>);
__int64 *__usercall sub_4BA6FC@<eax>(__int64 *result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4BA74C@<eax>(
        __int64 *a1@<eax>,
        int a2@<ecx>,
        void (__stdcall *a3)(struct _EXCEPTION_REGISTRATION_RECORD *),
        int a4);
int __usercall sub_4BA7D4@<eax>(int a1@<eax>);
OLECHAR ***__userpurge sub_4BA7EC@<eax>(int a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_4BA988@<eax>(int a1@<eax>, OLECHAR **a2@<edx>, int a3@<ecx>, int a4@<edi>);
int __usercall sub_4BA9E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4BAA1C@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4BAA78@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4BAAB8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4BAAF8@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4BAB54@<eax>(int a1@<eax>, __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4BABB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4BAC38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4BACC0@<eax>(int a1@<eax>, int a2@<edx>, __int64 a3);
int __userpurge sub_4BAE04@<eax>(int a1@<eax>, int a2@<edx>, __int64 a3);
int __userpurge sub_4BAF48@<eax>(int a1@<eax>, int a2@<edx>, char a3);
int __userpurge sub_4BAFE8@<eax>(int a1@<eax>, int a2@<edx>, char a3, int a4);
int __fastcall sub_4BB108(int a1, int a2, int a3, int a4, __int16 a5);
int __usercall sub_4BB13C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4BB290(int a1, char a2);
_DWORD *sub_4BB2A4();
_DWORD *sub_4BB2F4();
int __usercall sub_4BB344@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4BB3E4@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4BB464@<eax>(int a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_4BB5B8@<eax>(int a1@<eax>, int *a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
OLECHAR **__usercall sub_4BB96C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 *__userpurge sub_4BBA2C@<eax>(__int64 *a1@<eax>, int a2@<ecx>, char a3, int a4, int a5);
__int64 *__userpurge sub_4BBA50@<eax>(__int64 *a1@<eax>, int a2@<ecx>, char a3);
__int64 *__userpurge sub_4BBA74@<eax>(__int64 *a1@<eax>, int a2@<ecx>, char a3, int a4);
__int64 *__userpurge sub_4BBA98@<eax>(__int64 *a1@<eax>, int a2@<ecx>, int a3, int a4);
__int64 *__userpurge sub_4BBAD0@<eax>(__int64 *a1@<eax>, int a2@<ecx>, int a3, int a4);
__int64 *__usercall sub_4BBD2C@<eax>(__int64 *a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 *__userpurge sub_4BBDA0@<eax>(__int64 *a1@<eax>, int a2@<ecx>, __int64 a3);
int __thiscall sub_4BBDF8(void *this);
int __thiscall sub_4BBE00(void *this);
__int64 *__usercall sub_4BBE08@<eax>(__int64 *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4BBE50@<eax>(int a1@<eax>, OLECHAR *a2@<edx>);
char __usercall sub_4BBF18@<al>(int a1@<eax>, int *a2@<edx>, int *a3@<ecx>);
int __usercall sub_4BBF30@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
OLECHAR *__usercall sub_4BC064@<eax>(int a1@<eax>, int a2);
int __usercall sub_4BC118@<eax>(int a1@<eax>, int a2@<ecx>, int a3@<edi>, int a4);
_DWORD *__usercall sub_4BC2C8@<eax>(int a1@<ebx>, int a2@<edi>, int a3);
int __usercall sub_4BC3AC@<eax>(int a1@<ebx>, int a2@<edi>, int a3);
int __usercall sub_4BC498@<eax>(int a1@<ebx>, int a2@<edi>, int a3);
int __usercall sub_4BC58C@<eax>(int a1@<ebx>, int a2@<edi>, int a3);
bool __usercall sub_4BC688@<al>(int a1@<eax>, int a2@<edx>, int a3);
bool __cdecl sub_4BC6E8(int a1);
int __usercall sub_4BC740@<eax>(int a1@<ebx>, int a2);
int __usercall sub_4BC7C0@<eax>(int a1@<ebx>, int a2);
int __usercall sub_4BC88C@<eax>(int a1@<ebx>, int a2);
int __usercall sub_4BC968@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, int a3);
_DWORD *__cdecl sub_4BC9C0(int a1);
int __usercall sub_4BCA60@<eax>(int a1@<ebx>, int a2@<edi>, int a3);
_DWORD *__userpurge sub_4BCB44@<eax>(
        _DWORD *a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        _DWORD *a4@<ebx>,
        int a5@<edi>,
        int a6,
        int a7,
        void (__fastcall *a8)(int **, int *, int **, _DWORD *),
        int a9);
_DWORD *__cdecl sub_4BCCA8(int a1);
_DWORD *__usercall sub_4BCD10@<eax>(int a1@<eax>, int a2);
_DWORD *__usercall sub_4BCDA4@<eax>(int a1@<eax>, int a2@<edx>, int a3);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4BCE10@<eax>(int a1@<eax>, int a2);
_DWORD *__cdecl sub_4BCEB4(int a1);
__int64 *__cdecl sub_4BCFAC(int a1);
__int64 *__cdecl sub_4BCFEC(int a1);
_DWORD *__cdecl sub_4BD028(int a1);
int __usercall sub_4BD088@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4BD0A0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>, int a4);
int __cdecl sub_4BD1F0(int a1);
_DWORD *__usercall sub_4BD41C@<eax>(int a1@<ebx>, int a2);
_DWORD *__cdecl sub_4BD4F8(int a1);
VARIANTARG *__cdecl sub_4BD588(int a1);
char __usercall sub_4BD5EC@<al>(_BYTE *a1@<eax>, _DWORD *a2@<edx>, _DWORD **a3@<ecx>, _DWORD *a4@<ebx>, int a5@<edi>);
_DWORD *__usercall sub_4BD740@<eax>(__int64 *a1@<eax>, VARIANTARG *a2@<edx>);
_DWORD *__usercall sub_4BDB38@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
__int64 *__usercall sub_4BDB94@<eax>(__int64 *a1@<eax>);
OLECHAR ***__usercall sub_4BDBA4@<eax>(
        __int64 *a1@<eax>,
        const CHAR *a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
OLECHAR ***__usercall sub_4BDC4C@<eax>(__int64 *a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4BDDD4@<eax>(__int64 *a1@<eax>, int a2@<edx>, int a3@<edi>);
__int64 *__usercall sub_4BDE70@<eax>(__int64 *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __userpurge sub_4BDE84@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, _DWORD *a4, _DWORD *a5);
int nullsub_274();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_275(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_276@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
_DWORD *__usercall sub_4BF6E8@<eax>(int a1@<eax>, char a2@<dl>);
void nullsub_277();
_DWORD *__usercall sub_4BF72C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4BF77C@<eax>(int a1@<eax>);
int nullsub_278();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_279(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_280@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
HANDLE __thiscall sub_4C1084(void *this);
BOOL sub_4C10B8();
_DWORD *sub_4C10D0();
BOOL sub_4C114C();
DWORD __usercall sub_4C1158@<eax>(DWORD a1@<eax>);
BOOL sub_4C1174();
int __usercall sub_4C1180@<eax>(signed int a1@<eax>);
void __usercall  sub_4C13C0(_DWORD *a1@<eax>);
void nullsub_281();
// attributes: thunk
int __usercall sub_4C146C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4C1473@<eax>(int a1@<esi>);
_DWORD *__usercall sub_4C147C@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_4C14B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C15C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
BOOL sub_4C1648();
int __usercall sub_4C1670@<eax>(int result@<eax>, int a2@<ecx>);
_DWORD *__fastcall sub_4C16BC(int a1, DWORD a2);
void __fastcall sub_4C1738(int a1, char a2);
int __usercall sub_4C1750@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_4C1764@<eax>(int result@<eax>);
void nullsub_227();
int __usercall sub_4C177C@<eax>(_QWORD *a1@<eax>);
int sub_4C1848();
int __usercall sub_4C18B8@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_4C1964@<eax>(int a1@<eax>);
void __usercall sub_4C19A0(int a1@<eax>, unsigned __int8 a2@<dl>);
BOOL __usercall sub_4C19CC@<eax>(DWORD *a1@<eax>);
int __usercall sub_4C1A6C@<eax>(int result@<eax>, char a2@<dl>);
// attributes: thunk
DWORD sub_4C1A78();
int __userpurge sub_4C1A80@<eax>(OLECHAR *a1@<eax>, int a2@<edi>, OLECHAR *a3, OLECHAR *a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C1B0C@<eax>(OLECHAR *a1@<eax>, int a2@<edx>, int a3@<edi>);
int __userpurge sub_4C1BD8@<eax>(OLECHAR *a1@<eax>, OLECHAR **a2@<ecx>, int a3@<edi>, OLECHAR *a4, OLECHAR *a5);
int __userpurge sub_4C1C78@<eax>(int a1@<eax>, void *a2@<ecx>, int a3, int a4);
int __userpurge sub_4C1D80@<eax>(OLECHAR *a1@<eax>, OLECHAR **a2@<ecx>, int a3@<edi>, OLECHAR *a4, OLECHAR *a5);
_DWORD *__fastcall sub_4C1D94(char a1, int a2);
_DWORD *__userpurge sub_4C1F34@<eax>(_DWORD *a1@<eax>, int a2, int a3);
_DWORD *__usercall sub_4C1F68@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __userpurge sub_4C1FD0@<eax>(_DWORD *a1@<eax>, int a2@<ecx>, int a3, int a4);
_DWORD *__usercall sub_4C2060@<eax>(OLECHAR *a1@<eax>, int a2@<edx>, int a3@<edi>);
_DWORD *__usercall sub_4C2144@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __userpurge sub_4C21E0@<eax>(_DWORD *a1@<eax>, int a2@<ecx>, int a3, int a4);
int __usercall sub_4C21F4@<eax>(int a1@<eax>, void *a2@<ecx>);
int __thiscall sub_4C22A0(void *this, int a2, int a3);
int __usercall sub_4C22B4@<eax>(int result@<eax>, char a2@<dl>);
void __usercall sub_4C22DC(DWORD a1@<eax>);
// attributes: thunk
BOOL sub_4C22E4(void);
int __usercall sub_4C22F4@<eax>(int a1@<eax>);
void __usercall sub_4C2364(int a1@<eax>);
int __usercall sub_4C23B4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4C2478@<eax>(const CHAR *a1@<eax>);
_DWORD *__usercall sub_4C24E0@<eax>(int a1@<eax>, ULONG_PTR a2@<edx>);
_DWORD *__usercall sub_4C25AC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4C25FC@<al>(int a1@<eax>);
_DWORD *__usercall sub_4C2618@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C2664@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C26B4@<eax>(int result@<eax>);
_DWORD *__usercall sub_4C26C0@<eax>(_DWORD *result@<eax>, int a2@<ecx>);
int __usercall sub_4C2760@<eax>(int result@<eax>);
int sub_4C279C();
__int64 __usercall sub_4C27A4@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_4C27B8@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_4C27CC@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C2820@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C28B0@<eax>(_BYTE *a1@<eax>, int *a2@<edx>);
_DWORD *__usercall sub_4C2968@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4C29A0@<eax>(int a1@<eax>);
int __usercall sub_4C2A10@<eax>(int result@<eax>, int a2@<ecx>);
int __userpurge sub_4C2A4C@<eax>(int result@<eax>, int a2@<edx>, int a3, int a4);
_DWORD *__usercall sub_4C2A70@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C2AD4@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4C2AF0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_4C2B50@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int sub_4C2BE8();
void __stdcall sub_4C2BEC(int a1, int a2);
int sub_4C2BF4();
void nullsub_229();
volatile __int32 *__usercall sub_4C2C0C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_4C2C20@<eax>(int a1@<eax>);
void nullsub_231();
int sub_4C2C28();
void nullsub_232();
int __usercall sub_4C2C30@<eax>(int result@<eax>);
int __usercall sub_4C2C3C@<eax>(int result@<eax>);
int __usercall sub_4C2C48@<eax>(int result@<eax>);
void nullsub_230();
int __usercall sub_4C2C58@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4C2C60(int a1, int a2);
char __userpurge sub_4C2C68@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
void __fastcall sub_4C2D14(int a1, int *a2);
void nullsub_233();
int nullsub_282();
int __usercall sub_4C335C@<eax>(int a1@<eax>, int a2@<edx>, unsigned int *a3@<ecx>);
int __usercall sub_4C33DC@<eax>(int a1@<eax>, int a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_4C3400@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4C3490@<eax>(int a1@<eax>, __int32 a2@<edx>);
int __usercall sub_4C34C4@<eax>(int a1@<eax>, int a2@<ecx>);
void __stdcall sub_4C34E0(int a1, int a2);
int __usercall sub_4C3514@<eax>(int a1@<eax>);
int __usercall sub_4C3524@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C37E0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C3888@<eax>(int result@<eax>, int a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_4C38D8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C3900@<eax>(int a1@<edx>, int a2@<ebx>);
int __usercall sub_4C393C@<eax>(int a1@<edx>, int a2@<ebx>);
int __usercall sub_4C3978@<eax>(int result@<eax>, char a2@<dl>);
int sub_4C398C();
void nullsub_228();
_DWORD *__usercall sub_4C3994@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4C3A4C@<eax>(int a1@<eax>);
int __usercall sub_4C3A64@<eax>(int result@<eax>);
void __stdcall sub_4C3A74(int a1);
int __stdcall sub_4C3A7C(int a1, int a2, _DWORD *a3);
int __usercall sub_4C3B00@<eax>(int a1@<eax>, int (__stdcall ***a2)(_DWORD, int, int)@<edx>);
BOOL __usercall sub_4C3B80@<eax>(_DWORD *a1@<eax>, int (__stdcall ***a2)(_DWORD, int, int)@<edx>, char a3@<cl>);
void (***__usercall sub_4C3C28@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>))(void);
void nullsub_87();
int __usercall sub_4C3C70@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C3CA4@<eax>(int result@<eax>, int a2@<ecx>);
void __usercall sub_4C3CBC(int a1@<eax>);
int __usercall sub_4C3CD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char sub_4C3D04();
void __stdcall sub_4C3D08(int a1, int a2);
bool __usercall sub_4C3D10@<al>(int a1@<eax>);
_DWORD *__usercall sub_4C3D34@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C3D78@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int sub_4C3DE8();
int sub_4C3DEC();
void nullsub_235();
int sub_4C3DF4();
int __usercall sub_4C3E00@<eax>(int a1@<eax>);
int __usercall sub_4C3E10@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
void nullsub_234();
char __usercall sub_4C3E3C@<al>(int a1@<eax>, int a2@<ecx>);
char __usercall sub_4C3E58@<al>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4C3E74@<eax>(_DWORD *a1@<eax>, int a2, int a3);
int __usercall sub_4C3ED0@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_4C3EE4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C3EF0@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4C3F30@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __userpurge sub_4C3F5C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, char a4);
int __usercall sub_4C3FA8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __stdcall sub_4C3FE0(int a1, int a2, int a3, int *a4);
int __stdcall sub_4C4048(int a1, int a2, int a3, int *a4);
int __stdcall sub_4C40B0(int a1, int a2, int a3, unsigned int a4, __int64 *a5);
int __stdcall sub_4C4144(int a1, __int64 a2);
int __stdcall sub_4C41A8(int a1, int a2, __int64 a3, _QWORD *a4, _QWORD *a5);
int __stdcall sub_4C43B0(int a1, int a2);
int __stdcall sub_4C43BC(int a1);
int __stdcall sub_4C43C8(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_4C43D4(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_4C43E0(int a1, int a2, int a3);
int __stdcall sub_4C444C(int a1, _DWORD *a2);
_DWORD *sub_4C4464();
// attributes: thunk
int __usercall sub_4C44D4@<eax>(void *a1@<eax>, void *a2@<ecx>);
_DWORD *__usercall sub_4C44DC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_BYTE *__usercall sub_4C4610@<eax>(_BYTE *result@<eax>);
_DWORD *__userpurge sub_4C461C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_4C4678@<eax>(_BYTE *a1@<eax>);
int __usercall sub_4C46A4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C4740@<eax>(int result@<eax>);
int __usercall sub_4C47A0@<eax>(int result@<eax>);
bool __cdecl sub_4C4804(int a1);
bool __cdecl sub_4C482C(int a1);
bool __cdecl sub_4C4860(int a1);
bool __cdecl sub_4C4894(int a1);
int __usercall sub_4C48BC@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __userpurge sub_4C4A0C(int a1@<eax>, int a2@<edx>, void (*a3)(void), int a4);
char __usercall sub_4C4A78@<al>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C4A98@<eax>(int a1@<eax>, int a2@<edx>);
__int64 __usercall sub_4C4AAC@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_4C4AC0@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_4C4AD4@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_4C4AE8@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_4C4AFC@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_4C4B08@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_4C4B14@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_4C4B20@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __thiscall sub_4C4B2C(void (__cdecl **this)(int, int, int), int a2, int a3, int a4, int a5);
int __usercall sub_4C4B4C@<eax>(int a1@<eax>, int a2@<edx>);
int __stdcall sub_4C4B54(int a1, int a2);
int __usercall sub_4C4BEC@<eax>(int result@<eax>);
unsigned int __usercall sub_4C4C00@<eax>(unsigned int result@<eax>, unsigned int a2@<edx>);
int __usercall sub_4C4C3C@<eax>(int a1@<eax>, int a2@<edx>);
void sub_4C4C6C();
HWND __stdcall sub_4C4CEC(int a1, int a2);
int __usercall sub_4C4DA0@<eax>(HWND a1@<eax>);
_DWORD *__userpurge sub_4C4DC8@<eax>(int a1@<eax>, char a2@<dl>, int **a3@<ecx>, int a4);
_DWORD *__usercall sub_4C4E78@<eax>(int a1@<eax>, char a2@<dl>, void *a3@<ecx>);
_DWORD *__userpurge sub_4C4EC0@<eax>(int a1@<eax>, char a2@<dl>, void *a3@<ecx>, char a4);
int __userpurge sub_4C4F14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, char a5, int a6);
int __userpurge sub_4C5034@<eax>(int a1@<eax>, char a2@<dl>, int a3, char a4, int a5);
int __userpurge sub_4C5098@<eax>(int a1@<eax>, char a2@<dl>, char a3);
int __usercall sub_4C50F4@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_4C5144@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4C5170@<eax>(int a1@<eax>);
int __usercall sub_4C51A0@<eax>(int a1@<eax>);
int __usercall sub_4C51BC@<eax>(int a1@<eax>, int *a2@<edx>, OLECHAR **a3@<ecx>);
int __usercall sub_4C5250@<eax>(int result@<eax>, int a2@<edx>, int __saved_registers);
_DWORD *__usercall sub_4C52D4@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<edi>);
bool __usercall sub_4C54BC@<al>(int a1@<eax>, int a2@<edi>);
int __usercall sub_4C54FC@<eax>(int result@<eax>);
int __usercall sub_4C5504@<eax>(int a1@<eax>, int a2@<edi>);
int __userpurge sub_4C5544@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4C55D0@<eax>(int a1@<eax>, int a2);
int __usercall sub_4C55E4@<eax>(int a1@<eax>, int a2@<edi>);
_DWORD *__usercall sub_4C5630@<eax>(int a1@<eax>, __int64 **a2@<edx>);
unsigned __int8 __usercall sub_4C576C@<al>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<edi>);
OLECHAR *__usercall sub_4C57B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
_DWORD *sub_4C5898();
int __stdcall sub_4C58BC(int a1, int a2);
_DWORD *__userpurge sub_4C5914@<eax>(_DWORD *result@<eax>, char a2@<dl>, int a3, int a4);
_DWORD *__userpurge sub_4C5948@<eax>(int a1@<eax>, int a2, int a3);
_DWORD *__userpurge sub_4C5A38@<eax>(int a1@<eax>, int a2, int a3);
_DWORD *__usercall sub_4C5B30@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_4C5C48@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __usercall sub_4C5CA0@<eax>(int a1@<eax>, int a2@<edx>);
int sub_4C5D04();
int __userpurge sub_4C5FA8@<eax>(
        int a1@<eax>,
        volatile __int32 *a2@<edx>,
        volatile __int32 *a3@<ecx>,
        volatile __int32 *a4);
_DWORD *__usercall sub_4C6048@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __userpurge sub_4C608C@<eax>(int a1@<eax>, int a2@<ecx>, _BYTE *a3, int a4, int a5);
_DWORD *__usercall sub_4C60B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C60FC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool __usercall sub_4C6128@<al>(int a1@<eax>);
_DWORD *__userpurge sub_4C614C@<eax>(
        int a1@<eax>,
        _DWORD *a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        int (__stdcall ***a7)(_DWORD, int, int));
int __usercall sub_4C63B0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4C63C8@<eax>(int a1@<edx>, _DWORD *a2@<ecx>, int a3@<edi>);
_DWORD *__usercall sub_4C6518@<eax>(int a1@<edx>, _DWORD *a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4C6694@<eax>(int a1@<edx>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
int __usercall sub_4C6764@<eax>(int a1@<edx>, _DWORD *a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4C6850@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_4C6868@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>, int a4);
int __thiscall sub_4C69B4(void *this);
void nullsub_78();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C6A48@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C6B6C@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
int __usercall sub_4C6C14@<eax>(unsigned __int8 a1@<al>, _BYTE *a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C6C24@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
int __usercall sub_4C6CCC@<eax>(unsigned __int8 a1@<al>, _BYTE *a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_4C6CDC@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
int __usercall sub_4C6DC0@<eax>(unsigned __int8 a1@<al>, _BYTE *a2@<edx>);
void nullsub_79();
int __thiscall sub_4C6DE0(void *this);
int __usercall sub_4C6ECC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C6F24@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4C6FA0@<eax>(int a1@<eax>);
int __usercall sub_4C7080@<eax>(int a1@<eax>);
int __usercall sub_4C70C8@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4C70F8@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __thiscall sub_4C714C(void *this);
int __usercall sub_4C7158@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C717C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4C7184@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_4C726C@<eax>(int a1@<eax>);
int __usercall sub_4C7274@<eax>(int a1@<eax>);
int __usercall sub_4C728C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C7348@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C73E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C7428@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>);
int __fastcall sub_4C7510(int a1, int a2);
// attributes: thunk
int sub_4C7538();
int __usercall sub_4C7540@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C7558@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C75D0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C7674@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C7714@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4C774C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4C7784@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4C77EC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4C77F8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C7884@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4C7960@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C7A80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>, int a6@<esi>);
_DWORD *__usercall sub_4C7B04@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4C7BA8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C7C14@<eax>(int result@<eax>, int a2@<edx>);
int sub_4C7CD0();
int __fastcall sub_4C7CF0(int a1, int a2);
_DWORD *__usercall sub_4C7D10@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4C7D18@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_4C7EAC(void *this);
_DWORD *__userpurge sub_4C7EC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4);
_DWORD *__usercall sub_4C7F08@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C7F74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4C808C(int a1, int a2);
int __usercall sub_4C80A0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C80B8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C80D0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4C8120(int a1, int a2);
int __usercall sub_4C8138@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C8174@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4C81F0@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4C8228@<eax>(int a1@<eax>);
int __usercall sub_4C82A0@<eax>(int a1@<eax>);
int __usercall sub_4C82C8@<eax>(int a1@<eax>);
int __usercall sub_4C82F4@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4C8330@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
_DWORD *__usercall sub_4C837C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4C8408@<eax>(int a1@<eax>);
int __usercall sub_4C8418@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C8430@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4C8444();
_DWORD *__usercall sub_4C844C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4C8490@<al>(int a1@<eax>);
int __usercall sub_4C84B0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C84D4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4C84DC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C8590@<eax>(int a1@<eax>);
int __usercall sub_4C8598@<eax>(int a1@<eax>);
int __usercall sub_4C85B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C86A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C86EC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4C87A0();
int __usercall sub_4C87A8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C87C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C8838@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C88DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C897C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4C89B4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4C89EC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4C8A54@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4C8A60@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4C8AB4(void *this);
int __usercall sub_4C8AE0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4C8BB4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C8CE0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4C8D58@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4C8DD0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C8E3C@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_4C8EF8(int a1, int a2);
int sub_4C8F18();
int __usercall sub_4C8F38@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4C8F40@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4C90DC@<eax>(int a1@<eax>);
int __usercall sub_4C9108@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C9128@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int sub_4C9208();
int __usercall sub_4C9214@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C922C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4C927C(int a1, int a2);
int __usercall sub_4C9294@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C92D0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4C9324@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4C935C@<eax>(int result@<eax>);
int __usercall sub_4C938C@<eax>(int a1@<eax>);
int __usercall sub_4C93B4@<eax>(int a1@<eax>);
int __usercall sub_4C93E0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4C941C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4C9468@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4C94B4@<eax>(int a1@<eax>);
int sub_4C94C4();
_DWORD *__usercall sub_4C94E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4C9524@<al>(int a1@<eax>);
int __usercall sub_4C9544@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4C9568@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4C9570@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_4C9624@<eax>(int a1@<eax>);
int __usercall sub_4C962C@<eax>(int a1@<eax>);
int __usercall sub_4C9644@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C973C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4C9780@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4C9834();
int __usercall sub_4C983C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4C9854@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C98CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4C9970@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4C9A10@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4C9A48(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4C9A80@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4C9AE8@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4C9AF4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4C9B48(void *this);
int __usercall sub_4C9B74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4C9C48@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4C9D74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4C9DEC@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4C9E64@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4C9ED0@<eax>(int result@<eax>, int a2@<edx>);
int sub_4C9F8C();
int sub_4C9FAC();
int __usercall sub_4C9FCC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4C9FD4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4CA170@<eax>(int a1@<eax>);
int __usercall sub_4CA19C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CA1BC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CA2A8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CA2C0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4CA310(int a1, int a2);
int __usercall sub_4CA328@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CA364@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4CA3B8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CA3F0@<eax>(int result@<eax>);
int __usercall sub_4CA420@<eax>(int a1@<eax>);
int __usercall sub_4CA448@<eax>(int a1@<eax>);
int __usercall sub_4CA474@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4CA4B0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4CA4FC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CA548@<eax>(int a1@<eax>);
int __usercall sub_4CA558@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4CA574@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4CA5B8@<al>(int a1@<eax>);
int __usercall sub_4CA5D8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CA5FC@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_4CA6B8@<eax>(int a1@<eax>);
int __usercall sub_4CA6C0@<eax>(int a1@<eax>);
int __usercall sub_4CA6D8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CA7D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CA814@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4CA8C8();
int __usercall sub_4CA8D0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CA8E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CA960@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CAA04@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CAAA4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4CAADC(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4CAB14@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4CAB7C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4CAB88@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4CABDC(void *this);
int __usercall sub_4CAC08@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4CACDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4CAE08@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4CAE80@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4CAEF8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CAF64@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_4CB020(int a1, int a2);
int sub_4CB040();
int __usercall sub_4CB060@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4CB068@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4CB204@<eax>(int a1@<eax>);
int __usercall sub_4CB230@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CB250@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CB330@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CB33C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CB354@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4CB3A4(int a1, int a2);
int __usercall sub_4CB3BC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CB3F8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4CB44C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CB484@<eax>(int result@<eax>);
int __usercall sub_4CB4B4@<eax>(int a1@<eax>);
int __usercall sub_4CB4DC@<eax>(int a1@<eax>);
int __usercall sub_4CB508@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4CB544@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4CB590@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CB5DC@<eax>(int a1@<eax>);
int __usercall sub_4CB5EC@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4CB608@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4CB64C@<al>(int a1@<eax>);
_DWORD *__usercall sub_4CB66C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4CB684(volatile signed __int8 ***a1, int a2);
int __usercall sub_4CB760@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CB784@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_4CB78C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CB884@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_4CB8CC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_4CB9FC@<eax>(int a1@<eax>);
int __usercall sub_4CBA24@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CBAD0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4CBB40@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4CBBF4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4CBC44@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4CBC94@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4CBD14@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, unsigned __int8 a5);
// attributes: thunk
int sub_4CBE6C();
int __usercall sub_4CBE74@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CBE8C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CBEA4@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4CBEDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_4CBF14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4CBFCC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_4CC0B8@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_4CC1A8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CC1E4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CC248@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4CC2A0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_4CC330@<eax>(int *a1@<eax>, int a2@<edi>);
BOOL __usercall sub_4CC408@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_4CC464@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_4CC4CC@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CC4F0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CC590@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CC5A8@<eax>(int a1@<eax>);
int __usercall sub_4CC5C8@<eax>(int a1@<eax>);
int __usercall sub_4CC5E8@<eax>(int a1@<eax>);
int __fastcall sub_4CC5F8(volatile signed __int8 ***a1, int a2);
int __usercall sub_4CC684@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CC6A8@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4CC6B0@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CC764@<eax>(int a1@<eax>);
int __usercall sub_4CC76C@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4CC774();
_DWORD *__usercall sub_4CC77C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CC7B8@<eax>(int a1@<eax>);
int __usercall sub_4CC7C8@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CC7E0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4CC804@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CC848@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__fastcall sub_4CC880(volatile signed __int8 ***a1, int a2);
int __usercall sub_4CC944@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CC968@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4CC970@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_4CCA58@<eax>(int a1@<eax>);
int __usercall sub_4CCA60@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4CCA68();
_DWORD *__usercall sub_4CCA70@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CCAAC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4CCABC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
_DWORD *__usercall sub_4CCAD4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4CCAF4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_4CCB08();
_DWORD *__usercall sub_4CCB10@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CCB54@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_4CCB8C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4CCBC0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_4CCBD4();
_DWORD *__usercall sub_4CCBDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CCC20@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_4CCC58@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CCC7C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4CCC84@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CCD38@<eax>(int a1@<eax>);
int __usercall sub_4CCD40@<eax>(int a1@<eax>);
int __usercall sub_4CCD58@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CCE50@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CCE94@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4CCF48();
int __usercall sub_4CCF50@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CCF68@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CCFE0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CD084@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CD124@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4CD15C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4CD194@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4CD1FC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4CD208@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4CD25C(void *this);
int __usercall sub_4CD288@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4CD35C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4CD488@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4CD500@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4CD578@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CD5E4@<eax>(int result@<eax>, int a2@<edx>);
int sub_4CD6A0();
int sub_4CD6C0();
int __usercall sub_4CD6E0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4CD6E8@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4CD884@<eax>(int a1@<eax>);
int __usercall sub_4CD8B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CD8D0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CD9BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CD9D4@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4CDA24(int a1, int a2);
int __usercall sub_4CDA3C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CDA78@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4CDACC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CDB04@<eax>(int result@<eax>);
int __usercall sub_4CDB34@<eax>(int a1@<eax>);
int __usercall sub_4CDB5C@<eax>(int a1@<eax>);
int __usercall sub_4CDB88@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4CDBC4@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4CDC10@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CDC5C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4CDC88@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4CDCCC@<al>(int a1@<eax>);
int __usercall sub_4CDCEC@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __fastcall sub_4CDD08(volatile signed __int8 ***a1, int a2);
int __usercall sub_4CDDE4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CDE08@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_4CDE10@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CDF08@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_4CDF50@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_4CE080@<eax>(int a1@<eax>);
int __usercall sub_4CE0A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CE154@<eax>(int a1@<eax>);
int __userpurge sub_4CE220@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4CE270@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, __int32 a5);
int __usercall sub_4CE2C0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4CE2F4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
int __usercall sub_4CE450@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CE468@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CE480@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4CE4B8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_4CE4F0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4CE5A8@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_4CE694@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_4CE784@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CE7C0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CE824@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4CE844@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_4CE894@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_4CE96C@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_4CE9AC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_4CEA14@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CEA38@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CEAD8@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CEAF0@<eax>(int a1@<eax>);
int __usercall sub_4CEB10@<eax>(int a1@<eax>);
int __usercall sub_4CEB30@<eax>(int a1@<eax>);
int __usercall sub_4CEB40@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4CEB48();
_DWORD *__usercall sub_4CEB50@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CEB8C@<eax>(int a1@<eax>);
int __usercall sub_4CEB9C@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_4CEBB4@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_4CEBD4@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int sub_4CEBE8();
_DWORD *__usercall sub_4CEBF0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CEC34@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_4CEC6C(volatile signed __int8 ***a1, int a2);
int __usercall sub_4CECF8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CED1C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4CED24@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CEDD8@<eax>(int a1@<eax>);
int __usercall sub_4CEDE0@<eax>(int a1@<eax>);
// attributes: thunk
int sub_4CEDE8();
_DWORD *__usercall sub_4CEDF0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CEE2C@<eax>(int a1@<eax>);
int __usercall sub_4CEE3C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CEE54@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4CEE78@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CEEBC@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_4CEEF4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CEF28@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4CEF3C();
_DWORD *__usercall sub_4CEF44@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CEF88@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_4CEFC0@<eax>(int a1@<eax>);
int __usercall sub_4CEFD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CF0D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CF114@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4CF1C8();
int __usercall sub_4CF1D0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4CF1E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CF260@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4CF304@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4CF3A4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4CF3DC(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4CF414@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4CF47C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4CF488@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4CF4DC(void *this);
int __usercall sub_4CF508@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4CF5DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4CF708@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4CF780@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4CF7F8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CF864@<eax>(int result@<eax>, int a2@<edx>);
int sub_4CF920();
int sub_4CF940();
int __usercall sub_4CF960@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4CF968@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4CFB04@<eax>(int a1@<eax>);
int __usercall sub_4CFB30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CFB50@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4CFC3C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4CFC54@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4CFCA4(int a1, int a2);
int __usercall sub_4CFCBC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CFCF8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4CFD4C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4CFD84@<eax>(int result@<eax>);
int __usercall sub_4CFDB4@<eax>(int a1@<eax>);
int __usercall sub_4CFDDC@<eax>(int a1@<eax>);
int __usercall sub_4CFE08@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4CFE44@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4CFE90@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4CFEDC@<eax>(int a1@<eax>);
int __usercall sub_4CFEEC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_4CFF00();
_DWORD *__usercall sub_4CFF08@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4CFF4C@<al>(int a1@<eax>);
int __usercall sub_4CFF6C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4CFF90@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4CFF98@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D004C@<eax>(int a1@<eax>);
int __usercall sub_4D0054@<eax>(int a1@<eax>);
int __usercall sub_4D006C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D0164@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D01A8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4D025C();
int __usercall sub_4D0264@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D027C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D02F4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D0398@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D0438@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D0470(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D04A8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D0510@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D051C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D0570(void *this);
int __usercall sub_4D059C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D0670@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D079C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D0814@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D088C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D08F8@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D09B4();
int sub_4D09D4();
int __usercall sub_4D09F4@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D09FC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D0B98@<eax>(int a1@<eax>);
int __usercall sub_4D0BC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D0BE4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D0CD0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D0CE8@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D0D38(int a1, int a2);
int __usercall sub_4D0D50@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D0D8C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D0DE0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D0E18@<eax>(int result@<eax>);
int __usercall sub_4D0E48@<eax>(int a1@<eax>);
int __usercall sub_4D0E70@<eax>(int a1@<eax>);
int __usercall sub_4D0E9C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D0ED8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D0F24@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D0F70@<eax>(int a1@<eax>);
int __usercall sub_4D0F80@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4D0F9C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D0FE0@<al>(int a1@<eax>);
_DWORD *__usercall sub_4D1000@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_4D102C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __userpurge sub_4D1070@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, char a4);
int __userpurge sub_4D10B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, char a4);
int __usercall sub_4D10F8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D1150@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4D11CC@<eax>(int a1@<eax>);
int __usercall sub_4D12AC@<eax>(unsigned int a1@<eax>);
int __usercall sub_4D12F4@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4D1324@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __thiscall sub_4D1378(void *this);
int __usercall sub_4D1384@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D13A8@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D13B0@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D1464@<eax>(int a1@<eax>);
int __usercall sub_4D146C@<eax>(int a1@<eax>);
int __usercall sub_4D1484@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D157C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D15C0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __fastcall sub_4D1674(int a1, int a2);
// attributes: thunk
int sub_4D169C();
int __usercall sub_4D16A4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D16BC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D1734@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D17D8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D1878@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D18B0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D18E8@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D1950@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D195C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D19B0(void *this);
int __usercall sub_4D19DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D1AB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D1BDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D1C54@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D1CCC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D1D38@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D1DF4();
int sub_4D1E14();
int __usercall sub_4D1E34@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D1E3C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D1FD8@<eax>(int a1@<eax>);
int __usercall sub_4D2004@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D2024@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D2110@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D2128@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D2178(int a1, int a2);
int __usercall sub_4D2190@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D21CC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D2220@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D2258@<eax>(int result@<eax>);
int __usercall sub_4D2288@<eax>(int a1@<eax>);
int __usercall sub_4D22B0@<eax>(int a1@<eax>);
int __usercall sub_4D22DC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D2318@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D2364@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D23B0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4D23DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D2420@<al>(int a1@<eax>);
int __usercall sub_4D2440@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D2464@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D246C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D2520@<eax>(int a1@<eax>);
int __usercall sub_4D2528@<eax>(int a1@<eax>);
int __usercall sub_4D2540@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D2638@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D267C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4D2730();
int __usercall sub_4D2738@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D2750@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D27C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D286C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D290C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D2944(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D297C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D29E4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D29F0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D2A44(void *this);
int __usercall sub_4D2A70@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D2B44@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D2C70@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D2CE8@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D2D60@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D2DCC@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D2E88();
int sub_4D2EA8();
int __usercall sub_4D2EC8@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D2ED0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D306C@<eax>(int a1@<eax>);
int __usercall sub_4D3098@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D30B8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D31A4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D31BC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D320C(int a1, int a2);
int __usercall sub_4D3224@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D3260@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D32B4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D32EC@<eax>(int result@<eax>);
int __usercall sub_4D331C@<eax>(int a1@<eax>);
int __usercall sub_4D3344@<eax>(int a1@<eax>);
int __usercall sub_4D3370@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D33AC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D33F8@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D3444@<eax>(int a1@<eax>);
int __usercall sub_4D3454@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4D3470@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D34B4@<al>(int a1@<eax>);
int __usercall sub_4D34D4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D34F8@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D3500@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D35B4@<eax>(int a1@<eax>);
int __usercall sub_4D35BC@<eax>(int a1@<eax>);
int __usercall sub_4D35D4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D36CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D3710@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4D37C4();
int __usercall sub_4D37CC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D37E4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D385C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D3900@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D39A0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D39D8(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D3A10@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D3A78@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D3A84@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D3AD8(void *this);
int __usercall sub_4D3B04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D3BD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D3D04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D3D7C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D3DF4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D3E60@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D3F1C();
int sub_4D3F3C();
int __usercall sub_4D3F5C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D3F64@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D4100@<eax>(int a1@<eax>);
int __usercall sub_4D412C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D414C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D422C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D4238@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D4250@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D42A0(int a1, int a2);
int __usercall sub_4D42B8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D42F4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D4348@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D4380@<eax>(int result@<eax>);
int __usercall sub_4D43B0@<eax>(int a1@<eax>);
int __usercall sub_4D43D8@<eax>(int a1@<eax>);
int __usercall sub_4D4404@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D4440@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D448C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D44D8@<eax>(int a1@<eax>);
int __usercall sub_4D44E8@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4D4504@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D4548@<al>(int a1@<eax>);
int __usercall sub_4D4568@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D45C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4D463C@<eax>(int a1@<eax>);
int __usercall sub_4D4764@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4D4794@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __thiscall sub_4D47E8(void *this);
int __usercall sub_4D47F4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D4818@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D4820@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D48D4@<eax>(int a1@<eax>);
int __usercall sub_4D48DC@<eax>(int a1@<eax>);
int __usercall sub_4D48F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D49EC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D4A30@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __fastcall sub_4D4AE4(int a1, int a2);
// attributes: thunk
int sub_4D4B0C();
int __usercall sub_4D4B14@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D4B2C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D4BA4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D4C48@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D4CE8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D4D20(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D4D58@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D4DC0@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D4DCC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D4E20(void *this);
int __usercall sub_4D4E4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D4F20@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D504C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D50C4@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D513C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D51A8@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D5264();
int sub_4D5284();
int __usercall sub_4D52A4@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D52AC@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D5448@<eax>(int a1@<eax>);
int __usercall sub_4D5474@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D5494@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D5580@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D5598@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D55E8(int a1, int a2);
int __usercall sub_4D5600@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D563C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D5690@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D56C8@<eax>(int result@<eax>);
int __usercall sub_4D56F8@<eax>(int a1@<eax>);
int __usercall sub_4D5720@<eax>(int a1@<eax>);
int __usercall sub_4D574C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D5788@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D57D4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D5820@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4D584C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D5890@<al>(int a1@<eax>);
int __usercall sub_4D58B0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D58D4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D58DC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_4D5990@<eax>(int a1@<eax>);
int __usercall sub_4D5998@<eax>(int a1@<eax>);
int __usercall sub_4D59B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D5AA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D5AEC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_4D5BA0();
int __usercall sub_4D5BA8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D5BC0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D5C38@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D5CDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D5D7C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D5DB4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D5DEC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D5E54@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D5E60@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D5EB4(void *this);
int __usercall sub_4D5EE0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D5FB4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D60E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D6158@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D61D0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D623C@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_4D62F8(int a1, int a2);
int sub_4D6318();
int __usercall sub_4D6338@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D6340@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D64DC@<eax>(int a1@<eax>);
int __usercall sub_4D6508@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D6528@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D6614@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D662C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D667C(int a1, int a2);
int __usercall sub_4D6694@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D66D0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D6724@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D675C@<eax>(int result@<eax>);
int __usercall sub_4D678C@<eax>(int a1@<eax>);
int __usercall sub_4D67B4@<eax>(int a1@<eax>);
int __usercall sub_4D67E0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D681C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D6868@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D68B4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4D68E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D6924@<al>(int a1@<eax>);
int __usercall sub_4D6944@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D699C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_4D6A18@<eax>(int a1@<eax>);
int __usercall sub_4D6AF8@<eax>(unsigned int a1@<eax>);
int __usercall sub_4D6B40@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_4D6B70@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __thiscall sub_4D6BC4(void *this);
int __usercall sub_4D6BD0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4D6BF4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_4D6BFC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D6CB0@<eax>(int a1@<eax>);
int __usercall sub_4D6CB8@<eax>(int a1@<eax>);
int __usercall sub_4D6CD0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D6DC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D6E0C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __fastcall sub_4D6EC0(int a1, int a2);
// attributes: thunk
int sub_4D6EE8();
int __usercall sub_4D6EF0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D6F08@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D6F80@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D7024@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D70C4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D70FC(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D7134@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D719C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D71A8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D71FC(void *this);
int __usercall sub_4D7228@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D72FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4D7428@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_4D74A0@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D7518@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D7584@<eax>(int result@<eax>, int a2@<edx>);
int sub_4D7640();
int sub_4D7660();
int __usercall sub_4D7680@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D7688@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_4D7824@<eax>(int a1@<eax>);
int __usercall sub_4D7850@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D7870@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D795C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D7974@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D79C4(int a1, int a2);
int __usercall sub_4D79DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D7A18@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D7A6C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D7AA4@<eax>(int result@<eax>);
int __usercall sub_4D7AD4@<eax>(int a1@<eax>);
int __usercall sub_4D7AFC@<eax>(int a1@<eax>);
int __usercall sub_4D7B28@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D7B64@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D7BB0@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4D7BFC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4D7C28@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D7C6C@<al>(int a1@<eax>);
_DWORD *__fastcall sub_4D7C8C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4D7CAC(_DWORD *a1, int a2);
_DWORD *__usercall sub_4D7CD4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D7D10@<eax>(int a1@<eax>);
_DWORD *__fastcall sub_4D7D1C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4D7D3C(_DWORD *a1, int a2);
__int64 *__fastcall sub_4D7D64(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4D7D90(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4D7DBC(int a1, int a2, int a3, int a4);
bool __usercall sub_4D7DE0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D7E04@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4D7E64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4D7F1C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4D7F3C(_DWORD *a1, int a2);
__int64 *__fastcall sub_4D7F64(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4D7F90(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4D7FBC(int a1, int a2, int a3, int a4);
bool __usercall sub_4D7FE0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D8004@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4D8064@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4D811C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4D813C(_DWORD *a1, int a2);
__int64 *__fastcall sub_4D8164(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4D8190(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4D81BC(int a1, int a2, int a3, int a4);
bool __usercall sub_4D81E0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D8204@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4D8264@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
__int64 *__fastcall sub_4D831C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4D8348(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4D8374(int a1, int a2, int a3, int a4);
bool __usercall sub_4D8398@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D83BC@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4D841C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_4D84D4@<eax>(int a1@<eax>);
int __usercall sub_4D84EC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D85AC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D8660@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D86A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D87B8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D87D0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D8848@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D88EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D898C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D89C4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D89FC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D8A64@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D8A70@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D8AD4(void *this);
int __usercall sub_4D8AE8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D8AF4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D8B00@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D8BE0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4D8D04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D8DA0@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4D8E58@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_4D8EC4@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_4D8FF8();
int sub_4D9018();
int __usercall sub_4D9038@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4D9040@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_4D91D4(void *this);
_DWORD *__userpurge sub_4D91F0@<eax>(int a1@<eax>, int a2);
int __usercall sub_4D9240@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D92D4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4D9414(int a1, int a2);
int __usercall sub_4D9428@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D9440@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D9458@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4D94A8(int a1, int a2);
int __usercall sub_4D94C0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D94FC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4D9580@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D95B8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D9658@<eax>(int a1@<eax>);
int __usercall sub_4D9680@<eax>(int a1@<eax>);
int __usercall sub_4D96AC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4D96E8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4D9728@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4D9734@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_4D97C8@<eax>(int a1@<eax>);
int __usercall sub_4D97D8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D97F0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4D9804();
_DWORD *__usercall sub_4D980C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4D9850@<al>(int a1@<eax>);
_DWORD *__usercall sub_4D9870@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_4D9890@<eax>(_DWORD *a1@<eax>);
int __usercall sub_4D98B0@<eax>(int a1@<eax>);
int __usercall sub_4D98C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D9984@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4D9A20@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D9A64@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>);
// attributes: thunk
int sub_4D9B4C();
int __usercall sub_4D9B54@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4D9B6C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D9BE4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4D9C88@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4D9D28@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4D9D60(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4D9D98@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4D9E00@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4D9E0C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4D9E6C(void *this);
int __usercall sub_4D9E80@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D9E8C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4D9E98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4D9F74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4DA094@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>, int a6@<esi>);
_DWORD *__usercall sub_4DA118@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4DA1BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4DA228@<eax>(int result@<eax>, int a2@<edx>);
int sub_4DA2E4();
int sub_4DA304();
_DWORD *__usercall sub_4DA324@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4DA32C@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_4DA4C0(void *this);
_DWORD *__userpurge sub_4DA4DC@<eax>(int a1@<eax>, _DWORD *a2);
_DWORD *__usercall sub_4DA51C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4DA588@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4DA6A0(int a1, int a2);
int __usercall sub_4DA6B4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DA6CC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4DA6E4@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4DA734(int a1, int a2);
int __usercall sub_4DA74C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DA788@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4DA804@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4DA83C@<eax>(int a1@<eax>);
int __usercall sub_4DA8B4@<eax>(int a1@<eax>);
int __usercall sub_4DA8DC@<eax>(int a1@<eax>);
int __usercall sub_4DA908@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4DA944@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4DA984@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_4DA990@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_4DAA1C@<eax>(int a1@<eax>);
int __usercall sub_4DAA2C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DAA44@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4DAA58();
_DWORD *__usercall sub_4DAA60@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4DAAA4@<al>(int a1@<eax>);
_DWORD *__fastcall sub_4DAAC4(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DAAE4(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DAB0C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DAB38(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DAB64(int a1, int a2, int a3, int a4);
bool __usercall sub_4DAB88@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DABAC@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DAC0C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_4DACC4@<eax>(int a1@<eax>);
int __usercall sub_4DACDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DAD9C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DAE50@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DAE94@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DAFA8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_4DAFC0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4DB038@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4DB0DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DB17C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_4DB1B4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_4DB1EC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_4DB254@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4DB260@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_4DB2C4(void *this);
int __usercall sub_4DB2D8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DB2E4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DB2F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DB3D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_4DB4F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DB590@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_4DB648@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_4DB6B4@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_4DB7E8();
int sub_4DB808();
int __usercall sub_4DB828@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_4DB830@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_4DB9C4(void *this);
_DWORD *__userpurge sub_4DB9E0@<eax>(int a1@<eax>, int a2);
int __usercall sub_4DBA30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4DBAC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_4DBC04(int a1, int a2);
int __usercall sub_4DBC18@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DBC30@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4DBC48@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_4DBC98(int a1, int a2);
int __usercall sub_4DBCB0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DBCEC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_4DBD70@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DBDA8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4DBE48@<eax>(int a1@<eax>);
int __usercall sub_4DBE70@<eax>(int a1@<eax>);
int __usercall sub_4DBE9C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_4DBED8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_4DBF18@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_4DBF24@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_4DBFB8@<eax>(int a1@<eax>);
int __usercall sub_4DBFC8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4DBFE0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_4DBFF4();
_DWORD *__usercall sub_4DBFFC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_4DC040@<al>(int a1@<eax>);
_DWORD *__usercall sub_4DC060@<eax>(_DWORD *a1@<eax>);
_DWORD *__fastcall sub_4DC080(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DC0A0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DC0C8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DC0F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DC120(int a1, int a2, int a3, int a4);
bool __usercall sub_4DC144@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DC168@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DC1C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DC280(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DC2A0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DC2C8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DC2F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DC320(int a1, int a2, int a3, int a4);
bool __usercall sub_4DC344@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DC368@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DC3C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DC480(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DC4A0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DC4C8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DC4F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DC520(int a1, int a2, int a3, int a4);
bool __usercall sub_4DC544@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DC568@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DC5C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DC680(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DC6A0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DC6C8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DC6F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DC720(int a1, int a2, int a3, int a4);
bool __usercall sub_4DC744@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DC768@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DC7C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DC880(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DC8A0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DC8C8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DC8F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DC920(int a1, int a2, int a3, int a4);
bool __usercall sub_4DC944@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DC968@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DC9C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DCA80(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DCAA0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DCAC8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DCAF4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DCB20(int a1, int a2, int a3, int a4);
bool __usercall sub_4DCB44@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DCB68@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DCBC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DCC80(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DCCA0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DCCC8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DCCF4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DCD20(int a1, int a2, int a3, int a4);
bool __usercall sub_4DCD44@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DCD68@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DCDC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DCE80(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DCEA0(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DCEC8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DCEF4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DCF20(int a1, int a2, int a3, int a4);
bool __usercall sub_4DCF44@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DCF68@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DCFC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_4DD080@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DD0BC@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_4DD0C8@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_4DD1EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DD228@<eax>(int a1@<eax>);
int __userpurge sub_4DD234@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DD300@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DD33C@<eax>(int a1@<eax>);
int __userpurge sub_4DD348@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_4DD414@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__fastcall sub_4DD4E0(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DD500(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DD528(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DD558(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DD588(int a1, int a2, int a3, int a4);
bool __usercall sub_4DD5B0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DD5D4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DD634@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DD6EC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DD70C(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DD734(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DD760(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DD78C(int a1, int a2, int a3, int a4);
bool __usercall sub_4DD7B0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DD7D4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DD834@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_4DD8EC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DD90C(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DD934(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DD960(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DD98C(int a1, int a2, int a3, int a4);
bool __usercall sub_4DD9B0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DD9D4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DDA34@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_4DDAEC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DDB28@<eax>(int a1@<eax>);
int __userpurge sub_4DDB34@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__fastcall sub_4DDC00(int a1, _DWORD *a2);
_DWORD *__fastcall sub_4DDC20(_DWORD *a1, int a2);
__int64 *__fastcall sub_4DDC48(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_4DDC78(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_4DDCA8(int a1, int a2, int a3, int a4);
bool __usercall sub_4DDCD0@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4DDCF4@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_4DDD54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_4DDE0C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DDE48@<eax>(int a1@<eax>);
int __userpurge sub_4DDE54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DDF20@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DDF5C@<eax>(int a1@<eax>);
int __userpurge sub_4DDF68@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE034@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE070@<eax>(int a1@<eax>);
int __userpurge sub_4DE07C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE148@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE184@<eax>(int a1@<eax>);
int __userpurge sub_4DE190@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE25C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE298@<eax>(int a1@<eax>);
int __userpurge sub_4DE2A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE370@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE3AC@<eax>(int a1@<eax>);
int __userpurge sub_4DE3B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE484@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE4C0@<eax>(int a1@<eax>);
int __userpurge sub_4DE4CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE598@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE5D4@<eax>(int a1@<eax>);
int __userpurge sub_4DE5E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE6AC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE6E8@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_4DE6F8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_4DE848@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE884@<eax>(int a1@<eax>);
int __userpurge sub_4DE890@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_4DE95C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DE998@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_4DE9A4@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_4DEAC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4DEB04@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_4DEB14@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
__int32 __usercall sub_4DF3D1@<eax>(int a1@<eax>);
int __stdcall sub_4DF3DD(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4DF3E7(int a1);
signed __int32 __stdcall sub_4DF3F1(int a1);
int nullsub_283();
__int32 __usercall sub_4DFB45@<eax>(int a1@<eax>);
int __stdcall sub_4DFB51(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4DFB5B(int a1);
signed __int32 __stdcall sub_4DFB65(int a1);
int nullsub_284();
int nullsub_285();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_286(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_287@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_288();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_289(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_290@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_291();
int nullsub_292();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_293(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_294@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_295();
int nullsub_296();
int nullsub_297();
int nullsub_298();
int nullsub_299();
int nullsub_300();
__int32 __usercall sub_4E79C1@<eax>(int a1@<eax>);
int __stdcall sub_4E79CD(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4E79D7(int a1);
signed __int32 __stdcall sub_4E79E1(int a1);
int nullsub_301();
__int32 __usercall sub_4E8119@<eax>(int a1@<eax>);
int __stdcall sub_4E8125(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4E812F(int a1);
signed __int32 __stdcall sub_4E8139(int a1);
int nullsub_302();
__int32 __usercall sub_4E8D5D@<eax>(int a1@<eax>);
int __stdcall sub_4E8D69(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4E8D73(int a1);
signed __int32 __stdcall sub_4E8D7D(int a1);
int nullsub_303();
__int32 __usercall sub_4E9615@<eax>(int a1@<eax>);
int __stdcall sub_4E9621(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_4E962B(int a1);
signed __int32 __stdcall sub_4E9635(int a1);
int nullsub_304();
int nullsub_305();
int nullsub_306();
__int64 __userpurge sub_4EC32C@<edx:eax>(_QWORD *a1@<eax>, __int64 a2);
__int64 __userpurge sub_4EC344@<edx:eax>(_QWORD *a1@<eax>, __int64 a2);
int __userpurge sub_4EC35C@<eax>(int a1@<eax>, __int64 a2);
int __usercall sub_4EC3A0@<eax>(int a1@<eax>, int a2@<edx>);
WCHAR *__usercall sub_4EC3EC@<eax>(int a1@<eax>);
int __usercall sub_4EC440@<eax>(int a1@<eax>, int a2@<edx>);
unsigned __int64 __stdcall sub_4EC448(int a1);
int __usercall sub_4EC484@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
void sub_4EC48C();
bool __usercall sub_4EC494@<al>(int a1@<eax>);
int __usercall sub_4EC4A0@<eax>(int a1@<eax>, const void *a2@<edx>, int *a3@<ecx>);
unsigned int *__stdcall sub_4EC5A4(_DWORD *a1, unsigned int a2);
int __stdcall sub_4EC690(int a1);
int __stdcall sub_4ECA00(int a1);
volatile __int32 *__stdcall sub_4ECA78(int *a1, char a2);
int *__userpurge sub_4ECBDC@<eax>(__int64 *a1@<eax>, char a2@<dl>, char a3@<cl>, int a4, int a5);
int __usercall sub_4ED0D0@<eax>(_DWORD *a1@<eax>, unsigned __int16 *a2@<edx>);
int __usercall sub_4ED3EC@<eax>(int result@<eax>);
int sub_4ED4AC();
__int32 __usercall sub_4ED578@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall WICConvertBitmapSource(
        REFWICPixelFormatGUID dstFormat,
        IWICBitmapSource *pISrc,
        IWICBitmapSource **ppIDst);
void sub_4ED590();
int __usercall sub_4EDDF0@<eax>(int *a1@<eax>);
__int64 sub_4EDE28();
int __usercall sub_4EDEF8@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_4EE024@<al>(int *a1@<eax>, int *a2@<edx>);
int *__usercall sub_4EE3B0@<eax>(int *a1@<eax>);
char __usercall sub_4EE45C@<al>(int a1@<eax>, __int32 a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__userpurge sub_4EE67C@<eax>(_DWORD *result@<eax>, int a2, int a3);
int *__userpurge sub_4EE690@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4EE770@<eax>(int a1@<eax>, int a2, int a3);
int *__userpurge sub_4EE790@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6);
_DWORD *__usercall sub_4EE8BC@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_4EE988@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
double __userpurge sub_4EE9A0@<st0>(int *a1@<eax>, double a2);
double __userpurge sub_4EEA10@<st0>(int *a1@<eax>, double a2);
_DWORD *__usercall sub_4EEA30@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_4EEAD4@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
int __fastcall sub_4EEAEC(int a1, int a2);
int __stdcall sub_4EEB00(double a1);
int __stdcall sub_4EEB20(double a1);
int __stdcall sub_4EEB40(double a1);
int __stdcall sub_4EEB60(double a1);
int __stdcall sub_4EEB80(double a1);
_DWORD *__userpurge sub_4EEBA0@<eax>(_DWORD *a1@<eax>, int a2, int a3);
double __usercall sub_4EEBB8@<st0>(__int64 *a1@<eax>);
bool __usercall sub_4EEC34@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
bool __usercall sub_4EEC50@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
int __fastcall sub_4EEC6C(int a1, int a2);
_DWORD *__userpurge sub_4EEC80@<eax>(__int64 *a1@<eax>, _DWORD *a2@<edx>, double a3);
bool __usercall sub_4EEDAC@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
bool __usercall sub_4EEDC8@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
_DWORD *__usercall sub_4EEDE4@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4EEE6C@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
bool __usercall sub_4EEE80@<al>(_QWORD *a1@<eax>, _QWORD *a2@<edx>);
int __fastcall sub_4EEE98(int a1, _DWORD *a2);
_DWORD *__usercall sub_4EEEFC@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
int __fastcall sub_4EEF08(int a1, int a2);
_DWORD *__usercall sub_4EEF20@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_4EEFEC@<eax>(int *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4EF1D4@<eax>(__int32 a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_4EF268@<eax>(_DWORD *a1@<eax>, double a2, double a3);
double __userpurge sub_4EF2C8@<st0>(__int64 *a1@<eax>, double a2);
int sub_4EF360();
void sub_4EF3D4();
_DWORD *__userpurge sub_4EF3DC@<eax>(__int64 *a1@<eax>, __int32 a2@<edx>, char a3@<cl>, volatile __int32 *a4);
int __usercall sub_4EF50C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __fastcall sub_4EF5E0(int a1, _BYTE *a2);
int __thiscall sub_4EF634(void *this);
int __usercall sub_4EF640@<eax>(int a1@<eax>, char a2@<dl>, void *a3@<ecx>);
int __usercall sub_4EF6B8@<eax>(unsigned __int16 a1@<ax>, unsigned __int16 *a2@<edx>);
int sub_4EF720();
int __usercall sub_4EF734@<eax>(int a1@<eax>);
int __usercall sub_4EF770@<eax>(unsigned __int16 a1@<ax>);
char __usercall sub_4EF77C@<al>(unsigned __int16 a1@<ax>);
bool __usercall sub_4EF790@<al>(char a1@<al>);
int __usercall sub_4EF798@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_4EF7A0@<al>(__int16 a1@<ax>);
int __usercall sub_4EF7C4@<eax>(int a1@<edi>);
void sub_4EFA50();
bool __usercall sub_4F0A50@<al>(_WORD *a1@<eax>);
int __usercall sub_4F0A68@<eax>(char a1@<al>);
char __usercall sub_4F0A98@<al>(int a1@<eax>);
_DWORD *__userpurge sub_4F0AC0@<eax>(unsigned __int8 *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, volatile __int32 *a4);
int __usercall sub_4F0BA4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_4F0BE8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4F0C24@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool __usercall sub_4F0C50@<al>(int a1@<eax>, int a2@<edx>);
HKEY __usercall sub_4F0C5C@<eax>(int a1@<eax>);
HKEY __usercall sub_4F0C8C@<eax>(int a1@<eax>, HKEY a2@<edx>);
volatile __int32 *__usercall sub_4F0CB8@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
int __usercall sub_4F0CDC@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_4F0CF0@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_4F0CF4@<eax>(int a1@<eax>, __int32 a2@<edx>);
BOOL __usercall sub_4F0DE4@<eax>(int a1@<eax>, __int32 a2@<edx>, char a3@<cl>);
BOOL __usercall sub_4F0F18@<eax>(int a1@<eax>, __int32 a2@<edx>);
int __usercall sub_4F1120@<eax>(int a1@<eax>, __int32 a2@<edx>);
bool __usercall sub_4F12EC@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4F1310@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4F137C@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4F1444@<eax>(int a1@<eax>, __int64 **a2@<edx>);
volatile __int32 *__usercall sub_4F15B4@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_4F15EC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4F16B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4F1708@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_4F1730@<eax>(int a1@<eax>, int a2@<edx>);
int __thiscall sub_4F1758(_DWORD *this);
int __thiscall sub_4F178C(_DWORD *this);
volatile signed __int8 *__usercall sub_4F17C0@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
OLECHAR ***__userpurge sub_4F187C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>, __int64 **a4);
int sub_4F1A38();
__int64 sub_4F1A4C();
bool sub_4F1A88();
int __stdcall sub_4F1AA0(char a1, int a2);
double sub_4F1AB4();
int __stdcall sub_4F1AE8(char a1, int a2);
double sub_4F1AFC();
int __stdcall sub_4F1B30(char a1, int a2);
double sub_4F1B44();
int __stdcall sub_4F1B78(char a1, int a2);
double sub_4F1B8C();
int __stdcall sub_4F1BA0(char a1, int a2);
double sub_4F1BB4();
int __stdcall sub_4F1BC8(DWORD cbData);
DWORD __userpurge sub_4F1BDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, signed int a4);
char __userpurge sub_4F1C40@<al>(int a1@<eax>, int a2@<edx>, BYTE *a3@<ecx>, char a4, DWORD cbData);
DWORD __userpurge sub_4F1CB4@<eax>(LPBYTE lpData@<ecx>, int a2@<eax>, int a3@<edx>, char *a4, DWORD cbData);
bool __usercall sub_4F1D30@<al>(int a1@<eax>);
int __usercall sub_4F1D54@<eax>(int a1@<eax>, int a2@<edx>);
HKEY __usercall sub_4F1D64@<eax>(int a1@<eax>, __int32 a2@<edx>);
int __usercall sub_4F1DFC@<eax>(int a1@<eax>, int a2@<edx>, HKEY a3@<ecx>);
int __usercall sub_4F1E38@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __usercall sub_4F1EC8@<eax>(int a1@<eax>, __int32 a2@<edx>);
BOOL __usercall sub_4F1F4C@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_4F1FB0@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_4F1FC4@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>, int a4);
BOOL __usercall sub_4F2068@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_4F20CC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
BOOL __usercall sub_4F20E0@<eax>(int a1@<eax>, __int32 a2@<edx>);
volatile signed __int8 **__usercall sub_4F2158@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4F21F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4F2314@<eax>(HKEY a1@<eax>, unsigned int a2@<edx>, int a3);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_4F244C@<eax>(HKEY a1@<eax>, int a2@<edx>, int a3);
HKEY __userpurge sub_4F26A8@<eax>(int a1@<eax>, __int32 a2@<edx>, __int32 a3@<ecx>, char a4);
// attributes: thunk
int __usercall sub_4F276C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4F278A@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4F2A54@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
char __usercall sub_4F2A64@<al>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4F31C0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
char __usercall sub_4F31D0@<al>(int a1@<eax>, _DWORD *a2@<edx>);
int sub_4F31E0();
int __usercall sub_4F4874@<eax>(__int32 a1@<eax>, int a2@<ebx>);
int __usercall sub_4F49B0@<eax>(unsigned int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_4F4A38@<eax>(__int32 a1@<eax>, int *a2@<edx>);
int sub_4F4B2C();
void __userpurge nullsub_307(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
void nullsub_308();
int __userpurge nullsub_309@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_310();
__int32 __usercall sub_4F7F45@<eax>(int a1@<eax>);
__int32 __usercall sub_4F7F52@<eax>(int a1@<eax>);
int __cdecl sub_4F7F5F(int a1);
int __stdcall sub_4F7F6D(int a1);
int __stdcall sub_4F7F77(int a1);
HPALETTE __usercall sub_4FAB1C@<eax>(HPALETTE result@<eax>);
int __usercall sub_4FAEEC@<eax>(_BYTE *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4FAF00@<eax>(int a1@<eax>, char a2@<dl>, __int16 a3@<cx>);
void __usercall sub_4FAF3C(_DWORD *a1@<eax>, char a2@<dl>);
volatile signed __int8 **__usercall sub_4FAF78@<eax>(int a1@<eax>, __int64 *a2@<edx>);
// attributes: thunk
int __usercall sub_4FB074@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_4FB088(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int __usercall sub_4FB123@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_4FB158(int a1@<eax>, _DWORD *a2@<edx>, __int64 *a3@<ecx>);
// attributes: thunk
int __usercall sub_4FB1D1@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void nullsub_314();
void __usercall sub_4FB1E4(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_4FB269@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_4FB298(int a1@<eax>);
// attributes: thunk
int __usercall sub_4FB30E@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __thiscall sub_4FB31C(void *this);
signed int __usercall sub_4FB3CC@<eax>(signed int result@<eax>);
int __usercall sub_4FB3DC@<eax>(int result@<eax>, int a2@<ecx>);
void __usercall sub_4FB3F0(int a1@<eax>);
void __usercall sub_4FB400(int a1@<eax>);
char __usercall sub_4FB740@<al>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4FB750@<eax>(void *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_4FB85C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FB8BC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FB8F0@<eax>(int a1@<eax>, int a2@<ecx>);
void __usercall sub_4FB90C(_DWORD *a1@<eax>, int (***a2)(void)@<edx>, int a3@<ecx>);
int __usercall sub_4FB9E0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_4FB9F8(_DWORD *a1@<eax>, __int64 *a2@<edx>);
_DWORD *__usercall sub_4FBA48@<eax>(_DWORD *result@<eax>, int a2@<edx>);
bool __usercall sub_4FBA58@<al>(int a1@<eax>);
int __usercall sub_4FBA84@<eax>(int a1@<eax>);
void __usercall sub_4FBCBC(_DWORD *a1@<eax>, void *a2@<edx>);
int __usercall sub_4FBCE4@<eax>(int a1@<eax>);
void __usercall sub_4FBCEC(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4FBD20@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
void __usercall sub_4FBD7C(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FBDD8@<eax>(int a1@<eax>);
void __usercall sub_4FBDF4(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FBE14@<eax>(int a1@<eax>);
void __usercall sub_4FBE20(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FBE60@<eax>(int a1@<eax>);
int __usercall sub_4FBE68@<eax>(int a1@<eax>);
void __usercall sub_4FBE74(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_4FBEAC(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FBEE8@<eax>(int a1@<eax>);
void __usercall sub_4FBEF0(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FBF28@<eax>(int a1@<eax>);
void __usercall sub_4FBF30(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FBF68@<eax>(int result@<eax>, int *a2@<edx>);
int __usercall sub_4FC078@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FC0C4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_4FC0F8(_DWORD *a1@<eax>, int (***a2)(void)@<edx>, int a3@<ecx>);
int __usercall sub_4FC1B0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_4FC1C8(_DWORD *a1@<eax>, __int64 *a2@<edx>);
int __usercall sub_4FC218@<eax>(int a1@<eax>);
void __usercall sub_4FC220(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FC250@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_4FC2EE@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_4FC300(_DWORD *a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_4FC324@<eax>(_BYTE *result@<eax>, char a2@<dl>);
int __usercall sub_4FC334@<eax>(int a1@<eax>);
void __usercall sub_4FC33C(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FC36C@<eax>(int a1@<eax>);
void __usercall sub_4FC374(_DWORD *a1@<eax>, int a2@<edx>);
void *__usercall sub_4FC3A8@<eax>(void *result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_4FC430@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FC478@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_4FC4AC(_DWORD *a1@<eax>, int (***a2)(void)@<edx>, int a3@<ecx>);
int __usercall sub_4FC554@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_4FC570(_DWORD *a1@<eax>, __int64 *a2@<edx>);
int __usercall sub_4FC5C0@<eax>(int a1@<eax>);
void __usercall sub_4FC5C8(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FC5EC@<eax>(int a1@<eax>);
void __usercall sub_4FC5F4(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_4FC654@<eax>(int a1@<eax>);
void __usercall sub_4FC748(_DWORD *a1@<eax>, void *a2@<edx>);
int __usercall sub_4FC76C@<eax>(int a1@<eax>);
void __usercall sub_4FC774(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FC7D0@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_4FC7E4@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_4FC7F8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_4FC810(int a1@<eax>);
int __usercall sub_4FC838@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_4FC850@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_4FC87C@<eax>(int a1@<eax>, int a2@<edx>);
__int64 __usercall sub_4FC89C@<edx:eax>(int a1@<eax>, int a2@<edx>);
BOOL __usercall sub_4FC8BC@<eax>(int a1@<eax>);
void __usercall sub_4FC918(int a1@<eax>);
int __usercall sub_4FC940@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FCA04@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __userpurge sub_4FCA60@<eax>(
        int y1@<ecx>,
        int x1@<edx>,
        HDC *a3@<eax>,
        int y4,
        int x4,
        int y3,
        int x3,
        int y2,
        int x2);
int __userpurge sub_4FCAB8@<eax>(
        int top@<ecx>,
        int left@<edx>,
        HDC *a3@<eax>,
        int yr2,
        int xr2,
        int yr1,
        int xr1,
        int bottom,
        int right);
int __userpurge sub_4FCB10@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>, FLOAT SweepAngle, FLOAT StartAngle, DWORD r);
void __userpurge sub_4FCB58(int a1@<eax>, int *a2@<edx>, unsigned int a3@<ecx>, int a4, int *a5);
// attributes: thunk
int __usercall sub_4FCDBC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FCDDE@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FCE03@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_4FCE1C@<eax>(
        int y1@<ecx>,
        int x1@<edx>,
        HDC *a3@<eax>,
        int y4,
        int x4,
        int y3,
        int x3,
        int y2,
        int x2);
int __userpurge sub_4FCE74@<eax>(int a1@<eax>, int *a2@<edx>, HDC *a3@<ecx>, int *a4);
int __userpurge sub_4FCEFC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_4FCFB0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4, int a5);
int __usercall sub_4FD06C@<eax>(HDC *a1@<eax>, const RECT *a2@<edx>);
int __userpurge sub_4FD0A0@<eax>(int top@<ecx>, int left@<edx>, HDC *a3@<eax>, int bottom, int right);
int __usercall sub_4FD0E8@<eax>(int a1@<eax>, const RECT *a2@<edx>);
int __userpurge sub_4FD124@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>, unsigned __int8 a4, COLORREF color);
int __usercall sub_4FD174@<eax>(int a1@<eax>, const RECT *a2@<edx>);
int __usercall sub_4FD1B8@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>);
BOOL __usercall sub_4FD1F0@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>);
int __userpurge sub_4FD21C@<eax>(
        int top@<ecx>,
        int left@<edx>,
        HDC *a3@<eax>,
        int yr2,
        int xr2,
        int yr1,
        int xr1,
        int bottom,
        int right);
int __usercall sub_4FD274@<eax>(HDC *a1@<eax>, const POINT *a2@<edx>, int a3@<ecx>);
int __usercall sub_4FD2B0@<eax>(HDC *a1@<eax>, const POINT *a2@<edx>, int a3@<ecx>);
int __usercall sub_4FD2EC@<eax>(HDC *a1@<eax>, const POINT *a2@<edx>, int a3@<ecx>);
int __usercall sub_4FD328@<eax>(HDC *a1@<eax>, const POINT *a2@<edx>, int a3@<ecx>);
int __userpurge sub_4FD364@<eax>(int top@<ecx>, int left@<edx>, HDC *a3@<eax>, int bottom, int right);
// attributes: thunk
int sub_4FD3AC();
int __userpurge sub_4FD3B4@<eax>(
        int top@<ecx>,
        int left@<edx>,
        HDC *a3@<eax>,
        int height,
        int width,
        int bottom,
        int right);
int __usercall sub_4FD404@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4FD440@<eax>(int a1@<eax>);
int __userpurge sub_4FD46C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, UINT c);
int __userpurge sub_4FD514@<eax>(HDC *a1@<eax>, RECT *a2@<edx>, int a3@<ecx>, UINT c, int y);
_DWORD *__fastcall sub_4FD5C8(int *a1, struct tagRECT *a2, int a3);
BOOL __usercall sub_4FD6A8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, struct tagSIZE *a3@<ecx>);
int __usercall sub_4FD6FC@<eax>(int a1@<eax>);
int __usercall sub_4FD714@<eax>(int a1@<eax>);
BOOL __usercall sub_4FD720@<eax>(HDC *a1@<eax>, struct tagPOINT *a2@<edx>);
int __usercall sub_4FD748@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
COLORREF __usercall sub_4FD768@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>);
int __userpurge sub_4FD794@<eax>(int y@<ecx>, int x@<edx>, HDC *a3@<eax>, int a4);
int __usercall sub_4FD7DC@<eax>(HDC *a1@<eax>, struct tagRECT *a2@<edx>);
int __usercall sub_4FD804@<eax>(_DWORD *a1@<eax>);
char __usercall sub_4FD828@<al>(int a1@<eax>);
void nullsub_80();
int __usercall sub_4FD888@<eax>(int a1@<eax>, int a2@<edx>);
COLORREF __usercall sub_4FD954@<eax>(int a1@<eax>);
int __usercall sub_4FD980@<eax>(int a1@<eax>);
int __usercall sub_4FD9B0@<eax>(int a1@<eax>);
HGDIOBJ __usercall sub_4FDA30@<eax>(HGDIOBJ result@<eax>);
HGDIOBJ __usercall sub_4FDA50@<eax>(HGDIOBJ result@<eax>);
HGDIOBJ __usercall sub_4FDA70@<eax>(HGDIOBJ result@<eax>);
int sub_4FDAC0();
int sub_4FDACC();
int sub_4FDAD8();
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_4FDAE4();
_DWORD *sub_4FDB38();
int __usercall sub_4FDBE0@<eax>(int a1@<eax>);
HGDIOBJ __usercall sub_4FDBF0@<eax>(void *a1@<eax>, int *a2@<edx>, char a3@<cl>);
// attributes: thunk
int __usercall sub_4FDCAD@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FDD3E@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4FDD50@<eax>(__int16 a1@<ax>);
int __usercall sub_4FDD70@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4FDD84@<eax>(
        HDC a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int yMask,
        int xMask,
        HDC hdcSrc,
        int cy,
        int wDest,
        int ySrc,
        int xSrc,
        HDC hdc,
        int height,
        int width);
// attributes: thunk
int __usercall sub_4FDE4C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FDFF9@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_BYTE *__usercall sub_4FE010@<eax>(int a1@<eax>);
int *__usercall sub_4FE04C@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_4FE0C8@<eax>(int a1@<eax>, int a2@<edx>);
HPALETTE __usercall sub_4FE11C@<eax>(__int64 *a1@<eax>);
// attributes: thunk
int __usercall sub_4FE219@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_4FE234@<eax>(int a1@<eax>);
HPALETTE __usercall sub_4FE2CC@<eax>(void *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
int __usercall sub_4FE388@<eax>(HPALETTE a1@<eax>, struct tagPALETTEENTRY *a2@<edx>, int a3@<ecx>);
int __userpurge sub_4FE3DC@<eax>(
        BITMAPINFOHEADER *a1@<eax>,
        HGDIOBJ *a2@<edx>,
        struct _EXCEPTION_REGISTRATION_RECORD *a3@<ecx>,
        int *a4);
// attributes: thunk
int __usercall sub_4FE4AC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FE560@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_4FE580@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
bool __usercall sub_4FE590@<al>(unsigned __int8 *a1@<eax>, unsigned __int8 *a2@<edx>, int a3);
int __userpurge sub_4FE674@<eax>(int a1@<eax>, HICON *a2@<edx>, int a3@<ecx>, int *a4, int *a5, int a6);
int __usercall sub_4FE9AC@<eax>(int a1@<eax>);
unsigned int __usercall sub_4FE9E4@<eax>(void *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_4FEAC8@<eax>(void *a1@<eax>, int *a2@<edx>, _DWORD *a3@<ecx>, int a4);
int __usercall sub_4FEB30@<eax>(void *a1@<eax>, int *a2@<edx>, _DWORD *a3@<ecx>);
BOOL __userpurge sub_4FEB38@<eax>(
        LPBITMAPINFO lpbmi@<ecx>,
        HPALETTE hPal@<edx>,
        HBITMAP a3@<eax>,
        int a4,
        LPVOID lpvBits);
BOOL __userpurge sub_4FEBEC@<eax>(HBITMAP a1@<eax>, HPALETTE a2@<edx>, struct tagBITMAPINFO *a3@<ecx>, LPVOID lpvBits);
void nullsub_81();
void __usercall sub_4FEC04(int a1@<eax>);
BOOL __usercall sub_4FEC10@<eax>(int a1@<eax>, HICON a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_4FEE10@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FEE48@<eax>(int result@<eax>, int a2@<ecx>);
char __cdecl sub_4FEE60(int a1);
int __usercall sub_4FEEB4@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4FEF08@<eax>(int a1@<eax>, int a2);
BOOL __usercall sub_4FEF18@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_4FF058@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int sub_4FF088();
int sub_4FF08C();
int __usercall sub_4FF090@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4FF098@<eax>(int a1@<eax>);
int __userpurge sub_4FF0EC@<eax>(int result@<eax>, int a2, int a3, unsigned __int8 a4, unsigned __int8 a5);
int __usercall sub_4FF118@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4FF120@<eax>(int a1@<eax>);
void nullsub_311();
int __usercall sub_4FF190@<eax>(int a1@<eax>);
_BYTE *__usercall sub_4FF1AC@<eax>(_BYTE *result@<eax>, char a2@<dl>);
int __usercall sub_4FF1BC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_4FF504@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ebx>, int a4@<esi>);
_DWORD *__userpurge sub_4FF718@<eax>(
        _DWORD *a1@<eax>,
        _DWORD *a2@<edx>,
        __int32 a3@<ecx>,
        volatile signed __int8 *a4,
        volatile signed __int8 *a5);
int __usercall sub_4FF7AC@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_4FF844@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_4FF90C@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>, volatile __int32 *a4);
_DWORD *__usercall sub_4FFDAC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_4FFE34@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_4FFE68@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>, int a3@<ecx>);
int __usercall sub_4FFF54@<eax>(int a1@<ebx>, int a2@<esi>);
int __thiscall sub_4FFF74(void *this);
_DWORD *__usercall sub_4FFF94@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_4FFFD4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_500000@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
void __usercall sub_500038(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_50009C@<eax>(int *a1@<eax>, int a2@<ecx>);
int __usercall sub_5000B4@<eax>(int *a1@<eax>, int a2@<ecx>);
int __usercall sub_5000CC@<eax>(int *a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_5000E4();
// attributes: thunk
int sub_5000EC();
// attributes: thunk
int sub_5000F4();
int __usercall sub_5000FC@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5001A8@<eax>(int a1@<eax>);
void __userpurge sub_5002EC(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_5003B0@<eax>(int result@<eax>, int a2);
bool __fastcall sub_5003D4(void *a1, int a2);
int __usercall sub_50041C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__fastcall sub_500478(int a1, _DWORD *a2, volatile signed __int8 *a3);
_DWORD *__fastcall sub_50049C(volatile signed __int8 *a1, _DWORD *a2, volatile signed __int8 *a3);
int __fastcall sub_5004C0(void *a1, unsigned __int16 a2);
int __fastcall sub_5004D8(int a1, int a2);
int __usercall sub_500508@<eax>(int result@<eax>, int a2@<ecx>);
int __userpurge sub_50052C@<eax>(int result@<eax>, int a2, int a3, unsigned __int8 a4, unsigned __int8 a5);
_DWORD *__usercall sub_500558@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5006CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_500788@<eax>(int a1@<ecx>, int a2@<ebx>, int a3);
int __usercall sub_5007FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>);
int __usercall sub_500850@<eax>(int a1@<eax>);
int __usercall sub_500868@<eax>(int a1@<eax>);
int __usercall sub_500880@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void nullsub_86();
_BYTE *__usercall sub_5008C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_500908@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_500934@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
// attributes: thunk
int sub_5009C8();
HPALETTE __usercall sub_5009D0@<eax>(HPALETTE result@<eax>, _DWORD *a2@<edx>, RECT *a3@<ecx>);
volatile signed __int8 *__usercall sub_500A60@<eax>(int a1@<eax>, __int64 **a2@<edx>);
volatile signed __int8 *__usercall sub_500AC4@<eax>(int a1@<eax>, __int64 **a2@<edx>);
bool __usercall sub_500B44@<al>(int a1@<eax>);
int __usercall sub_500B4C@<eax>(int a1@<eax>);
int __usercall sub_500B70@<eax>(int a1@<eax>);
int __usercall sub_500BE4@<eax>(int a1@<eax>);
int __usercall sub_500BFC@<eax>(int a1@<eax>);
int __usercall sub_500C14@<eax>(int a1@<eax>);
int __usercall sub_500CA0@<eax>(int a1@<eax>);
int __usercall sub_500D04@<eax>(_BYTE *a1@<eax>, int (***a2)(void)@<edx>, int a3@<ecx>);
int __usercall sub_500D58@<eax>(int a1@<eax>);
int __usercall sub_500D80@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_500DEC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_500EC8@<eax>(int a1@<eax>, int a2@<edx>, UINT a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_501048@<eax>(int a1@<eax>);
int __usercall sub_501118@<eax>(int result@<eax>);
int __usercall sub_501134@<eax>(int a1@<eax>, HENHMETAFILE a2@<edx>);
int __usercall sub_5011C4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_501238@<eax>(_DWORD *a1@<eax>, __int16 a2@<dx>);
int __usercall sub_501270@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5012AC@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
void nullsub_312();
int __usercall sub_5012EC@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
bool __fastcall sub_501360(int a1, int a2);
int __usercall sub_5013C0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_501444@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5014C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_501554@<eax>(int result@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_50168F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_50169C@<eax>(int a1@<eax>, int a2);
HENHMETAFILE __userpurge sub_501720@<eax>(
        HENHMETAFILE result@<eax>,
        _WORD *a2@<edx>,
        HENHMETAFILE *a3@<ecx>,
        _DWORD *a4);
int __usercall sub_501754@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_501770@<eax>(int nNumber@<ecx>, int a2@<edx>, _DWORD *a3@<eax>);
int __thiscall sub_501A14(void *this);
int __usercall sub_501AC0@<eax>(int result@<eax>, void *a2@<ecx>);
_DWORD *__usercall sub_501B40@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_501B7C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_501BA8(int a1@<eax>);
void __usercall sub_501C4C(_DWORD *a1@<eax>);
int __usercall sub_501D38@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_501D5C@<eax>(int result@<eax>);
_DWORD *__usercall sub_501D60@<eax>(_DWORD *result@<eax>);
int __usercall sub_501D80@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_501DEC@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_501E38@<eax>(int result@<eax>, HPALETTE a2@<edx>, int a3@<ecx>);
int __usercall sub_501EF4@<eax>(int result@<eax>);
HGDIOBJ __userpurge sub_501F40@<eax>(void *a1@<eax>, HPALETTE a2@<edx>, HPALETTE a3@<ecx>, int a4, char *a5);
// attributes: thunk
int __usercall sub_5024E2@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_50250C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_50252E@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __cdecl sub_50253F(
        int a1,
        int __return_address,
        __int64 ExceptionInfo,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9);
// attributes: thunk
int __usercall sub_50258E@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
HPALETTE __usercall sub_5025A4@<eax>(HPALETTE a1@<eax>);
HGDIOBJ __usercall sub_502608@<eax>(COLORREF color@<ecx>, HPALETTE hPal@<edx>, void *a3@<eax>);
_DWORD *__usercall sub_502814@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_502888@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5028C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_50299F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_5029D8@<eax>(int a1@<eax>, void *a2@<edx>, HPALETTE a3@<ecx>, const void *a4);
_DWORD *__usercall sub_502A98@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_502ACC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_502AD8@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
HPALETTE __usercall sub_502B60@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int *a3@<ecx>);
// attributes: thunk
int __usercall sub_502D33@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_502DF7@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
HPALETTE __userpurge sub_502E0C@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int *a3@<ecx>, BYTE a4);
// attributes: thunk
int __usercall sub_502FDF@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5030B3@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5030C8@<eax>(int a1@<eax>);
bool __usercall sub_50312C@<al>(int a1@<eax>);
int __usercall sub_503148@<eax>(_DWORD *a1@<eax>);
int __usercall sub_503190@<eax>(int a1@<eax>);
bool __usercall sub_5031C8@<al>(int a1@<eax>);
int __usercall sub_5031F4@<eax>(int a1@<eax>);
int __usercall sub_503204@<eax>(int a1@<eax>);
bool __usercall sub_503218@<al>(int a1@<eax>);
int __usercall sub_503234@<eax>(int a1@<eax>);
int __usercall sub_503248@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_5032CC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_503330@<al>(int a1@<eax>);
unsigned int __usercall sub_50334C@<eax>(int a1@<eax>);
unsigned int __usercall sub_5033F0@<eax>(int a1@<eax>);
int __usercall sub_5034B0@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_50350C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_503554@<eax>(int a1@<eax>);
_DWORD *__usercall sub_50355C@<eax>(_DWORD *result@<eax>);
void __usercall sub_5035D0(int a1@<eax>);
int __usercall sub_5035E0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_503680@<eax>(_DWORD *a1@<eax>, signed int a2@<edx>);
_DWORD *__usercall sub_503764@<eax>(_DWORD *result@<eax>, void *a2@<ecx>);
HPALETTE __usercall sub_5037C4@<eax>(HPALETTE result@<eax>, void *a2@<ecx>);
int __userpurge sub_50387C@<eax>(HANDLE h@<ecx>, int a2@<eax>, __int16 a3@<dx>, HPALETTE a4);
_DWORD *__usercall sub_503900@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_503970@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_5039E0(int a1, int (***a2)(void));
int __userpurge sub_503A04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, const void *a6);
int __fastcall sub_503B04(int a1, int a2);
int __userpurge sub_503B2C@<eax>(
        int a1@<eax>,
        __int64 (__cdecl ***a2)(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *)@<edx>,
        int a3@<ecx>,
        __int16 *a4);
// attributes: thunk
int __usercall sub_503EF6@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_503F22@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __cdecl sub_503F89(
        int a1,
        int __return_address,
        __int64 ExceptionInfo,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9);
// attributes: thunk
int __usercall sub_503FBA@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __cdecl sub_504048(
        int a1,
        int __return_address,
        __int64 ExceptionInfo,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9);
// attributes: thunk
int __usercall sub_504075@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5040E0@<eax>(
        int a1@<eax>,
        __int64 (__cdecl ***a2)(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *)@<edx>,
        int a3@<ecx>);
int __usercall sub_504150@<eax>(int result@<eax>, void *a2@<edx>);
char __usercall sub_504214@<al>(HPALETTE a1@<eax>, char a2@<dl>);
int __usercall sub_504350@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
char __usercall sub_504380@<al>(_DWORD *a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_5043FC@<eax>(int a1@<eax>, HPALETTE a2@<edx>);
int __usercall sub_5044D0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_50461C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_504638@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_504688@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5046B4@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int sub_5046D0();
void *__usercall sub_5046D8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5049B4@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5049E8@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5049FC@<eax>(_DWORD *a1@<eax>);
void *__usercall sub_504A20@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_504A28@<eax>(_DWORD *a1@<eax>, _WORD *a2@<edx>, _DWORD *a3@<ecx>, HPALETTE *a4);
int __usercall sub_504AC8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_504B28@<al>(int a1@<eax>);
int __usercall sub_504B30@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_504B5C@<eax>(int a1@<eax>);
int __usercall sub_504B74@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_504BAC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
// attributes: thunk
int __usercall sub_504E1A@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_504E37@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_504E54@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_504E6C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_504EC0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_504EEC@<eax>(_DWORD **a1@<eax>, int a2@<edx>, int a3@<ecx>);
BOOL __fastcall sub_504F48(int *a1, HDC *a2);
bool __usercall sub_504F8C@<al>(int a1@<eax>);
int __usercall sub_504FA4@<eax>(int a1@<eax>);
int __usercall sub_504FCC@<eax>(int a1@<eax>);
int __usercall sub_504FF8@<eax>(int a1@<eax>);
HICON __usercall sub_505024@<eax>(HICON result@<eax>);
int __usercall sub_50509C@<eax>(int result@<eax>, int a2@<ecx>);
int __fastcall sub_505150(LPCWSTR lpIconName, HINSTANCE hInstance);
int __fastcall sub_505170(int a1, HINSTANCE a2);
int __usercall sub_505194@<eax>(int a1@<eax>, void (***a2)(void)@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_50524C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5052C0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5052FC@<eax>(int a1@<eax>, HICON a2@<edx>);
int __usercall sub_505390@<eax>(int result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5053A8@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
void nullsub_313();
int __usercall sub_5053CC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5053E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __stdcall sub_50540C(int a1);
int __stdcall sub_505420(int a1);
int __usercall sub_505434@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5055C0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5055F8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50569C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
OLECHAR ***__usercall sub_505738@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_50588C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_5058B8@<al>(int a1@<eax>);
_DWORD *__usercall sub_5058C0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5058D4@<eax>(int a1@<eax>);
int __usercall sub_5058D8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5058DC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_50593C@<eax>(
        int a1@<eax>,
        __int64 (__cdecl ***a2)(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *)@<edx>);
_DWORD *__usercall sub_505A98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_505C4C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_505CE8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_505D18@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_505DCC@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_505E70@<eax>(int a1@<eax>, int a2@<edx>);
int sub_505ED4();
int sub_505EE0();
_DWORD *__usercall sub_505F24@<eax>(int a1@<eax>, int a2@<edi>);
HPALETTE sub_5060EC();
// attributes: thunk
int __usercall sub_506131@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_506150@<eax>(int tmCharSet@<ebx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_506194@<eax>(int a1@<ebx>);
_DWORD *__usercall sub_506600@<eax>(int a1@<eax>, char a2@<dl>);
void __usercall sub_506638(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_506664(int a1@<eax>);
void __usercall sub_506670(int a1@<eax>);
volatile signed __int8 **__usercall sub_50667C@<eax>(
        int a1@<eax>,
        volatile signed __int8 *a2@<edx>,
        volatile signed __int8 *a3@<ecx>);
_DWORD *__fastcall sub_506730(int a1, int a2);
int __usercall sub_50683C@<eax>(int a1@<eax>);
volatile signed __int8 *__usercall sub_5068BC@<eax>(signed int a1@<eax>, signed int a2@<edx>);
int __usercall sub_5068F4@<eax>(signed __int32 a1@<eax>);
void sub_506924();
void __cdecl sub_506938();
int __usercall sub_506944@<eax>(int a1@<eax>);
int sub_506B0C();
int nullsub_328();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_329(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_330@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int __usercall sub_5096EC@<eax>(int a1@<eax>);
int __usercall sub_509700@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_509744@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_5097E8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_509898@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5098E4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_509934@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_509B10@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_509B2C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_509B84@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_509BB0(int *a1@<eax>);
char __usercall sub_509BBC@<al>(int a1@<eax>);
char __usercall sub_509BCC@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_509C00@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_509C28@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_509C54@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_509CB0@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_509D18@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_509D68@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_509E74@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_509EEC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_509FBC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_50A018@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_50A080@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_50A0E0@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_50A150@<eax>(int result@<eax>, char a2@<dl>);
bool __usercall sub_50A1B0@<al>(int a1@<eax>);
int __usercall sub_50A1C4@<eax>(int result@<eax>, __int16 a2@<dx>);
int sub_50A228();
int __usercall sub_50A22C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_50A250@<eax>(_DWORD *a1@<eax>);
bool __usercall sub_50A27C@<al>(int a1@<eax>);
int __usercall sub_50A2A0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_50A2C8@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_50A328@<eax>(int result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_50A38C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_50A470@<al>(int a1@<eax>);
int __usercall sub_50A48C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50A4D4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_50A530@<al>(int a1@<eax>);
int __usercall sub_50A538@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_50A648@<al>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_50A68C(int a1, int a2, char a3);
int __fastcall sub_50A91C(int a1, int a2, int a3, int a4);
int __fastcall sub_50A9B8(int a1, int a2, char a3);
int __usercall sub_50AB40@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_50ABF8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_50ACB0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_50AD5C@<eax>(int a1@<eax>);
int __usercall sub_50AE10@<eax>(int a1@<eax>);
int __userpurge sub_50AE20@<eax>(int a1@<eax>, int a2@<edx>, void (*a3)(void), int a4);
_DWORD *__usercall sub_50AF4C@<eax>(int a1@<eax>);
char __usercall sub_50AF5C@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
_DWORD *__usercall sub_50AF94@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_50AFC4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_50AFFC@<eax>(int a1@<eax>, char a2@<dl>);
bool __usercall sub_50B164@<al>(int a1@<eax>, bool *a2@<edx>, int a3@<ecx>);
int __usercall sub_50B180@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B190@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1A0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1B0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1C0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1D0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1E0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B1F0@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B200@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B210@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_50B220@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
void nullsub_315();
void nullsub_316();
void nullsub_317();
void nullsub_318();
void nullsub_319();
void nullsub_320();
void nullsub_321();
void nullsub_322();
void nullsub_323();
void nullsub_324();
void nullsub_325();
void nullsub_326();
void nullsub_327();
_DWORD *sub_50B264();
int __usercall sub_50B280@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_50B2A4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_50B2AC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_50B360@<eax>(int a1@<eax>);
int __usercall sub_50B368@<eax>(int a1@<eax>);
int __usercall sub_50B380@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_50B478@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_50B4BC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_50B570();
int __usercall sub_50B578@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_50B590@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_50B608@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_50B6AC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50B74C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_50B784(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_50B7BC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_50B824@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_50B830@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_50B884(void *this);
int __usercall sub_50B8B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_50B984@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_50BAB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_50BB28@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_50BBA0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_50BC0C@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_50BCC8(int a1, int a2);
int sub_50BCE8();
int __usercall sub_50BD08@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_50BD10@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_50BEAC@<eax>(int a1@<eax>);
int __usercall sub_50BED8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_50BEF8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_50BFD8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_50BFE4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_50BFFC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_50C04C(int a1, int a2);
int __usercall sub_50C064@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_50C0A0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_50C0F4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_50C12C@<eax>(int result@<eax>);
int __usercall sub_50C15C@<eax>(int a1@<eax>);
int __usercall sub_50C184@<eax>(int a1@<eax>);
int __usercall sub_50C1B0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_50C1EC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_50C238@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_50C284@<eax>(int a1@<eax>);
int __usercall sub_50C294@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int __usercall sub_50C2A0@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_50C2A8();
_DWORD *__usercall sub_50C2B0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_50C2F4@<al>(int a1@<eax>);
_DWORD *__fastcall sub_50C314(int a1, _DWORD *a2);
_DWORD *__fastcall sub_50C334(_DWORD *a1, int a2);
__int64 *__fastcall sub_50C35C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_50C388(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_50C3B4(int a1, int a2, int a3, int a4);
bool __usercall sub_50C3D8@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_50C3FC@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_50C45C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_50C514@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50C550@<eax>(int a1@<eax>);
int __userpurge sub_50C55C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int nullsub_331();
int __usercall sub_50D24C@<eax>(void (***a1)(void)@<eax>, int a2@<edx>);
int __usercall sub_50D25C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_50D264@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50D2A8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_50D2E8@<eax>(__int64 ***a1@<eax>);
int __usercall sub_50D308@<eax>(int a1@<eax>, int a2@<edx>);
void sub_50D38C();
// attributes: thunk
HIMAGELIST __stdcall ImageList_Create(int cx, int cy, UINT flags, int cInitial, int cGrow);
// attributes: thunk
BOOL __stdcall ImageList_Destroy(HIMAGELIST himl);
// attributes: thunk
int __stdcall ImageList_GetImageCount(HIMAGELIST himl);
// attributes: thunk
BOOL __stdcall ImageList_SetImageCount(HIMAGELIST himl, UINT uNewCount);
// attributes: thunk
int __stdcall ImageList_Add(HIMAGELIST himl, HBITMAP hbmImage, HBITMAP hbmMask);
// attributes: thunk
int __stdcall ImageList_ReplaceIcon(HIMAGELIST himl, int i, HICON hicon);
// attributes: thunk
COLORREF __stdcall ImageList_SetBkColor(HIMAGELIST himl, COLORREF clrBk);
// attributes: thunk
COLORREF __stdcall ImageList_GetBkColor(HIMAGELIST himl);
// attributes: thunk
BOOL __stdcall ImageList_SetOverlayImage(HIMAGELIST himl, int iImage, int iOverlay);
// attributes: thunk
BOOL __stdcall ImageList_Draw(HIMAGELIST himl, int i, HDC hdcDst, int x, int y, UINT fStyle);
// attributes: thunk
BOOL __stdcall ImageList_Replace(HIMAGELIST himl, int i, HBITMAP hbmImage, HBITMAP hbmMask);
// attributes: thunk
BOOL __stdcall ImageList_DrawEx(
        HIMAGELIST himl,
        int i,
        HDC hdcDst,
        int x,
        int y,
        int dx,
        int dy,
        COLORREF rgbBk,
        COLORREF rgbFg,
        UINT fStyle);
// attributes: thunk
BOOL __stdcall ImageList_Remove(HIMAGELIST himl, int i);
// attributes: thunk
HICON __stdcall ImageList_GetIcon(HIMAGELIST himl, int i, UINT flags);
// attributes: thunk
HIMAGELIST __stdcall ImageList_LoadImageW(
        HINSTANCE hi,
        LPCWSTR lpbmp,
        int cx,
        int cGrow,
        COLORREF crMask,
        UINT uType,
        UINT uFlags);
// attributes: thunk
BOOL __stdcall ImageList_Copy(HIMAGELIST himlDst, int iDst, HIMAGELIST himlSrc, int iSrc, UINT uFlags);
// attributes: thunk
BOOL __stdcall ImageList_BeginDrag(HIMAGELIST himlTrack, int iTrack, int dxHotspot, int dyHotspot);
// attributes: thunk
void __stdcall ImageList_EndDrag();
// attributes: thunk
BOOL __stdcall ImageList_DragEnter(HWND hwndLock, int x, int y);
// attributes: thunk
BOOL __stdcall ImageList_DragLeave(HWND hwndLock);
// attributes: thunk
BOOL __stdcall ImageList_DragMove(int x, int y);
// attributes: thunk
BOOL __stdcall ImageList_DragShowNolock(BOOL fShow);
// attributes: thunk
HIMAGELIST __stdcall ImageList_GetDragImage(POINT *ppt, POINT *pptHotspot);
// attributes: thunk
HIMAGELIST __stdcall ImageList_Read(struct IStream *pstm);
// attributes: thunk
BOOL __stdcall ImageList_Write(HIMAGELIST himl, struct IStream *pstm);
// attributes: thunk
BOOL __stdcall ImageList_GetIconSize(HIMAGELIST himl, int *cx, int *cy);
// attributes: thunk
BOOL __stdcall ImageList_SetIconSize(HIMAGELIST himl, int cx, int cy);
// attributes: thunk
BOOL __stdcall ImageList_GetImageInfo(HIMAGELIST himl, int i, IMAGEINFO *pImageInfo);
// attributes: thunk
BOOL __stdcall TrackMouseEvent(LPTRACKMOUSEEVENT lpEventTrack);
// attributes: thunk
BOOL __stdcall FlatSB_GetScrollInfo(HWND a1, int code, LPSCROLLINFO a3);
// attributes: thunk
int __stdcall FlatSB_GetScrollPos(HWND a1, int code);
// attributes: thunk
int __stdcall FlatSB_SetScrollInfo(HWND a1, int code, LPSCROLLINFO psi, BOOL fRedraw);
// attributes: thunk
int __stdcall FlatSB_SetScrollPos(HWND a1, int code, int pos, BOOL fRedraw);
// attributes: thunk
BOOL __stdcall FlatSB_SetScrollProp(HWND a1, UINT index, INT_PTR newValue, BOOL a4);
// attributes: thunk
BOOL __stdcall InitializeFlatSB(HWND a1);
int __userpurge sub_50D524@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int sub_50DE68();
int __stdcall sub_50DF3C(DWORD dwFlags, DWORD dwMilliseconds, DWORD nCount, HANDLE *pHandles, DWORD *a5);
HMODULE sub_50E020();
int __userpurge sub_50E0A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_50E0D4@<eax>(int a1@<eax>);
void nullsub_332();
char sub_50E0E4();
int __usercall sub_50E0E8@<eax>(int a1@<eax>, __int64 *a2@<edx>);
int __usercall sub_50E1A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50E1E4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_50E214@<eax>(int a1@<eax>, DWORD a2@<edx>, int a3@<ecx>, int a4@<ebx>);
int __fastcall sub_50E2E8(DWORD dwMilliseconds, int a2, int a3, char a4, _DWORD *a5, char a6);
_DWORD *__userpurge sub_50E4A8@<eax>(
        LPSECURITY_ATTRIBUTES lpEventAttributes@<ecx>,
        int a2@<eax>,
        char a3@<dl>,
        unsigned __int8 a4,
        int a5,
        char a6,
        char a7);
_DWORD *__usercall sub_50E510@<eax>(unsigned __int8 a1@<cl>, int a2@<eax>, char a3@<dl>);
BOOL __usercall sub_50E550@<eax>(int a1@<eax>);
BOOL __usercall sub_50E55C@<eax>(int a1@<eax>);
int __usercall sub_50E568@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_50E5B4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_50E600@<eax>(int a1@<eax>);
_DWORD *__stdcall sub_50E63C(_DWORD *a1);
int __stdcall sub_50E64C(int a1);
int __stdcall sub_50E65C(int a1);
int __stdcall sub_50E66C(int a1, int a2, int a3);
int __usercall sub_50E688@<eax>(int a1@<eax>);
_DWORD *__fastcall sub_50E6E0(int a1, _DWORD **a2);
unsigned int __usercall sub_50E6FC@<eax>(volatile signed __int32 *a1@<eax>);
int __usercall sub_50E754@<eax>(volatile signed __int32 *a1@<eax>, _DWORD *a2@<edx>);
unsigned int __usercall sub_50E7BC@<eax>(volatile signed __int32 *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_50E850@<eax>(
        volatile signed __int32 *a1@<eax>,
        struct _RTL_CRITICAL_SECTION *a2@<edx>,
        DWORD a3@<ecx>);
unsigned int *__usercall sub_50E960@<eax>(unsigned int *result@<eax>, int a2@<edx>);
int __usercall sub_50E968@<eax>(int a1@<eax>);
unsigned int *__usercall sub_50E97C@<eax>(unsigned int *a1@<eax>);
FARPROC sub_50E9F0();
void sub_50EB5C();
__int32 __usercall sub_50EBF4@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall DrawThemeTextEx(
        HTHEME hTheme,
        HDC hdc,
        int iPartId,
        int iStateId,
        LPCWSTR pszText,
        int cchText,
        DWORD dwTextFlags,
        LPRECT pRect,
        const DTTOPTS *pOptions);
__int32 __usercall sub_50EC0C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall MEMORY[0x50EC1C]();
__int32 __usercall sub_50EC24@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall BufferedPaintUnInit();
__int32 __usercall sub_50EC3C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HPAINTBUFFER __stdcall MEMORY[0x50EC4C](
        HDC hdcTarget,
        const RECT *prcTarget,
        BP_BUFFERFORMAT dwFormat,
        BP_PAINTPARAMS *pPaintParams,
        HDC *phdc);
__int32 __usercall sub_50EC54@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall EndBufferedPaint(HPAINTBUFFER hBufferedPaint, BOOL fUpdateTarget);
__int32 __usercall sub_50EC6C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall MEMORY[0x50EC7C](HPAINTBUFFER hBufferedPaint, const RECT *prc, BYTE alpha);
__int32 __usercall sub_50EC84@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall BufferedPaintStopAllAnimations(HWND hwnd);
__int32 __usercall sub_50EC9C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HANIMATIONBUFFER __stdcall BeginBufferedAnimation(
        HWND hwnd,
        HDC hdcTarget,
        const RECT *prcTarget,
        BP_BUFFERFORMAT dwFormat,
        BP_PAINTPARAMS *pPaintParams,
        BP_ANIMATIONPARAMS *pAnimationParams,
        HDC *phdcFrom,
        HDC *phdcTo);
__int32 __usercall sub_50ECB4@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall EndBufferedAnimation(HANIMATIONBUFFER hbpAnimation, BOOL fUpdateTarget);
int __usercall sub_50ECCC@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall BufferedPaintRenderAnimation(HWND hwnd, HDC hdcTarget);
int sub_50ECE4();
int sub_50EEA4();
bool sub_50F988();
int sub_50F9B8();
// attributes: thunk
HMONITOR __stdcall MonitorFromWindow(HWND hwnd, DWORD dwFlags);
// attributes: thunk
HMONITOR __stdcall MonitorFromRect(LPCRECT lprc, DWORD dwFlags);
// attributes: thunk
HMONITOR __stdcall MonitorFromPoint(POINT pt, DWORD dwFlags);
// attributes: thunk
BOOL __stdcall GetMonitorInfoW(HMONITOR hMonitor, LPMONITORINFO lpmi);
// attributes: thunk
BOOL __stdcall EnumDisplayMonitors(HDC hdc, LPCRECT lprcClip, MONITORENUMPROC lpfnEnum, LPARAM dwData);
__int32 __usercall sub_50FA40@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall ImmIsIME(HKL a1);
__int32 __usercall sub_50FA58@<eax>(__int32 a1@<eax>);
// attributes: thunk
HIMC __stdcall ImmGetContext(HWND a1);
__int32 __usercall sub_50FA70@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall ImmReleaseContext(HWND a1, HIMC a2);
__int32 __usercall sub_50FA88@<eax>(__int32 a1@<eax>);
// attributes: thunk
HIMC __stdcall ImmAssociateContext(HWND a1, HIMC a2);
__int32 __usercall sub_50FAA0@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall ImmGetConversionStatus(HIMC a1, LPDWORD lpfdwConversion, LPDWORD lpfdwSentence);
__int32 __usercall sub_50FAB8@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall ImmSetConversionStatus(HIMC a1, DWORD a2, DWORD a3);
__int32 __usercall sub_50FAD0@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall ImmSetOpenStatus(HIMC a1, BOOL a2);
char __usercall sub_51021C@<al>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_510264@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5102C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_510300@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_51030C@<eax>(int a1@<eax>);
char __usercall sub_5103B8@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_5103E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_510418@<eax>(int a1@<eax>);
_DWORD *__usercall sub_510444@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__thiscall sub_51047C(void *this);
_DWORD *__usercall sub_51048C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool __usercall sub_5104C8@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5104E4@<eax>(int a1@<eax>);
int __usercall sub_510590@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_510594@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_5105AC@<al>(int a1@<eax>, int a2@<ecx>);
void sub_510604();
__int32 __usercall sub_51061C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall DwmExtendFrameIntoClientArea(HWND hWnd, const MARGINS *pMarInset);
__int32 __usercall sub_510634@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall DwmIsCompositionEnabled(BOOL *pfEnabled);
bool __thiscall sub_51064C(void *this);
BOOL __userpurge sub_510670@<eax>(
        _DWORD *a1@<eax>,
        signed int a2@<edx>,
        signed int a3@<ecx>,
        unsigned __int8 a4,
        LONG *a5);
void sub_510740();
char __usercall sub_510B3C@<al>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__userpurge sub_510BB8@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3@<ecx>, int a4, DWORD a5);
int __userpurge sub_510C8C@<eax>(
        int a1@<eax>,
        char a2@<dl>,
        __int32 a3@<ecx>,
        int a4,
        __int32 a5,
        __int32 a6,
        DWORD a7);
int __usercall sub_510D40@<eax>(int result@<eax>);
HMODULE sub_510D54();
_DWORD *__usercall sub_510ED8@<eax>(DWORD a1@<eax>);
int __usercall sub_510FFC@<eax>(DWORD a1@<eax>, int a2, int a3, int a4, int a5);
OLECHAR ***__userpurge sub_511010@<eax>(int a1@<eax>, unsigned __int8 *a2@<edx>, int a3@<ecx>, int a4, const CHAR **a5);
OLECHAR ***__userpurge sub_511240@<eax>(unsigned int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__cdecl sub_5113B8(VARIANTARG *a1, int a2, unsigned __int8 *a3, const CHAR **a4);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_511454@<eax>(DWORD a1@<eax>, int a2@<edx>, int a3@<ebx>);
void nullsub_82();
void nullsub_83();
__int64 __stdcall sub_511504(__int64 a1);
void sub_511524(BSTR *a1, int a2, unsigned __int8 *a3, ...);
void sub_5117C0();
void sub_511854();
int nullsub_340();
int sub_51C77C();
_BYTE *__usercall sub_51C7B8@<eax>(_BYTE *result@<eax>);
int __stdcall sub_51C7CC(HWND hWnd, int a2, int a3, int a4);
LRESULT __usercall sub_51C8DC@<eax>(HWND a1@<eax>, DWORD a2@<ecx>);
HANDLE __usercall sub_51C910@<eax>(HWND a1@<eax>, DWORD a2@<ecx>);
char __usercall sub_51C96C@<al>(HWND a1@<eax>, DWORD a2@<ecx>);
LRESULT __usercall sub_51C99C@<eax>(LPARAM lParam@<ecx>, WPARAM wParam@<edx>, UINT a3@<eax>);
// attributes: thunk
int __usercall sub_51C9C4@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
char __usercall sub_51C9CC@<al>(int a1@<eax>, _DWORD *a2@<edx>);
volatile __int32 *__usercall sub_51C9D4@<eax>(int a1@<eax>, __int64 **a2@<edx>);
volatile __int32 *__usercall sub_51CA1C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
BOOL __usercall sub_51CA64@<eax>(int a1@<eax>, HDC a2@<edx>);
int __usercall sub_51CAB4@<eax>(HWND a1@<eax>, RECT *a2@<edx>);
// attributes: thunk
int __usercall sub_51CB3F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_51CB61@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
HANDLE sub_51CB6C();
unsigned __int8 __usercall sub_51CB94@<al>(int a1@<eax>);
HWND sub_51CDA4();
int __usercall sub_51CDD0@<eax>(_DWORD *a1@<eax>, volatile signed __int8 *a2@<edx>);
int __usercall sub_51CE54@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_51CE84@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_51CEE8@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
HWND __usercall sub_51CF28@<eax>(int a1@<eax>);
void __stdcall sub_51CF40(int a1, int a2);
int __fastcall sub_51CF48(int a1, int a2);
int __fastcall sub_51CF5C(int a1, HWND a2);
int __usercall sub_51CF70@<eax>(int a1@<eax>, int a2@<edx>);
int sub_51D0A4();
__int16 __fastcall sub_51D0A8(int a1, char a2, int a3);
void nullsub_333();
HMODULE sub_51D0C4();
void nullsub_334();
int __usercall sub_51D0D0@<eax>(unsigned int a1@<eax>);
int sub_51D11C();
int sub_51D12C();
_DWORD *__usercall sub_51D13C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
char __usercall sub_51D178@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
void __userpurge sub_51D1A4(int a1@<eax>, int a2);
int __userpurge sub_51D1D8@<eax>(int **a1@<eax>, int a2@<ecx>, char a3, int a4);
__int16 __userpurge sub_51D20C@<ax>(int a1@<eax>, char a2@<dl>, int a3);
int __usercall sub_51D228@<eax>(int a1@<eax>);
int __usercall sub_51D234@<eax>(int a1@<eax>);
int __usercall sub_51D258@<eax>(int a1@<eax>);
void nullsub_335();
int __usercall sub_51D280@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_51D2E8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
char __usercall sub_51D314@<al>(int a1@<eax>, int a2@<edx>);
void __userpurge sub_51D380(int a1@<eax>, int a2);
int __usercall sub_51D3AC@<eax>(int result@<eax>, int a2@<edx>);
char __usercall sub_51D3D0@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_51D44C(int a1@<eax>);
void __usercall sub_51D460(int a1@<eax>);
int __stdcall sub_51D474(int a1);
char sub_51D480();
int sub_51D484();
void nullsub_336();
BOOL __stdcall fn(HWND hWnd, OLDFONTENUMPROCW a2);
int __usercall sub_51D4F0@<eax>(int *a1@<eax>, int a2);
int *__usercall sub_51D6CC@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
__int64 *__usercall sub_51D818@<eax>(__int64 *result@<eax>, char a2@<dl>, int a3@<ecx>);
LRESULT __userpurge sub_51D874@<eax>(HWND a1@<eax>, char a2@<dl>, LPARAM a3@<ecx>, LPARAM *a4, LPARAM a5);
int __usercall sub_51D8CC@<eax>(HWND a1@<eax>, DWORD a2@<ecx>);
HWND __usercall sub_51D92C@<eax>(POINT *a1@<eax>);
LRESULT __userpurge sub_51D958@<eax>(POINT *a1@<eax>, HWND *a2@<edx>, char a3@<cl>, int *a4);
BOOL __usercall sub_51D9A8@<eax>(char a1@<al>);
int sub_51D9E4();
void __usercall sub_51DA84(POINT *a1@<eax>);
int __usercall sub_51DD74@<eax>(double *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_51DEDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_51E09C@<eax>(int a1@<ebx>, int a2);
int __usercall sub_51E110@<eax>(int result@<eax>, int a2@<ecx>);
int __thiscall sub_51E434(void *this);
HANDLE __usercall sub_51E44C@<eax>(POINT *a1@<eax>);
HANDLE __usercall sub_51E480@<eax>(POINT *a1@<eax>);
int __usercall sub_51E4CC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
__int64 **__usercall sub_51E4F4@<eax>(__int64 ***a1@<eax>, int a2@<edx>);
BOOL __usercall sub_51E544@<eax>(HDC a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_51E574(void *this);
int __thiscall sub_51E634(void *this);
int __usercall sub_51E6E0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_51E70C(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_51E7E0@<eax>(int result@<eax>);
int __usercall sub_51E814@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_51E82C@<eax>(int result@<eax>);
_DWORD *__usercall sub_51E858@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_51E894@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_51E8DC@<eax>(_DWORD *result@<eax>, int a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_51E958@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_51E96C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_51E988@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_51EA88@<eax>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_51EAF0@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_51EB04@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_51EB2C@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_51EB40@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_51EB70@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_51EBA4@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_51EBCC@<al>(int a1@<eax>);
int __usercall sub_51EBF4@<eax>(int a1@<eax>);
void nullsub_337();
int __usercall sub_51EC18@<eax>(_DWORD **a1@<eax>);
void nullsub_338();
volatile __int32 *__usercall sub_51EC40@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>);
int __usercall sub_51EC64@<eax>(int a1@<eax>);
int __userpurge sub_51EC84@<eax>(_DWORD *a1@<eax>, int a2, int a3);
bool __usercall sub_51ECB0@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_51ED04@<eax>(int a1@<eax>);
int __usercall sub_51ED24@<eax>(int a1@<eax>);
int __usercall sub_51ED44@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_51ED64@<eax>(int a1@<eax>);
_DWORD *__usercall sub_51ED88@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_51EEEC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int sub_51F024();
int __usercall sub_51F028@<eax>(int a1@<eax>);
int sub_51F030();
bool __usercall sub_51F034@<al>(int a1@<eax>);
int __usercall sub_51F03C@<eax>(int a1@<eax>);
char __usercall sub_51F040@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_51F06C@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_51F0EC@<eax>(int a1@<eax>);
int __usercall sub_51F0FC@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_51F19C@<eax>(int *a1@<eax>, int a2@<edx>);
bool __usercall sub_51F218@<al>(int a1@<eax>);
char __usercall sub_51F230@<al>(int a1@<eax>, char a2@<dl>);
char __usercall sub_51F290@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_51F2C8@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_51F2CC@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_51F2DC@<eax>(int a1@<eax>);
int __usercall sub_51F2E4@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_51F304@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_51F3B8@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_51F438@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
void __userpurge sub_51F520(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __fastcall sub_51F5C0(int a1, int a2);
int __usercall sub_51F5E4@<eax>(int result@<eax>);
int __usercall sub_51F78C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_51F7C4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_51F7FC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_51F834@<eax>(int a1@<eax>, int a2@<edx>);
int *__usercall sub_51F86C@<eax>(int *a1@<eax>, int a2@<edx>, int *a3@<ecx>);
int __usercall sub_51F9A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_51F9FC@<eax>(int result@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_51FA10@<eax>(int a1@<eax>, __int32 a2@<edx>);
void __usercall sub_51FA34(int *a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_51FA5C@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
int __usercall sub_51FA7C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_51FAA8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_51FAC0@<eax>(int a1@<eax>);
int __fastcall sub_51FAD8(int a1, int a2);
int __usercall sub_51FB00@<eax>(int a1@<eax>);
int __usercall sub_51FB18@<eax>(int a1@<eax>);
_DWORD *__usercall sub_51FB40@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_51FBD0@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
_DWORD *__usercall sub_51FBFC@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, _DWORD *result@<eax>);
int __usercall sub_51FC80@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int result@<eax>);
int sub_51FD04();
int __usercall sub_51FD10@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
char __usercall sub_51FD3C@<al>(int a1@<eax>, int a2@<ecx>);
__int16 __userpurge sub_51FD6C@<ax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_51FDD8@<eax>(int a1@<eax>);
int __usercall sub_51FDE8@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int a3@<eax>);
void __usercall sub_51FFB0(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_51FFCC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_520070@<eax>(_DWORD *a1@<eax>, int *a2@<edx>);
int __usercall sub_520104@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_52013C@<eax>(int result@<eax>, char a2@<dl>);
int sub_520154();
int __fastcall sub_520164(int a1, int a2);
int __usercall sub_520170@<eax>(int a1@<eax>);
int __usercall sub_520184@<eax>(int a1@<eax>);
int __usercall sub_5201C0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
volatile signed __int8 *__fastcall sub_5201E8(int a1, __int64 **a2);
_DWORD *__fastcall sub_52023C(int a1, int a2);
int __usercall sub_5202A0@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5202BC@<eax>(int a1@<eax>);
int __usercall sub_520300@<eax>(int a1@<eax>);
bool __usercall sub_52030C@<al>(int a1@<eax>);
char __usercall sub_520320@<al>(int a1@<eax>);
char __usercall sub_52032C@<al>(int a1@<eax>);
int __usercall sub_520334@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_520358@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_52037C@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5203B8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_520404@<al>(int a1@<eax>);
int __usercall sub_52040C@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_520430@<eax>(int result@<eax>, char a2@<dl>);
bool __usercall sub_520474@<al>(HANDLE a1@<eax>);
unsigned __int8 __usercall sub_520484@<al>(void *a1@<eax>, char a2@<dl>);
void __usercall sub_5204AC(int *a1@<eax>);
void __usercall sub_5204CC(int a1@<eax>, int a2@<edx>);
void __usercall sub_520558(int a1@<eax>, char a2@<dl>);
int __usercall sub_52057C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
HDC __usercall sub_5205B4@<eax>(_DWORD *a1@<eax>);
int __cdecl sub_520660(int a1);
int __usercall sub_5206E8@<eax>(int result@<eax>, char a2@<dl>, char a3@<cl>);
int __usercall sub_52077C@<eax>(int a1@<eax>);
int __userpurge sub_520790@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>, int a4, int a5, int a6);
void __usercall sub_5207D8(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52084C@<eax>(int a1@<eax>);
int __usercall sub_520878@<eax>(int result@<eax>);
int __usercall sub_520890@<eax>(int a1@<eax>);
int __usercall sub_5208A0@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_520979@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int sub_52099C();
bool __usercall sub_5209A0@<al>(int a1@<eax>);
bool __usercall sub_5209B8@<al>(int a1@<eax>);
bool __usercall sub_5209D0@<al>(int a1@<eax>);
bool __usercall sub_5209E8@<al>(int a1@<eax>);
int sub_520A04();
int __usercall sub_520A20@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __fastcall sub_520B00(int a1, int a2);
void nullsub_341();
bool __usercall sub_520B38@<al>(int a1@<eax>);
int __userpurge sub_520B44@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, _BYTE *a4, unsigned __int8 a5, int a6);
int __userpurge sub_520B80@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_520BAC@<eax>(int result@<eax>, int a2@<edx>);
void __thiscall sub_520BCC(_BYTE *this);
int __usercall sub_520BD0@<eax>(int a1@<eax>, _BYTE *a2@<edx>, _BYTE *a3@<ecx>);
int __userpurge sub_520BEC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __fastcall sub_520C18(int a1, int a2);
void __userpurge sub_520CEC(int *a1@<eax>, int a2);
int __userpurge sub_520D08@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_520D34@<eax>(int result@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_520D64@<eax>(int *a1@<eax>, int a2@<edx>);
int __userpurge sub_520D98@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>, int a3@<ecx>, _DWORD *a4);
int __usercall sub_520E68@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>, _DWORD *a3@<ecx>);
int __usercall sub_520EB4@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>, _DWORD *a3@<ecx>);
int __usercall sub_520F00@<eax>(int a1@<eax>, int *a2@<edx>, char a3@<cl>);
// attributes: thunk
int __usercall sub_52101C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_52102C(int *a1@<eax>);
void __usercall sub_521044(int *a1@<eax>);
void __usercall sub_52105C(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
BOOL __userpurge sub_52114C@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>, char a4);
BOOL __usercall sub_521360@<eax>(int a1@<eax>);
int __userpurge sub_521400@<eax>(
        struct _EXCEPTION_REGISTRATION_RECORD *a1@<eax>,
        int a2@<edx>,
        int *a3@<ecx>,
        unsigned __int8 a4,
        int a5);
void __usercall sub_5214F8(int *a1@<eax>);
char sub_521508();
int __usercall sub_52150C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_52153C@<al>(_BYTE *a1@<eax>, int *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5215A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5215D8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
LONG __usercall sub_521608@<eax>(int a1@<eax>, struct tagPOINT *a2@<edx>);
bool __usercall sub_521634@<al>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_521668@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, int *a3@<ecx>);
int __userpurge sub_521754@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_521788@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_52179C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5217B0@<eax>(int a1@<eax>);
char __usercall sub_5217D8@<al>(int a1@<eax>);
int __usercall sub_52184C@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
void nullsub_342();
void __usercall sub_521880(int a1@<eax>, unsigned int *a2@<edx>, int a3@<ecx>);
int __usercall sub_521B50@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_521BF4@<al>(int a1@<eax>);
char __cdecl sub_521C14(int a1);
bool __usercall sub_521C44@<al>(char a1@<al>, int a2);
int __usercall sub_521E58@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_522038@<al>(int a1@<eax>);
int __usercall sub_5220B4@<eax>(int result@<eax>, int a2@<ecx>);
int __userpurge sub_5220D4@<eax>(int result@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>, int a4, int a5);
void __userpurge sub_52210C(int a1@<eax>, int a2@<edx>, char a3@<cl>, __int16 a4);
void __usercall sub_5221A8(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5221F4@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
void __usercall sub_522210(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_522264@<eax>(int a1@<eax>);
int __usercall sub_52226C@<eax>(_BYTE *a1@<eax>, int *a2@<edx>, int *a3@<ecx>);
void __usercall sub_522308(_DWORD *a1@<eax>, int a2@<edx>);
void __usercall sub_522334(_DWORD *a1@<eax>, int a2@<edx>);
void __usercall sub_522360(_DWORD *a1@<eax>, int a2@<edx>);
void __usercall sub_52238C(_DWORD *a1@<eax>, int a2@<edx>);
int __userpurge sub_5223B8@<eax>(int result@<eax>, unsigned __int16 a2@<dx>, int a3@<ecx>, int a4);
int __usercall sub_5223EC@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_522474@<eax>(int result@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>, int a4, int a5);
int __usercall sub_5224AC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5224F0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_522570@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_522590@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
void __usercall sub_5225B0(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_522608@<al>(_BYTE *a1@<eax>);
char __usercall sub_522644@<al>(int a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_5226FC@<eax>(_BYTE *result@<eax>);
int __usercall sub_522724@<eax>(int a1@<eax>);
int __usercall sub_522734@<eax>(int a1@<eax>);
int __usercall sub_522744@<eax>(int a1@<eax>);
int __usercall sub_522754@<eax>(int result@<eax>, int a2);
int __usercall sub_52278C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5227C8@<eax>(int result@<eax>);
void __usercall sub_5227EC(int *a1@<eax>, int *a2@<edx>);
int __usercall sub_522860@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int *__usercall sub_5228D4@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5228F4@<al>(int a1@<eax>);
int __usercall sub_522930@<eax>(int result@<eax>);
int __usercall sub_522960@<eax>(int result@<eax>);
void __fastcall sub_522984(int a1, int a2);
int __usercall sub_52298C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5229F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_522A54(int a1, int a2);
int __usercall sub_522A5C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_522A90@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_522B0C@<eax>(int a1@<eax>);
int __cdecl sub_522B28(int a1);
int __usercall sub_522BCC@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_522C2C@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_522D30(int *a1@<eax>, int a2@<edx>);
int (**sub_522D54())();
bool __usercall sub_522D5C@<al>(int a1@<eax>);
bool __usercall sub_522D7C@<al>(int a1@<eax>);
bool __usercall sub_522D9C@<al>(int a1@<eax>);
bool __usercall sub_522DBC@<al>(int a1@<eax>);
bool __usercall sub_522DDC@<al>(int a1@<eax>);
bool __usercall sub_522DFC@<al>(int a1@<eax>);
int __usercall sub_522E1C@<eax>(int *a1@<eax>);
_DWORD *__usercall sub_522E54@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_522F04@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_522F40@<eax>(int a1@<eax>, int *a2@<edx>);
bool __usercall sub_522FF0@<al>(int *a1@<eax>);
int __usercall sub_52301C@<eax>(int a1@<eax>);
int __usercall sub_523024@<eax>(int result@<eax>);
int __usercall sub_52304C@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_523090@<eax>(int a1@<eax>);
int __usercall sub_5230AC@<eax>(int result@<eax>);
int __usercall sub_5230BC@<eax>(int result@<eax>, int a2@<edx>);
void __usercall sub_5230EC(int *a1@<eax>, int a2@<edx>);
int __usercall sub_523230@<eax>(int result@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_523264@<eax>(int a1@<eax>);
int __userpurge sub_523270@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, _DWORD *a4);
int __userpurge sub_523380@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, _DWORD *a4);
int __usercall sub_523490@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5234B4@<eax>(int a1@<eax>);
int __usercall sub_5234CC@<eax>(int a1@<eax>);
int __usercall sub_5234D8@<eax>(int a1@<eax>);
int __usercall sub_5234E8@<eax>(_BYTE *a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_523558@<eax>(int result@<eax>);
__int64 *__usercall sub_52358C@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 *__usercall sub_5235AC@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 __usercall sub_5235BC@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_5235D4@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
__int64 __usercall sub_5235E4@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_5235FC@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 __usercall sub_523614@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
int __usercall sub_52362C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_523650@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_523658@<eax>(int a1@<eax>);
int __usercall sub_523660@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5237CC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_523814@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_523838@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_52398C@<eax>(_DWORD *result@<eax>, int a2@<ecx>);
int __usercall sub_523A60@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_523AD8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_523B08@<eax>(
        int result@<eax>,
        int a2@<edx>,
        int *a3@<ecx>,
        char a4,
        int *a5,
        _DWORD *a6,
        unsigned __int8 a7);
int __usercall sub_523F50@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_523FB8@<al>(int a1@<eax>, int a2@<edx>, char a3@<cl>, int a4);
int __usercall sub_524110@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>, _DWORD *a3@<ecx>, int a4);
int __usercall sub_524158@<eax>(char a1@<al>, int a2);
int __usercall sub_5242E4@<eax>(int a1@<ebx>);
OLECHAR ***__usercall sub_524338@<eax>(int a1@<ecx>, int a2@<edi>, int a3);
void __cdecl sub_5245B0(int a1);
void __usercall sub_52461C(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>);
int __usercall sub_5247F8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52488C@<eax>(int result@<eax>);
int __usercall sub_524894@<eax>(int result@<eax>);
int __usercall sub_5248B4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5248BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_524990@<eax>(int a1@<eax>);
int __usercall sub_5249A8@<eax>(int *a1@<eax>, char a2@<dl>);
// attributes: thunk
int __usercall sub_524A98@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_524A9F(int a1@<ebp>);
bool __usercall sub_524AF0@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_524B04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_524B24@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_524B70@<eax>(__int64 ***a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_524BB8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_524CD8@<eax>(__int64 ***a1@<eax>, char *a2@<edx>);
int sub_524D74();
int __usercall sub_524DB0@<eax>(int a1@<eax>);
int __usercall sub_524DD0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_524E10@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_524E40@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>);
void __fastcall sub_524E68(LPCWSTR lpClassName, int a2);
void __usercall sub_524ED4(int *a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_524F3C@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_525050@<eax>(int *a1@<eax>);
HWND __usercall sub_525324@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_525364@<eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 *__usercall sub_5253A0@<eax>(int *a1@<eax>, __int64 *a2@<edx>);
bool __usercall sub_5253F8@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __cdecl sub_52540C(int a1);
int __usercall sub_5254E0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52554C@<eax>(_DWORD *a1@<eax>, void *a2@<ecx>);
int __usercall sub_5255B4@<eax>(int a1@<eax>);
int __usercall sub_525630@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_525678@<eax>(_DWORD *result@<eax>);
int __usercall sub_525710@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_525734@<eax>(
        int result@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        _DWORD *a4,
        int a5,
        int a6,
        int a7,
        int a8);
BOOL __thiscall EnumFunc(void *this, HWND hWnd, LPARAM a3);
int __usercall sub_5257C8@<eax>(int result@<eax>);
int __usercall sub_52583C@<eax>(int result@<eax>);
HWND __usercall sub_525854@<eax>(int *a1@<eax>);
int __usercall sub_5258E0@<eax>(int a1@<eax>);
_BYTE *__usercall sub_525A40@<eax>(_BYTE *a1@<eax>, int a2@<ecx>);
int __usercall sub_525B08@<eax>(int result@<eax>, char a2@<dl>);
_BYTE *__usercall sub_525B34@<eax>(_BYTE *result@<eax>, HWND a2@<edx>);
int __usercall sub_525C18@<eax>(int a1@<eax>);
bool __usercall sub_525C90@<al>(int a1@<eax>, int a2);
int __userpurge sub_525D5C@<eax>(int a1@<eax>, char a2, char a3);
char __usercall sub_525E20@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_525EE4@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_52603C(int *a1@<eax>, unsigned int *a2@<edx>, int a3@<ecx>);
__int16 __usercall sub_526634@<ax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52674C@<eax>(HWND a1@<eax>, _DWORD *a2@<edx>, DWORD a3@<ecx>);
BOOL __usercall sub_526780@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5268F0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_526924@<eax>(int a1@<eax>, HDC a2@<edx>, int a3@<ecx>);
void __fastcall sub_526C04(int a1, _DWORD *a2, int a3);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_526C64@<eax>(HDC a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int __usercall sub_526D02@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_526D20@<eax>(int a1@<eax>, HDC a2@<edx>, int a3@<ecx>, int a4);
// attributes: thunk
int __usercall sub_526F58@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_526F78@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
// attributes: thunk
int __usercall sub_527082@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5270A9@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5271A4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5271DD@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5271EC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_52720C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_527230@<eax>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_52724C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_527260@<eax>(int a1@<eax>);
int __usercall sub_527270@<eax>(int a1@<eax>);
int __usercall sub_527280@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5272A0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5272C0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5272E4@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_527308@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_52732C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
char __usercall sub_52734C@<al>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_527380@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_527438@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5274F0@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_527544(int a1@<eax>);
int __usercall sub_5275C0@<eax>(_DWORD *a1@<eax>);
HCURSOR __usercall sub_5275DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5276E8@<eax>(int a1@<eax>);
int __usercall sub_527710@<eax>(_DWORD *a1@<eax>);
int __usercall sub_52772C@<eax>(int a1@<eax>);
int __usercall sub_527794@<eax>(int a1@<eax>);
int __usercall sub_5277A4@<eax>(int result@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_52782C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_52791C@<eax>(int a1@<eax>);
int __fastcall sub_5279B4(int a1, int a2);
void nullsub_344();
int __usercall sub_5279C4@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5279E4@<eax>(int result@<eax>, int a2@<ecx>);
int __userpurge sub_527A04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_527A58@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>, int a4, unsigned __int8 a5, int a6);
void __userpurge sub_527A8C(int *a1@<eax>, int a2, char a3, int a4);
int __usercall sub_527AD0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_527B2C(int *this);
int __usercall sub_527B50@<eax>(int a1@<eax>);
int __usercall sub_527B64@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_527B88@<eax>(LPRECT lpRect@<ecx>, int a2@<eax>, int a3@<edx>, int a4, _DWORD *a5);
int __usercall sub_527BEC@<eax>(int a1@<eax>);
void nullsub_343();
int __usercall sub_527C2C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_527C98@<al>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_527CCC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_527D84@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_527DA8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_527E94@<eax>(int result@<eax>, int a2@<edx>);
void __usercall sub_527EBC(int *a1@<eax>, int a2@<edx>);
int __usercall sub_527F3C@<eax>(int result@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>);
int __usercall sub_527F68@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528018@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528044@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528070@<eax>(int result@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>);
int __usercall sub_52809C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52814C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52816C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52818C@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5281AC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52821C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52823C@<eax>(int a1@<eax>, int a2);
int __usercall sub_5282EC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_528398@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5283B8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5283EC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_52840C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_528490@<eax>(int a1@<eax>);
int __usercall sub_5284AC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5284C8@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_528520@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_528544@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_528564@<eax>(_DWORD *a1@<eax>);
int __usercall sub_52857C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5285B4@<eax>(int a1@<eax>);
void __usercall sub_5285D8(int *a1@<eax>);
void __usercall sub_528618(int *a1@<eax>);
char __usercall sub_528628@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_528648@<eax>(int result@<eax>);
int __usercall sub_52865C@<eax>(int result@<eax>);
// attributes: thunk
int __usercall sub_528670@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_528678@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_528680@<eax>(int a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_528688@<eax>(_BYTE *result@<eax>, int a2@<ecx>);
BOOL __usercall sub_5286B8@<eax>(int a1@<eax>);
int __usercall sub_5286E0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_528728@<eax>(int a1@<eax>);
int __usercall sub_528750@<eax>(int a1@<eax>);
void *__usercall sub_52878C@<eax>(int a1@<eax>);
int __usercall sub_5287CC@<eax>(_BYTE *a1@<eax>);
int __usercall sub_52880C@<eax>(int a1@<eax>);
int __usercall sub_52884C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52888C@<eax>(int result@<eax>);
// attributes: thunk
int __usercall sub_5288B8@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5288C0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5288C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5288D0@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_5288EC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5288F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528954@<eax>(int result@<eax>);
int __usercall sub_528968@<eax>(int result@<eax>);
int __usercall sub_52897C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_528998@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528A30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528B14@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_528B68@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_528BB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_528C14@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_528C48@<eax>(int Y@<ecx>, int X@<edx>, int a3@<eax>, int cy, int a5);
int __usercall sub_528D24@<eax>(int a1@<eax>);
int __usercall sub_528D6C@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int result@<eax>);
int __usercall sub_528DF0@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int a3@<eax>);
int __usercall sub_528EA8@<eax>(int *a1@<eax>);
int __usercall sub_528F58@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_529034@<eax>(int result@<eax>);
int __usercall sub_529048@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_529120@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5291D4@<eax>(int a1@<eax>);
char __usercall sub_5291E4@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_529238@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5292D4@<eax>(int a1@<eax>);
int __usercall sub_5292F0@<eax>(int a1@<eax>);
BOOL __usercall sub_52930C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_529348@<eax>(int a1@<eax>, int a2@<ecx>);
HWND __usercall sub_529388@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_5293C4@<al>(int a1@<eax>);
int __usercall sub_5293E8@<eax>(int result@<eax>);
int __usercall sub_52940C@<eax>(int a1@<eax>);
int __usercall sub_529420@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
BOOL __usercall sub_529578@<eax>(int a1@<eax>, struct tagPOINT *a2@<edx>);
BOOL __usercall sub_529598@<eax>(int a1@<eax>, struct tagRECT *a2@<edx>);
int __usercall sub_5295B0@<eax>(int result@<eax>);
int __usercall sub_5295EC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_52960C@<eax>(int result@<eax>, char a2@<dl>);
char __usercall sub_529630@<al>(int a1@<eax>);
char __usercall sub_52963C@<al>(int a1@<eax>);
int __usercall sub_529648@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_529674@<eax>(int a1@<eax>);
int __usercall sub_529698@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_5296F4@<eax>(int result@<eax>, __int16 a2@<dx>);
int __usercall sub_52970C@<eax>(int result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_52976C@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
bool __usercall sub_5297DC@<al>(int a1@<eax>);
int __usercall sub_5297E8@<eax>(int a1@<eax>);
int __usercall sub_529904@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_529940@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __userpurge sub_5299A0@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, char a5);
int __userpurge sub_529AAC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4);
int __userpurge sub_529AD8@<eax>(int a1@<eax>, int a2@<edx>, int (*a3)(void), int a4);
void __fastcall sub_529B20(int a1, int a2);
// attributes: thunk
int __usercall sub_529B60@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_529B68@<eax>(int a1@<eax>, int *a2@<edx>, int *a3@<ecx>, int *a4, int *a5);
char __userpurge sub_529C2C@<al>(_DWORD **a1@<eax>, int *a2@<edx>, int *a3@<ecx>, int *a4, int *a5);
int __userpurge sub_52A0DC@<eax>(_DWORD **a1@<eax>, int *a2@<edx>, int *a3@<ecx>, int *a4, int *a5);
// attributes: thunk
int __usercall sub_52A118@<eax>(int a1@<eax>);
char __usercall sub_52A120@<al>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int (**sub_52A160())();
char __usercall sub_52A168@<al>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_52A198@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_52A370@<eax>(int result@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_52A3B4@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_52A3E4@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_52A404@<eax>(int result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_52A424@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52A4B0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_52A84D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_52A890@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_52A8F0(int *a1@<eax>, int a2@<edx>);
int __fastcall sub_52A9B0(int a1, int a2);
_DWORD *__usercall sub_52A9FC@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_52AA8E@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_52AACB@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_52AAD8@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_52AE4C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
OLECHAR ***__usercall sub_52AEB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_52B2A0@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_52B348@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_52B380@<eax>(_DWORD *a1@<eax>);
__int16 __usercall sub_52B398@<ax>(int a1@<eax>, char a2@<dl>);
int __stdcall sub_52B3CC(int a1, int a2, int a3);
int sub_52B3D8();
HANDLE __usercall sub_52B3DC@<eax>(int a1@<eax>);
bool __usercall sub_52B40C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52B430@<eax>(int a1@<eax>);
int __usercall sub_52B438@<eax>(int a1@<eax>);
int __usercall sub_52B444@<eax>(int a1@<eax>, char a2@<dl>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__cdecl sub_52B494(int a1);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__cdecl sub_52B4FC(int a1);
_DWORD *__usercall sub_52B564@<eax>(_DWORD *result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_52B590@<eax>(_DWORD *result@<eax>);
int __usercall sub_52B5BC@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_52B638@<eax>(int a1@<eax>);
_DWORD *__usercall sub_52B6C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_52B71C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __usercall sub_52B75C(int a1@<eax>, int a2@<edx>);
void nullsub_345();
_DWORD *__usercall sub_52B814@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
void __usercall sub_52B880(int *a1@<eax>, _DWORD *a2@<edx>);
void __fastcall sub_52B8D4(int a1, int a2);
int __usercall sub_52B8DC@<eax>(HDC a1@<eax>);
// attributes: thunk
int __usercall sub_52B932@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_DWORD *__usercall sub_52B940@<eax>(_DWORD **a1@<eax>);
bool __fastcall sub_52BB3C(int a1, int a2);
int __usercall sub_52BBA0@<eax>(int a1@<eax>);
int __usercall sub_52BBB0@<eax>(int a1@<eax>);
_BYTE *__usercall sub_52BC48@<eax>(_BYTE *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
int __userpurge sub_52BEC4@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
LPRECT __userpurge sub_52BEEC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, LPRECT lprc, int a5);
int __usercall sub_52BF50@<eax>(int a1@<eax>, HDC a2@<edx>);
int __usercall sub_52BFD8@<eax>(int a1@<eax>, int a2@<edx>);
char sub_52BFFC();
int __userpurge sub_52C000@<eax>(HWND a1@<eax>, LONG a2@<edx>, LONG a3@<ecx>, _DWORD *a4);
int sub_52C040();
char __userpurge sub_52C058@<al>(int dxHotspot@<ecx>, int iTrack@<edx>, int a3@<eax>, int dyHotspot);
int __usercall sub_52C0AC@<eax>(int result@<eax>, __int16 a2@<dx>);
HIMAGELIST __usercall sub_52C0D8@<eax>(int a1@<eax>, POINT *a2@<edx>, int a3@<ecx>);
int __userpurge sub_52C108@<eax>(int a1@<eax>, int a2);
BOOL __userpurge sub_52C18C@<eax>(int a1@<eax>, HWND a2@<edx>, LONG a3@<ecx>, LONG a4);
int __usercall sub_52C1F8@<eax>(int a1@<eax>);
BOOL __usercall sub_52C228@<eax>(int a1@<eax>, LONG a2@<edx>, LONG a3@<ecx>);
int sub_52C270();
int sub_52C288();
BOOL __usercall sub_52C2A0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_52C2F8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_52C354@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_52C384@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
void __usercall sub_52C3A4(int *a1@<eax>, int a2@<edx>);
void nullsub_346();
int __usercall sub_52C454@<eax>(int a1@<eax>);
bool __usercall sub_52C470@<al>(int a1@<eax>);
_DWORD *__usercall sub_52C494@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_52C4D0@<eax>(int a1@<eax>);
int sub_52C4E4();
int __usercall sub_52C508@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_52C5D0@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_52C654@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_52C70C@<eax>(int a1@<eax>);
int __usercall sub_52C7F8@<eax>(int a1@<eax>);
int __cdecl sub_52C880(int a1);
int __usercall sub_52C8B0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_52CA2C@<eax>(int a1@<eax>);
int __usercall sub_52CA54@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_52CA58@<eax>(int a1@<eax>);
int __usercall sub_52CA68@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_52CAA4@<eax>(int result@<eax>);
int __usercall sub_52CB04@<eax>(int a1@<eax>);
int __usercall sub_52CB10@<eax>(int a1@<eax>);
int __usercall sub_52CB2C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_52CB38@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_52CCA0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
char __usercall sub_52CCF4@<al>(int a1@<eax>, _DWORD *a2@<ecx>);
int __usercall sub_52CD0C@<eax>(int result@<eax>);
int __usercall sub_52CD10@<eax>(int result@<eax>);
int __usercall sub_52CD24@<eax>(_DWORD *a1@<eax>, int a2);
int __usercall sub_52CD7C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52CDA8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __userpurge sub_52CDE4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_52CDFC@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int sub_52CE74();
int __userpurge sub_52CE84@<eax>(int result@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>, int a4);
int __userpurge sub_52D0AC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, char a4, char a5);
int __userpurge sub_52D264@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, char a4);
int __userpurge sub_52D2DC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int *a3@<ecx>, _DWORD *a4);
int __usercall sub_52D3E0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_52D478@<eax>(int a1@<eax>, int a2);
int __usercall sub_52D58C@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_52D614@<eax>(volatile __int32 *a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>, int a5);
_DWORD *__usercall sub_52D6DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_52DA18@<eax>(int a1@<eax>, int a2@<edx>, int a3);
int __userpurge sub_52DAB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_52DB44@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6);
int __userpurge sub_52DBAC@<eax>(int a1@<eax>, int *a2);
_DWORD *__usercall sub_52DD08@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_52DE3C@<eax>(int a1@<eax>, int a2@<ecx>, LPPOINT lpPoints, char a4);
_DWORD *__usercall sub_52DFB0@<eax>(_DWORD *a1@<eax>, int a2);
_DWORD *__usercall sub_52DFE4@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
int __usercall sub_52E040@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52E080@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
char __usercall sub_52E320@<al>(int *a1@<eax>, char a2@<dl>);
int __usercall sub_52E418@<eax>(int result@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_52E498@<eax>(int a1@<eax>, void *a2@<ecx>, int a3@<edi>, int a4);
_DWORD *__usercall sub_52E524@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>, int a4);
OLECHAR ***__usercall sub_52E638@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_52E828@<eax>(int result@<eax>, int a2);
int __usercall sub_52E8BC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52E8EC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52E904@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_52E93C@<eax>(int *a1@<eax>, int a2@<edx>, int *a3@<ecx>);
int __usercall sub_52E99C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_52EA28@<eax>(int result@<eax>);
int __usercall sub_52EA50@<eax>(int result@<eax>, _DWORD *a2@<edx>);
int __usercall sub_52EA60@<eax>(int a1@<eax>);
_DWORD *__usercall sub_52EA6C@<eax>(_DWORD *result@<eax>);
int __usercall sub_52EB58@<eax>(_DWORD *a1@<eax>, int a2);
int __usercall sub_52EC00@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_52EC58@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ebx>);
int __usercall sub_52ECD4@<eax>(int *a1@<eax>, int a2);
int __usercall sub_52ED54@<eax>(int *a1@<eax>, int a2);
int *__usercall sub_52EEA0@<eax>(_DWORD **a1@<eax>, _DWORD *a2@<edx>, char a3@<cl>);
HCURSOR __usercall sub_52EF28@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_52F1C0(int a1, int a2);
int __fastcall sub_52F1E8(int a1, int a2);
int __fastcall sub_52F220(int a1, char a2);
int __fastcall sub_52F24C(_DWORD *a1, _DWORD *a2);
int __userpurge sub_52F28C@<eax>(int result@<eax>, char a2@<dl>, __int16 a3@<cx>, _BYTE *a4, int a5, int a6);
int __cdecl sub_52F3B4(int a1);
_DWORD *__userpurge sub_52F444@<eax>(_DWORD *result@<eax>, int a2@<ecx>, int a3, int a4);
int __userpurge sub_52F490@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5, int a6);
_DWORD *__userpurge sub_52F4FC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, volatile __int32 *a4);
int __usercall sub_52F5F0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_52F680@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_52F6AC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
// attributes: thunk
HWND sub_52F6DC();
BOOL __fastcall sub_52F6E4(int a1, struct tagPOINT *a2);
bool sub_52F710();
bool __usercall sub_52F71C@<al>(int a1@<eax>);
BOOL __usercall sub_52F740@<eax>(int a1@<eax>);
int __usercall sub_52F758@<eax>(int a1@<eax>);
HWND __usercall sub_52F784@<eax>(int a1@<eax>, LRESULT a2@<ecx>);
HWND __fastcall sub_52F7AC(int a1, HWND a2);
BOOL __fastcall sub_52F7D4(int a1, int *a2);
_DWORD *__usercall sub_52F7E4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
HWND __usercall sub_52F814@<eax>(HWND result@<eax>, int a2@<edx>);
int *__thiscall sub_52F878(void *this);
int __usercall sub_52F900@<eax>(__int32 a1@<eax>);
// attributes: thunk
BOOL __stdcall WINNLSEnableIME(HWND a1, BOOL a2);
BOOL __usercall sub_52F918@<eax>(HWND a1@<eax>, char a2@<dl>);
HIMC __usercall sub_52F944@<eax>(HWND a1@<eax>, unsigned __int8 a2@<dl>);
BOOL __usercall sub_52FA4C@<eax>(HKL a1@<eax>);
_DWORD *sub_52FA60();
_DWORD *sub_52FB04();
_DWORD *__usercall sub_52FD6C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_52FDB0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_52FDF8@<eax>(int result@<eax>, int a2@<ecx>);
void __fastcall sub_52FE0C(int a1, _DWORD *a2);
_DWORD *__usercall sub_52FE2C@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_52FE74@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>, char a4, int a5, int a6);
_DWORD *__usercall sub_52FF68@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, char a3@<cl>);
_DWORD *__userpurge sub_52FF8C@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_52FFC4@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
void nullsub_339();
int __usercall sub_530194@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_5301A4@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5301AC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_530230@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_53024C@<eax>(int *a1@<eax>);
int __usercall sub_5302AC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5302C0@<eax>(int a1@<eax>);
int sub_5302D0();
int __usercall sub_5302EC@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_530390@<eax>(int a1@<eax>, int *a2@<edx>);
void __fastcall sub_5303CC(int a1, int a2);
int __usercall sub_5303D4@<eax>(HDC a1@<eax>);
// attributes: thunk
int __usercall sub_53042A@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_530438@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_53045C(int a1, int a2);
int __usercall sub_5305C8@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5305E0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_530630@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_530680@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_53068C@<eax>(int result@<eax>);
void nullsub_347();
int __usercall sub_530698@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
// bad sp value at call has been detected, the output may be wrong!
BOOL __fastcall sub_5306C4(int a1, char *a2);
// attributes: thunk
int __usercall sub_5308F9@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_530910@<eax>(int result@<eax>);
int __usercall sub_530918@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_530A84@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_530B1C@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_530B58@<eax>(int a1@<eax>);
int __userpurge sub_530B70@<eax>(int a1@<eax>, char a2@<dl>, int a3);
_DWORD *__usercall sub_530BF4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __cdecl sub_530CB8(int a1);
_DWORD *__usercall sub_530DC4@<eax>(_DWORD *a1@<eax>);
// attributes: thunk
int __usercall sub_530F1F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_530FEA@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5310E6@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_53116F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5311EF@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void nullsub_84();
// attributes: thunk
int __usercall sub_5311F7@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_53124C@<eax>(int result@<eax>);
int __usercall sub_531254@<eax>(int a1@<eax>, int a2@<edx>);
BOOL __usercall sub_531260@<eax>(int a1@<eax>);
int sub_53126C();
_DWORD *__usercall sub_531270@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5312DC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_531328@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_531394@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5313A4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5313C4@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_5313E4@<eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<edi>);
int __usercall sub_531410@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_531488(int a1@<eax>);
int __usercall sub_53149C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5314C0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5314E0@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_531500@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_531548@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
char __usercall sub_5315E4@<al>(int a1@<eax>, _BYTE *a2@<edx>);
int __usercall sub_531618@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_53164C@<eax>(int result@<eax>, int a2@<edx>);
int sub_531664();
int __usercall sub_536964@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
volatile signed __int8 *__fastcall sub_536A1C(int a1, __int64 **a2);
int __userpurge sub_536A30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __fastcall sub_536ACC(int cchText, HDC hdc, UINT format, LPRECT lprc);
int __usercall sub_536B00@<eax>(int *a1@<eax>, struct _EXCEPTION_REGISTRATION_RECORD *a2@<edx>, int a3@<ecx>);
HRESULT __usercall sub_536E24@<eax>(_DWORD *a1@<eax>, RECT *a2@<edx>);
// attributes: thunk
int __usercall sub_536EA3@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_536EB4(int a1@<eax>);
void __usercall sub_536FB0(int *a1@<eax>);
int *__usercall sub_536FCC@<eax>(int *result@<eax>);
// attributes: thunk
int __usercall sub_537079@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __usercall sub_537124(int a1@<eax>, char a2@<dl>);
bool __usercall sub_537148@<al>(int a1@<eax>);
int __usercall sub_537154@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5371A8@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_53720C@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_537238@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
void __usercall sub_537268(int *a1@<eax>);
int __usercall sub_537284@<eax>(int a1@<eax>);
int __usercall sub_537294@<eax>(int a1@<eax>);
void __usercall sub_5372EC(int *a1@<eax>);
_DWORD *__usercall sub_537308@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_537414@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int sub_5374F8();
LRESULT __usercall sub_537518@<eax>(int a1@<eax>, WPARAM a2@<edx>);
char __usercall sub_537538@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_537598@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5375AC@<eax>(int result@<eax>, char a2@<dl>);
volatile __int32 *__usercall sub_5375E4@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_537634@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_537678@<eax>(int a1@<eax>);
int __usercall sub_5376B0@<eax>(int a1@<eax>);
int __usercall sub_5376B8@<eax>(int a1@<eax>);
char __usercall sub_5376EC@<al>(int a1@<eax>, unsigned __int8 a2@<dl>);
char __usercall sub_537724@<al>(int a1@<eax>, char a2@<dl>);
char __usercall sub_53779C@<al>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_5377C4@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
WPARAM __usercall sub_53780C@<eax>(int a1@<eax>, WPARAM a2@<ecx>);
LRESULT __usercall sub_537830@<eax>(int a1@<eax>, WPARAM a2@<edx>);
WPARAM __usercall sub_537850@<eax>(int a1@<eax>);
LRESULT __usercall sub_537880@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5378E4@<eax>(_DWORD *a1@<eax>);
BOOL __usercall sub_537908@<eax>(int a1@<eax>);
LRESULT __usercall sub_537920@<eax>(int a1@<eax>);
LRESULT __usercall sub_53793C@<eax>(int a1@<eax>);
LRESULT __usercall sub_537958@<eax>(int a1@<eax>);
LRESULT __usercall sub_537974@<eax>(int a1@<eax>);
LRESULT __usercall sub_537990@<eax>(int a1@<eax>);
LRESULT __usercall sub_5379AC@<eax>(int a1@<eax>);
LRESULT __usercall sub_5379C8@<eax>(int a1@<eax>);
signed int __usercall sub_5379E4@<eax>(int a1@<eax>, __int64 *a2@<edx>, signed int a3@<ecx>);
LRESULT __usercall sub_537A84@<eax>(int a1@<eax>, LPARAM a2@<edx>);
_DWORD *__usercall sub_537AA4@<eax>(int a1@<eax>, __int64 **a2@<edx>);
OLECHAR **__usercall sub_537B44@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int16 a3@<cx>, int a4@<edi>);
OLECHAR **__usercall sub_537C2C@<eax>(int a1@<eax>, _WORD *a2@<edx>);
bool __fastcall sub_537E58(int a1, int a2);
_DWORD *__usercall sub_53800C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_53808C@<eax>(int a1@<eax>, int (__stdcall ***a2)(_DWORD, int, int)@<edx>, char a3@<cl>);
LRESULT __usercall sub_538134@<eax>(int a1@<eax>, int a2@<edx>);
char *__usercall sub_538154@<eax>(int a1@<eax>, int a2@<edx>);
HWND __usercall sub_538248@<eax>(int a1@<eax>, _BYTE *a2@<edx>);
int __usercall sub_5382B8@<eax>(int a1@<eax>);
int __usercall sub_5383D0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_53840C@<eax>(int a1@<eax>);
int __usercall sub_538444@<eax>(int a1@<eax>);
int __usercall sub_538528@<eax>(int a1@<eax>);
__int16 __usercall sub_53854C@<ax>(char *a1@<eax>, int a2@<edx>);
LRESULT __usercall sub_5385F0@<eax>(_DWORD *a1@<eax>);
bool __usercall sub_538630@<al>(int a1@<eax>);
int __usercall sub_538660@<eax>(int a1@<eax>);
int __usercall sub_538694@<eax>(int a1@<eax>);
char __usercall sub_5386BC@<al>(int a1@<eax>);
void __usercall sub_538700(int a1@<eax>, int a2@<edx>);
void __usercall sub_538724(int a1@<eax>);
_DWORD *__usercall sub_538760@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<edi>, int a4@<esi>);
void __usercall sub_538840(int *a1@<eax>);
void __usercall sub_538880(int a1@<eax>, int a2@<edx>);
int __usercall sub_538960@<eax>(int a1@<eax>);
int __usercall sub_538968@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_53898C@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_5389B8@<eax>(int a1@<eax>);
int __usercall sub_538A1C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
char __usercall sub_538A74@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int (**sub_538AD4())();
int sub_538ADC();
void nullsub_348();
void __usercall sub_538AE4(int a1@<eax>, unsigned int *a2@<edx>, int a3@<ecx>);
HGDIOBJ __usercall sub_538B5C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_538BC4@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_538BF0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_538C28@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_538C70@<eax>(int result@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_538C84@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_538CCC@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
int __usercall sub_538CF8@<eax>(int a1@<eax>);
int __usercall sub_538D18@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int sub_538E24();
char __usercall sub_538E44@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_538E88@<al>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_538EB0@<eax>(int result@<eax>);
int __usercall sub_538ED0@<eax>(_DWORD *a1@<eax>);
char __usercall sub_539018@<al>(_DWORD *a1@<eax>);
int sub_539198();
char __usercall sub_53919C@<al>(int a1@<eax>, unsigned __int8 a2@<dl>);
char __usercall sub_539228@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_539268@<al>(int a1@<eax>, char a2@<dl>);
char __usercall sub_539324@<al>(int a1@<eax>);
int __usercall sub_539394@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5393D0@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
char __usercall sub_539438@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5394E0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_539530@<eax>(_DWORD *result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_539560@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_539590@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_539714@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5397AC@<eax>(int a1@<eax>);
int __usercall sub_5397EC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int (**sub_539874())();
int *__usercall sub_53987C@<eax>(int a1@<eax>);
char __usercall sub_5398B8@<al>(int a1@<eax>);
int __usercall sub_5398D4@<eax>(_DWORD *a1@<eax>);
bool __usercall sub_53990C@<al>(int a1@<eax>);
int *__usercall sub_53992C@<eax>(int a1@<eax>);
int __usercall sub_53995C@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
void __usercall sub_5399A4(int *a1@<eax>, int a2@<edx>);
void __usercall sub_5399BC(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_539A2C@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_539AB0@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_539B04@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
HGDIOBJ __usercall sub_539B30@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_539B98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_539C14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int sub_539CCC();
int __usercall sub_539CEC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_539D78@<eax>(int *a1@<eax>);
bool __usercall sub_539E34@<al>(int a1@<eax>);
int __usercall sub_539E54@<eax>(int result@<eax>, char a2@<dl>);
_DWORD *__userpurge sub_539E90@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int nMaxPos);
_DWORD *__usercall sub_53A050@<eax>(int *a1@<eax>, int a2@<edx>);
char __usercall sub_53A064@<al>(int a1@<eax>, signed int a2@<edx>);
_DWORD *__usercall sub_53A0FC@<eax>(int *a1@<eax>, int a2@<edx>);
bool __fastcall sub_53A128(int a1, int a2);
int __usercall sub_53A13C@<eax>(int a1@<eax>);
int __usercall sub_53A160@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_53A180@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_53A2F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>, int a4@<esi>);
LRESULT __usercall sub_53A350@<eax>(int a1@<eax>, UINT *a2@<edx>);
int __usercall sub_53A378@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_53A380@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_53A3C4@<eax>(int a1@<eax>, int a2@<edx>);
void __fastcall sub_53A400(int a1, int a2);
BOOL __usercall sub_53A408@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_53A4AC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_53A58D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_53A5B4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
void __usercall sub_53A5C0(int *a1@<eax>, unsigned int *a2@<edx>, int a3@<ecx>);
int __usercall sub_53A5C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_53A61C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool __usercall sub_53A668@<al>(int a1@<eax>);
int __usercall sub_53A678@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_53A6A4@<eax>(_DWORD **a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_53A6E4@<al>(int a1@<eax>);
// attributes: thunk
int sub_53A728();
char __usercall sub_53A730@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53A784@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
// attributes: thunk
int sub_53A7B0();
int __usercall sub_53A7B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53A7D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53A7E8@<eax>(int a1@<eax>);
int __usercall sub_53A888@<eax>(int a1@<eax>);
int __usercall sub_53A8DC@<eax>(int result@<eax>);
// attributes: thunk
int __usercall sub_53A8F4@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_53A8FC@<eax>(int a1@<eax>);
bool sub_53A904();
_DWORD *__usercall sub_53A918@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53A93C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53AC3C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53AC90@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53AD5C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53AE2C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53AE50@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53B14C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53B1A0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53B268@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_53B334@<eax>(int a1@<eax>, HDC a2@<edx>);
_DWORD *__usercall sub_53B628@<eax>(int a1@<eax>, HDC a2@<edx>);
int __usercall sub_53B904@<eax>(int result@<eax>);
int __usercall sub_53B910@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_53B928@<al>(_BYTE *a1@<eax>, int a2@<edx>);
char __usercall sub_53BA50@<al>(_BYTE *a1@<eax>, int a2@<edx>);
char __usercall sub_53BBC8@<al>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
// attributes: thunk
char __usercall sub_53BEA8@<al>(_BYTE *a1@<eax>, int a2@<edx>);
int __usercall sub_53BEB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53BEC8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53BEE0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53BEF8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53BF10@<eax>(_BYTE *a1@<eax>);
_BYTE *__usercall sub_53BF60@<eax>(_BYTE *result@<eax>, int a2@<edx>);
int __usercall sub_53BFD8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
char __usercall sub_53C01C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53C068@<eax>(int a1@<eax>);
int __usercall sub_53C070@<eax>(int a1@<eax>);
int __usercall sub_53C078@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53C198@<eax>(int a1@<eax>);
int __usercall sub_53C200@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53C2B0@<eax>(int a1@<eax>);
int __usercall sub_53C2F0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_53C33C@<al>(int a1@<eax>);
int __usercall sub_53C378@<eax>(int a1@<eax>, HDC a2@<edx>);
int __fastcall sub_53C45C(int a1, _DWORD *a2);
_DWORD *__userpurge sub_53C4B0@<eax>(_DWORD *a1@<eax>, HDC a2@<edx>, char a3@<cl>, char a4);
int __cdecl sub_53C64C(int a1);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_53C6FC@<eax>(
        int (__usercall *a1)@<eax>(unsigned int@<ebp>, _DWORD *, int)@<eax>,
        struct _EXCEPTION_REGISTRATION_RECORD *a2@<edx>,
        int a3@<ecx>);
// attributes: thunk
int __usercall sub_53CEF1@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_53D0A6@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_53D0CC@<eax>(int a1@<eax>, HDC a2@<edx>, int a3@<ebx>);
int __usercall sub_53D120@<eax>(unsigned __int8 *a1@<eax>);
LRESULT __usercall sub_53D12C@<eax>(int a1@<eax>);
int __usercall sub_53D17C@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_53D1B4@<al>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_53D2F4@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_BYTE *__usercall sub_53D32C@<eax>(_BYTE *result@<eax>, int a2@<edx>);
int __usercall sub_53D348@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53D394@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53D3F8@<eax>(int a1@<eax>);
int __usercall sub_53D408@<eax>(int a1@<eax>, int a2@<edx>);
LRESULT __usercall sub_53D4B8@<eax>(int a1@<eax>);
int __usercall sub_53D4EC@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_53D528@<eax>(_BYTE *a1@<eax>);
int __usercall sub_53D540@<eax>(_BYTE *a1@<eax>);
int sub_53D558();
int sub_53D578();
__int32 __usercall sub_53D76C@<eax>(__int32 a1@<eax>);
// attributes: thunk
HRESULT __stdcall SHCreateItemFromParsingName(PCWSTR pszPath, IBindCtx *pbc, const IID *const riid, void **ppv);
// attributes: thunk
BOOL __stdcall MEMORY[0x53D784](HANDLE hPrinter);
// attributes: thunk
LONG __stdcall DocumentPropertiesW(
        HWND hWnd,
        HANDLE hPrinter,
        LPWSTR pDeviceName,
        PDEVMODEW pDevModeOutput,
        PDEVMODEW pDevModeInput,
        DWORD fMode);
// attributes: thunk
LONG __stdcall DocumentPropertiesW_0(
        HWND hWnd,
        HANDLE hPrinter,
        LPWSTR pDeviceName,
        PDEVMODEW pDevModeOutput,
        PDEVMODEW pDevModeInput,
        DWORD fMode);
// attributes: thunk
BOOL __stdcall EnumPrintersW(
        DWORD Flags,
        LPWSTR Name,
        DWORD Level,
        LPBYTE pPrinterEnum,
        DWORD cbBuf,
        LPDWORD pcbNeeded,
        LPDWORD pcReturned);
// attributes: thunk
BOOL __stdcall OpenPrinterW(LPWSTR pPrinterName, LPHANDLE phPrinter, LPPRINTER_DEFAULTSW pDefault);
_WORD *__usercall sub_53DEA0@<eax>(_DWORD *a1@<eax>);
BOOL __stdcall proc(HDC a1, int a2);
int __userpurge sub_53E01C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_53E07C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
_DWORD *__usercall sub_53E37C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_53E3B8@<eax>(int a1@<eax>, int a2@<ecx>);
void __usercall sub_53E3FC(int a1@<eax>);
_DWORD *__usercall sub_53E444@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_53E480@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_53E4F8@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_53E628@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_53E698@<eax>(int a1@<eax>);
int __usercall sub_53E6C8@<eax>(int a1@<eax>);
int __usercall sub_53E75C@<eax>(int a1@<eax>);
int __usercall sub_53E790@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_53E7C4@<eax>(int a1@<eax>, _WORD *a2@<edx>, _WORD *a3@<ecx>, _DWORD *a4, _WORD *a5);
int __usercall sub_53E830@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __userpurge sub_53E86C@<eax>(
        int a1@<eax>,
        WCHAR *a2@<edx>,
        int a3@<ecx>,
        int a4,
        struct _EXCEPTION_REGISTRATION_RECORD *a5);
int __usercall sub_53EA88@<eax>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
int __stdcall Proc(const LOGFONTW *a1, const TEXTMETRICW *a2, DWORD a3, LPARAM a4);
int __usercall sub_53EB04@<eax>(int a1@<eax>);
int __usercall sub_53EBA0@<eax>(int a1@<eax>);
int __usercall sub_53EBB4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_53EC18@<eax>(int a1@<eax>, __int16 a2@<dx>);
int __usercall sub_53EC90@<eax>(int a1@<eax>);
_DWORD *__usercall sub_53ECFC@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_53ED80@<eax>(int a1@<eax>);
int __usercall sub_53ED9C@<eax>(int a1@<eax>);
int __usercall sub_53EDB8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_53EDD0@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_53EEEC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
BOOL __stdcall GetDefaultPrinterW(LPWSTR pszBuffer, LPDWORD pcchBuffer);
int __usercall sub_53F134@<eax>(int a1@<eax>);
_DWORD *__usercall sub_53F354@<eax>(_DWORD *result@<eax>);
_DWORD *__usercall sub_53F3A4@<eax>(int a1@<eax>);
int __thiscall sub_53F3C0(void *this);
_DWORD *__usercall sub_53F3E0@<eax>(_DWORD *a1@<eax>);
_DWORD *sub_53F3F4();
int __usercall sub_53F5A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_53F87C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __userpurge sub_53F8B4@<eax>(int a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4);
int __userpurge sub_53F910@<eax>(int a1@<edx>, OLECHAR **a2@<ecx>, int a3@<edi>, int a4);
void sub_53F96C();
void sub_53F9CC();
_WORD *__usercall sub_53FA04@<eax>(_WORD *a1@<eax>, _WORD *a2@<edx>, int a3@<ecx>);
_WORD *__usercall sub_53FA2C@<eax>(_WORD *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
int nullsub_353();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_354(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_355@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
void __thiscall sub_541DE4(void *this);
bool __usercall sub_541E10@<al>(_DWORD *a1@<eax>, void *a2@<ecx>);
_DWORD *__usercall sub_541E50@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_541E94@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_541EF8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_541F6C@<eax>(int a1@<eax>, int (__stdcall ***a2)(_DWORD, int, int)@<edx>, _DWORD *a3@<ecx>);
char __usercall sub_54201C@<al>(char a1@<sf>, int a2@<eax>, int _ECX@<ecx>, char a4@<bh>);
_DWORD *__usercall sub_54203C@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5420AC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5420DC@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, int a4, unsigned __int16 a5);
_DWORD *__usercall sub_542194@<eax>(
        unsigned __int64 a1@<edx:eax>,
        __int32 a2@<ecx>,
        int a3@<ebx>,
        _DWORD *a4@<ebp>,
        _BYTE *a5@<edi>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_54244C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_5424E0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5427A0@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5428AC@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        __int32 a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
_DWORD *__usercall sub_54298C@<eax>(int a1@<eax>, int a2@<edx>);
char __userpurge sub_5429A0@<al>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, int a4, unsigned __int16 a5);
int __usercall sub_542A24@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
_DWORD *__usercall sub_542B64@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
_DWORD *__usercall sub_542CC4@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>);
_DWORD *__userpurge sub_542E24@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int32 a4);
_DWORD *__usercall sub_542F30@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ebx>, int a4@<esi>);
int __usercall sub_543008@<eax>(char a1@<cf>, int a2@<ecx>, int a3@<esi>);
_DWORD *__usercall sub_543018@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>, int a5@<edi>, int a6@<esi>);
int __usercall sub_5430EC@<eax>(char a1@<cf>, int a2@<ecx>, int a3@<esi>);
int __usercall sub_5430FC@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_543100@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_543114@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int sub_543184();
int __usercall sub_5431C0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5431E4@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_5431EC@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5432A0@<eax>(int a1@<eax>);
int __usercall sub_5432A8@<eax>(int a1@<eax>);
int __usercall sub_5432C0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5433B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5433FC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_5434B0();
int __usercall sub_5434B8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5434D0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_543548@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5435EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54368C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_5436C4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_5436FC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_543764@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_543770@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_5437C4(void *this);
int __usercall sub_5437F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5438C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_5439F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_543A68@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_543AE0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_543B4C@<eax>(int result@<eax>, int a2@<edx>);
int sub_543C08();
int sub_543C28();
int __usercall sub_543C48@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_543C50@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_543DEC@<eax>(int a1@<eax>);
int __usercall sub_543E18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_543E38@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_543F24@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_543F3C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_543F8C(int a1, int a2);
int __usercall sub_543FA4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_543FE0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_544034@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_54406C@<eax>(int result@<eax>);
int __usercall sub_54409C@<eax>(int a1@<eax>);
int __usercall sub_5440C4@<eax>(int a1@<eax>);
int __usercall sub_5440F0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_54412C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_544178@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5441C4@<eax>(int a1@<eax>);
int __usercall sub_5441D4@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5441F0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_544234@<al>(int a1@<eax>);
_DWORD *__fastcall sub_544254(int a1, _DWORD *a2);
_DWORD *__fastcall sub_544274(_DWORD *a1, int a2);
__int64 *__fastcall sub_54429C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5442C8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_5442F4(int a1, int a2, int a3, int a4);
bool __usercall sub_544318@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_54433C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_54439C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_544454@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_544490@<eax>(int a1@<eax>);
int __userpurge sub_54449C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int nullsub_356();
int sub_548810();
int __usercall sub_548848@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_548890@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5488E8@<eax>(int a1@<eax>);
int __usercall sub_548924@<eax>(int a1@<eax>);
int __usercall sub_548928@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
void __usercall sub_548950(int a1@<eax>, UINT *a2@<edx>);
int __usercall sub_548988@<eax>(unsigned int a1@<eax>);
int __usercall sub_5489D4@<eax>(_DWORD *a1@<eax>);
void __usercall sub_5489DC(int *a1@<eax>);
int __usercall sub_5489F8@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_548A10@<eax>(_DWORD *a1@<eax>);
int __usercall sub_548A24@<eax>(
        int a1@<eax>,
        int (__stdcall *a2)(int, _DWORD, void *, int *, struct _EXCEPTION_REGISTRATION_RECORD *)@<edx>,
        int a3@<ecx>);
// attributes: thunk
int __usercall sub_548ADD@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_548AF0@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_548B04@<eax>(int result@<eax>, int a2@<ecx>);
_WORD *__usercall sub_548B18@<eax>(int a1@<eax>);
_DWORD *__usercall sub_548B8C@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_548BCC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_WORD *__usercall sub_548C20@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_548C4C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
_WORD *__usercall sub_548C74@<eax>(int a1@<eax>);
int __usercall sub_548CA0@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
_WORD *__usercall sub_548CAC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __fastcall sub_548D14(int a1, int a2);
_DWORD *__usercall sub_548D30@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_548D74@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_548D80@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_548D9C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_548DC4@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_548DD0@<eax>(int a1@<eax>);
int __fastcall sub_548DE0(int a1, int a2);
int __usercall sub_5491FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
void __stdcall sub_54923C(int a1, int a2);
void __stdcall sub_549268(int a1, int a2);
void __stdcall sub_549294(int a1, int a2, int a3);
void __stdcall sub_5492C4(int a1, int a2, int a3, int a4);
void __stdcall sub_5492F8(int a1, int a2);
void __stdcall sub_549338(int a1, int a2, int a3, int a4);
void __stdcall sub_54936C(int a1, int a2);
_DWORD *__usercall sub_549398@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_549430@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_54947C@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_54949C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5494C8@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5494E8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_549514@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_549534@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_549554@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_549574@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_549594@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_5495E0@<eax>(int a1@<eax>);
int __usercall sub_5495F4@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
// attributes: thunk
int __usercall sub_5499EA@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// positive sp value has been detected, the output may be wrong!
void __usercall sub_5499F1(int a1@<ebp>, int a2@<edi>);
// attributes: thunk
int __usercall sub_549A18@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_549A38@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_549A90@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_549B5C@<eax>(int *a1@<eax>);
int __usercall sub_549B9C@<eax>(int a1@<eax>);
int __usercall sub_549C00@<eax>(int *a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_549C98@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_549CAC@<eax>(int *a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int __usercall sub_549DA1@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_549E23@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_549E70@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_549FE0@<eax>(int a1@<eax>);
void *__fastcall sub_549FE4(volatile __int32 *a1, int a2);
// attributes: thunk
int __usercall sub_54A082@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_54A0A7@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_54A0B8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_54A13C@<eax>(int a1@<eax>);
int __usercall sub_54A1AC@<eax>(int *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_54A250@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_54A2B4@<eax>(int a1@<eax>, _WORD *a2@<edx>);
volatile __int32 *__usercall sub_54A2E8@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_54A308@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_54A348@<eax>(int *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_54A3EC@<eax>(int a1@<eax>);
int __usercall sub_54A428@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54A480@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_54A544@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
LRESULT __usercall sub_54A608@<eax>(LRESULT result@<eax>, unsigned int a2@<edx>);
LRESULT __usercall sub_54A6D4@<eax>(int a1@<eax>);
int __usercall sub_54A774@<eax>(int a1@<eax>, char a2@<dl>, int *a3@<ecx>);
int __usercall sub_54A7D4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
LRESULT __usercall sub_54A810@<eax>(LRESULT result@<eax>);
LRESULT __usercall sub_54A82C@<eax>(LRESULT result@<eax>);
volatile __int32 *__usercall sub_54A854@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_54A874@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
_WORD *__usercall sub_54A898@<eax>(LPVOID *a1@<eax>);
int __usercall sub_54A944@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>);
_BYTE *__usercall sub_54A978@<eax>(_BYTE *result@<eax>);
int __usercall sub_54A984@<eax>(int a1@<eax>, char a2@<dl>, int *a3@<ecx>);
LRESULT __usercall sub_54AA34@<eax>(LRESULT result@<eax>);
volatile __int32 *__usercall sub_54AA54@<eax>(int a1@<eax>, __int64 **a2@<edx>);
_BYTE *__usercall sub_54AAB8@<eax>(_BYTE *a1@<eax>);
_DWORD *__usercall sub_54AAD4@<eax>(int a1@<eax>, char a2@<dl>, int *a3@<ecx>);
LRESULT __usercall sub_54AB80@<eax>(LRESULT result@<eax>);
LRESULT __usercall sub_54AB9C@<eax>(LRESULT result@<eax>);
_DWORD *__usercall sub_54ABBC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54AC00@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_54AC0C@<eax>(int a1@<eax>);
int __usercall sub_54AC28@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_54AC4C@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
int __usercall sub_54AC58@<eax>(int a1@<eax>);
int __fastcall sub_54ACC0(int a1, int a2);
_DWORD *__usercall sub_54AD3C@<eax>(int a1@<eax>);
int __fastcall sub_54AD4C(int a1, int a2);
int __usercall sub_54AD60@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_54AD6C@<eax>(int a1@<eax>);
int __usercall sub_54ADD8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54AEA4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __userpurge sub_54AEF8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6);
void __stdcall sub_54B094(int a1, int a2, int a3, int a4, int *a5);
BOOL __usercall sub_54B0BC@<eax>(int a1@<eax>, HWND a2@<edx>);
// attributes: thunk
int __usercall sub_54B44F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_54B47F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_54B494@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_54B4CC@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_54B4EC@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_54B50C@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_54B52C@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54B54C@<eax>(unsigned int a1@<eax>, int a2@<ecx>);
int __usercall sub_54B5B0@<eax>(int result@<eax>, __int32 a2@<edx>);
int __usercall sub_54B5E0@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_54B600@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_54B634@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_54B654@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>);
void __usercall sub_54B684(int *a1@<eax>);
void __usercall sub_54B6D4(int *a1@<eax>);
int __usercall sub_54B6E8@<eax>(int result@<eax>, int a2@<edx>);
HWND __usercall sub_54B718@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_54B754@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>);
LRESULT __usercall sub_54B7A8@<eax>(LRESULT result@<eax>, int a2@<edx>);
HWND __usercall sub_54B7D0@<eax>(int a1@<eax>, int a2@<edx>);
LRESULT __usercall sub_54B80C@<eax>(LRESULT result@<eax>, int a2@<edx>);
HWND __usercall sub_54B848@<eax>(int a1@<eax>, int a2@<edx>);
HWND __usercall sub_54B888@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_54B8CC@<eax>(int a1@<eax>, __int32 *a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_54B9C8@<eax>(_DWORD *a1@<eax>, struct tagSIZE *a2@<edx>);
int __userpurge sub_54BC68@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __usercall sub_54BCBC@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__thiscall sub_54BCD4(_WORD *this, __int16 a2);
_DWORD *__fastcall sub_54BD44(int a1, int a2);
// attributes: thunk
int __usercall sub_54BE11@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __cdecl sub_54BE22(
        int a1,
        int __return_address,
        __int64 ExceptionInfo,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9);
// attributes: thunk
int __usercall sub_54BE4D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_54BE81@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_54BE90@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_54C214@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>, signed __int16 a3@<cx>, char a4);
int __usercall sub_54C81C@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>, signed __int16 a3@<cx>);
int __userpurge sub_54C844@<eax>(volatile __int32 *a1@<eax>, int a2@<edx>, int a3@<ecx>, __int32 a4, int a5);
int __userpurge sub_54C8E0@<eax>(
        int a1@<eax>,
        unsigned __int8 a2@<dl>,
        unsigned __int16 a3@<cx>,
        __int32 a4,
        int a5,
        int a6,
        int a7);
BOOL __usercall sub_54CBC4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_54CC68@<eax>(int a1@<eax>, int a2@<ebx>, int a3@<edi>, int a4@<esi>);
void __usercall sub_54CD60(int *a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge sub_54CD6C@<eax>(
        int a1@<eax>,
        unsigned int a2@<edx>,
        unsigned __int8 a3@<cl>,
        char a4,
        __int32 a5,
        int a6,
        __int64 *a7,
        int a8,
        __int16 a9);
int __userpurge sub_54CF74@<eax>(
        int a1@<eax>,
        unsigned int a2@<edx>,
        unsigned __int8 a3@<cl>,
        __int32 a4,
        int a5,
        __int64 *a6,
        int a7,
        __int16 a8);
bool __usercall sub_54D20C@<al>(int a1@<eax>);
int __usercall sub_54D238@<eax>(int *a1@<eax>, _DWORD *a2@<edx>);
volatile __int32 *__usercall sub_54D47C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
int __cdecl sub_54D4C0(int a1);
__int16 __usercall sub_54D594@<ax>(_WORD *a1@<eax>);
int __userpurge sub_54D6B4@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>, int a4, int a5, int *a6);
OLECHAR ***__fastcall sub_54DF54(__int32 a1, int a2, int a3, int a4);
OLECHAR ***__userpurge sub_54E29C@<eax>(
        int a1@<edx>,
        _BYTE *a2@<ecx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>,
        int a6,
        int a7);
ATOM sub_54E3D4();
int __usercall sub_54E568@<eax>(int a1@<edi>);
int *__usercall sub_54F8C4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_54F958@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool __fastcall sub_54F9A4(int a1, int a2);
char __usercall sub_54F9AC@<al>(int a1@<eax>, _DWORD *a2@<edx>);
HRESULT __usercall sub_54FAD8@<eax>(_DWORD *a1@<eax>, int a2);
int __usercall sub_54FB84@<eax>(int a1@<eax>);
int __usercall sub_54FC88@<eax>(int a1@<eax>);
int __userpurge sub_54FD24@<eax>(
        int result@<eax>,
        int a2@<edx>,
        unsigned __int8 a3@<cl>,
        int a4,
        int a5,
        int a6,
        unsigned __int8 a7);
_DWORD *__usercall sub_54FD90@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_54FE90@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>);
OLECHAR **__usercall sub_54FEFC@<eax>(int a1@<eax>, int a2@<edi>);
int __usercall sub_550108@<eax>(int a1@<eax>, int *a2@<edx>, int *a3@<ecx>, int a4@<ebx>);
char __usercall sub_550170@<al>(int a1@<eax>);
int __usercall sub_5501D4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_550224@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
LRESULT __usercall sub_550268@<eax>(int *a1@<eax>, UINT *a2@<edx>);
_DWORD *__usercall sub_5502DC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_550368@<eax>(_DWORD *result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_550378@<eax>(_DWORD *result@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_550388@<eax>(int a1@<eax>, int a2, int a3);
int __usercall sub_5503A0@<eax>(int result@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5503B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4@<ebx>, int a5@<esi>);
int __usercall sub_55055C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5505C0@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_550684@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5506BC@<eax>(int a1@<eax>, unsigned __int32 a2@<edx>);
int __usercall sub_550718@<eax>(int a1@<eax>);
_DWORD *__usercall sub_550720@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_55072C@<eax>(_DWORD *result@<eax>, char a2@<dl>);
int sub_550784();
int __usercall sub_5507C4@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_550B08@<eax>(int result@<eax>);
BOOL __usercall sub_550B34@<eax>(int a1@<eax>, DWORD a2@<edx>);
int __usercall sub_550B50@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_550B80@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_550BD0@<eax>(int a1@<eax>);
int __usercall sub_550BF4@<eax>(int a1@<eax>, unsigned __int32 a2@<edx>);
int __usercall sub_550C38@<eax>(int a1@<eax>);
int __usercall sub_550C74@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_550C80@<eax>(int a1@<eax>);
int __usercall sub_550C8C@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
BOOL __usercall sub_550CC4@<eax>(int a1@<eax>);
int __usercall sub_550CE4@<eax>(int a1@<eax>, unsigned __int32 a2@<edx>);
void sub_550D28();
int nullsub_357();
int nullsub_360();
int nullsub_361();
void sub_55CB5C();
int nullsub_362();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_363(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_364@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_365();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_366(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_367@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_368();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_369(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_370@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_371();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_372(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_373@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
bool __usercall sub_56F3CC@<al>(int a1@<eax>);
// attributes: thunk
int __cdecl sub_56F438();
bool __usercall sub_56F440@<al>(int a1@<eax>);
_DWORD *__userpurge sub_56F49C@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
OLECHAR **__usercall sub_56F514@<eax>(char a1@<al>, char a2@<dl>, int a3@<edi>, int a4);
_DWORD *__userpurge sub_56F73C@<eax>(int a1@<eax>, _DWORD *a2@<edx>, char a3@<cl>, int a4);
_DWORD *__usercall sub_56F9C4@<eax>(HWND a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_56F9F4@<eax>(HWND a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_56FA24@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_56FA5C@<eax>(int a1@<eax>);
int __usercall sub_56FA78@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_56FA80@<eax>(int (***a1)(void)@<eax>);
int __stdcall sub_56FA9C(int a1, int a2);
int __usercall sub_56FAC4@<eax>(int result@<eax>, int a2@<ecx>);
int __stdcall sub_56FAD8(int a1, int a2, int a3, int a4);
int __userpurge sub_56FB28@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4, unsigned __int8 a5, int a6);
int __stdcall sub_56FB5C(int a1, int a2);
int __userpurge sub_56FB84@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4);
int __userpurge sub_56FBB0@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4, int a5);
int __stdcall sub_56FBE0(int a1, char a2, int a3);
int __userpurge sub_56FBFC@<eax>(int a1@<eax>, int a2, unsigned __int8 a3, int a4);
int __userpurge sub_56FC18@<eax>(int a1@<eax>, int a2, unsigned __int8 a3, int a4);
int __thiscall sub_56FC34(int *this, int a2, int a3, int *a4, int a5);
int __userpurge sub_56FC84@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6, int a7);
int __userpurge sub_56FD0C@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, const void *a3, int a4, int a5, int a6);
int __userpurge sub_56FD50@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_56FD78@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4);
int __userpurge sub_56FDA4@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, unsigned __int8 a4);
int __userpurge sub_56FDD4@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, unsigned __int8 a4, int a5);
int __thiscall sub_56FE04(void *this, int a2);
int __userpurge sub_56FE2C@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4);
int __userpurge sub_56FE58@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, unsigned __int8 a4);
int __userpurge sub_56FE88@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, unsigned __int8 a4, int a5);
bool __usercall sub_56FEB8@<al>(int a1@<eax>);
int __usercall sub_56FEC8@<eax>(int a1@<eax>);
int __usercall sub_56FED0@<eax>(int a1@<eax>);
int __usercall sub_56FED8@<eax>(int a1@<eax>);
int __userpurge sub_56FEE0@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4, int a5);
int __userpurge sub_56FF10@<eax>(int a1@<eax>, _DWORD *a2@<ecx>, int a3, int a4, int a5, int a6);
int sub_56FF44();
int __usercall sub_56FF50@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_56FF6C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_56FF88@<eax>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
LONG __usercall sub_56FFE8@<eax>(int a1@<eax>, HDC a2@<edx>, char a3@<cl>);
// attributes: thunk
int __usercall sub_570188@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_DWORD *__usercall sub_570198@<eax>(int a1@<eax>);
int __usercall sub_570208@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57020C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
char *__usercall sub_5702E8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_570318@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __userpurge sub_570350@<al>(
        int a1@<eax>,
        int a2@<edx>,
        _DWORD *a3@<ecx>,
        int a4,
        int a5,
        unsigned __int8 a6,
        int a7);
char __userpurge sub_5703F0@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5);
char __userpurge sub_570468@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6);
char __userpurge sub_5704E8@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, int a6);
char __userpurge sub_57052C@<al>(
        int a1@<eax>,
        HDC a2@<edx>,
        int *a3@<ecx>,
        const void *a4,
        int a5,
        struct tagRECT *pRect,
        int cchText);
// attributes: thunk
int __usercall sub_5706F4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
char __userpurge sub_570750@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5);
char __userpurge sub_5707C8@<al>(int a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>, int a4);
char __userpurge sub_570840@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, unsigned __int8 a5, int a6);
char __userpurge sub_5708CC@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5);
char __userpurge sub_570944@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, unsigned __int8 a5, int a6);
int __fastcall sub_5709D0(int a1, char a2);
int __usercall sub_570B18@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_570B50@<eax>(int a1@<eax>, char a2@<dl>);
int __fastcall sub_571520(int a1, int a2);
char __userpurge sub_571524@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6, int a7);
int __usercall sub_5715C8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int sub_571628();
int __usercall sub_57162C@<eax>(int a1@<ecx>, int a2@<ebx>);
int __fastcall sub_571684(int a1, char a2);
int __fastcall sub_5717A0(int a1, char a2);
int __fastcall sub_5717CC(int a1, char a2);
int __fastcall sub_571894(int a1, char a2);
int __fastcall sub_571AA0(int a1, char a2);
int __fastcall sub_571AE0(int a1, char a2);
int __fastcall sub_571C00(int a1, char a2);
int __fastcall sub_571C50(int a1, char a2);
int __fastcall sub_571D68(int a1, char a2);
int __fastcall sub_571DCC(int a1, char a2);
int __fastcall sub_571DF8(int a1, unsigned __int8 a2);
int __fastcall sub_571EA4(int a1, char a2);
int __fastcall sub_571F88(int a1, unsigned __int8 a2);
int __fastcall sub_571F98(int a1, unsigned __int8 a2);
int __fastcall sub_571FA8(int a1, char a2);
int __fastcall sub_571FF8(int a1, char a2);
int __fastcall sub_57212C(int a1, char a2);
int __fastcall sub_572228(int a1, char a2);
int __fastcall sub_572300(int a1, char a2);
int __fastcall sub_5723E0(int a1, char a2);
int __fastcall sub_5724F0(int a1, char a2);
int __fastcall sub_5725DC(int a1, unsigned __int8 a2);
int __fastcall sub_572688(int a1, char a2);
int __fastcall sub_572A28(int a1, unsigned __int8 a2);
int __fastcall sub_572A38(int a1, unsigned __int8 a2);
int __fastcall sub_572A48(int a1, unsigned __int8 a2);
int __fastcall sub_572A58(int a1, unsigned __int8 a2);
int __fastcall sub_572A68(int a1, unsigned __int8 a2);
int __fastcall sub_572A78(int a1, unsigned __int8 a2);
int __fastcall sub_572A88(int a1, unsigned __int8 a2);
int __fastcall sub_572A98(int a1, unsigned __int8 a2);
volatile __int32 *__fastcall sub_572AA8(int a1, volatile __int32 *a2);
int __fastcall sub_572AD8(int a1, char a2);
int __fastcall sub_572B3C(int a1, char a2);
int __fastcall sub_572B78(int a1, char a2);
int __fastcall sub_572C38(int a1, char a2);
int __fastcall sub_572E24(int a1, char a2);
int __fastcall sub_572E88(int a1, unsigned __int8 a2);
int __fastcall sub_572F98(int a1, char a2);
int __fastcall sub_572FE8(int a1, char a2);
int __fastcall sub_5731CC(int a1, char a2);
int __fastcall sub_5732F8(int a1, char a2);
int __fastcall sub_5733DC(int a1, unsigned __int8 a2);
int __fastcall sub_5733EC(int a1, char a2);
int __usercall sub_57343C@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_573480@<eax>(int a1@<eax>);
bool __usercall sub_573488@<al>(_BYTE *a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_5734A0@<eax>(int a1@<ebx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *sub_5734F8();
int __usercall sub_57354C@<eax>(int a1@<eax>);
bool __usercall sub_57357C@<al>(_BYTE *a1@<eax>);
_DWORD *__thiscall sub_573598(void *this);
int __usercall sub_5735D4@<eax>(int a1@<edx>, int a2@<ebx>);
int nullsub_374();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_375(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_376@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
BOOL __stdcall sub_574C1C(HMODULE hModule, LPCWSTR lpType, LPWSTR lpName, LONG_PTR lParam);
int __usercall sub_574CB4@<eax>(HMODULE a1@<eax>, HMODULE *a2@<edx>, int a3@<ecx>);
int __thiscall sub_574D80(void *this);
int __fastcall sub_574E9C(int a1, int a2, _DWORD *a3, int a4);
__int64 (__cdecl ***__fastcall sub_574F60(
        int *a1,
        __int64 (__cdecl ***a2)(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *)))(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *);
int __fastcall sub_5750A8(int a1, int a2, _WORD *a3);
int __thiscall sub_5751C0(void *this);
int __thiscall sub_5751DC(void *this);
int __usercall sub_57520C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5753B0@<eax>(int a1@<eax>, int a2@<ecx>);
int __thiscall sub_575550(void *this);
bool __thiscall sub_57556C(void *this);
int __fastcall sub_575590(void *a1, int a2, int a3, int a4);
int __thiscall sub_5755F4(void *this);
int __fastcall sub_575680(int a1, int a2);
int __thiscall sub_5756E4(void *this);
__int64 (__cdecl ***__fastcall sub_5757F8(int a1, int a2))(struct _EXCEPTION_REGISTRATION_RECORD *, void *, int *);
int __userpurge sub_5758F0@<eax>(
        int a1@<edx>,
        void *a2@<ecx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>,
        unsigned int a6);
int __usercall sub_5759C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int sub_575B74();
_DWORD *__fastcall sub_575B88(int a1, int a2);
int __userpurge sub_575C14@<eax>(void *a1@<ecx>, int a2@<ebx>, int a3@<edi>, int a4@<esi>, int a5, unsigned int a6);
int __fastcall sub_575CD0(int a1, __int32 a2, __int32 a3, __int32 a4);
_DWORD *__usercall sub_575E08@<eax>(_DWORD *result@<eax>);
char __fastcall sub_575E4C(void *a1, int a2);
int __fastcall sub_575F38(int a1, int a2);
int __fastcall sub_575F78(int a1, int a2);
int __userpurge sub_57605C@<eax>(int a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>, int *a6, int a7);
int __usercall sub_576118@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__fastcall sub_576318(int a1, int a2);
int __thiscall sub_576368(void *this);
_DWORD *__fastcall sub_5764F4(int a1, int a2);
int __usercall sub_5765DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __stdcall sub_5766B8(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5766C4(int a1, int a2, int a3, int a4);
int __stdcall sub_5766D0(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5766DC(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_576700(int a1, int a2, int a3);
int __stdcall sub_57670C(int a1, int a2, int a3, int a4);
int __stdcall sub_576718(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_576724(int a1, int a2, int a3, int a4);
int __stdcall sub_576730(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_57673C(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_576748(int a1);
int __fastcall sub_576754(int a1, int a2, int a3, int *a4, int a5, int a6);
int __fastcall sub_57698C(int a1, int a2, const void *a3, int a4, int a5, int a6, char a7, int a8);
char __fastcall sub_5769FC(int a1, int a2, _DWORD *a3, unsigned __int8 a4, unsigned __int8 a5);
char __userpurge sub_576E34@<al>(
        int a1@<eax>,
        int a2@<edx>,
        HDC a3@<ecx>,
        const void *a4,
        int a5,
        LPRECT pRect,
        UINT cchText,
        int a8,
        int a9);
// attributes: thunk
int __usercall sub_577146@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_577158@<eax>(int a1@<ebx>, signed int *a2, char a3, char a4);
char __stdcall sub_5771B0(_DWORD *a1, _DWORD *a2, int a3, int a4);
int __fastcall sub_5771CC(int a1, int a2, _DWORD *a3, _DWORD *a4, int a5, int a6, unsigned __int8 a7, int a8);
int __fastcall sub_57724C(int a1, int a2, int a3, int a4, char a5, int a6);
char __stdcall sub_5772BC(_DWORD *a1, char a2, char a3);
int __fastcall sub_57745C(int a1, int a2, int a3, int a4, char a5, int a6);
int __userpurge sub_5775D0@<eax>(
        int a1@<edx>,
        HDC a2@<ecx>,
        int a3@<ebx>,
        const void *a4,
        int a5,
        struct tagRECT *lprc,
        int cchText,
        char a8,
        int a9);
char __stdcall sub_577670(_DWORD *a1, char a2, char a3);
int __userpurge sub_577704@<eax>(
        int a1@<edx>,
        int a2@<ecx>,
        int a3@<ebx>,
        _DWORD *a4,
        char a5,
        int a6,
        char a7,
        int a8);
int __fastcall sub_577838(int a1, int a2, const void *a3, int a4, int a5, int a6, int a7, int a8);
char __stdcall sub_577888(_DWORD *a1, char a2, char a3);
char __stdcall sub_5779BC(_DWORD *a1, char a2, char a3);
int __usercall sub_577A64@<eax>(int result@<eax>);
int __usercall sub_577A70@<eax>(int result@<eax>);
int __usercall sub_577A84@<eax>(unsigned __int8 a1@<al>);
int __usercall sub_577AB8@<eax>(char a1@<al>);
void sub_577B50();
void sub_577B5C();
int __usercall sub_577B70@<eax>(signed __int32 a1@<eax>);
int __usercall sub_577BA0@<eax>(__int16 a1@<ax>);
char __stdcall sub_577D04(_DWORD *a1, char a2, char a3);
char __stdcall sub_577E34(_DWORD *a1, char a2, char a3);
char __stdcall sub_577E74(_DWORD *a1, char a2, char a3);
int __usercall sub_577F14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_577FA8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_577FD4@<eax>(int a1@<eax>);
int __userpurge sub_578000@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6);
int *__usercall sub_5780E4@<eax>(int a1@<eax>, int *a2@<edx>);
int __usercall sub_578148@<eax>(_BYTE *a1@<eax>, int *a2@<edx>);
_BYTE ***__usercall sub_5781C0@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
volatile __int32 *__usercall sub_578238@<eax>(int a1@<eax>, __int64 **a2@<edx>);
char __usercall sub_5782B0@<al>(int a1@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_5782E8@<eax>(int a1@<eax>);
bool __usercall sub_578308@<al>(int a1@<eax>);
bool __usercall sub_578348@<al>(int a1@<eax>);
char __usercall sub_578364@<al>(int a1@<eax>);
bool __usercall sub_57838C@<al>(int a1@<eax>);
int sub_5783BC();
void nullsub_349();
int __usercall sub_5783C4@<eax>(int a1@<eax>, _DWORD **a2@<edx>);
void nullsub_350();
int *__usercall sub_5783FC@<eax>(int *result@<eax>, int a2@<edx>, int a3@<ecx>);
HDC __usercall sub_5785B8@<eax>(HDC result@<eax>, int a2@<ecx>);
// attributes: thunk
int __usercall sub_578648@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_BYTE *__usercall sub_57865C@<eax>(_BYTE *result@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_57870B@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_BYTE *__usercall sub_578728@<eax>(_BYTE *result@<eax>);
_BYTE *__usercall sub_578738@<eax>(_BYTE *result@<eax>);
int __usercall sub_578748@<eax>(_BYTE *a1@<eax>);
int __usercall sub_578760@<eax>(_BYTE *a1@<eax>);
int __usercall sub_578778@<eax>(_BYTE *a1@<eax>);
int __usercall sub_578790@<eax>(_BYTE *a1@<eax>);
int __usercall sub_5787A8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57882C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_578874@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int sub_5788A8();
int __usercall sub_5788AC@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5788DC@<eax>(int *a1@<eax>);
_DWORD *__usercall sub_578928@<eax>(int a1@<eax>);
int __usercall sub_578954@<eax>(_BYTE *a1@<eax>);
int __usercall sub_5789A0@<eax>(int *a1@<eax>);
int __usercall sub_5789EC@<eax>(int a1@<eax>);
void nullsub_351();
void nullsub_352();
// attributes: thunk
int __usercall sub_578A18@<eax>(int a1@<edx>, int a2@<eax>);
void sub_578A20();
int __usercall sub_578B34@<eax>(int a1@<edx>, int a2@<ecx>, int a3@<ebx>);
int __usercall sub_578BD0@<eax>(int a1@<edx>, int a2@<ebx>);
int __fastcall sub_578C50(int a1, int a2);
int __fastcall sub_578D5C(int a1, int a2);
char __userpurge sub_578F00@<al>(char result@<al>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_578F14@<eax>(_DWORD *result@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_578F44@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_578F94@<eax>(int *a1@<eax>, int a2@<edx>);
int sub_578FD8();
bool __usercall sub_578FF4@<al>(int a1@<eax>);
int sub_579010();
bool sub_579064();
int __fastcall sub_579098(int a1, _DWORD *a2);
bool sub_5790E0();
BOOL __usercall sub_5790FC@<eax>(int a1@<eax>, struct tagRECT *a2@<edx>);
_DWORD *__usercall sub_579120@<eax>(int a1@<eax>, __int64 **a2@<edx>);
BOOL __usercall sub_579140@<eax>(int a1@<eax>);
int __thiscall sub_57915C(void *this);
int __thiscall sub_579178(void *this);
_DWORD *__usercall sub_579190@<eax>(int a1@<eax>);
HWND __usercall sub_5791E0@<eax>(int a1@<eax>);
LONG __usercall sub_5791EC@<eax>(int a1@<eax>);
LONG __usercall sub_5791F8@<eax>(int a1@<eax>);
_DWORD *__usercall sub_579204@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57936C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __thiscall sub_579380(void *this);
BOOL __usercall sub_579398@<eax>(int a1@<eax>);
int __thiscall sub_5793AC(void *this);
BOOL __usercall sub_5793C8@<eax>(int a1@<eax>, struct tagRECT *a2@<edx>);
LONG __usercall sub_5793EC@<eax>(int a1@<eax>);
LONG __usercall sub_5793F8@<eax>(int a1@<eax>, LONG a2@<edx>);
LONG __usercall sub_579408@<eax>(int a1@<eax>, LONG a2@<edx>);
LONG __usercall sub_579418@<eax>(int a1@<eax>, LONG a2@<edx>);
bool sub_579438();
bool sub_57945C();
bool __usercall sub_579480@<al>(HWND a1@<eax>);
_DWORD *__usercall sub_5794A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_579590@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
LRESULT __usercall sub_57962C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_579648@<eax>(int a1@<eax>);
int __userpurge sub_579684@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6);
_DWORD *__usercall sub_579750@<eax>(int a1@<eax>, HDC a2@<edx>, LONG *a3@<ecx>);
unsigned int __userpurge sub_5798B4@<eax>(int a1@<eax>, HDC a2@<edx>, _DWORD *a3@<ecx>, int a4, LPRECT lprc, int a6);
// attributes: thunk
int __usercall sub_57998D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5799AA@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
UINT __userpurge sub_5799C0@<eax>(int a1@<eax>, HDC a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, LONG *a6);
// attributes: thunk
int __usercall sub_579B03@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_579B20@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
bool __usercall sub_579B34@<al>(int a1@<eax>);
int __fastcall sub_579B44(int a1, _DWORD *a2);
int __usercall sub_579B58@<eax>(int a1@<eax>);
int __usercall sub_579B5C@<eax>(int a1@<eax>);
HWND __usercall sub_579B60@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_579B6C@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int sub_579BB0();
void __usercall sub_579BB4(int a1@<eax>, int a2@<edx>);
int __usercall sub_579BF8@<eax>(int result@<eax>, char a2@<dl>);
LRESULT __fastcall sub_579C04(unsigned __int8 a1, HWND a2);
int __usercall sub_579C14@<eax>(_BYTE *a1@<eax>, char a2@<dl>);
bool __usercall sub_579C50@<al>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_579C94@<eax>(int a1@<eax>, void *a2@<ecx>);
bool __usercall sub_579CF4@<al>(int a1@<eax>);
BOOL __usercall sub_579D10@<eax>(int a1@<eax>);
LRESULT __usercall sub_579D30@<eax>(int a1@<eax>);
void nullsub_358();
int __usercall sub_579D48@<eax>(int a1@<eax>, _DWORD **a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
LONG __usercall sub_579D7C@<eax>(void (***a1)(void)@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int __usercall sub_579F34@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void nullsub_359();
_DWORD *__usercall sub_579F48@<eax>(int a1@<eax>, HDC a2@<edx>);
LRESULT __usercall sub_579F50@<eax>(int a1@<eax>);
char __usercall sub_579F60@<al>(HWND *a1@<eax>, int a2@<edx>, void *a3@<ecx>);
// attributes: thunk
int __usercall sub_57A0B7@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_57A0D4@<eax>(int a1@<eax>);
char __usercall sub_57A108@<al>(int a1@<eax>, void *a2@<ecx>);
// attributes: thunk
int __usercall sub_57A1CD@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
char __usercall sub_57A1E0@<al>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
_DWORD *__usercall sub_57A3B8@<eax>(int a1@<eax>, int a2@<edx>, void *a3@<ecx>);
int __usercall sub_57A660@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57A684@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57A68C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57A740@<eax>(int a1@<eax>);
int __usercall sub_57A748@<eax>(int a1@<eax>);
int __usercall sub_57A760@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57A858@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57A89C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_57A950();
int __usercall sub_57A958@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57A970@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_57A9E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_57AA8C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57AB2C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_57AB64(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_57AB9C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_57AC04@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_57AC10@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_57AC64(void *this);
int __usercall sub_57AC90@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_57AD64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_57AE90@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_57AF08@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_57AF80@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_57AFEC@<eax>(int result@<eax>, int a2@<edx>);
int sub_57B0A8();
int sub_57B0C8();
int __usercall sub_57B0E8@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_57B0F0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_57B28C@<eax>(int a1@<eax>);
int __usercall sub_57B2B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57B2D8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57B3C4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_57B3DC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_57B42C(int a1, int a2);
int __usercall sub_57B444@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57B480@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_57B4D4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57B50C@<eax>(int result@<eax>);
int __usercall sub_57B53C@<eax>(int a1@<eax>);
int __usercall sub_57B564@<eax>(int a1@<eax>);
int __usercall sub_57B590@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_57B5CC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_57B618@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57B664@<eax>(int a1@<eax>);
int __usercall sub_57B674@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_57B690@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_57B6D4@<al>(int a1@<eax>);
_DWORD *__usercall sub_57B6F4@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_57B6FC(volatile signed __int8 ***a1, int a2);
int __usercall sub_57B794@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57B7B8@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57B7C0@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57B878@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_57B8C0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_57B9F0@<eax>(int a1@<eax>);
int __usercall sub_57BA18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57BAC4@<eax>(int a1@<eax>);
int __userpurge sub_57BB90@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_57BBD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_57BC28@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_57BC5C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
// attributes: thunk
int sub_57BDB0();
int __usercall sub_57BDB8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57BDD0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57BDE8@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_57BE20@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_57BE58@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_57BF10@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>);
_DWORD *__userpurge sub_57BFC0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>, int a4);
int __usercall sub_57C074@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57C0B0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57C114@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_57C134@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_57C184@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_57C25C@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_57C29C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_57C304@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57C328@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57C3C8@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57C3E0@<eax>(int a1@<eax>);
int __usercall sub_57C400@<eax>(int a1@<eax>);
int __usercall sub_57C420@<eax>(int a1@<eax>);
int __fastcall sub_57C430(volatile signed __int8 ***a1, int a2);
int __usercall sub_57C4BC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57C4E0@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57C4E8@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57C59C@<eax>(int a1@<eax>);
int __usercall sub_57C5A4@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57C5AC();
_DWORD *__usercall sub_57C5B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57C5F0@<eax>(int a1@<eax>);
int __usercall sub_57C600@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57C618@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57C63C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57C680@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_57C6B8(volatile signed __int8 ***a1, int a2);
int __usercall sub_57C744@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57C768@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57C770@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57C824@<eax>(int a1@<eax>);
int __usercall sub_57C82C@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57C834();
_DWORD *__usercall sub_57C83C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57C878@<eax>(int a1@<eax>);
int __usercall sub_57C888@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57C8A0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57C8C4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57C908@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_57C940@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_57C968@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_57C97C();
_DWORD *__usercall sub_57C984@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57C9C8@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_57CA00@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57CA08@<eax>(int a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
int __fastcall sub_57CA24(volatile signed __int8 ***a1, int a2);
int __usercall sub_57CB00@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57CB24@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_57CB2C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57CC24@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_57CC6C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_57CD9C@<eax>(int a1@<eax>);
int __usercall sub_57CDC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57CE70@<eax>(int a1@<eax>);
int __userpurge sub_57CF3C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_57CF8C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, __int32 a5);
int __usercall sub_57CFDC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_57D010@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
// attributes: thunk
int sub_57D164();
int __usercall sub_57D16C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57D184@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57D19C@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_57D1D4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_57D20C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_57D2C4@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_57D3B0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_57D4A0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57D4DC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57D540@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_57D560@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_57D5B0@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_57D688@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_57D6C8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_57D730@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57D754@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57D7F4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57D80C@<eax>(int a1@<eax>);
int __usercall sub_57D82C@<eax>(int a1@<eax>);
int __usercall sub_57D84C@<eax>(int a1@<eax>);
_DWORD *__fastcall sub_57D85C(volatile signed __int8 ***a1, int a2);
int __usercall sub_57D920@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57D944@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57D94C@<eax>(int (***a1)(void)@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57DA34@<eax>(int a1@<eax>);
int __usercall sub_57DA3C@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57DA44();
_DWORD *__usercall sub_57DA4C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57DA88@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57DA98@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
volatile __int32 *__usercall sub_57DAB0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_57DAD0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int sub_57DAE4();
_DWORD *__usercall sub_57DAEC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57DB30@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_57DB68(volatile signed __int8 ***a1, int a2);
int __usercall sub_57DBF4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57DC18@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57DC20@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57DCD4@<eax>(int a1@<eax>);
int __usercall sub_57DCDC@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57DCE4();
_DWORD *__usercall sub_57DCEC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57DD28@<eax>(int a1@<eax>);
int __usercall sub_57DD38@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57DD50@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57DD74@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57DDB8@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_57DDF0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57DE24@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_57DE38();
_DWORD *__usercall sub_57DE40@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57DE84@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_57DEBC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57DEEC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_57DF1C@<eax>(int a1@<eax>, char a2@<dl>, int a3);
_DWORD *__userpurge sub_57DF68@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __userpurge sub_57DFB4@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>, int a4, int a5);
_DWORD *__usercall sub_57E058@<eax>(_DWORD *result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_57E060(volatile signed __int8 ***a1, int a2);
int __usercall sub_57E0F8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57E11C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57E124@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57E1DC@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_57E224@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_57E354@<eax>(int a1@<eax>);
int __usercall sub_57E37C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57E428@<eax>(int a1@<eax>);
int __userpurge sub_57E4F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_57E53C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_57E58C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_57E5C0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4);
// attributes: thunk
int sub_57E714();
int __usercall sub_57E71C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57E734@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57E74C@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_57E784@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_57E7BC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_57E874@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>);
_DWORD *__userpurge sub_57E924@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>, int a4);
int __usercall sub_57E9D8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57EA14@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57EA78@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_57EA98@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_57EAE8@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_57EBC0@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_57EC00@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_57EC68@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57EC8C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_57ED2C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57ED44@<eax>(int a1@<eax>);
int __usercall sub_57ED64@<eax>(int a1@<eax>);
int __usercall sub_57ED84@<eax>(int a1@<eax>);
int __fastcall sub_57ED94(volatile signed __int8 ***a1, int a2);
int __usercall sub_57EE20@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57EE44@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57EE4C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57EF00@<eax>(int a1@<eax>);
int __usercall sub_57EF08@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57EF10();
_DWORD *__usercall sub_57EF18@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57EF54@<eax>(int a1@<eax>);
int __usercall sub_57EF64@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57EF7C@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57EFA0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57EFE4@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_57F01C(volatile signed __int8 ***a1, int a2);
int __usercall sub_57F0A8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57F0CC@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57F0D4@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57F188@<eax>(int a1@<eax>);
int __usercall sub_57F190@<eax>(int a1@<eax>);
// attributes: thunk
int sub_57F198();
_DWORD *__usercall sub_57F1A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57F1DC@<eax>(int a1@<eax>);
int __usercall sub_57F1EC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_57F204@<eax>(int a1@<eax>);
_DWORD *__usercall sub_57F228@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57F26C@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_57F2A4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_57F2CC@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_57F2E0();
_DWORD *__usercall sub_57F2E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_57F32C@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_57F364@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57F394@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_57F3C4@<eax>(int a1@<eax>, char a2@<dl>, int a3);
_DWORD *__userpurge sub_57F410@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __userpurge sub_57F45C@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>, int a4, int a5);
_DWORD *__usercall sub_57F500@<eax>(_DWORD *result@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __fastcall sub_57F518(volatile signed __int8 ***a1, int a2);
int __usercall sub_57F5B4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57F5D8@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_57F5E0@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57F698@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_57F6E0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_57F814@<eax>(int a1@<eax>);
int __usercall sub_57F83C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57F8E8@<eax>(int a1@<eax>);
int __usercall sub_57F960@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __userpurge sub_57F9F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4);
int __userpurge sub_57FA4C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, int a5);
int __usercall sub_57FAAC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __userpurge sub_57FB08@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, unsigned __int8 a5);
// attributes: thunk
int sub_57FC6C();
int __usercall sub_57FC74@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_57FC8C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_57FCA4@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_57FCDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_57FD14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_57FDCC@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>);
_DWORD *__userpurge sub_57FE7C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int (***a3)(void)@<ecx>, int a4);
int __usercall sub_57FF30@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_57FF6C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_57FFD0@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_57FFFC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
OLECHAR ***__usercall sub_580064@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_58013C@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4@<ebx>);
int __usercall sub_580198@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
bool __usercall sub_580200@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_580224@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5802C4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5802DC@<eax>(int a1@<eax>);
int __usercall sub_5802FC@<eax>(int a1@<eax>);
int __usercall sub_58031C@<eax>(int a1@<eax>);
int __usercall sub_58032C@<eax>(int a1@<eax>);
// attributes: thunk
int sub_580334();
_DWORD *__usercall sub_58033C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_580378@<eax>(int a1@<eax>);
int __usercall sub_580388@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5803A0@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5803C4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_580408@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_580440(volatile signed __int8 ***a1, int a2);
int __usercall sub_5804E0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_580504@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_58050C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5805C4@<eax>(int a1@<eax>);
int __usercall sub_5805CC@<eax>(int a1@<eax>);
// attributes: thunk
int sub_5805D4();
_DWORD *__usercall sub_5805DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_580618@<eax>(int a1@<eax>);
int __usercall sub_580628@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_580640@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_580664@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_580678();
_DWORD *__usercall sub_580680@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5806C4@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_5806FC@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_580734@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_580748();
_DWORD *__usercall sub_580750@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_580794@<eax>(int a1@<eax>, int a2@<ebx>);
_DWORD *__usercall sub_5807CC@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5807FC@<eax>(int a1@<eax>, _DWORD **a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_58082C@<eax>(int a1@<eax>, char a2@<dl>, int a3);
_DWORD *__userpurge sub_580878@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __userpurge sub_5808C4@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>, int a4, int a5);
int __usercall sub_580968@<eax>(int a1@<eax>, __int32 a2@<edx>, _DWORD *a3@<ecx>);
int __fastcall sub_58098C(volatile signed __int8 ***a1, int a2);
int __usercall sub_580A68@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_580A8C@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_580A94@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_580B8C@<eax>(int a1@<eax>);
OLECHAR **__usercall sub_580BD4@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR **__usercall sub_580D08@<eax>(int a1@<eax>);
int __usercall sub_580D30@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_580DDC@<eax>(int a1@<eax>);
int __usercall sub_580E4C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __userpurge sub_580ED0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4);
int __userpurge sub_580F2C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, __int32 a5);
int __usercall sub_580F8C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __userpurge sub_580FD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, _DWORD *a4, unsigned __int8 a5);
int __usercall sub_581148@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_581160@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_581178@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5811B0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_5811E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_5812A0@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_58138C@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_58147C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5814B8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_58151C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_581548@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR ***__usercall sub_5815AC@<eax>(int *a1@<eax>, int a2@<edi>);
int __usercall sub_581678@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_581684@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4@<ebx>);
int __usercall sub_5816D4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
bool __usercall sub_58173C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_581760@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_581800@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_581818@<eax>(int a1@<eax>);
int __usercall sub_581838@<eax>(int a1@<eax>);
int __usercall sub_581858@<eax>(int a1@<eax>);
int __usercall sub_581868@<eax>(int a1@<eax>);
// attributes: thunk
int sub_581870();
_DWORD *__usercall sub_581878@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5818B4@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5818C4@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
volatile __int32 *__usercall sub_5818DC@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_5818FC@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
// attributes: thunk
int sub_581910();
_DWORD *__usercall sub_581918@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58195C@<eax>(int a1@<eax>, int a2@<ebx>);
int __fastcall sub_581994(volatile signed __int8 ***a1, int a2);
int __usercall sub_581A2C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_581A50@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_581A58@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_581B10@<eax>(int a1@<eax>);
int __usercall sub_581B18@<eax>(int a1@<eax>);
// attributes: thunk
int sub_581B20();
_DWORD *__usercall sub_581B28@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_581B64@<eax>(int a1@<eax>);
int __usercall sub_581B74@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_581B8C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_581BA8@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int sub_581BBC();
_DWORD *__usercall sub_581BC4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_581C08@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_581C40@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_581C78@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_581C8C();
_DWORD *__usercall sub_581C94@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_581CD8@<eax>(int a1@<eax>, int a2@<ebx>);
int __usercall sub_581D10@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_581D34@<eax>(int (***a1)(void)@<eax>);
int __usercall sub_581D3C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_581E34@<eax>(int a1@<eax>);
int __usercall sub_581E3C@<eax>(int a1@<eax>);
int __usercall sub_581E54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_581F18@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_581FD4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_582018@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_582138@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_582150@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5821C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58226C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58230C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_582344(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58237C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_5823E4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5823F0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_582484@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_582568@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_582690@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58272C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_5827E4@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_582850@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_582988();
int sub_5829A8();
int __usercall sub_5829C8@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_5829D0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_582B68(void *this);
int __userpurge sub_582B84@<eax>(int a1@<eax>, int a2);
int __usercall sub_582BDC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_582C80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_582DFC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_582E14@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_582E64(int a1, int a2);
int __usercall sub_582E7C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_582EBC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_582F44@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_582F80@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_583030@<eax>(int a1@<eax>);
int __usercall sub_583058@<eax>(int a1@<eax>);
int __usercall sub_583084@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5830C0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58310C@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_5831A8@<eax>(int a1@<eax>);
int __fastcall sub_5831D0(int a1, int a2);
// attributes: thunk
int sub_5831E4();
_DWORD *__usercall sub_5831EC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_583230@<al>(int a1@<eax>);
int __usercall sub_583250@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_583274@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_58327C@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_583330@<eax>(int a1@<eax>);
int __usercall sub_583338@<eax>(int a1@<eax>);
int __usercall sub_583350@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_583448@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58348C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_583540();
int __usercall sub_583548@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_583560@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5835D8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58367C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58371C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_583754(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58378C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_5837F4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_583800@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_583854(void *this);
int __usercall sub_583880@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_583954@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_583A80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_583AF8@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_583B70@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_583BDC@<eax>(int result@<eax>, int a2@<edx>);
int __fastcall sub_583C98(int a1, int a2);
int sub_583CB8();
int __usercall sub_583CD8@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_583CE0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_583E7C@<eax>(int a1@<eax>);
int __usercall sub_583EA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_583EC8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_583FB4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_583FCC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58401C(int a1, int a2);
int __usercall sub_584034@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_584070@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5840C4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5840FC@<eax>(int result@<eax>);
int __usercall sub_58412C@<eax>(int a1@<eax>);
int __usercall sub_584154@<eax>(int a1@<eax>);
int __usercall sub_584180@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5841BC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_584208@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_584254@<eax>(int a1@<eax>);
int __usercall sub_584264@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_584280@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_5842C4@<al>(int a1@<eax>);
int __usercall sub_5842E4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_584308@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_584310@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5843C4@<eax>(int a1@<eax>);
int __usercall sub_5843CC@<eax>(int a1@<eax>);
int __usercall sub_5843E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5844DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_584520@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_5845D4();
int __usercall sub_5845DC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5845F4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58466C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_584710@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5847B0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_5847E8(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_584820@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_584888@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_584894@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_5848E8(void *this);
int __usercall sub_584914@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5849E8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_584B14@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_584B8C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_584C04@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_584C70@<eax>(int result@<eax>, int a2@<edx>);
int sub_584D2C();
int sub_584D4C();
int __usercall sub_584D6C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_584D74@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_584F10@<eax>(int a1@<eax>);
int __usercall sub_584F3C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_584F5C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_585048@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_585060@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_5850B0(int a1, int a2);
int __usercall sub_5850C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_585104@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_585158@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_585190@<eax>(int result@<eax>);
int __usercall sub_5851C0@<eax>(int a1@<eax>);
int __usercall sub_5851E8@<eax>(int a1@<eax>);
int __usercall sub_585214@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_585250@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58529C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5852E8@<eax>(int a1@<eax>);
int __usercall sub_5852F8@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int __usercall sub_585304@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_58530C();
_DWORD *__usercall sub_585314@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_585358@<al>(int a1@<eax>);
int __usercall sub_585378@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_58539C@<eax>(int (***a1)(void)@<eax>);
_DWORD *__usercall sub_5853A4@<eax>(int (***a1)(void)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58545C@<eax>(int a1@<eax>);
int __usercall sub_585464@<eax>(int a1@<eax>);
int __usercall sub_58547C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_585530@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_585598@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5855DC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_5856A0();
int __usercall sub_5856A8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5856C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_585738@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5857DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58587C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_5858B4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_5858EC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_585954@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_585960@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_5859C4(void *this);
int __usercall sub_5859F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_585AD0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_585C04@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_585C84@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_585CF8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_585D64@<eax>(int result@<eax>, int a2@<edx>);
int sub_585E38();
int sub_585E58();
int __usercall sub_585E78@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_585E80@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_586014(void *this);
int __userpurge sub_586030@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_586074@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5860B8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_5861AC(int a1, int a2);
int __usercall sub_5861C0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5861D8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5861F0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_586240(int a1, int a2);
int __usercall sub_586258@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_586294@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5862E8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_586320@<eax>(int result@<eax>);
int __usercall sub_586374@<eax>(int a1@<eax>);
int __usercall sub_58639C@<eax>(int a1@<eax>);
int __usercall sub_5863C8@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_586404@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
volatile signed __int8 **__usercall sub_586450@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5864B0@<eax>(int a1@<eax>);
int __usercall sub_5864C0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5864D8@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_5864EC();
_DWORD *__usercall sub_5864F4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_586538@<al>(int a1@<eax>);
_DWORD *__fastcall sub_586558(int a1, _DWORD *a2);
_DWORD *__fastcall sub_586578(_DWORD *a1, int a2);
__int64 *__fastcall sub_5865A0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5865CC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_5865F8(int a1, int a2, int a3, int a4);
bool __usercall sub_58661C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_586640@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5866A0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
int __usercall sub_586758@<eax>(int a1@<eax>);
int __usercall sub_586770@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_586824@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_58688C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5868D0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58699C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5869B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_586A2C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_586AD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_586B70@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_586BA8(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_586BE0@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_586C48@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_586C54@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_586CB8(void *this);
int __usercall sub_586CCC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_586CD8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_586CE4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_586DC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_586EF8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_586F78@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_586FEC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_587058@<eax>(int result@<eax>, int a2@<edx>);
int sub_58712C();
int sub_58714C();
int __usercall sub_58716C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_587174@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_587308(void *this);
int __userpurge sub_587324@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_587368@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5873AC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_5874A0(int a1, int a2);
int __usercall sub_5874B4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5874CC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5874E4@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_587534(int a1, int a2);
int __usercall sub_58754C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_587588@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5875DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_587614@<eax>(int result@<eax>);
int __usercall sub_587668@<eax>(int a1@<eax>);
int __usercall sub_587690@<eax>(int a1@<eax>);
int __usercall sub_5876BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5876F8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_587738@<eax>(int a1@<eax>, int a2@<ecx>);
volatile signed __int8 **__usercall sub_587744@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5877A4@<eax>(int a1@<eax>);
int __usercall sub_5877B4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5877CC@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_5877E0();
_DWORD *__usercall sub_5877E8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58782C@<al>(int a1@<eax>);
_DWORD *__usercall sub_58784C@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_58786C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_58788C@<eax>(int a1@<eax>);
int __usercall sub_5878A4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58799C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5879E0@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_587A9C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_587AB4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_587B2C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_587BD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_587C70@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_587CA8(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_587CE0@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_587D48@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_587D54@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_587DA8(void *this);
int __usercall sub_587DBC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_587DC8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_587DD4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_587EA8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_587FD4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_58804C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_5880C4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_588130@<eax>(int result@<eax>, int a2@<edx>);
int sub_5881EC();
int sub_58820C();
int __usercall sub_58822C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_588234@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_5883C8();
int __usercall sub_5883D0@<eax>(int a1@<eax>);
int __usercall sub_5883FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58841C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_5884F4(void *this);
int __usercall sub_5884FC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_588508@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_588520@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_588570(int a1, int a2);
int __usercall sub_588588@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5885C4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_588618@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_588650@<eax>(int result@<eax>);
int __usercall sub_588680@<eax>(int a1@<eax>);
int __usercall sub_5886A8@<eax>(int a1@<eax>);
int __usercall sub_5886D4@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_588710@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_588750@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58875C@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5887A8@<eax>(int a1@<eax>);
int __usercall sub_5887B8@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_5887CC();
_DWORD *__usercall sub_5887D4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_588818@<al>(int a1@<eax>);
int __usercall sub_588838@<eax>(int a1@<eax>);
int __usercall sub_588850@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_588948@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58898C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_588A48@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_588A60@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_588AD8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_588B7C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_588C1C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_588C54(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_588C8C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_588CF4@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_588D00@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_588D54(void *this);
int __usercall sub_588D68@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_588D74@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_588D80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_588E54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_588F80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_588FF8@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_589070@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5890DC@<eax>(int result@<eax>, int a2@<edx>);
int sub_589198();
int sub_5891B8();
int __usercall sub_5891D8@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_5891E0@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_589374();
int __usercall sub_58937C@<eax>(int a1@<eax>);
int __usercall sub_5893A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5893C8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_5894A0(void *this);
int __usercall sub_5894A8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5894B4@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5894CC@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58951C(int a1, int a2);
int __usercall sub_589534@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_589570@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5895C4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5895FC@<eax>(int result@<eax>);
int __usercall sub_58962C@<eax>(int a1@<eax>);
int __usercall sub_589654@<eax>(int a1@<eax>);
int __usercall sub_589680@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5896BC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_5896FC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_589708@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_589754@<eax>(int a1@<eax>);
int __usercall sub_589764@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_589778();
_DWORD *__usercall sub_589780@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_5897C4@<al>(int a1@<eax>);
int __usercall sub_5897E4@<eax>(int a1@<eax>);
int __usercall sub_5897FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5898BC@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_589970@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5899B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_589AC8@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_589AE0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_589B58@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_589BFC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_589C9C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_589CD4(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_589D0C@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_589D74@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_589D80@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_589DE4(void *this);
int __usercall sub_589DF8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_589E04@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_589E10@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_589EF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_58A014@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58A0B0@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58A168@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_58A1D4@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_58A308();
int sub_58A328();
int __usercall sub_58A348@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58A350@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_58A4E4(void *this);
_DWORD *__userpurge sub_58A500@<eax>(int a1@<eax>, int a2);
int __usercall sub_58A550@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58A5E4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_58A724(int a1, int a2);
int __usercall sub_58A738@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58A750@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58A768@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58A7B8(int a1, int a2);
int __usercall sub_58A7D0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58A80C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58A890@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58A8C8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58A968@<eax>(int a1@<eax>);
int __usercall sub_58A990@<eax>(int a1@<eax>);
int __usercall sub_58A9BC@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58A9F8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58AA38@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58AA44@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_58AAD8@<eax>(int a1@<eax>);
int __usercall sub_58AAE8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58AB00@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_58AB14();
_DWORD *__usercall sub_58AB1C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58AB60@<al>(int a1@<eax>);
_DWORD *__usercall sub_58AB80@<eax>(_DWORD *a1@<eax>);
int __usercall sub_58ABA0@<eax>(int a1@<eax>);
int __usercall sub_58ABB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58ACB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58ACF4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58ADB0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58ADC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58AE40@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58AEE4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58AF84@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_58AFBC(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58AFF4@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_58B05C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_58B068@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58B0BC(void *this);
int __usercall sub_58B0D0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58B0DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58B0E8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_58B1BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_58B2E8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_58B360@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58B3D8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58B444@<eax>(int result@<eax>, int a2@<edx>);
int sub_58B500();
int sub_58B520();
int __usercall sub_58B540@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58B548@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_58B6DC();
int __usercall sub_58B6E4@<eax>(int a1@<eax>);
int __usercall sub_58B710@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58B730@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58B808(void *this);
int __usercall sub_58B810@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58B81C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58B834@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58B884(int a1, int a2);
int __usercall sub_58B89C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58B8D8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58B92C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58B964@<eax>(int result@<eax>);
int __usercall sub_58B994@<eax>(int a1@<eax>);
int __usercall sub_58B9BC@<eax>(int a1@<eax>);
int __usercall sub_58B9E8@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58BA24@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58BA64@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58BA70@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_58BABC@<eax>(int a1@<eax>);
int __usercall sub_58BACC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_58BAE0();
_DWORD *__usercall sub_58BAE8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58BB2C@<al>(int a1@<eax>);
int __usercall sub_58BB4C@<eax>(int a1@<eax>);
int __usercall sub_58BB64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58BC18@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_58BC80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58BCC4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58BD90@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58BDA8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58BE20@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58BEC4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58BF64@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_58BF9C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58BFD4@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_58C03C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_58C048@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_58C0AC(void *this);
int __usercall sub_58C0C0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58C0CC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58C0D8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_58C1B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_58C2EC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58C36C@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58C3E0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58C44C@<eax>(int result@<eax>, int a2@<edx>);
int sub_58C520();
int sub_58C540();
int __usercall sub_58C560@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58C568@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_58C6FC(void *this);
int __userpurge sub_58C718@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_58C75C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58C7A0@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_58C894(int a1, int a2);
int __usercall sub_58C8A8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58C8C0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58C8D8@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58C928(int a1, int a2);
int __usercall sub_58C940@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58C97C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58C9D0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58CA08@<eax>(int result@<eax>);
int __usercall sub_58CA5C@<eax>(int a1@<eax>);
int __usercall sub_58CA84@<eax>(int a1@<eax>);
int __usercall sub_58CAB0@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58CAEC@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58CB2C@<eax>(int a1@<eax>, int a2@<ecx>);
volatile signed __int8 **__usercall sub_58CB38@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_58CB98@<eax>(int a1@<eax>);
int __usercall sub_58CBA8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58CBC0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_58CBD4();
_DWORD *__usercall sub_58CBDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58CC20@<al>(int a1@<eax>);
_DWORD *__usercall sub_58CC40@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_58CC60@<eax>(_DWORD *a1@<eax>);
int __usercall sub_58CC80@<eax>(int a1@<eax>);
int __usercall sub_58CC98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58CD90@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58CDD4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58CE90@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58CEA8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58CF20@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58CFC4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58D064@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_58D09C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58D0D4@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_58D13C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_58D148@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58D19C(void *this);
int __usercall sub_58D1B0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58D1BC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58D1C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_58D29C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_58D3C8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_58D440@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58D4B8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58D524@<eax>(int result@<eax>, int a2@<edx>);
int sub_58D5E0();
int sub_58D600();
int __usercall sub_58D620@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58D628@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_58D7BC();
int __usercall sub_58D7C4@<eax>(int a1@<eax>);
int __usercall sub_58D7F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58D810@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58D8E8(void *this);
int __usercall sub_58D8F0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58D8FC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58D914@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58D964(int a1, int a2);
int __usercall sub_58D97C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58D9B8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58DA0C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58DA44@<eax>(int result@<eax>);
int __usercall sub_58DA74@<eax>(int a1@<eax>);
int __usercall sub_58DA9C@<eax>(int a1@<eax>);
int __usercall sub_58DAC8@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58DB04@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58DB44@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58DB50@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_58DB9C@<eax>(int a1@<eax>);
int __usercall sub_58DBAC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_58DBC0();
_DWORD *__usercall sub_58DBC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58DC0C@<al>(int a1@<eax>);
int __usercall sub_58DC2C@<eax>(int a1@<eax>);
int __usercall sub_58DC44@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58DD3C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58DD80@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58DE3C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58DE54@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58DECC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58DF70@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58E010@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_58E048(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58E080@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_58E0E8@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_58E0F4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58E148(void *this);
int __usercall sub_58E15C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58E168@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58E174@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_58E248@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_58E374@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_58E3EC@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58E464@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58E4D0@<eax>(int result@<eax>, int a2@<edx>);
int sub_58E58C();
int sub_58E5AC();
int __usercall sub_58E5CC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58E5D4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int sub_58E768();
int __usercall sub_58E770@<eax>(int a1@<eax>);
int __usercall sub_58E79C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58E7BC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_58E894(void *this);
int __usercall sub_58E89C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58E8A8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58E8C0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58E910(int a1, int a2);
int __usercall sub_58E928@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58E964@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58E9B8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58E9F0@<eax>(int result@<eax>);
int __usercall sub_58EA20@<eax>(int a1@<eax>);
int __usercall sub_58EA48@<eax>(int a1@<eax>);
int __usercall sub_58EA74@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58EAB0@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58EAF0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58EAFC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_58EB48@<eax>(int a1@<eax>);
int __usercall sub_58EB58@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int sub_58EB6C();
_DWORD *__usercall sub_58EB74@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58EBB8@<al>(int a1@<eax>);
int __usercall sub_58EBD8@<eax>(int a1@<eax>);
int __usercall sub_58EBF0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58ECA8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_58ED10@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58ED54@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58EE30@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58EE48@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58EEC0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_58EF64@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_58F004@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_58F03C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_58F074@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_58F0DC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_58F0E8@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_58F14C(void *this);
int __usercall sub_58F160@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58F16C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58F178@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_58F258@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_58F388@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58F408@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_58F47C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58F4E8@<eax>(int result@<eax>, int a2@<edx>);
int sub_58F5CC();
int sub_58F5EC();
int __usercall sub_58F60C@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_58F614@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_58F7AC(void *this);
int __userpurge sub_58F7C8@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_58F814@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58F860@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_58F964(int a1, int a2);
int __usercall sub_58F978@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58F990@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58F9A8@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_58F9F8(int a1, int a2);
int __usercall sub_58FA10@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58FA50@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58FAA8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58FAE4@<eax>(int result@<eax>);
int __usercall sub_58FB44@<eax>(int a1@<eax>);
int __usercall sub_58FB6C@<eax>(int a1@<eax>);
int __usercall sub_58FB98@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_58FBD4@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_58FC14@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_58FC20@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_58FC84@<eax>(int a1@<eax>);
int __usercall sub_58FC94@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_58FCAC@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_58FCC0();
_DWORD *__usercall sub_58FCC8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_58FD0C@<al>(int a1@<eax>);
_DWORD *__usercall sub_58FD2C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_58FD4C@<eax>(int a1@<eax>);
int __usercall sub_58FD64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58FE24@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_58FEA0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_58FEE4@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_58FFC4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_58FFDC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_590054@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5900F8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_590198@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_5901D0(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_590208@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_590270@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_59027C@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_5902E8(void *this);
int __usercall sub_5902FC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590308@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590314@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5903FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_590538@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5905B8@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_59062C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_590698@<eax>(int result@<eax>, int a2@<edx>);
int sub_59077C();
int sub_59079C();
int __usercall sub_5907BC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_5907C4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_590958(void *this);
int __userpurge sub_590974@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_5909C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_590A2C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_590B40(int a1, int a2);
int __usercall sub_590B54@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590B6C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_590B84@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_590BD4(int a1, int a2);
int __usercall sub_590BEC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590C2C@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_590C84@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590CC0@<eax>(int result@<eax>);
int __usercall sub_590D38@<eax>(int a1@<eax>);
int __usercall sub_590D60@<eax>(int a1@<eax>);
int __usercall sub_590D8C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_590DC8@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_590E08@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_590E14@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_590E7C@<eax>(int a1@<eax>);
int __usercall sub_590E8C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_590EA4@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_590EB8();
_DWORD *__usercall sub_590EC0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_590F04@<al>(int a1@<eax>);
int __usercall sub_590F24@<eax>(int a1@<eax>);
int __usercall sub_590F3C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_591000@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5910BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_591100@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_591220@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_591238@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5912B0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_591354@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5913F4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_59142C(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_591464@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_5914CC@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5914D8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_591540(void *this);
int __usercall sub_591554@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_591560@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_59156C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_591650@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_591778@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_591814@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_5918CC@<eax>(int a1@<eax>, int a2@<ecx>);
OLECHAR **__usercall sub_591938@<eax>(
        _DWORD *a1@<eax>,
        void (__fastcall ***a2)(int, int, int, int, int)@<edx>,
        void (__fastcall **a3)(int, int, int, int, int)@<edi>);
int sub_591A70();
int sub_591A90();
int __usercall sub_591AB0@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_591AB8@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_591C4C(void *this);
int __userpurge sub_591C68@<eax>(int a1@<eax>, int a2);
int __usercall sub_591CC0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_591D60@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_591EAC(int a1, int a2);
int __usercall sub_591EC0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_591ED8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_591EF0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_591F40(int a1, int a2);
int __usercall sub_591F58@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_591F98@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_592020@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_59205C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_592108@<eax>(int a1@<eax>);
int __usercall sub_592130@<eax>(int a1@<eax>);
int __usercall sub_59215C@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_592198@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_5921D8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5921E4@<eax>(
        int a1@<eax>,
        volatile signed __int8 ***a2@<edx>,
        int a3@<ebx>,
        int a4@<edi>,
        int a5@<esi>);
int __usercall sub_59227C@<eax>(int a1@<eax>);
int __usercall sub_59228C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5922A4@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_5922B8();
_DWORD *__usercall sub_5922C0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_592304@<al>(int a1@<eax>);
_DWORD *__usercall sub_592324@<eax>(_DWORD *a1@<eax>);
int __usercall sub_592344@<eax>(int a1@<eax>);
int __usercall sub_59235C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_592410@<eax>(_DWORD *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_592478@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5924BC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_592588@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5925A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_592618@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5926BC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_59275C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_592794(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_5927CC@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_592834@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
__int64 __usercall sub_592840@<edx:eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __thiscall sub_5928A4(void *this);
int __usercall sub_5928B8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5928C4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5928D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5929B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_592AE4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_592B64@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_592BD8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_592C44@<eax>(int result@<eax>, int a2@<edx>);
int sub_592D18();
int sub_592D38();
int __usercall sub_592D58@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_592D60@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __thiscall sub_592EF4(void *this);
int __userpurge sub_592F10@<eax>(int a1@<eax>, _DWORD *a2);
int __usercall sub_592F54@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_592F98@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __fastcall sub_59308C(int a1, int a2);
int __usercall sub_5930A0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5930B8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5930D0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_593120(int a1, int a2);
int __usercall sub_593138@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_593174@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5931C8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_593200@<eax>(int result@<eax>);
int __usercall sub_593254@<eax>(int a1@<eax>);
int __usercall sub_59327C@<eax>(int a1@<eax>);
int __usercall sub_5932A8@<eax>(int a1@<eax>, int a2@<ecx>);
int __userpurge sub_5932E4@<eax>(int a1@<eax>, int a2@<ecx>, int a3);
int __usercall sub_593324@<eax>(int a1@<eax>, int a2@<ecx>);
volatile signed __int8 **__usercall sub_593330@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_593390@<eax>(int a1@<eax>);
int __usercall sub_5933A0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5933B8@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int sub_5933CC();
_DWORD *__usercall sub_5933D4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_593418@<al>(int a1@<eax>);
_DWORD *__fastcall sub_593438(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593458(_DWORD *a1, int a2);
__int64 *__fastcall sub_593480(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5934B0(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_5934E0(int a1, int a2, int a3, int a4);
bool __usercall sub_593504@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_593528@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_593588@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_593644(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593664(_DWORD *a1, int a2);
__int64 *__fastcall sub_59368C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5936B8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_5936E4(int a1, int a2, int a3, int a4);
bool __usercall sub_593708@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_59372C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_59378C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_593844(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593864(_DWORD *a1, int a2);
__int64 *__fastcall sub_59388C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5938B8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_5938E4(int a1, int a2, int a3, int a4);
bool __usercall sub_593908@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_59392C@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_59398C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_593A44(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593A64(_DWORD *a1, int a2);
__int64 *__fastcall sub_593A8C(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_593ABC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_593AEC(int a1, int a2, int a3, int a4);
bool __usercall sub_593B14@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_593B38@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_593B98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_593C50@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_593C8C@<eax>(int a1@<eax>);
int __userpurge sub_593C98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__fastcall sub_593D64(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593D84(_DWORD *a1, int a2);
__int64 *__fastcall sub_593DAC(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_593DDC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_593E0C(int a1, int a2, int a3, int a4);
bool __usercall sub_593E34@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_593E58@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_593EB8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_593F70(int a1, _DWORD *a2);
_DWORD *__fastcall sub_593F90(_DWORD *a1, int a2);
__int64 *__fastcall sub_593FB8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_593FE4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594010(int a1, int a2, int a3, int a4);
bool __usercall sub_594034@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594058@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5940B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594170(int a1, _DWORD *a2);
_DWORD *__fastcall sub_594190(_DWORD *a1, int a2);
__int64 *__fastcall sub_5941B8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5941E4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594210(int a1, int a2, int a3, int a4);
bool __usercall sub_594234@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594258@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5942B8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594370(int a1, _DWORD *a2);
_DWORD *__fastcall sub_594390(_DWORD *a1, int a2);
__int64 *__fastcall sub_5943B8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5943E8(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594418(int a1, int a2, int a3, int a4);
bool __usercall sub_594440@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594464@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5944C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_59457C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_59459C(_DWORD *a1, int a2);
__int64 *__fastcall sub_5945C4(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5945F0(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_59461C(int a1, int a2, int a3, int a4);
bool __usercall sub_594640@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594664@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5946C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_59477C(int a1, _DWORD *a2);
_DWORD *__fastcall sub_59479C(_DWORD *a1, int a2);
__int64 *__fastcall sub_5947C4(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5947F4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594824(int a1, int a2, int a3, int a4);
bool __usercall sub_59484C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594870@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5948D0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594988(int a1, _DWORD *a2);
_DWORD *__fastcall sub_5949A8(_DWORD *a1, int a2);
__int64 *__fastcall sub_5949D0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_5949FC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594A28(int a1, int a2, int a3, int a4);
bool __usercall sub_594A4C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594A70@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_594AD0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594B88(int a1, _DWORD *a2);
_DWORD *__fastcall sub_594BA8(_DWORD *a1, int a2);
__int64 *__fastcall sub_594BD0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_594BFC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594C28(int a1, int a2, int a3, int a4);
bool __usercall sub_594C4C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594C70@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_594CD0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594D88(int a1, _DWORD *a2);
_DWORD *__fastcall sub_594DA8(_DWORD *a1, int a2);
__int64 *__fastcall sub_594DD0(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_594E00(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_594E30(int a1, int a2, int a3, int a4);
bool __usercall sub_594E54@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_594E78@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_594ED8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_594F94(int a1, _DWORD *a2);
_DWORD *__fastcall sub_594FB4(_DWORD *a1, int a2);
__int64 *__fastcall sub_594FDC(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_595010(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_595044(int a1, int a2, int a3, int a4);
bool __usercall sub_595070@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_595094@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_5950F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_5951B0(int a1, _DWORD *a2);
_DWORD *__fastcall sub_5951D0(_DWORD *a1, int a2);
__int64 *__fastcall sub_5951F8(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_59522C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_595260(int a1, int a2, int a3, int a4);
bool __usercall sub_59528C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5952B0@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_595310@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__fastcall sub_5953CC(int a1, _DWORD *a2);
_DWORD *__fastcall sub_5953EC(_DWORD *a1, int a2);
__int64 *__fastcall sub_595414(int a1, int a2, int a3, int a4, int a5);
__int64 *__fastcall sub_595444(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __fastcall sub_595474(int a1, int a2, int a3, int a4);
bool __usercall sub_59549C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5954C0@<eax>(int a1@<eax>, int a2@<edx>, int a3, int a4);
int __userpurge sub_595520@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5, int a6, int *a7);
_DWORD *__usercall sub_5955D8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_595614@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_595624@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_59578C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5957C8@<eax>(int a1@<eax>);
int __userpurge sub_5957D4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_5958A0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5958DC@<eax>(int a1@<eax>);
int __userpurge sub_5958E8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_5959B4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5959F0@<eax>(int a1@<eax>);
int __userpurge sub_595A00@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_595AEC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_595B28@<eax>(int a1@<eax>);
int __userpurge sub_595B38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_595C24@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_595C60@<eax>(int a1@<eax>);
int __userpurge sub_595C6C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_595D38@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_595D74@<eax>(int a1@<eax>);
int __userpurge sub_595D80@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_595E4C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_595E88@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_595E98@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_595FE8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596024@<eax>(int a1@<eax>);
int __userpurge sub_596030@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_5960FC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596138@<eax>(int a1@<eax>);
int __userpurge sub_596148@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_596234@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596270@<eax>(int a1@<eax>);
int __userpurge sub_59627C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_596348@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596384@<eax>(int a1@<eax>);
int __userpurge sub_596390@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_59645C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596498@<eax>(int a1@<eax>);
int __userpurge sub_5964A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_5965B0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5965EC@<eax>(int a1@<eax>);
int __userpurge sub_5965FC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__usercall sub_59671C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596758@<eax>(int a1@<eax>);
OLECHAR **__userpurge sub_596768@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
_DWORD *__usercall sub_5968CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_596908@<eax>(int a1@<eax>);
int __userpurge sub_596918@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
__int32 __usercall sub_596A69@<eax>(int a1@<eax>);
int __stdcall sub_596A75(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_596A7F(int a1);
signed __int32 __stdcall sub_596A89(int a1);
int nullsub_377();
int nullsub_378();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_379(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_380@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_381();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_382(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_383@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_384();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_385(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_386@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_387();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_388(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_389@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_390();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_391(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_392@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_393();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_394(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_395@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_396();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_397(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_398@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_399();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_400(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_401@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_402();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_403(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_404@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_405();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_406(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_407@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_408();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_409(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_410@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int nullsub_411();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_412(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_413@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
__int32 __usercall sub_5A5F19@<eax>(int a1@<eax>);
int __stdcall sub_5A5F25(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_5A5F2F(int a1);
signed __int32 __stdcall sub_5A5F39(int a1);
__int32 __usercall sub_5A672D@<eax>(int a1@<eax>);
int __stdcall sub_5A6739(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_5A6743(int a1);
signed __int32 __stdcall sub_5A674D(int a1);
int nullsub_414();
int nullsub_415();
int nullsub_416();
int nullsub_417();
int nullsub_418();
int nullsub_419();
__int32 __usercall sub_5AA83D@<eax>(int a1@<eax>);
int __stdcall sub_5AA849(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_5AA853(int a1);
signed __int32 __stdcall sub_5AA85D(int a1);
int nullsub_420();
int nullsub_421();
int nullsub_422();
__int32 __usercall sub_5ABF55@<eax>(int a1@<eax>);
int __stdcall sub_5ABF61(int a1, int a2, _DWORD *a3);
signed __int32 __stdcall sub_5ABF6B(int a1);
signed __int32 __stdcall sub_5ABF75(int a1);
int nullsub_423();
int nullsub_424();
int nullsub_425();
int nullsub_426();
signed int __usercall sub_5B133C@<eax>(signed int a1@<eax>);
int __usercall sub_5B135C@<eax>(int result@<eax>);
_DWORD *__usercall sub_5B137C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__userpurge sub_5B13C8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_5B141C@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5B1494@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_5B1558@<al>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_5B156C@<eax>(int *a1@<eax>);
// attributes: thunk
int __usercall sub_5B160D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_DWORD *__usercall sub_5B1650@<eax>(int *a1@<eax>, struct _IMAGELIST *a2@<edx>);
int __usercall sub_5B1688@<eax>(int result@<eax>, char a2@<dl>);
void __usercall sub_5B1694(int *a1@<eax>, int a2@<edx>);
void __usercall sub_5B16D8(int *a1@<eax>, int a2@<edx>);
void __usercall sub_5B171C(int *a1@<eax>, struct _IMAGELIST *a2@<edx>);
int __usercall sub_5B1748@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5B1758@<eax>(int a1@<eax>);
int __usercall sub_5B1768@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
void __usercall sub_5B17F4(int a1@<eax>);
_DWORD *__usercall sub_5B182C@<eax>(int a1@<eax>);
HBITMAP __usercall sub_5B18D8@<eax>(int a1@<eax>);
HBITMAP __usercall sub_5B190C@<eax>(int a1@<eax>);
unsigned int __usercall sub_5B1940@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5B1A0C@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
unsigned int __usercall sub_5B1B28@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5B1B78@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5B1BF4@<eax>(int a1@<eax>);
char __userpurge sub_5B1C08@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4, unsigned __int8 a5);
int __usercall sub_5B1C58@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_5B1C7C@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_5B1DA4@<eax>(int *a1@<eax>, void *a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_5B1FCC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5B2078@<eax>(int *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5B2104@<eax>(int *a1@<eax>);
void __usercall sub_5B2110(int *a1@<eax>, signed int a2@<edx>);
int __usercall sub_5B2148@<eax>(int result@<eax>, char a2@<dl>);
void __usercall sub_5B21B0(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5B21F8@<eax>(int a1@<eax>);
int __usercall sub_5B2220@<eax>(int a1@<eax>, int a2);
char __userpurge sub_5B2304@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, UINT fStyle, int y, int x);
int __userpurge sub_5B2608@<eax>(int a1@<eax>, char a2, int a3, int a4);
char __userpurge sub_5B2630@<al>(
        _DWORD *a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        unsigned __int8 a4,
        unsigned __int8 a5,
        unsigned __int8 a6,
        int a7,
        int a8);
int __stdcall sub_5B2678(char a1, char a2, int a3, int a4);
char __userpurge sub_5B269C@<al>(
        _DWORD *a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        unsigned __int8 a4,
        unsigned __int8 a5,
        unsigned __int8 a6,
        unsigned __int8 a7,
        int a8,
        int a9);
BOOL __usercall sub_5B26F4@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_5B272C@<eax>(int *a1@<eax>, struct _IMAGELIST *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_5B28E4@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
_DWORD *__userpurge sub_5B29E8@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__userpurge sub_5B29FC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_5B2A10@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_5B2B6C(int iDst@<ecx>, int iSrc@<edx>, int *a3@<eax>);
int __usercall sub_5B2BDC@<eax>(int *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5B2C14@<eax>(int result@<eax>, int a2@<edx>);
void __usercall sub_5B2C34(int a1@<eax>, int (***a2)(void)@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5B2CC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5B2D48@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_5B2DC0(int a1@<eax>, char a2@<dl>);
__int64 __fastcall sub_5B2DD4(int a1, _DWORD *a2);
int __stdcall sub_5B2DF4(COLORREF crMask, unsigned __int8 a2, int a3, LPCWSTR lpbmp);
int __stdcall sub_5B2E14(COLORREF crMask, unsigned __int8 a2, int a3, int a4);
char __userpurge sub_5B2E48@<al>(
        int *a1@<eax>,
        HINSTANCE a2@<edx>,
        unsigned __int8 a3@<cl>,
        COLORREF crMask,
        char a5,
        int a6,
        LPCWSTR lpbmp);
int __thiscall sub_5B2ED8(void *this, COLORREF a2, unsigned __int8 a3, int a4);
int __userpurge sub_5B2EFC@<eax>(int a1@<eax>, COLORREF a2, int a3);
int __userpurge sub_5B2F24@<eax>(int a1@<eax>, int a2@<ecx>, COLORREF a3);
int __userpurge sub_5B2FFC@<eax>(int a1@<eax>, void *a2@<ecx>, COLORREF a3);
void __usercall sub_5B3020(int a1@<eax>, int a2@<ecx>);
__int64 *__usercall sub_5B3070@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5B30B4@<eax>(int result@<eax>, int a2@<edx>);
bool __usercall sub_5B30C8@<al>(int a1@<eax>, int a2@<edx>);
BOOL __usercall sub_5B310C@<eax>(int a1@<eax>, int a2@<edx>);
bool __cdecl sub_5B31FC(int a1);
int __usercall sub_5B3254@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_5B32B8@<eax>(int *a1@<eax>, int a2@<edx>);
char __usercall sub_5B354C@<al>(int *a1@<eax>, int (***a2)(void)@<edx>);
int __usercall sub_5B3718@<eax>(int *a1@<eax>, int (***a2)(void)@<edx>);
_DWORD *__usercall sub_5B37CC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5B393C@<eax>(int result@<eax>);
void __usercall sub_5B3940(int a1@<eax>);
int __usercall sub_5B3960@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5B3994@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5B6370@<eax>(POINT *a1@<eax>);
int __usercall sub_5B63A4@<eax>(int **a1@<eax>, int a2, int a3, int a4, int a5);
int __usercall sub_5B63C8@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5B6400@<eax>(unsigned __int8 a1@<al>, __int64 **a2@<edx>);
int __usercall sub_5B645C@<eax>(__int16 a1@<ax>, __int64 **a2@<edx>);
int __usercall sub_5B6658@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5B66D8@<eax>(int a1@<eax>, int a2@<ebx>);
int sub_5B67D4();
int __usercall sub_5B67F4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int (__cdecl *a3)(_DWORD)@<ecx>, _DWORD *a4);
int __usercall sub_5B6858@<eax>(int (__cdecl *a1)(_DWORD)@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5B6968@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_5B6984@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_5B69B8@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B69E4@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6A0C@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6A34@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6A58@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6A84@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6AB4@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6ADC@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6B08@<al>(int a1@<eax>, unsigned __int8 a2@<cl>);
bool __usercall sub_5B6B30@<al>(int a1@<eax>);
int __usercall sub_5B6B58@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5B6B78@<eax>(int a1@<eax>);
int __usercall sub_5B6B98@<eax>(int a1@<eax>);
int __usercall sub_5B6BB8@<eax>(int a1@<eax>);
int __usercall sub_5B6BD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5B6BF4@<eax>(_DWORD *a1@<eax>, __int32 a2@<edx>);
int __usercall sub_5B6C18@<eax>(int a1@<eax>);
int __usercall sub_5B6C38@<eax>(int a1@<eax>);
int __usercall sub_5B6C58@<eax>(int a1@<eax>);
int __userpurge sub_5B6C78@<eax>(_DWORD *a1@<eax>, int a2, int a3);
_DWORD *__usercall sub_5B6CA4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_5B6CF4@<al>(int a1@<eax>);
int __usercall sub_5B6D10@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5B6D94@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5B6E84@<eax>(int a1@<eax>, HMENU a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_5B7190@<eax>(int a1@<eax>, int a2);
int __usercall sub_5B71B0@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5B7220@<eax>(int a1@<eax>, __int64 *a2@<edx>, int a3@<edi>);
int __usercall sub_5B7278@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_5B72B4(int a1@<eax>);
int __usercall sub_5B72F4@<eax>(int result@<eax>);
int __fastcall sub_5B73CC(unsigned __int8 a1, int a2);
int __usercall sub_5B7484@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
_DWORD *__userpurge sub_5B74D8@<eax>(
        int a1@<eax>,
        _DWORD *a2@<edx>,
        __int32 a3@<ecx>,
        UINT format,
        char a5,
        LPRECT lprc);
int __userpurge sub_5B7710@<eax>(int result@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, unsigned __int8 a4);
_DWORD *__userpurge sub_5B7750@<eax>(int a1@<eax>, int a2@<edx>, __int32 a3@<ecx>, unsigned int a4, int a5, int a6);
_DWORD *__usercall sub_5B78B4@<eax>(char a1@<al>, void *a2@<ecx>, struct tagRECT *a3);
_DWORD *__cdecl sub_5B83E8(struct tagRECT *a1);
_DWORD *__cdecl sub_5B8D48(struct tagRECT *a1);
_DWORD *__userpurge sub_5B96C8@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, unsigned __int16 a5);
int __usercall sub_5B9880@<eax>(int a1@<eax>);
_DWORD *__cdecl sub_5B98B4(int a1);
_DWORD *__cdecl sub_5B9900(int a1);
_DWORD *__userpurge sub_5B9D48@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, _DWORD *a4);
char sub_5B9FB4();
int __usercall sub_5B9FD0@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5B9FF8@<eax>(int result@<eax>);
DWORD __usercall sub_5BA044@<eax>(DWORD result@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_5BA098@<eax>(int result@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_5BA110@<eax>(int result@<eax>, unsigned __int8 a2@<dl>, int a3@<ecx>);
int __usercall sub_5BA154@<eax>(int a1@<eax>);
int (**sub_5BA164())();
int __usercall sub_5BA16C@<eax>(int a1@<eax>);
_WORD *__usercall sub_5BA1A0@<eax>(_WORD *result@<eax>, __int16 a2@<dx>);
_BYTE *__usercall sub_5BA1B8@<eax>(_BYTE *result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5BA1D0@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_5BA1E8@<eax>(int a1@<eax>);
int __usercall sub_5BA200@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_5BA248@<eax>(int a1@<eax>, int (*a2)(void), int a3);
int __fastcall sub_5BA280(int a1, int a2);
int __usercall sub_5BA2A0@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5BA2FC@<eax>(int result@<eax>);
int __usercall sub_5BA30C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5BA440@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5BA4F4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5BA50C@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5BA550@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __userpurge sub_5BA594@<al>(int *a1@<eax>, int a2@<ecx>, char a3);
int __usercall sub_5BA5F0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5BA618@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5BA688@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
int __usercall sub_5BA6BC@<eax>(int a1@<eax>);
int __usercall sub_5BA6E8@<eax>(int a1@<eax>);
char __usercall sub_5BA6FC@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5BA750@<eax>(int a1@<eax>);
char __usercall sub_5BA78C@<al>(DWORD a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_5BA8B0(int *a1@<eax>, int a2@<edx>);
bool __usercall sub_5BA8D4@<al>(int a1@<eax>);
bool __usercall sub_5BA8F4@<al>(int a1@<eax>);
bool __usercall sub_5BA914@<al>(int a1@<eax>);
bool __usercall sub_5BA934@<al>(int a1@<eax>);
bool __usercall sub_5BA954@<al>(int a1@<eax>);
bool __usercall sub_5BA974@<al>(int a1@<eax>);
bool __usercall sub_5BA994@<al>(int a1@<eax>);
bool __usercall sub_5BA9B4@<al>(int a1@<eax>);
bool __usercall sub_5BA9D4@<al>(int a1@<eax>);
_DWORD *__usercall sub_5BA9F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5BAA78@<eax>(int *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
int __usercall sub_5BAACC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5BAB18@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5BAC18@<eax>(int *a1@<eax>);
int __fastcall sub_5BAC40(int a1, int a2);
int __usercall sub_5BAC4C@<eax>(int a1@<eax>);
int __usercall sub_5BAC5C@<eax>(int result@<eax>, int *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5BAC80@<eax>(int a1@<eax>);
int __usercall sub_5BACAC@<eax>(int a1@<eax>, int a2@<ebx>, int a3);
volatile __int32 *__cdecl sub_5BACE0(int a1);
int __usercall sub_5BAD64@<eax>(__int64 **a1@<eax>, int a2@<edx>, int a3@<ecx>);
BOOL __usercall sub_5BAF54@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5BB4B4@<al>(int a1@<eax>);
int __usercall sub_5BB4DC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5BB5A8@<eax>(_DWORD *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5BB6CC@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5BB710@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5BB74C@<eax>(int a1@<eax>, char a2@<dl>);
_BYTE *__usercall sub_5BB894@<eax>(_BYTE *result@<eax>, char a2@<dl>);
int __usercall sub_5BB904@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5BB934@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5BB9D0@<eax>(int a1@<eax>);
int __usercall sub_5BB9E0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
void __userpurge sub_5BBA14(int a1@<eax>, int a2, int a3);
void __usercall sub_5BBA44(int a1@<eax>);
int __usercall sub_5BBA64@<eax>(int a1@<eax>);
int __usercall sub_5BBA7C@<eax>(int a1@<eax>, int a2);
int __usercall sub_5BBB18@<eax>(int a1@<eax>);
int __usercall sub_5BBB48@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5BBBB8@<eax>(int a1@<eax>);
int __usercall sub_5BBBDC@<eax>(int a1@<eax>);
bool __usercall sub_5BBC9C@<al>(int a1@<eax>);
BOOL sub_5BBCB0();
_DWORD *sub_5BBD24();
int sub_5BBF50();
int __usercall sub_5BBF8C@<eax>(int a1@<eax>);
int __usercall sub_5BBFDC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5BBFEC@<eax>(int *a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_5BC140@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5BC234@<al>(int a1@<eax>);
int *__usercall sub_5BC23C@<eax>(HWND *a1@<eax>);
UINT __usercall sub_5BC344@<eax>(HMENU a1@<eax>, int a2);
int __usercall sub_5BC414@<eax>(int a1@<eax>);
int __usercall sub_5BC498@<eax>(int result@<eax>, char a2@<dl>);
int *__usercall sub_5BC4A8@<eax>(int a1@<eax>);
int *__usercall sub_5BC528@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5BC560@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5BC578@<eax>(int a1@<eax>);
__int16 __userpurge sub_5BC590@<ax>(_WORD *a1@<eax>, int a2@<ecx>, unsigned __int8 a3);
int __usercall sub_5BC5CC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5BC5D8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5BC614@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>, unsigned __int8 a3@<cl>);
bool __usercall sub_5BC640@<al>(int a1@<eax>);
int __userpurge sub_5BC658@<eax>(int nPos@<ecx>, HMENU a2@<eax>, char a3@<dl>, __int16 a4, int a5);
int __userpurge sub_5BC6B4@<eax>(
        int nPos@<ecx>,
        HMENU a2@<eax>,
        __int16 a3@<dx>,
        int a4@<ebx>,
        int a5@<esi>,
        __int16 a6,
        int a7);
int __fastcall sub_5BC79C(int a1, int a2);
int __userpurge sub_5BC918@<eax>(
        UINT uIDItem@<ecx>,
        HMENU hMenu@<edx>,
        int a3@<eax>,
        UINT uFlags,
        int cchMax,
        LPWSTR lpString);
int *__usercall sub_5BC9C4@<eax>(int *result@<eax>, char a2@<dl>);
void *__usercall sub_5BC9E8@<eax>(void *result@<eax>, DWORD a2@<ecx>);
int *__usercall sub_5BCA10@<eax>(int *result@<eax>, int a2@<edx>, int a3@<ecx>);
__int16 __userpurge sub_5BCAA4@<ax>(int a1@<eax>, int a2@<ecx>, unsigned __int8 a3);
int __usercall sub_5BCB00@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5BCB1C@<eax>(int result@<eax>, int a2@<edx>);
HWND __usercall sub_5BCB38@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5BCB64@<eax>(int a1@<eax>);
int __usercall sub_5BCB74@<eax>(int a1@<eax>, int a2);
int __usercall sub_5BCC10@<eax>(int a1@<eax>, int a2);
_DWORD *__userpurge sub_5BCC48@<eax>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5);
int __usercall sub_5BCCCC@<eax>(int a1@<eax>, int a2);
int __userpurge sub_5BCD18@<eax>(int a1@<eax>, int a2, _DWORD *a3, int a4);
int __usercall sub_5BCD74@<eax>(unsigned int a1@<eax>);
_DWORD *__usercall sub_5BCDC0@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5BD0FF@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5BD11C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5BD23B@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5BD258@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5BD27D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5BD307@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5BD318@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5BD340@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5BD35C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5BD3D4@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
// attributes: thunk
BOOL sub_5BD404();
int __usercall sub_5BD40C@<eax>(int result@<eax>);
int __usercall sub_5BD428@<eax>(int a1@<eax>);
int __usercall sub_5BD430@<eax>(int a1@<eax>, int a2@<edx>);
int *__usercall sub_5BD438@<eax>(int a1@<eax>);
int __usercall sub_5BD484@<eax>(int a1@<eax>);
BOOL __usercall sub_5BD4D4@<eax>(int y@<ecx>, int x@<edx>, int a3@<eax>);
int __usercall sub_5BD580@<eax>(int result@<eax>, _DWORD *a2@<edx>);
_DWORD *__usercall sub_5BD5A0@<eax>(int a1@<eax>, int a2@<edx>);
int *sub_5BD5DC();
int __userpurge sub_5BD610@<eax>(int *a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, unsigned __int16 a4);
int __usercall sub_5BD6F8@<eax>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_5BD7FC@<eax>(int a1@<eax>, __int64 **a2@<edx>);
int __usercall sub_5BD874@<eax>(__int32 a1@<eax>, __int32 a2@<edx>);
int __usercall sub_5BD9D0@<eax>(int a1@<edi>);
HMODULE sub_5BDD54();
void __userpurge nullsub_428(int a1);
void nullsub_429();
int nullsub_430();
void __userpurge nullsub_433(int a1);
void nullsub_434();
void __userpurge nullsub_435(int a1);
int __usercall sub_5C6598@<eax>(HWND a1@<eax>);
int sub_5C65BC();
int __usercall sub_5C65C4@<eax>(int result@<eax>);
LONG __usercall sub_5C65CC@<eax>(LONG result@<eax>, char a2@<dl>);
LONG __usercall sub_5C661C@<eax>(HWND a1@<eax>, char a2@<dl>, unsigned __int8 a3@<cl>);
_DWORD *__thiscall sub_5C66E0(void *this);
BOOL __stdcall sub_5C671C(HWND hWnd, LPARAM a2);
int __usercall sub_5C676C@<eax>(int a1@<eax>);
int __usercall sub_5C6830@<eax>(int result@<eax>);
BOOL __stdcall sub_5C6864(HWND hWnd, LPARAM a2);
int __usercall sub_5C68C8@<eax>(int a1@<eax>);
bool __usercall sub_5C6908@<al>(HWND a1@<eax>, unsigned __int16 a2@<dx>);
BOOL __stdcall sub_5C6928(HWND a1, LPARAM a2);
BOOL __stdcall sub_5C6948(HWND hWnd, LPARAM a2);
int __usercall sub_5C6980@<eax>(char a1@<al>);
int __usercall sub_5C69C4@<eax>(int a1@<eax>);
int __stdcall sub_5C6A44(int a1, int a2);
// attributes: thunk
int __usercall sub_5C6A58@<eax>(int a1@<eax>);
HWND __stdcall sub_5C6A60(int a1, int a2);
// attributes: thunk
int __usercall sub_5C6A74@<eax>(HWND a1@<eax>);
int __usercall sub_5C6A7C@<eax>(char a1@<al>);
int __usercall sub_5C6AD0@<eax>(int a1@<eax>);
int __usercall sub_5C6B10@<eax>(char *a1@<eax>);
int __fastcall sub_5C6B60(int a1, int a2);
int __usercall sub_5C6BD0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5C6C14@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5C6C24@<eax>(int a1@<eax>, char a2@<dl>);
int __userpurge sub_5C6CA4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, char a4);
int __usercall sub_5C6D38@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5C6D88@<eax>(int result@<eax>);
char __usercall sub_5C6DC0@<al>(int a1@<eax>, int a2);
char __usercall sub_5C6E48@<al>(int a1@<eax>, int a2);
int __usercall sub_5C6EC8@<eax>(int result@<eax>);
bool __usercall sub_5C6F74@<al>(int a1@<eax>);
bool __usercall sub_5C6FA8@<al>(__int16 a1@<ax>, int a2);
int __usercall sub_5C6FDC@<eax>(__int16 a1@<ax>, unsigned __int16 a2@<dx>, int a3);
int __usercall sub_5C7050@<eax>(int a1@<eax>);
bool __usercall sub_5C70E0@<al>(int a1@<eax>);
int __cdecl sub_5C70F8(int a1);
__int16 __usercall sub_5C7154@<ax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5C7458@<eax>(int result@<eax>, int SystemMetrics@<edx>);
int __usercall sub_5C7498@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5C74CC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5C7588@<eax>(int result@<eax>, int SystemMetrics@<edx>);
int __usercall sub_5C75F8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5C7610@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5C7624@<al>(int a1@<eax>);
int __usercall sub_5C7634@<eax>(int a1@<eax>, char a2@<dl>);
BOOL __usercall sub_5C7640@<eax>(char a1@<al>, int a2);
unsigned int __usercall sub_5C7748@<eax>(int a1@<eax>, char a2@<dl>, char a3@<cl>);
int __usercall sub_5C785C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5C78FC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5C795C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5C796C@<eax>(int *a1@<eax>);
void __usercall sub_5C79AC(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool __usercall sub_5C79CC@<al>(_BYTE *a1@<eax>);
_DWORD *__usercall sub_5C79EC@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5C7B04@<eax>(_DWORD *result@<eax>, int a2@<edx>, _BYTE *a3@<ecx>);
char __usercall sub_5C7B78@<al>(int a1@<eax>, _BYTE *a2@<edx>, _BYTE *a3@<ecx>);
int __usercall sub_5C7BBC@<eax>(int result@<eax>);
int __usercall sub_5C7BE0@<eax>(int result@<eax>, char a2@<dl>);
char __usercall sub_5C7C34@<al>(int a1@<eax>);
int __usercall sub_5C7D54@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5C7D70@<eax>(int result@<eax>);
char __usercall sub_5C7DB0@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5C7DFC@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5C7F50@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int a3@<eax>);
int __usercall sub_5C7FF4@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, int a3@<eax>);
void nullsub_427();
char __usercall sub_5C801C@<al>(int a1@<eax>);
__int16 __usercall sub_5C810C@<ax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
__int16 __usercall sub_5C8130@<ax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5C8154@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_5C81F4@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int *__usercall sub_5C8284@<eax>(int *a1@<eax>, char a2@<dl>, int a3@<ecx>);
void __usercall sub_5C845C(int *a1@<eax>);
int __usercall sub_5C8494@<eax>(int a1@<eax>, int a2@<ecx>);
int *__userpurge sub_5C8608@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4);
int __usercall sub_5C8650@<eax>(int a1@<eax>);
int __usercall sub_5C86C8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5C8838@<eax>(int a1@<eax>, int *a2@<ecx>);
int __usercall sub_5C88B4@<eax>(int result@<eax>);
int __usercall sub_5C8914@<eax>(int a1@<eax>);
char __usercall sub_5C8998@<al>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_5C8AE4@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5C8D78@<eax>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5C8E60@<al>(int a1@<eax>);
__int64 __usercall sub_5C8E80@<edx:eax>(int a1@<eax>, __int64 *a2@<edx>);
__int64 *__fastcall sub_5C8E98(int a1, __int64 *a2);
__int64 *__fastcall sub_5C8EB4(int a1, __int64 *a2);
int __usercall sub_5C8ED0@<eax>(int a1@<eax>);
int __usercall sub_5C8EF0@<eax>(int a1@<eax>);
void nullsub_432();
_DWORD *__usercall sub_5C8F38@<eax>(int nDenominator@<ecx>, int nNumerator@<edx>, _DWORD *a3@<eax>);
char __usercall sub_5C8FC0@<al>(_BYTE *a1@<eax>);
char sub_5C901C();
bool __usercall sub_5C902C@<al>(int a1@<eax>);
bool __usercall sub_5C9054@<al>(int a1@<eax>);
int __usercall sub_5C9088@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5C90A8@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5C90C8@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5C90E8@<eax>(int result@<eax>);
int __usercall sub_5C90FC@<eax>(int result@<eax>);
int __usercall sub_5C9110@<eax>(int result@<eax>);
BOOL __usercall sub_5C9128@<eax>(_DWORD *a1@<eax>, struct tagRECT *a2@<edx>);
void __userpurge sub_5C91B0(int a1@<eax>, int a2@<edx>, int (*a3)(void), int a4);
HWND __usercall sub_5C921C@<eax>(int a1@<eax>);
bool __usercall sub_5C9234@<al>(int *a1@<eax>);
void __usercall sub_5C9268(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5C92FC@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5C9324@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5C9350@<eax>(int a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_5C937C@<eax>(_BYTE *result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5C93E0@<eax>(int a1@<eax>);
int sub_5C944C();
int __usercall sub_5C9450@<eax>(int a1@<eax>, _BYTE *a2@<edx>);
char __userpurge sub_5C950C@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
void __usercall sub_5C954C(int *a1@<eax>, unsigned int *a2@<edx>, DWORD a3@<ecx>);
// attributes: thunk
int __usercall sub_5C9925@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5C9942@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5C9A2C@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5C9A49@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5C9A70@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
LRESULT __cdecl sub_5C9B8C(int a1);
char sub_5C9BD8();
_DWORD *__usercall sub_5C9C18@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
// attributes: thunk
int __usercall sub_5C9DE9@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
HWND __usercall sub_5C9DFC@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>);
char *__usercall sub_5C9EB8@<eax>(int *a1@<eax>, int a2@<edx>, LONG a3@<ecx>);
_BYTE *__usercall sub_5C9F50@<eax>(_BYTE *result@<eax>);
int __usercall sub_5C9FE4@<eax>(int a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
_DWORD *__usercall sub_5CA058@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CA0A8@<eax>(_BYTE *a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>);
char __usercall sub_5CA170@<al>(int a1@<eax>, char a2@<dl>);
char __userpurge sub_5CA258@<al>(int a1@<eax>, _DWORD *a2@<edx>, _DWORD *a3@<ecx>, _DWORD *a4);
char __usercall sub_5CA36C@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5CA50C@<eax>(int *a1@<eax>, int a2@<edx>, int *a3@<ecx>);
int __usercall sub_5CA550@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
HANDLE __usercall sub_5CA5A8@<eax>(int a1@<eax>);
int __usercall sub_5CA5DC@<eax>(int a1@<eax>);
int __usercall sub_5CA628@<eax>(int a1@<eax>, int a2@<edx>);
char __thiscall fnEnum(void *this, HMONITOR a2, HDC a3, LPRECT a4, _DWORD *a5);
int __usercall sub_5CA6A8@<eax>(int a1@<eax>);
int __usercall sub_5CA744@<eax>(int a1@<eax>);
char __usercall sub_5CA758@<al>(int a1@<eax>);
bool __usercall sub_5CA760@<al>(int a1@<eax>);
char __usercall sub_5CA788@<al>(_BYTE *a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5CA8FC@<eax>(int result@<eax>, int a2@<edx>);
LRESULT __usercall sub_5CA90C@<eax>(LRESULT result@<eax>);
int __usercall sub_5CA988@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
LRESULT __usercall sub_5CA9AC@<eax>(LRESULT result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5CA9D4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CAC14@<eax>(int a1@<eax>);
int __usercall sub_5CAC28@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CAC50@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CAC78@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CACAC@<eax>(int result@<eax>, char a2@<dl>);
char __usercall sub_5CACC8@<al>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
char __usercall sub_5CAD1C@<al>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
bool __usercall sub_5CAD80@<al>(int a1@<eax>);
char __usercall sub_5CAD8C@<al>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5CADBC@<eax>(int a1@<eax>);
int __usercall sub_5CADF0@<eax>(int a1@<eax>);
int __usercall sub_5CAE08@<eax>(int a1@<eax>);
int __usercall sub_5CAE50@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5CAE70@<eax>(LRESULT a1@<eax>);
_BYTE *__usercall sub_5CAE8C@<eax>(_BYTE *result@<eax>, unsigned __int8 a2@<dl>);
int __usercall sub_5CAECC@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5CB278@<eax>(HWND a1@<eax>);
char __usercall sub_5CB2F4@<al>(int a1@<eax>, int a2@<edx>);
unsigned __int8 __usercall sub_5CB900@<al>(int a1@<eax>);
_DWORD *__usercall sub_5CBB18@<eax>(int a1@<eax>, LPARAM *a2@<edx>);
BOOL __thiscall sub_5CBC50(void *this, HWND hWnd, LPARAM a3);
int __usercall sub_5CBC94@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CBDC8@<eax>(int a1@<eax>);
__int16 __usercall sub_5CBE24@<ax>(int a1@<eax>, UINT *a2@<edx>);
_DWORD *__usercall sub_5CBE88@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
unsigned __int8 __usercall sub_5CBF64@<al>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_5CBFAC@<eax>(int a1@<eax>, int *a2@<edx>, int a3@<ecx>);
int __usercall sub_5CC018@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
void nullsub_431();
HWND __usercall sub_5CC2BC@<eax>(int *a1@<eax>);
int __usercall sub_5CC334@<eax>(int a1@<eax>, unsigned __int8 a2@<dl>, char a3@<cl>);
_DWORD *__usercall sub_5CC3AC@<eax>(_DWORD *result@<eax>, int a2@<edx>);
int __usercall sub_5CC3FC@<eax>(int result@<eax>, char a2@<dl>);
char __usercall sub_5CC4A4@<al>(UINT a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5CC4F0@<al>(int a1@<eax>);
char __usercall sub_5CC520@<al>(int a1@<eax>);
int __usercall sub_5CC550@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5CC570@<eax>(int a1@<eax>);
void __usercall sub_5CC58C(int *a1@<eax>, HDC a2@<edx>);
// attributes: thunk
int __usercall sub_5CC708@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5CC755@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5CC778@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5CC788@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5CC82C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CC89C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CC8C4@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5CC924@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5CC958@<eax>(int a1@<eax>, int a2@<edx>);
_BYTE *__cdecl sub_5CC96C(int a1);
_BYTE *__usercall sub_5CCA68@<eax>(int a1@<eax>);
int __usercall sub_5CCA9C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CCAB4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5CCB40@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CCCE0@<eax>(_DWORD *a1@<eax>, int a2@<edx>, DWORD a3@<ecx>);
int __usercall sub_5CCD30@<eax>(int result@<eax>);
int __usercall sub_5CCD48@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5CCD80@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CCE28@<eax>(int a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_5CCE6C@<eax>(_BYTE *result@<eax>, char a2@<dl>);
// attributes: thunk
int sub_5CCEA4();
int __usercall sub_5CCEAC@<eax>(int a1@<eax>, int a2@<edx>);
LRESULT __usercall sub_5CCEC8@<eax>(LRESULT result@<eax>, int a2@<edx>);
int __usercall sub_5CCF20@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5CCFA8@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_5CD060(int a1@<eax>, int a2@<edx>);
HWND __usercall sub_5CD0B8@<eax>(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5CD0E4@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5CD100@<eax>(int a1@<eax>, int a2);
int __usercall sub_5CD140@<eax>(int a1@<eax>);
volatile __int32 *__userpurge sub_5CD178@<eax>(
        int a1@<eax>,
        _BYTE *a2@<edx>,
        volatile __int32 **a3@<ecx>,
        volatile __int32 *a4);
_DWORD *__usercall sub_5CD1AC@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CD310@<eax>(int a1@<eax>, int a2@<edx>);
signed int __usercall sub_5CD37C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5CD3A8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CD588@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
OLECHAR ***__usercall sub_5CD5DC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<edi>);
int __usercall sub_5CD5E4@<eax>(int a1@<eax>);
int __usercall sub_5CD5FC@<eax>(int a1@<eax>, int a2@<edx>);
void __usercall sub_5CD624(int a1@<eax>);
void __usercall sub_5CD648(int a1@<eax>);
int __usercall sub_5CD66C@<eax>(int *a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5CD708@<eax>(int a1@<eax>);
char __usercall sub_5CDD78@<al>(int a1@<eax>);
// attributes: thunk
_DWORD *__usercall sub_5CDD98@<eax>(_DWORD *a1@<eax>);
LRESULT __usercall sub_5CDDA0@<eax>(int a1@<eax>);
int __usercall sub_5CDDF0@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5CDDF8@<eax>(int result@<eax>, int a2@<edx>);
void __usercall sub_5CDE30(int *a1@<eax>, int a2@<edx>);
int __usercall sub_5CDE5C@<eax>(int a1@<eax>);
int *__usercall sub_5CDE6C@<eax>(int *result@<eax>);
int __usercall sub_5CDF10@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CDF74@<eax>(int *a1@<eax>);
_DWORD *__usercall sub_5CE00C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5CE124@<eax>(int a1@<eax>, void *a2@<ecx>);
_BYTE *__usercall sub_5CE354@<eax>(_BYTE *a1@<eax>);
void __usercall sub_5CE35C(int *a1@<eax>);
_DWORD *__usercall sub_5CE374@<eax>(int *a1@<eax>);
_BYTE *__usercall sub_5CE400@<eax>(int a1@<eax>, int a2@<edx>);
BOOL __usercall sub_5CE430@<eax>(int a1@<eax>);
int __usercall sub_5CE44C@<eax>(int *a1@<eax>, void *a2@<ecx>);
// attributes: thunk
int __usercall sub_5CE756@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5CE778@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5CE795@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
char __usercall sub_5CE7A4@<al>(int a1@<eax>, int a2);
_BYTE *__usercall sub_5CE828@<eax>(_BYTE *result@<eax>);
char __usercall sub_5CE8A0@<al>(int a1@<eax>);
int __usercall sub_5CE8F4@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5CE914@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5CE934@<al>(int *a1@<eax>);
char __usercall sub_5CE964@<al>(int a1@<eax>, int a2);
char __usercall sub_5CE9EC@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5CEA40@<al>(int a1@<eax>);
char __usercall sub_5CEA68@<al>(int a1@<eax>, int a2);
char __usercall sub_5CEAF8@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CEB4C@<eax>(int a1@<eax>, int a2);
int __usercall sub_5CEBC8@<eax>(int a1@<eax>, int a2@<edx>);
int __stdcall sub_5CEC40(int a1, int a2, _DWORD *a3);
void __usercall sub_5CEC7C(int *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
char __usercall sub_5CECB4@<al>(int a1@<eax>, int a2@<ecx>);
char __usercall sub_5CECC4@<al>(int a1@<eax>);
char __usercall sub_5CEDDC@<al>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_BYTE *__usercall sub_5CEE18@<eax>(_BYTE *result@<eax>, int a2@<edx>);
int __usercall sub_5CEE44@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
int __usercall sub_5CEF30@<eax>(int result@<eax>, int a2@<edx>);
int __usercall sub_5CEF6C@<eax>(int result@<eax>, unsigned __int16 a2@<dx>);
int __usercall sub_5CEFB8@<eax>(int a1@<eax>, void *a2@<ecx>);
char __usercall sub_5CF0B0@<al>(int a1@<eax>, int a2);
char __usercall sub_5CF1EC@<al>(int a1@<eax>, void *a2@<ecx>);
int sub_5CF218();
_BYTE *__usercall sub_5CF310@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5CF380@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5CF4B0@<eax>(int a1@<eax>);
int __usercall sub_5CF4D0@<eax>(int a1@<eax>);
bool *__userpurge sub_5CF51C@<eax>(int a1@<eax>, bool *a2, int a3);
int __usercall sub_5CF548@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CF570@<eax>(_BYTE *a1@<eax>, int a2@<edx>, int a3@<ecx>);
void __usercall sub_5CF604(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5CF65C@<eax>(_BYTE *a1@<eax>, int a2@<edx>);
int __usercall sub_5CF784@<eax>(int a1@<eax>, int a2@<edx>);
_BYTE *__usercall sub_5CF79C@<eax>(_BYTE *a1@<eax>, int a2@<ecx>);
int __thiscall sub_5CF7DC(void *this);
int __thiscall sub_5CF7F4(void *this);
int __thiscall sub_5CF810(void *this);
int __thiscall sub_5CF828(void *this);
BOOL __usercall sub_5CF844@<eax>(int a1@<eax>, RECT *a2@<edx>);
BOOL __usercall sub_5CF870@<eax>(int a1@<eax>, RECT *a2@<edx>);
bool __usercall sub_5CF89C@<al>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
int __stdcall sub_5CF8BC(const LOGFONTW *a1, const TEXTMETRICW *a2, DWORD a3, LPARAM a4);
_DWORD *__usercall sub_5CF954@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5CFAF0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int sub_5CFCAC();
int sub_5CFCB4();
int sub_5CFCBC();
int sub_5CFCC4();
int sub_5CFCCC();
int sub_5CFCD4();
int sub_5CFCDC();
int __usercall sub_5CFCF0@<eax>(int a1@<eax>);
int sub_5CFD08();
int __usercall sub_5CFD1C@<eax>(int a1@<eax>);
int sub_5CFD24();
int __usercall sub_5CFD38@<eax>(int a1@<eax>);
int __usercall sub_5CFD40@<eax>(int a1@<eax>, int a2@<ecx>);
char __usercall sub_5CFD8C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CFDC4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CFE1C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CFE28@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5CFE34@<eax>(int a1@<eax>);
HCURSOR __usercall sub_5CFE8C@<eax>(int a1@<eax>);
int __usercall sub_5CFEEC@<eax>(int result@<eax>, int a2@<edx>);
int __cdecl sub_5CFF34(int a1);
int __fastcall sub_5CFF88(int a1, int a2);
volatile signed __int8 **__usercall sub_5CFFB4@<eax>(
        int a1@<eax>,
        volatile signed __int8 *a2@<edx>,
        volatile signed __int8 *a3@<ecx>);
__int64 *__usercall sub_5CFFE0@<eax>(__int64 **a1@<eax>, int a2@<ecx>);
volatile __int32 *__usercall sub_5D0224@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>, int a3@<ecx>);
int __usercall sub_5D0240@<eax>(int a1@<eax>, int a2@<edx>);
int sub_5D0294();
int __usercall sub_5D02A8@<eax>(int a1@<eax>);
int __usercall sub_5D02B0@<eax>(int a1@<eax>, int a2@<edx>);
HCURSOR __usercall sub_5D02DC@<eax>(HCURSOR result@<eax>, __int16 a2@<dx>);
HCURSOR __usercall sub_5D0384@<eax>(
        HCURSOR result@<eax>,
        volatile signed __int8 *a2@<edx>,
        volatile signed __int8 *a3@<ecx>);
int __usercall sub_5D0410@<eax>(_DWORD **a1@<eax>, int a2@<ecx>);
int __usercall sub_5D05D8@<eax>(int result@<eax>);
int __usercall sub_5D05E0@<eax>(int result@<eax>);
int __thiscall sub_5D0600(void *this);
bool __usercall sub_5D0608@<al>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5D0690@<eax>(int a1@<eax>, char a2@<dl>, int a3);
int __usercall sub_5D0848@<eax>(char a1@<al>, int a2);
int __usercall sub_5D0998@<eax>(int a1@<ebx>, int a2);
_DWORD *__usercall sub_5D09F0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<ebx>);
int __usercall sub_5D0A78@<eax>(int a1@<eax>, int a2@<edx>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_5D0AFC@<eax>(int a1@<eax>, int a2@<ecx>);
// attributes: thunk
int __usercall sub_5D0BA0@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
_DWORD *__usercall sub_5D0BD0@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_5D0BEC@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_5D0C24@<eax>(int result@<eax>);
int __stdcall sub_5D0C44(int a1, int a2, int a3, int a4);
DWORD __stdcall sub_5D0C98(int a1);
LRESULT __stdcall sub_5D0CF4(int nCode, WPARAM wParam, LPARAM lParam);
HHOOK __thiscall sub_5D0D38(void *this);
void *sub_5D0DAC();
BOOL sub_5D0E30();
BOOL __usercall sub_5D0E60@<eax>(char a1@<al>);
BOOL __usercall sub_5D0E8C@<eax>(HWND a1@<eax>, int a2@<edx>);
int __fastcall sub_5D0EBC(int a1, _DWORD *a2);
int sub_5D0EEC();
int sub_5D0F08();
BOOL __fastcall sub_5D0F20(int a1, void *a2);
int __thiscall sub_5D0F30(void *this);
int __thiscall sub_5D0F48(void *this);
int __fastcall sub_5D0F64(unsigned __int8 a1, POINT *a2);
int __fastcall sub_5D0F90(unsigned __int8 a1, const RECT *a2);
int __fastcall sub_5D0FB8(unsigned __int8 a1, HWND a2);
int __usercall sub_5D0FE0@<eax>(int a1@<eax>);
BOOL __usercall sub_5D1018@<eax>(int a1@<eax>);
int __cdecl sub_5D1038(int a1);
int __usercall sub_5D1088@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_5D10C8@<eax>(int *a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5D1120@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5D1184@<eax>(__int32 *a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_5D1198@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
HKL __usercall sub_5D11AC@<eax>(HKL result@<eax>);
HKL __usercall sub_5D11BC@<eax>(HKL result@<eax>);
int __usercall sub_5D11CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
void __usercall sub_5D1440(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5D1610@<eax>(int a1@<eax>);
int __usercall sub_5D1828@<eax>(_DWORD *a1@<eax>, int a2@<edx>);
BOOL __stdcall sub_5D1890(HWND hWnd, LPARAM a2);
HWND __usercall sub_5D1954@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5D19FC@<eax>(int result@<eax>, int a2@<ecx>);
int __usercall sub_5D1A28@<eax>(int result@<eax>, int a2@<ecx>);
HWND __usercall sub_5D1A54@<eax>(_DWORD *a1@<eax>);
HWND __usercall sub_5D1A5C@<eax>(_DWORD *a1@<eax>);
int __usercall sub_5D1A64@<eax>(int result@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5D1ABC@<eax>(_DWORD *result@<eax>);
BOOL __stdcall sub_5D1B28(HWND hWnd, HWND a2);
OLECHAR ***__usercall sub_5D1C34@<eax>(int a1@<eax>, char a2@<dl>);
bool __usercall sub_5D1DB4@<al>(int a1@<eax>);
bool __usercall sub_5D1DCC@<al>(int a1@<eax>);
bool __usercall sub_5D1DE4@<al>(int a1@<eax>);
bool __usercall sub_5D1DFC@<al>(int a1@<eax>);
int __usercall sub_5D1E18@<eax>(int result@<eax>);
int __usercall sub_5D1E20@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5D1EA0@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
LRESULT __cdecl sub_5D1F1C(int a1);
BOOL __cdecl sub_5D1F5C(int a1);
int __usercall sub_5D1FAC@<eax>(_DWORD *a1@<eax>, int *a2@<edx>, int a3@<ecx>);
HICON __usercall sub_5D275C@<eax>(int a1@<eax>);
_BYTE *__usercall sub_5D2778@<eax>(int a1@<eax>);
HWND __usercall sub_5D287C@<eax>(int a1@<eax>);
HWND __usercall sub_5D29B0@<eax>(int a1@<eax>);
volatile __int32 *__usercall sub_5D2A08@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_5D2A88@<eax>(int result@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5D2AC8@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_5D2B24@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
volatile __int32 *__usercall sub_5D2B80@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5D2B8C@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5D2BA4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D2C04@<eax>(int result@<eax>, int a2@<edx>);
BOOL __usercall sub_5D2C4C@<eax>(int a1@<eax>, struct tagMSG *a2@<edx>);
BOOL __usercall sub_5D2C94@<eax>(int a1@<eax>, struct tagMSG *a2@<edx>);
int __usercall sub_5D2CE4@<eax>(int a1@<eax>, HWND *a2@<edx>);
int __usercall sub_5D2DDC@<eax>(int a1@<eax>);
int __usercall sub_5D2E10@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_BYTE *__usercall sub_5D2E7C@<eax>(int a1@<eax>, UINT *a2@<edx>);
int __usercall sub_5D2F48@<eax>(int a1@<eax>, struct tagMSG *a2@<edx>, int a3@<ecx>);
int __usercall sub_5D305C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5D3074@<eax>(int a1@<eax>, int a2@<ecx>);
HWND __userpurge sub_5D3098@<eax>(int a1@<eax>, volatile signed __int8 *lParam, volatile signed __int8 *a3);
__int64 *__userpurge sub_5D30F8@<eax>(int a1@<eax>, LPARAM lParam, int a3);
void *sub_5D3174();
char __usercall sub_5D318C@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5D32E8@<eax>(int a1@<eax>);
void __usercall sub_5D3408(int a1@<ebx>);
int __usercall sub_5D341C@<eax>(int *a1@<eax>, int a2@<ecx>);
OLECHAR ***__usercall sub_5D34A0@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_5D3524@<eax>(int a1@<eax>, const WCHAR *a2@<edx>, const WCHAR *a3@<ecx>, UINT uType);
// attributes: thunk
int __usercall sub_5D368F@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5D36A4@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D3778@<eax>(int a1@<eax>, int a2@<edx>, LPARAM a3@<ecx>);
int __userpurge sub_5D38AC@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>, int a3@<ecx>, _BYTE *a4);
int __usercall sub_5D3978@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D3A08@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5D3A90@<eax>(LPARAM a1@<ecx>, int a2@<edx>, int a3@<eax>);
int __usercall sub_5D3A98@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D3B28@<eax>(int a1@<eax>);
__int16 *__fastcall sub_5D3B94(int a1, int *a2);
int __usercall sub_5D3BA4@<eax>(int result@<eax>, int a2@<edx>);
char sub_5D3C2C();
HANDLE __usercall sub_5D3C90@<eax>(int a1@<eax>);
int __stdcall sub_5D3CB4(int a1, int a2, int a3, int a4);
int __usercall sub_5D3D1C@<eax>(int a1@<eax>);
int __usercall sub_5D3E94@<eax>(int a1@<eax>);
int __fastcall sub_5D3EBC(int a1, unsigned __int16 a2, int a3);
int __usercall sub_5D3F04@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5D3F78@<eax>(int a1@<eax>, int a2@<edx>);
BOOL __usercall sub_5D400C@<eax>(unsigned __int8 a1@<al>, int a2);
BOOL __usercall sub_5D40B4@<eax>(BOOL result@<eax>);
bool __usercall sub_5D413C@<al>(int a1@<eax>);
UINT_PTR __usercall sub_5D415C@<eax>(int a1@<eax>, UINT a2@<edx>, char a3@<cl>);
UINT_PTR __usercall sub_5D419C@<eax>(int a1@<eax>);
char __usercall sub_5D41BC@<al>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5D42EC@<eax>(int a1@<eax>);
char __usercall sub_5D4324@<al>(int a1@<eax>);
UINT_PTR __usercall sub_5D4398@<eax>(int a1@<eax>);
int __usercall sub_5D43CC@<eax>(_BYTE *a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>);
int sub_5D43DC();
char __usercall sub_5D4530@<al>(int (**a1)()@<eax>, int a2);
int __usercall sub_5D4588@<eax>(unsigned __int16 *a1@<eax>, int a2);
int __usercall sub_5D4668@<eax>(int a1@<eax>, POINT *a2@<edx>);
HKL __usercall sub_5D4A20@<eax>(int a1@<eax>);
HKL __usercall sub_5D4A2C@<eax>(int a1@<eax>);
int __usercall sub_5D4A38@<eax>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__usercall sub_5D4B1C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
LRESULT __usercall sub_5D4B80@<eax>(LRESULT result@<eax>, LPARAM a2@<edx>);
HWND __usercall sub_5D4BAC@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5D4BF8@<eax>(int a1@<eax>, int a2@<ecx>);
BOOL __usercall sub_5D4C38@<eax>(int a1@<eax>, int a2@<edx>, _BYTE *a3@<ecx>);
int __usercall sub_5D4CD0@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5D4CF8@<eax>(int a1@<eax>, int a2@<ecx>);
HMODULE sub_5D4D20();
int __usercall sub_5D4DA8@<eax>(int result@<eax>);
_DWORD *sub_5D4DB8();
int __usercall sub_5D4DC8@<eax>(int a1@<eax>, HWND *a2@<edx>);
HWND __usercall sub_5D4E34@<eax>(int a1@<eax>);
int __usercall sub_5D4EBC@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5D5014@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5D5068@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5D50C0@<al>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_5D511C@<al>(int a1@<eax>, void *a2@<ecx>);
int __usercall sub_5D5164@<eax>(int a1@<eax>, _DWORD *a2@<edx>, void *a3@<ecx>);
int __usercall sub_5D5248@<eax>(int result@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5D5278@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5D52FC@<al>(_DWORD *a1@<eax>, int *a2@<edx>, _DWORD *a3@<ecx>);
int __usercall sub_5D5360@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5D5464@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5D54A8@<eax>(int a1@<eax>);
int __usercall sub_5D54C0@<eax>(int a1@<eax>);
bool sub_5D55D4();
bool sub_5D5618();
int __usercall sub_5D5648@<eax>(int result@<eax>, char a2@<dl>);
int __usercall sub_5D56A0@<eax>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5D56D8@<al>(int a1@<eax>, int a2@<edx>);
bool __fastcall sub_5D56FC(int a1, int a2);
int sub_5D5718();
int __usercall sub_5D5738@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5D576C@<eax>(int a1@<eax>);
int __usercall sub_5D5808@<eax>(int a1@<eax>, unsigned __int16 a2@<dx>);
void __usercall sub_5D589C(int a1@<eax>, char a2@<dl>);
int __usercall sub_5D5BD0@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5D5C24@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5D5C6C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5D5CE4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5D5E70@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5D5FE4@<eax>(_DWORD *a1@<eax>, const void *a2@<edx>, POINT *a3@<ecx>);
HHOOK __usercall sub_5D6100@<eax>(int a1@<eax>);
int __usercall sub_5D6140@<eax>(int a1@<eax>);
int __usercall sub_5D6174@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
HANDLE sub_5D61BC();
HANDLE sub_5D61F8();
HANDLE sub_5D6234();
int __usercall sub_5D6270@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5D62C4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5D6344@<eax>(int a1@<eax>);
int sub_5D6350();
int __usercall sub_5D6378@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5D6408@<eax>(int a1@<eax>, int a2);
int __usercall sub_5D645C@<eax>(int a1@<eax>, int a2@<edx>, int a3);
int __usercall sub_5D6608@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_5D67E8(_DWORD *a1, int a2);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_5D68A0@<eax>(
        int (__usercall *a1)@<eax>(unsigned int@<ebp>, _DWORD *, int)@<eax>,
        const void *a2@<edx>,
        struct _EXCEPTION_REGISTRATION_RECORD *a3@<ecx>);
// attributes: thunk
int __usercall sub_5D69A0@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5D6B78@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5D6C08@<eax>(int a1@<eax>, int a2);
int __usercall sub_5D6C5C@<eax>(int a1@<eax>, int a2@<edx>, int a3);
bool __usercall sub_5D6E08@<al>(HMENU a1@<eax>, int a2@<edx>, int a3);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_5D6E70@<eax>(int a1@<eax>, unsigned int a2@<edx>);
// attributes: thunk
int __usercall sub_5D6FF5@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5D75AD@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
LRESULT __stdcall sub_5D75BC(int code, WPARAM wParam, LPARAM lParam);
_DWORD *__usercall sub_5D7B54@<eax>(_DWORD *result@<eax>, _DWORD *a2@<edx>);
HANDLE __usercall sub_5D7B64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5D7C44@<al>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5D7CF4@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_BYTE *__usercall sub_5D7E44@<eax>(int a1@<eax>);
int __usercall sub_5D7F48@<eax>(int a1@<eax>);
int __usercall sub_5D8034@<eax>(int a1@<eax>);
int __usercall sub_5D81A8@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5D82C8@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
bool sub_5D83E8();
void nullsub_436();
int __usercall sub_5D8414@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D84C4@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_5D8574@<eax>(int result@<eax>, char a2@<cl>, int a3);
int __userpurge sub_5D85C0@<eax>(int result@<eax>, char a2@<cl>, int a3);
bool sub_5D860C();
char __usercall sub_5D863C@<al>(int a1@<eax>, unsigned __int8 a2@<dl>);
int *__usercall sub_5D8C7C@<eax>(int *result@<eax>);
int __usercall sub_5D8DDC@<eax>(int *a1@<eax>, int a2@<ecx>);
char __usercall sub_5D8FFC@<al>(int a1@<eax>, struct tagRECT *a2@<edx>);
HANDLE __usercall sub_5D9058@<eax>(int a1@<eax>, UINT *a2@<edx>);
int __usercall sub_5D914C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5D91B4@<eax>(_DWORD *a1@<edx>, int a2@<ebx>);
int __usercall sub_5D9354@<eax>(int a1@<eax>);
int __usercall sub_5D9358@<eax>(LPPOINT lpPoint@<ecx>, _DWORD *a2@<eax>, LONG *a3@<edx>);
int __usercall sub_5D94B0@<eax>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5D9818@<eax>(int result@<eax>, int a2@<edx>);
char __usercall sub_5D985C@<al>(int a1@<eax>);
int __cdecl sub_5D988C(int a1);
char __usercall sub_5D9918@<al>(_DWORD *a1@<eax>, int a2@<edx>);
BOOL __usercall sub_5D9998@<eax>(BOOL result@<eax>);
char __usercall sub_5D99C8@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5D9A74@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5D9AAC@<al>(int a1@<eax>);
char __usercall sub_5D9AE4@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5D9B2C@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5D9CD8@<eax>(int a1@<eax>);
int __usercall sub_5D9CF0@<eax>(int a1@<eax>);
int __cdecl sub_5D9DF4(int a1);
char __usercall sub_5D9E90@<al>(int a1@<ebx>, int a2);
char __usercall sub_5D9F2C@<al>(int a1@<ebx>, int a2);
bool __usercall sub_5D9FC4@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
char __cdecl sub_5DA004(int a1);
_DWORD *__usercall sub_5DA24C@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
char __usercall sub_5DAE84@<al>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5DAF8C@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5DB00C@<eax>(int a1@<eax>, int a2@<ebx>);
// attributes: thunk
int __usercall sub_5DB0C5@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5DB11D@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
LRESULT __usercall sub_5DB128@<eax>(int a1@<eax>);
char __usercall sub_5DB160@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DB1E8@<al>(int a1@<eax>);
char __usercall sub_5DB2A8@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DB4B4@<al>(_DWORD *a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5DB528@<eax>(int a1@<eax>);
char __usercall sub_5DB550@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DB630@<al>(int a1@<eax>, int a2@<edx>);
void __usercall sub_5DB664(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DB784@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DB7D8@<al>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5DB970@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5DB9C0@<eax>(int a1@<eax>);
int __usercall sub_5DB9D4@<eax>(_DWORD *a1@<eax>);
bool __usercall sub_5DBA18@<al>(int a1@<eax>, int a2@<edx>);
char __usercall sub_5DBA44@<al>(_BYTE *a1@<eax>);
LRESULT __usercall sub_5DBA60@<eax>(int a1@<eax>);
LRESULT __usercall sub_5DBA8C@<eax>(int a1@<eax>);
int __usercall sub_5DBAC4@<eax>(int a1@<eax>);
int __usercall sub_5DBB28@<eax>(int a1@<eax>);
LRESULT __usercall sub_5DBB8C@<eax>(int a1@<eax>);
int __usercall sub_5DBBAC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
char __usercall sub_5DBCBC@<al>(int a1@<eax>, int a2@<edx>);
int __thiscall sub_5DBD0C(void *this);
_DWORD *sub_5DBD44();
int __usercall sub_5DBD58@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5DBD64@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5DBD70@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5DBD78@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5DBD84@<eax>(_DWORD *result@<eax>, char a2@<dl>);
_DWORD *__userpurge sub_5DBDA4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, int a6, int a7);
_DWORD *__userpurge sub_5DBDD8@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, int a6, int a7);
_DWORD *__userpurge sub_5DBE0C@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, int a6, int a7);
_DWORD *__userpurge sub_5DBE40@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, char a5, int a6, int a7);
unsigned __int8 *__usercall sub_5DBE74@<eax>(unsigned __int8 *result@<eax>, _DWORD *a2@<edx>, unsigned int a3@<ecx>);
_BYTE *__usercall sub_5DBEA8@<eax>(_BYTE *a1@<eax>, _BYTE *a2@<edx>, int a3@<ecx>);
int *__usercall sub_5DBEE8@<eax>(unsigned __int8 *a1@<eax>, int *a2@<edx>);
int __usercall sub_5DC618@<eax>(int a1@<eax>);
__int64 *__usercall sub_5DC650@<eax>(int a1@<eax>, __int64 *a2@<edx>, unsigned int a3@<ecx>);
int __usercall sub_5DC6D8@<eax>(_BYTE *a1@<eax>, _BYTE *a2@<edx>);
_DWORD *__usercall sub_5DC750@<eax>(int a1@<eax>, _BYTE *a2@<edx>);
int __usercall sub_5DC7C8@<eax>(_DWORD *a1@<eax>, __int64 **a2@<edx>);
_DWORD *__usercall sub_5DCBBC@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3@<ecx>);
int __fastcall sub_5DCFB8(OLECHAR ***a1, int a2, int a3, int a4);
int __fastcall sub_5DD048(int a1, int a2, int a3, int a4);
__int64 __fastcall sub_5DD088(int a1, int a2, int a3, int a4);
int nullsub_437();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_438(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_439@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_440@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int __usercall sub_5DF6B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5DF750@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5DF7BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5DF830@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5DF8CC@<eax>(int (__thiscall ***a1)(_DWORD)@<eax>, int a2@<edx>);
int __userpurge sub_5DF8E8@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5DF924@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>);
int __userpurge sub_5DF954@<eax>(int (__fastcall ***a1)(int, int)@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_5DF990@<eax>(int a1@<eax>, int a2@<edx>, OLECHAR ***a3@<ecx>);
int __userpurge sub_5DF9CC@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        OLECHAR ***a4,
        int a5);
int __fastcall sub_5DFA3C(int a1, int a2, int a3, int a4, int a5);
int __userpurge sub_5DFA74@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, OLECHAR ***a5);
int __userpurge sub_5DFAD8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int *a5);
int __usercall sub_5DFBAC@<eax>(
        int (__fastcall ***a1)(int, int)@<eax>,
        int a2@<edx>,
        OLECHAR ***a3@<ecx>,
        int a4@<edi>);
int __userpurge sub_5DFC18@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, OLECHAR ***a4, int a5);
int __userpurge sub_5DFC88@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int *a5, int a6);
int __usercall sub_5DFCCC@<eax>(int a1@<eax>, int a2@<edx>);
int __userpurge sub_5DFCE8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
OLECHAR ***__usercall sub_5DFD24@<eax>(int a1@<eax>, int a2@<edx>, OLECHAR ***a3@<ecx>);
int __userpurge sub_5DFD60@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, OLECHAR ***a4, int a5);
int __fastcall sub_5DFDD0(int a1, int a2, int a3, int a4, int a5);
int __userpurge sub_5DFE14@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, volatile signed __int8 ***a4);
int __userpurge sub_5DFE6C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int *a5);
OLECHAR ***__usercall sub_5DFF7C@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
_DWORD *__fastcall sub_5DFF90(_DWORD *a1, int a2);
int __userpurge sub_5DFFC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4, int a5);
int __userpurge sub_5E0024@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4);
_DWORD *__usercall sub_5E007C@<eax>(int a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5E00BC@<eax>(int a1@<eax>, char a2@<dl>);
UINT *__userpurge sub_5E0100@<eax>(UINT *a1@<eax>, char a2@<dl>, UINT a3@<ecx>, UINT a4, UINT a5);
int __usercall sub_5E01D8@<eax>(int cchWideChar@<ecx>, int a2@<eax>, const WCHAR *a3@<edx>);
int __userpurge sub_5E01F0@<eax>(
        int cchWideChar@<ecx>,
        int a2@<eax>,
        const WCHAR *a3@<edx>,
        int cbMultiByte,
        LPSTR lpMultiByteStr);
int __usercall sub_5E0214@<eax>(int cbMultiByte@<ecx>, int a2@<eax>, const CHAR *a3@<edx>);
int __userpurge sub_5E0228@<eax>(
        int cbMultiByte@<ecx>,
        int a2@<eax>,
        const CHAR *a3@<edx>,
        int cchWideChar,
        LPWSTR lpWideCharStr);
int __usercall sub_5E0248@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_5E0250(int a1, int a2);
volatile signed __int8 **__usercall sub_5E0254@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>, int a3@<edi>);
_DWORD *__usercall sub_5E02EC@<eax>(int a1@<eax>, char a2@<dl>);
// attributes: thunk
int __usercall sub_5E0328@<eax>(int a1@<eax>, const WCHAR *a2@<edx>, int a3@<ecx>);
int __userpurge sub_5E0330@<eax>(
        int a1@<eax>,
        const WCHAR *a2@<edx>,
        int a3@<ecx>,
        int cbMultiByte,
        LPSTR lpMultiByteStr);
// attributes: thunk
int __usercall sub_5E0348@<eax>(int a1@<eax>, const CHAR *a2@<edx>, int a3@<ecx>);
int __userpurge sub_5E0350@<eax>(
        int a1@<eax>,
        const CHAR *a2@<edx>,
        int a3@<ecx>,
        int cchWideChar,
        LPWSTR lpWideCharStr);
int __fastcall sub_5E0368(int a1, int a2);
int __fastcall sub_5E0370(int a1, int a2);
UINT *__usercall sub_5E0374@<eax>(UINT *a1@<eax>, char a2@<dl>);
int __fastcall sub_5E03B4(int a1, int a2);
int __fastcall sub_5E03BC(int a1, int a2);
volatile signed __int8 **__fastcall sub_5E03C0(int a1, volatile signed __int8 ***a2);
_DWORD *__usercall sub_5E03F0@<eax>(_DWORD *result@<eax>, char a2@<dl>);
int __fastcall sub_5E041C(int a1);
int __fastcall sub_5E0424(int a1, __int64 *a2, int a3, __int64 *a4);
int __fastcall sub_5E0440(int a1);
int __fastcall sub_5E044C(int a1, __int64 *a2, int a3, __int64 *a4);
int __fastcall sub_5E0470(int a1, int a2);
int __fastcall sub_5E0478(int a1, int a2);
volatile signed __int8 **__fastcall sub_5E0488(int a1, volatile signed __int8 ***a2);
int __fastcall sub_5E04B0(int a1, _WORD *a2, int a3, _BYTE *a4);
int __fastcall sub_5E04E8(int a1, _BYTE *a2, int a3, _WORD *a4);
volatile signed __int8 **__fastcall sub_5E0534(int a1, volatile signed __int8 ***a2);
_DWORD *__usercall sub_5E055C@<eax>(_DWORD *result@<eax>, char a2@<dl>);
void *__thiscall sub_5E0588(void *this);
int __fastcall sub_5E058C(int a1, _BYTE *a2, int a3, _BYTE *a4);
void *__thiscall sub_5E05D0(void *this);
int __fastcall sub_5E05D4(int a1, _BYTE *a2, int a3, _WORD *a4);
int __fastcall sub_5E0620(int a1, int a2);
int __fastcall sub_5E0624(int a1, int a2);
_DWORD *__usercall sub_5E0628@<eax>(_DWORD *result@<eax>, char a2@<dl>);
void *__thiscall sub_5E0654(void *this);
int __fastcall sub_5E0658(int a1, _BYTE *a2, int a3, _BYTE *a4);
void *__thiscall sub_5E069C(void *this);
int __fastcall sub_5E06A0(int a1, unsigned __int8 *a2, int a3, _WORD *a4);
int __fastcall sub_5E06D8(int a1, int a2);
int __fastcall sub_5E06DC(int a1, int a2);
int __usercall sub_5E075C@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5E077C@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E0814@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E08AC@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E0944@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E09DC@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E0A74@<eax>(_DWORD *a1@<eax>);
_DWORD *__usercall sub_5E0B0C@<eax>(_DWORD *a1@<eax>);
// attributes: thunk
int sub_5E0BA4();
__int32 __usercall sub_5E0BAC@<eax>(volatile __int32 *a1@<eax>, __int32 a2@<edx>);
_DWORD *__userpurge sub_5E0BBC@<eax>(
        volatile signed __int32 *a1@<eax>,
        signed __int32 a2@<edx>,
        signed __int32 a3@<ecx>,
        _DWORD *a4);
void nullsub_85();
_DWORD *__usercall sub_5E0C10@<eax>(_DWORD *result@<eax>, int a2@<edx>, char a3@<cl>);
volatile signed __int8 *__userpurge sub_5E0C28@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, __int64 **a4);
__int64 *__userpurge sub_5E0CD4@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5);
__int16 __usercall sub_5E0CF0@<ax>(__int16 result@<ax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_5E0CF8@<eax>(int result@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
_DWORD *__userpurge sub_5E0D00@<eax>(int *a1@<eax>, int a2@<edx>, char a3@<cl>, __int64 **a4, char a5);
int __userpurge sub_5E0DBC@<eax>(
        int *a1@<eax>,
        int a2@<edx>,
        char a3@<cl>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        __int64 **a7);
int __usercall sub_5E0EAC@<eax>(char a1@<al>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5E0EB8@<eax>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
_DWORD *__usercall sub_5E1470@<eax>(int a1@<eax>);
int __usercall sub_5E14EC@<eax>(
        __int32 a1@<eax>,
        _WORD *a2@<edx>,
        bool *a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>);
int __usercall sub_5E1628@<eax>(int result@<eax>, int a2@<edx>);
__int64 __stdcall sub_5E1630(__int64 a1, __int64 a2);
unsigned int __usercall sub_5E1670@<eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5E167C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5E1684@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
OLECHAR **__fastcall sub_5E1824(void *a1, int a2, int a3);
unsigned __int8 __usercall sub_5E1EC0@<al>(__int32 a1@<eax>, volatile __int32 *a2@<edx>);
int __usercall sub_5E1ED4@<eax>(__int32 a1@<eax>);
int __usercall sub_5E1F24@<eax>(__int32 a1@<eax>, int a2@<edx>);
_DWORD *__userpurge sub_5E1F78@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, OLECHAR ***a5, int a6);
int __usercall sub_5E205C@<eax>(int a1@<eax>, int a2@<edx>);
__int64 __userpurge sub_5E2064@<edx:eax>(int a1@<eax>, OLECHAR ***a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_5E209C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__thiscall sub_5E20B8(void *this);
_DWORD *__userpurge sub_5E2110@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
bool __usercall sub_5E21D4@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5E21EC@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5E2240@<al>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
bool __usercall sub_5E22A8@<al>(int a1@<eax>);
int sub_5E22B0();
int sub_5E22B8();
int sub_5E22C0();
bool __usercall sub_5E22C8@<al>(int a1@<eax>, int a2@<edx>);
int sub_5E22F4();
int sub_5E237C();
int sub_5E2380();
int sub_5E2384();
int sub_5E2388();
int sub_5E238C();
void nullsub_441();
OLECHAR ***__usercall sub_5E2394@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
int sub_5E23A8();
int sub_5E23AC();
int sub_5E23B0();
void nullsub_442();
OLECHAR ***__usercall sub_5E23B8@<eax>(OLECHAR ***a1@<edx>, int a2@<edi>);
void sub_5E23CC();
HMODULE sub_5E2620();
bool sub_5E2628();
_DWORD *sub_5E2634();
int sub_5E2764();
int __userpurge sub_5E27A4@<eax>(int a1@<eax>, char a2@<dl>, DWORD a3@<ecx>, void *a4, int a5, int a6);
int __usercall sub_5E28B0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __stdcall sub_5E294C(unsigned __int16 a1, int a2);
int sub_5E2AB0();
int __stdcall sub_5E2C08(int a1, int a2, int a3);
int __stdcall sub_5E2D58(int a1, int a2, int a3);
int __stdcall sub_5E2E9C(int a1);
int __stdcall sub_5E2FFC(int a1, int a2, int a3);
int __stdcall sub_5E314C(int a1, int a2, int a3);
int __stdcall sub_5E32B4(int a1, int a2, int a3);
int __stdcall sub_5E341C(int a1, int a2, int a3);
int __stdcall sub_5E3584(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E36F4(int a1);
int __stdcall sub_5E3830(unsigned __int16 a1);
int __stdcall sub_5E396C(int a1);
int __stdcall sub_5E3AC0(int a1);
int __stdcall sub_5E3C10(int a1, int a2);
int __stdcall sub_5E3D5C(int a1);
int __stdcall sub_5E3E98(unsigned __int16 a1);
int __stdcall sub_5E3FD4(int a1, int a2, int a3, int a4);
int __stdcall sub_5E411C(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E4284(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E43DC(int a1, int a2, int a3, int a4);
int __stdcall sub_5E4524(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E4680(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E47F0(int a1, int a2);
int __stdcall sub_5E4948(int a1, int a2, int a3);
int __stdcall sub_5E4A98(int a1, int a2, int a3);
int __stdcall sub_5E4C0C(int a1);
int __stdcall sub_5E4D78(int a1, int a2);
int __stdcall sub_5E4EDC(int a1, int a2);
int __stdcall sub_5E504C(int a1, int a2);
int __stdcall sub_5E51BC(int a1);
int __stdcall sub_5E5340(int a1);
_DWORD *__stdcall sub_5E54B8(int a1);
int sub_5E5628();
int sub_5E5798();
int sub_5E58FC();
int __stdcall sub_5E5A90(int a1);
int sub_5E5C20();
int __stdcall sub_5E5DB4(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E5F64(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E6114(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E62CC(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E6490(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E663C(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __stdcall sub_5E67F0(int a1);
int __stdcall sub_5E698C(int a1, int a2, int a3, int a4);
int __stdcall sub_5E6B10(int a1, int a2);
int __stdcall sub_5E6C80(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E6DE4(int a1);
int __stdcall sub_5E6F50(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int sub_5E70C8();
int __stdcall sub_5E7238(int a1, int a2, int a3);
int __stdcall sub_5E73D0(int a1, int a2, int a3);
int __stdcall sub_5E7568(int a1, int a2, int a3);
int __stdcall sub_5E7700(int a1, int a2, int a3);
int __stdcall sub_5E78A4(int a1, int a2, int a3);
int __stdcall sub_5E7A30(int a1, int a2, int a3);
int __stdcall sub_5E7BBC(int a1, int a2, int a3);
int __stdcall sub_5E7D48(int a1, int a2, int a3);
int __stdcall sub_5E7EC8(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E8080(int a1, int a2, int a3);
int __stdcall sub_5E8200(int a1, int a2, int a3);
int __stdcall sub_5E835C(int a1, unsigned __int16 a2, int a3);
int __stdcall sub_5E84B8(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9);
int __stdcall sub_5E862C(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8);
int __stdcall sub_5E87A8(int a1, int a2, int a3);
int __stdcall sub_5E8904(int a1, unsigned __int16 a2, int a3);
int __stdcall sub_5E8A60(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __stdcall sub_5E8BC0(int a1, int a2);
int __stdcall sub_5E8D48(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9);
int __stdcall sub_5E8EC8(int a1);
int __stdcall sub_5E9034(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __stdcall sub_5E9194(int a1, int a2);
int __stdcall sub_5E931C(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8, int a9);
int __stdcall sub_5E9490(int a1);
int __stdcall sub_5E95F0(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E9764(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E98D8(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5E9A4C(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E9C10(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E9DB0(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5E9F50(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5EA0F0(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5EA290(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5EA430(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5EA5D0(int a1, int a2, int a3);
int __stdcall sub_5EA780(int a1, int a2, int a3);
int __stdcall sub_5EA930(int a1, int a2, int a3);
int __stdcall sub_5EAAE0(int a1, int a2, int a3, int a4);
int __stdcall sub_5EAC88(int a1, int a2, int a3, int a4);
int __stdcall sub_5EAE30(int a1, int a2, int a3, int a4);
int __stdcall sub_5EAFD8(int a1);
int __stdcall sub_5EB168(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8);
int __stdcall sub_5EB2E4(int a1);
int __stdcall sub_5EB48C(int a1);
int __stdcall sub_5EB634(int a1);
int __stdcall sub_5EB7DC(int a1);
int __stdcall sub_5EB978(int a1, int a2, int a3, int a4);
int __stdcall sub_5EBB2C(int a1, int a2, int a3, int a4);
int __stdcall sub_5EBCE0(int a1, int a2, int a3, int a4);
int __stdcall sub_5EBE94(int a1, int a2);
int __stdcall sub_5EC058(int a1, int a2);
int __stdcall sub_5EC21C(int a1, int a2);
int __stdcall sub_5EC3E0(int a1, int a2, int a3);
int __stdcall sub_5EC5CC(int a1, int a2, int a3);
int __stdcall sub_5EC7B8(int a1, int a2, int a3);
int __stdcall sub_5EC9A4(int a1, int a2, int a3);
int __stdcall sub_5ECB24(int a1, int a2, int a3);
int __stdcall sub_5ECCA4(int a1, int a2, int a3);
int __stdcall sub_5ECE24(int a1, int a2, int a3);
int __stdcall sub_5ECFD4(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __stdcall sub_5ED040(int a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge sub_5ED0F4@<eax>(int a1@<ebx>, int a2, int a3, int a4, int a5);
int __stdcall sub_5ED2FC(int a1, int a2, int a3, int a4, int a5, int a6, int a7);
int __stdcall sub_5ED360(int a1, int a2, int a3, int a4);
int __stdcall sub_5ED3C0(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5ED420(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5ED48C(int a1, int a2, int a3, int a4, int a5, int a6);
int __stdcall sub_5ED4F0(int *a1, int a2, int a3);
void sub_5ED540();
BOOL __usercall sub_5ED9E8@<eax>(int a1@<eax>, int a2@<edx>);
_DWORD *__usercall sub_5EDA00@<eax>(_DWORD *result@<eax>);
void sub_5EDA08();
int __usercall sub_5EDA18@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5EDA5C@<eax>(int a1@<eax>);
int __usercall sub_5EDA60@<eax>(int a1@<eax>);
int __usercall sub_5EDA64@<eax>(int a1@<eax>);
void sub_5EDA80();
int __usercall sub_5EDA88@<eax>(int a1@<eax>);
int sub_5EDB20();
volatile signed __int8 **__usercall sub_5EDBB0@<eax>(int a1@<eax>);
// attributes: thunk
int __usercall sub_5EDBF8@<eax>(int a1@<eax>);
__int64 *__stdcall sub_5EDC00(__int64 *a1);
int __stdcall sub_5EDC44(int a1, int *a2);
volatile signed __int8 **__stdcall sub_5EDCD8(
        volatile signed __int8 *a1,
        volatile signed __int8 *a2,
        __int16 a3,
        volatile signed __int8 *a4);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge sub_5EDD40@<eax>(
        int a1@<ebx>,
        int a2@<edi>,
        int a3@<esi>,
        int a4,
        volatile signed __int8 *a5,
        volatile signed __int8 *a6,
        __int16 a7,
        __int64 *a8,
        volatile signed __int8 ***a9);
int __userpurge sub_5EDE7C@<eax>(
        int a1@<eax>,
        int a2@<ebx>,
        int a3@<edi>,
        __int64 *a4,
        volatile signed __int8 *a5,
        volatile signed __int8 *a6,
        __int16 a7,
        int a8,
        volatile signed __int8 ***a9);
int __stdcall sub_5EDF84(__int16 a1, volatile signed __int8 *a2);
int __stdcall sub_5EDFD4(int *a1);
int __stdcall sub_5EE018(__int64 *a1, int a2, int *a3, volatile signed __int8 ***a4);
int __stdcall sub_5EE3A8(int a1, unsigned int a2, __int64 *a3, unsigned int a4, __int64 *a5, unsigned int a6, char a7);
HMODULE sub_5EE68C();
int sub_5EEA8C();
int __userpurge sub_5EF9DC@<eax>(int a1@<eax>, unsigned __int8 *a2@<edx>, char a3@<cl>, __int64 **a4);
_DWORD *__userpurge sub_5EFB48@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4);
int __userpurge sub_5EFCB0@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, unsigned __int8 a4, unsigned __int8 a5);
_DWORD *__usercall sub_5EFCF4@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5EFD30@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
int __userpurge sub_5EFD68@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __userpurge sub_5EFDBC@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>, int a4, int a5, int a6);
int __userpurge sub_5EFE0C@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        unsigned __int8 a4,
        unsigned __int16 a5,
        int a6,
        int a7,
        int a8);
_DWORD *__userpurge sub_5EFE84@<eax>(int a1@<eax>, _DWORD *a2, int a3);
int __userpurge sub_5EFEB8@<eax>(int a1@<eax>, char a2, int a3);
int __stdcall sub_5EFED4(char a1, int a2);
int __stdcall sub_5EFF14(char a1, int a2);
int __userpurge sub_5EFF54@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>, char a4);
int __userpurge sub_5EFFAC@<eax>(int a1@<eax>, int a2@<edx>, unsigned __int8 a3@<cl>, char a4);
int __userpurge sub_5F0004@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, int a5, int a6);
_DWORD *__usercall sub_5F00B4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
bool sub_5F011C();
_DWORD *__usercall sub_5F014C@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
void sub_5F0214();
int sub_5F0498();
int sub_5F04E8();
int __stdcall sub_5F1720(int a1, _DWORD *a2, int a3);
int __stdcall sub_5F1734(int a1, int a2, int a3);
int __stdcall sub_5F17A8(int a1, _DWORD *a2);
int __stdcall sub_5F17BC(int a1, int a2);
int __stdcall sub_5F1848(int a1, _DWORD *a2);
int __stdcall sub_5F185C(int a1, int a2);
int __stdcall sub_5F18CC(int a1, int a2, int a3, int a4, _DWORD *a5);
int __stdcall sub_5F18E0(int a1, int a2, int a3, int a4, int a5);
int __stdcall sub_5F1968(unsigned int a1, _DWORD *a2);
int __stdcall sub_5F198C(int a1, int a2);
void sub_5F1A0C();
void sub_5F1A40();
void sub_5F1A88();
_DWORD *__usercall sub_5F1AAC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5F1B58@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __userpurge sub_5F1B7C@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>, _BYTE *a4, _WORD *a5);
int __userpurge sub_5F1CBC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, unsigned __int16 a5);
int __fastcall sub_5F1D84(int a1, int a2);
int __usercall sub_5F1D90@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        unsigned __int8 a3@<cl>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        __int64 **a7);
// attributes: thunk
int __usercall sub_5F1E98@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
void __stdcall sub_5F1E9F(int a1);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__fastcall sub_5F1EA8(int a1, __int64 **a2);
int __fastcall sub_5F1F18(int a1, int a2);
int __fastcall sub_5F1F3C(int a1, int a2, int a3, int a4);
int __userpurge sub_5F1F58@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        _BYTE *a4,
        _WORD *a5,
        volatile __int32 *a6,
        int a7,
        int a8);
int __fastcall sub_5F2098(int a1, int a2, int a3, int a4);
int __userpurge sub_5F20C8@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        char a4,
        unsigned __int16 a5,
        int a6,
        int a7,
        int a8);
int sub_5F2260();
int __fastcall sub_5F2278(int a1, int a2);
int __fastcall sub_5F2284(int a1, int a2, char a3, int a4);
int __fastcall sub_5F22B4(int a1, const WCHAR *a2);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_5F23A8@<eax>(int a1@<edx>, void **a2@<ecx>, int a3@<ebx>, int a4@<edi>, int a5@<esi>);
int __fastcall sub_5F2484(int a1, int a2);
int __fastcall sub_5F2490(int a1, int a2);
int __fastcall sub_5F249C(int a1, int a2);
int __fastcall sub_5F24A8(int a1, int a2);
unsigned __int64 __stdcall sub_5F24B4(int a1, int a2);
unsigned __int64 __stdcall sub_5F2504(int a1, int a2);
_DWORD *__usercall sub_5F2554@<eax>(int a1@<eax>, __int64 **a2@<edx>, int a3);
int __usercall sub_5F258C@<eax>(int a1@<eax>, int a2);
int __cdecl sub_5F26E4(int a1);
_DWORD *__usercall sub_5F2974@<eax>(int a1@<eax>, int a2);
_DWORD *__cdecl sub_5F2A8C(int a1);
_DWORD *sub_5F2CB0();
int __fastcall sub_5F2CD4(int a1, int a2);
int __userpurge sub_5F2CE0@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>, _BYTE *a4, _WORD *a5);
_DWORD *__usercall sub_5F2E10@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5F2EC4@<eax>(int a1@<eax>);
BOOL __usercall sub_5F2F0C@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5F2F64@<eax>(int a1@<eax>);
int __usercall sub_5F2FB0@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5F3068@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_5F30F8(int a1, int a2);
bool __fastcall sub_5F319C(int a1, int a2);
bool __fastcall sub_5F31D4(int a1, int a2, int a3, int a4);
int __usercall sub_5F3240@<eax>(int a1@<eax>, _DWORD *a2@<edx>, int a3@<ecx>);
int __usercall sub_5F329C@<eax>(int a1@<eax>, int a2@<edx>, _DWORD *a3@<ecx>);
BOOL __userpurge sub_5F32BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4, int a5);
int __usercall sub_5F335C@<eax>(int a1@<eax>, const void *a2@<edx>);
int __usercall sub_5F33B0@<eax>(int a1@<eax>, void *a2@<edx>);
int __fastcall sub_5F3404(unsigned __int8 a1, int a2);
int __usercall sub_5F3434@<eax>(int a1@<eax>, int a2@<ecx>);
bool sub_5F34D0();
int __usercall sub_5F34F4@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        unsigned __int8 a3@<cl>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        __int64 **a7);
// attributes: thunk
int __usercall sub_5F35F9@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
// attributes: thunk
int __usercall sub_5F3616@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_5F3628@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, unsigned __int16 a5);
int __userpurge sub_5F36E8@<eax>(int a1@<eax>, int a2@<edx>, volatile __int32 *a3@<ecx>, _BYTE *a4, _WORD *a5);
int __usercall sub_5F3818@<eax>(int a1@<eax>, int a2@<edx>);
int __fastcall sub_5F3840(int a1, int a2, int a3, int a4, int a5);
int __fastcall sub_5F3874(int a1, int a2, int a3, int a4, int a5);
int sub_5F38A8();
int __fastcall sub_5F3948(int a1, int a2, int a3);
__int64 *__userpurge sub_5F3960@<eax>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        __int64 *a4,
        __int64 *a5,
        unsigned __int16 a6);
__int16 __userpurge sub_5F39FC@<ax>(int a1@<eax>, _DWORD *a2@<ecx>, char a3, __int16 a4, int a5, int a6);
OLECHAR ***__userpurge sub_5F3A54@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, unsigned __int16 a4, int a5, int a6);
int __userpurge sub_5F3B94@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, volatile signed __int8 **a4@<edi>, int a5);
int __usercall sub_5F3E94@<eax>(int *a1@<eax>, unsigned __int8 a2@<dl>);
__int64 __usercall sub_5F3EDC@<edx:eax>(int a1@<eax>, int a2@<edx>);
// attributes: thunk
int __usercall sub_5F3FB7@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __userpurge sub_5F3FCC@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>, int a4, int a5);
void sub_5F4050();
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_443@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_444@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_445@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_446@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
int __usercall sub_5F6864@<eax>(int a1@<eax>);
_DWORD *__usercall sub_5F68BC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __thiscall sub_5F6910(void *this);
int __usercall sub_5F6930@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __usercall sub_5F6984@<eax>(int a1@<eax>);
char __stdcall sub_5F6998(int a1, int a2);
int __usercall sub_5F69B4@<eax>(int a1@<eax>);
_DWORD *__userpurge sub_5F69CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, __int32 a4);
int __userpurge sub_5F6A20@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3, char a4);
int __userpurge sub_5F6A80@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3, __int32 a4);
_DWORD *__userpurge sub_5F6AE0@<eax>(int a1@<eax>, char a2@<dl>, __int32 a3);
_DWORD *__usercall sub_5F6B30@<eax>(int a1@<eax>, char a2@<dl>);
int __fastcall sub_5F6B78(int a1, int a2);
int __usercall sub_5F6B9C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5F6BF8@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
_DWORD *__usercall sub_5F6C68@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5F6CAC@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
_DWORD *__usercall sub_5F6D00@<eax>(__int64 *a1@<eax>);
int __userpurge sub_5F6D60@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_5F6D94@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __userpurge sub_5F6DC4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
_DWORD *__usercall sub_5F6DF4@<eax>(int a1@<eax>, _DWORD *a2@<edx>);
int __usercall sub_5F6ED4@<eax>(_DWORD *a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5F6FE0@<eax>(int a1@<eax>, volatile __int32 *a2@<edx>);
bool __usercall sub_5F7090@<al>(int a1@<eax>, int a2@<edx>);
volatile __int32 *__userpurge sub_5F7238@<eax>(__int64 *a1@<eax>, __int32 a2@<edx>, char a3@<cl>, volatile __int32 *a4);
int __userpurge sub_5F7320@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, char a4, __int16 a5, int a6, int a7);
int __usercall sub_5F7360@<eax>(int a1@<eax>);
// bad sp value at call has been detected, the output may be wrong!
int __usercall sub_5F73D4@<eax>(void *a1@<eax>);
int __fastcall sub_5F74B0(int a1, int a2);
int __userpurge sub_5F74D8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
int __usercall sub_5F7544@<eax>(int a1@<eax>);
int __usercall sub_5F7560@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5F7600@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
int __usercall sub_5F7A3C@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5F7A7C@<eax>(int a1@<eax>, int a2@<ecx>);
bool __usercall sub_5F7ABC@<al>(int a1@<eax>, int a2@<edx>);
bool __usercall sub_5F7B74@<al>(int a1@<eax>, __int32 a2@<edx>);
__int16 __fastcall sub_5F7BF4(int a1, int a2);
int __userpurge sub_5F7C90@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>, int a4, int a5);
void sub_5F7CCC();
_DWORD *__usercall sub_5F7D34@<eax>(__int64 **a1@<eax>, void *a2@<ecx>);
int __usercall sub_5F7DB4@<eax>(int a1@<eax>, char a2@<dl>);
int __usercall sub_5F7DBC@<eax>(int a1@<edi>);
_DWORD *__usercall sub_5F83DC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__thiscall sub_5F8414(void *this, int a2);
_DWORD *__userpurge sub_5F84C4@<eax>(int a1@<eax>, void *a2@<ecx>, int a3@<edi>, int a4);
_DWORD *__fastcall sub_5F8540(int a1, int a2);
OLECHAR ***__usercall sub_5F85BC@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>);
int sub_5F8620();
OLECHAR ***__usercall sub_5F8640@<eax>(int a1@<eax>, int a2@<ecx>, int a3@<edi>);
int __userpurge sub_5F86A4@<eax>(
        int (__fastcall ***a1)(int, __int64 (***)(void), _DWORD, _DWORD)@<eax>,
        __int64 (***a2)(void)@<edx>,
        int a3@<ecx>,
        __int64 a4,
        __int64 a5);
OLECHAR ***__userpurge sub_5F873C@<eax>(
        int (__fastcall ***a1)(int, __int64 (***)(void), _DWORD, _DWORD)@<eax>,
        __int64 (***a2)(void)@<edx>,
        int a3@<ecx>,
        int a4@<edi>,
        __int64 a5,
        __int64 a6);
volatile signed __int8 *__fastcall sub_5F87B0(int a1, int a2, __int64 **a3);
char sub_5F87D4();
int sub_5F87D8();
OLECHAR ***__userpurge sub_5F87F4@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
volatile signed __int8 *__fastcall sub_5F890C(__int64 **a1, int a2);
int __usercall sub_5F8924@<eax>(int a1@<eax>);
int sub_5F8928();
int __thiscall sub_5F8938(void *this);
OLECHAR ***__userpurge sub_5F894C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5, int a6);
void __stdcall sub_5F8990(int a1, int a2);
_DWORD *__usercall sub_5F8D3C@<eax>(int a1@<eax>);
int __usercall sub_5F8D5C@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5F8DAC@<eax>(_DWORD *a1@<eax>);
int __userpurge sub_5F913C@<eax>(OLECHAR ***a1@<eax>, int a2@<edx>, OLECHAR ***a3@<ecx>, int a4@<edi>, __int64 a5);
int sub_5F92A0();
volatile signed __int8 *__fastcall sub_5F92B0(__int64 **a1, int a2);
bool sub_5F92CC();
int sub_5F92F4();
bool sub_5F9304();
_DWORD *__usercall sub_5F932C@<eax>(_DWORD *a1@<eax>);
int nullsub_447();
// bad sp value at call has been detected, the output may be wrong!
int __stdcall nullsub_448(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
// bad sp value at call has been detected, the output may be wrong!
int __userpurge nullsub_449@<eax>(
        int a1,
        int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        int a7,
        int a8,
        int a9,
        int a10,
        int a11,
        int a12,
        int a13,
        int a14,
        int a15,
        int a16,
        int a17,
        int a18,
        int a19,
        int a20,
        int a21,
        int a22,
        int a23,
        int a24,
        int a25,
        int a26,
        int a27,
        int a28,
        int a29,
        int a30,
        int a31,
        int a32,
        int a33,
        int a34,
        int a35,
        int a36,
        int a37,
        int a38,
        int a39,
        int a40,
        int a41,
        int a42,
        int a43,
        int a44,
        int a45,
        int a46,
        int a47,
        int a48,
        int a49,
        int a50,
        int a51,
        int a52,
        int a53,
        int a54,
        int a55,
        int a56,
        int a57,
        int a58,
        int a59,
        int a60,
        int a61,
        int a62,
        int a63);
_DWORD *sub_5FAD84();
int __usercall sub_5FAE2C@<eax>(int a1@<eax>);
int __usercall sub_5FAE44@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5FAF3C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5FAF80@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
// attributes: thunk
int sub_5FB034();
int __usercall sub_5FB03C@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
_DWORD *__usercall sub_5FB054@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5FB0CC@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
_DWORD *__usercall sub_5FB170@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
int __usercall sub_5FB210@<eax>(_DWORD *a1@<eax>, char a2@<dl>);
int __fastcall sub_5FB248(int a1, int a2, int a3, int a4, int a5, int a6);
int __usercall sub_5FB280@<eax>(int **a1@<edx>, int a2@<ecx>, int a3@<ebx>, int a4, int a5, int a6, int a7);
// attributes: thunk
int __usercall sub_5FB2E8@<eax>(unsigned int a1@<ebp>, _DWORD *a2, int a3);
int __usercall sub_5FB2F4@<eax>(_DWORD *a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __thiscall sub_5FB348(void *this);
int __usercall sub_5FB374@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __userpurge sub_5FB448@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__usercall sub_5FB574@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>, int a4@<edi>, int a5@<esi>);
int __usercall sub_5FB5EC@<eax>(int a1@<eax>, int a2@<edx>, int (***a3)(void)@<ecx>);
_DWORD *__usercall sub_5FB664@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5FB6D0@<eax>(int result@<eax>, int a2@<edx>);
int sub_5FB78C();
int sub_5FB7AC();
int __usercall sub_5FB7CC@<eax>(int a1@<eax>, int a2@<edx>);
OLECHAR ***__usercall sub_5FB7D4@<eax>(int __return_address@<ecx>, int a2@<eax>, int a3@<edx>, int a4@<edi>);
int __usercall sub_5FB970@<eax>(int a1@<eax>);
int __usercall sub_5FB99C@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5FB9BC@<eax>(int result@<eax>, int a2@<edx>, int a3@<ecx>);
int __usercall sub_5FBAA8@<eax>(int a1@<eax>, int a2@<ecx>);
int __usercall sub_5FBAC0@<eax>(int a1@<eax>, int a2@<ecx>);
bool __fastcall sub_5FBB10(int a1, int a2);
int __usercall sub_5FBB28@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5FBB64@<eax>(int a1@<eax>, int a2@<edx>, char a3@<cl>);
int __usercall sub_5FBBB8@<eax>(int a1@<eax>, int a2@<edx>);
int __usercall sub_5FBBF0@<eax>(int result@<eax>);
int __usercall sub_5FBC20@<eax>(int a1@<eax>);
int __usercall sub_5FBC48@<eax>(int a1@<eax>);
int __usercall sub_5FBC74@<eax>(int *a1@<eax>, int a2@<edx>, int *a3@<ecx>);
int __userpurge sub_5FBCB0@<eax>(int a1@<eax>, int a2@<edx>, int *a3@<ecx>, int a4);
int __usercall sub_5FBCFC@<eax>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
int __usercall sub_5FBD48@<eax>(int a1@<eax>);
int __usercall sub_5FBD58@<eax>(int a1@<eax>, int a2@<ecx>);
_DWORD *__usercall sub_5FBD74@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>);
bool __usercall sub_5FBDB8@<al>(int a1@<eax>);
_DWORD *__userpurge sub_5FBFA0@<eax>(int a1@<eax>, char a2@<dl>, int a3@<ecx>, int a4, int a5);
void sub_5FBFF0();
int __usercall sub_5FC066@<eax>(int a1@<edi>);
int __usercall sub_5FC0A8@<eax>(int a1@<eax>, int a2@<edx>, int a3@<ecx>);
void sub_5FC140();
__int32 __usercall sub_5FC178@<eax>(_BYTE *a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>);
char __usercall sub_5FC1BC@<al>(int a1@<eax>, volatile signed __int8 ***a2@<edx>);
__int64 *__usercall sub_5FC24C@<eax>(__int64 *a1@<eax>, __int64 *a2@<edx>, int a3@<ecx>);
_DWORD *__fastcall sub_5FC254(int a1, __int64 **a2);
_DWORD *__usercall sub_5FC2F0@<eax>(int a1@<edx>, int a2@<ecx>, int a3@<edi>);
int __usercall sub_5FC388@<eax>(int a1@<eax>, int a2@<edx>, __int64 **a3@<ecx>, int a4@<edi>);
void pVLhpV5W6jx7By7UqgKiyCw5AKZa70N();
void mzzn2a1nfgdDG4cmX7tmCpKTvtYnJuy();
void qG2bIVfDgyqyD7bkVoDaSwT1B85GdGq();
void XOHQxk5kjy1JgcLsKx0Ux88qPWO7mK5();
void xG1mYdXETwPVS8nj428xJgZYsxfilMz();
void ranvFl0A6Hkryo4oGQ2j68xNquzkH5T();
void x5bdYFdmbv1pVm3CaixG5p2ZLjoTusz();
void NokjDVvhZyVZs2XET63xLaAu8sKvPZP();
void iPKeYrhH6QVPEythrh2hyj0uaqV4ESH();
void q8HVUISemnurPMB0gmImIaq26KY5HiL();
void nG5ez5VgIx4mRZ8ts6wDw1ZB6EAOzA6();
void PBjID3Evu0uKs6Uichs5pjyMTmGi5rf();
void eCrfCxtnBGu2utYi8N3mNsIkE3zfqt6();
void lngyfCu5ZjkERi4SDgY8lzB9tF3ngvY();
void St3mAENL1qp77o0zmREiGaq4Iq9lzAm();
void nXNZCi3zoXSrUlKXRUasWWFetAPs7bw();
void DEczHIHmrU9rJtk0ZLUWO2WV7qsFsSv();
void mpYy5xHAdOVu2ZoR5AN5p6rKDDFW1yE();
void VlVpzANoaQ6sSeVo9yx375j74wWxDos();
void hSVVPJZQE1hKurktR9BiT4R9mM3IibH();
void nZUOHLdFcDJZFna4DtjPuNQZQWhC1bP();
void qB1TRJrX81tYURPUd3ABu7g61dUOlBv();
void XtPnbbp3nsC0mLnz0i3JBtj8C3LTeeX();
int __usercall IW2tkUqqoIoErrUR3IlsSkUsHtZdoYB@<eax>(void (__stdcall *a1)(int *, _UNKNOWN **, __int64 *)@<edi>);
void hnd95HRQoN6xCjYbOEzkK8whGdly8V0();
void zRHJgFix9tbGLCF9GGFxSP74Va5vvIC();
void mj9KsLIr7tQ7OxArBC2J0bBch8jgzGO();
void lbGYJgc7wYrvPEMG5fOuM8Asp4hTCAk();
void iNpArCuUqYcVu0t2LGmUcuGa1F4TcTz();
void S5rjUreUz3wOzWanC1w79c1Mez7KgnL();
void aL4F8KIQaVgi1cXR3P51RpO2NIFIzRO();
void QXZ6ZF8SJkiVfjDi05cU2mCrNC7EIar();
void Bb5uVjDY0jymkQmlo4A5fMa4qP3bOFN();
void OKw7gDBhZFB4jt8B8dWuuVC6aUjFJsl();
void kpEAXGWL2zfrN8GMCYdPzHFfMk6efNi();
void gUDoUIoTj3FkG10Hp6GDgjaMuQafeCD();
void ZDNHeMmMlZ84hr7RmfUw7fGIOYoCRRB();
void Pv0Q9qmNXp8EPIy23ywiYUuNflx7af0();
void Iv508pFDL57xiP936emYLH8kkUFMWri();
void RzN5ecB6OHJDXzcrLPBnzVDIoOAq1EW();
void rdYYctYy9M6FyObyusukMCvJg0cmhEX();
void QME5L7DBsaM4UR47lpQMZUfuRSU71DJ();
void ppRdWohbNR0wkLp9Ck1WN1tOJKDfsFz();
void YYQF2c8CZW6Wv4iaAczsUNa1tbd2FDP();
void oHGEuNzf99bBgMF8MkB0kPcxzCnrQAn();
void AesYhSM1qlrDwRbrozTmfu6BtdrVRLe();
void Zljg8exTzJzlUSIFnaXyQFdCzLVwvgE();
void Cr7S4kJMwynTR9l6AGvEs8Q64lOq0on();
void xYJlPRGIalqDXyWjEUpxYq4FSq4DZAW();
void rrkrtPDabWjMaFwSAUdMQ9YS9pPKCM1();
void yqg2oKTnjbzM45LURj7F3isfYzHTkpX();
void heeiynXnen6nzM2HFUzrGRunulymROk();
void nullsub_450();
void sub_605000();
void sub_6050B4();
int sub_6050BC();
void sub_605104();
void sub_60510C();
_DWORD (*sub_605114())();
void sub_605124();
int __usercall sub_6053D8@<eax>(int a1@<edi>);
FARPROC sub_60548C();
int __thiscall sub_60549C(void *this);
int sub_605554();
int *sub_605568();
void sub_605578();
int sub_605580();
void sub_6055CC();
int __thiscall sub_6055D4(void *this);
_DWORD *__thiscall sub_6055F0(void *this);
void __thiscall sub_605678(void *this);
int sub_605694();
void sub_605734();
void sub_60573C();
OLECHAR **__usercall sub_605784@<eax>(int a1@<edi>);
void sub_605BDC();
void sub_605BE4();
int sub_605D94();
FARPROC sub_605DAC();
void __thiscall sub_605DBC(void *this);
int sub_605EF0();
int sub_605F88();
int sub_605FA8();
int sub_605FC8();
int sub_605FE8();
int sub_606008();
void sub_606028();
void __thiscall sub_606030(void *this);
_DWORD *sub_606074();
int sub_6061C4();
void sub_6061E0();
void sub_6062FC();
void sub_606390();
void sub_6065D4();
void sub_606828();
void sub_606830();
void sub_606838();
void __thiscall sub_6068C4(void *this);
_DWORD *__thiscall sub_6068F4(void *this);
void sub_606A20();
int sub_606A28();
// attributes: thunk
BOOL __stdcall  DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved);
void __userpurge sub_606AD7(int a1@<ebx>, int a2, int a3);
void __usercall  sub_61A114(int a1@<ebx>, int a2@<edi>, int a3@<esi>);
