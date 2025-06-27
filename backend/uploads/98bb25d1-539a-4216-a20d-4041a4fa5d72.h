#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
HRESULT __stdcall StringCchCopyA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc);
HRESULT __stdcall StringCchCatA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc);
HRESULT StringCchPrintfA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszFormat, ...);
__int64 __fastcall CheckToken(_DWORD *a1);
BOOL __stdcall IsNTAdmin(DWORD dwReserved, DWORD *lpdwReserved);
__int64 __fastcall WarningDlgProc(HWND hWnd, int a2, INT_PTR a3, UINT a4);
char *__fastcall ExtractField(char **a1, CHAR *a2);
__int64 __fastcall AnalyzeCmd(STRSAFE_LPSTR pszDest, __int64 a2, char **a3, _DWORD *a4);
__int64 MyNTReboot();
unsigned int AddRegRunOnce();
void __fastcall DeleteMyDir(const CHAR *a1);
__int64 GetWininitSize();
DWORD __stdcall NeedRebootInit();
__int64 __fastcall IsWindowsDrive(_BYTE *a1);
__int64 __fastcall DiskSpaceErrMsg(int a1, int a2, int a3, __int64 a4);
__int64 __fastcall GetFileTobeChecked(STRSAFE_LPSTR pszDest, __int64 a2, const char *a3);
__int64 __fastcall CheckFileVersion(__int64 a1, CHAR *a2, DWORD a3, _DWORD *a4);
void __fastcall ExpandCmdParams(CHAR *lpsz, unsigned __int64 a2, LPSTR a3);
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd);
__int64 __fastcall Init(HMODULE hModule, CHAR *lpsz);
__int64 DoMain();
LRESULT __fastcall MEditSubProc(HWND hWnd, UINT Msg, WPARAM wParam, LPARAM lParam);
__int64 __fastcall LicenseDlgProc(HWND hWnd, int a2, __int64 a3);
__int64 __fastcall TempDirDlgProc(HWND hWnd, int a2, __int64 a3);
__int64 __fastcall OverwriteDlgProc(HWND hWnd, int a2, unsigned __int64 a3);
__int64 __fastcall ExtractDlgProc(HWND hWnd, int a2, __int64 a3);
DWORD __fastcall WaitForObject(void *a1);
__int64 __fastcall CheckOSVersion(__int64 a1);
__int64 DisplayLicense();
__int64 RunInstallCommand();
__int64 __fastcall RunApps(LPSTR lpCommandLine, LPSTARTUPINFOA lpStartupInfo);
HLOCAL FinishMessage();
__int64 __fastcall BrowseCallback(HWND a1, int a2, __int64 a3, LPARAM a4);
__int64 __fastcall BrowseForDir(HWND hWnd);
BOOL __fastcall CenterWindow(HWND hWnd, HWND a2);
__int64 __fastcall MsgBox2Param(HWND hWnd, UINT a2, __int64 a3, __int64 a4, UINT uType, int a6);
__int64 __fastcall GetResource(LPCSTR lpName, void *Destination, rsize_t DestinationSize);
__int64 __fastcall CatDirAndFile(STRSAFE_LPSTR pszDest, STRSAFE_LPCSTR pszSrc, STRSAFE_LPCSTR a3);
__int64 __fastcall CheckOverwrite(LPCSTR lpFileName);
__int64 __fastcall AddFile(STRSAFE_LPCSTR pszSrc);
INT_PTR __fastcall openfunc(const CHAR *pszFile, __int16 oflag, int pmode);
__int64 __fastcall readfunc(INT_PTR hf, void *pv, UINT cb);
__int64 __fastcall writefunc(INT_PTR hf, void *pv, UINT cb);
__int64 __fastcall closefunc(INT_PTR hf);
__int64 __fastcall seekfunc(INT_PTR hf, LONG dist, int seektype);
HGLOBAL __fastcall allocfunc(ULONG cb);
// attributes: thunk
HGLOBAL __stdcall freefunc(HGLOBAL hMem);
INT_PTR __fastcall fdiNotifyExtract(FDINOTIFICATIONTYPE fdint, __int64 pfdin);
__int64 __fastcall UpdateCabinetInfo(__int64 a1);
_BOOL8 VerifyCabinet();
void *__fastcall ExtractThread(LPVOID lpThreadParameter);
__int64 GetFileList();
__int64 GetUsersPermission();
LSTATUS DeleteExtractedFiles();
__int64 __fastcall GetNewTempDir(LPCSTR lpPathName, STRSAFE_LPSTR pszDest);
__int64 __fastcall CreateAndValidateSubdir(const CHAR *a1, int a2, int a3);
__int64 GetTempDirectory();
__int64 __fastcall IsGoodTempDir(LPCSTR lpFileName);
__int64 __fastcall IsEnoughSpace(LPCSTR lpPathName, char a2, int a3);
__int64 __fastcall RemoveLeadTailBlanks(char *a1, _DWORD *a2);
__int64 __fastcall ParseCmdLine(CHAR *lpsz);
__int64 MyGetLastError();
__int64 __fastcall TravelUpdatedFiles(unsigned int (__fastcall *a1)(_QWORD, _QWORD, char *, char *));
__int64 __fastcall ProcessUpdatedFile_Size(unsigned int a1);
__int64 __fastcall ProcessUpdatedFile_Write(DWORD nNumberOfBytesToWrite, __int64 a2, const char *a3, const void *a4);
HMODULE MyLoadLibrary();
INT_PTR __fastcall MyDialogBox(
        __int64 a1,
        const CHAR *a2,
        HWND a3,
        INT_PTR (__stdcall *a4)(HWND, UINT, WPARAM, LPARAM),
        LPARAM dwInitParam,
        __int64 a6);
HRESULT __fastcall AddPath(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc);
__int64 __fastcall GetParentDir(LPCSTR lpszStart);
LPSTR __fastcall ANSIStrChr(CHAR *lpsz, __int16 a2);
const CHAR *__fastcall ANSIStrRChr(LPCSTR lpsz, __int16 a2);
__int64 __fastcall EnumResLangProc(HMODULE hModule, LPCSTR lpType, LPCSTR lpName, WORD wLanguage, LONG_PTR lParam);
__int64 IsBiDiLocalizedBinary();
__int64 RunningOnWin95BiDiLoc();
// write access to const memory has been detected, the output may be wrong!
__int64 pre_c_init();
__int64 pre_cpp_init();
int WinMainCRTStartup();
int _mainCRTStartup();
void __cdecl _security_check_cookie(uintptr_t StackCookie);
BOOL __fastcall _raise_securityfailure(struct _EXCEPTION_POINTERS *ExceptionInfo);
void __cdecl  _report_gsfailure(uintptr_t StackCookie);
void  _report_rangecheckfailure();
__int64 __fastcall __CxxUnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo);
__int64 _CxxSetUnhandledExceptionFilter();
// attributes: thunk
__int64 XcptFilter_0();
_DWORD *__fastcall RtlpImageNtHeader(__int64 a1);
__int64 __fastcall get_image_app_type(unsigned int a1);
// attributes: thunk
__int64 __fastcall amsg_exit_0(__int64 a1);
int __cdecl matherr(struct _exception *Except);
__int64 __fastcall FindPESection(__int64 a1, unsigned __int64 a2);
__int64 __fastcall IsNonwritableInCurrentImage(__int64 a1);
_BOOL8 __fastcall ValidateImageBase(__int64 a1);
void __cdecl _security_init_cookie();
// attributes: thunk
void __cdecl initterm_0(_PVFV *First, _PVFV *Last);
// attributes: thunk
EXCEPTION_DISPOSITION __cdecl _C_specific_handler_0(
        struct _EXCEPTION_RECORD *ExceptionRecord,
        void *EstablisherFrame,
        struct _CONTEXT *ContextRecord,
        struct _DISPATCHER_CONTEXT *DispatcherContext);
void guard_check_icall_nop();
__int64 __fastcall _GSHandlerCheck(__int64 a1, __int64 a2, __int64 a3, __int64 a4);
__int64 __fastcall _GSHandlerCheckCommon(__int64 a1, __int64 a2);
// attributes: thunk
void *__cdecl memcpy_0(void *a1, const void *Src, size_t Size);
// attributes: thunk
void *__cdecl memset_0(void *a1, int Val, size_t Size);
__int64 __fastcall guard_dispatch_icall_nop();
