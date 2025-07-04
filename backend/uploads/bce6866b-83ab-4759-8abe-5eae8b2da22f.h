#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
HRESULT __stdcall StringCchCatA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszSrc);
HRESULT StringCchPrintfA(STRSAFE_LPSTR pszDest, size_t cchDest, STRSAFE_LPCSTR pszFormat, ...);
HRESULT __stdcall StringCopyWorkerA(
        STRSAFE_LPSTR pszDest,
        size_t cchDest,
        size_t *pcchNewDestLength,
        STRSAFE_PCNZCH pszSrc,
        size_t cchToCopy);
int __fastcall AvailableBufferCch(unsigned int a1, int a2, unsigned int a3);
int __thiscall CheckToken(_DWORD *this);
BOOL __stdcall IsNTAdmin(DWORD dwReserved, DWORD *lpdwReserved);
int __stdcall WarningDlgProc(HWND hDlg, int a2, INT_PTR nResult, UINT uID);
_BYTE *__fastcall ExtractField(_BYTE **a1, const CHAR *a2);
int __thiscall AnalyzeCmd(STRSAFE_LPSTR pszDest, char **a2, _DWORD *a3);
int CheckReboot();
int MyNTReboot();
int __fastcall MyRestartDialog(char a1);
void __thiscall CleanRegRunOnce(HKEY this);
HLOCAL AddRegRunOnce();
void ConvertRegRunOnce();
void __thiscall DeleteMyDir(char *this);
LONG GetWininitSize();
DWORD __stdcall NeedRebootInit();
BOOL __thiscall IsWindowsDrive(_BYTE *this);
BOOL __fastcall DiskSpaceErrMsg(int a1, int a2, int a3, int a4);
int __thiscall GetFileTobeChecked(LPSTR lpBuffer, int a2);
int __fastcall CheckFileVersion(int a1, const CHAR *a2, int a3, _DWORD *a4);
int __fastcall CompareVersion(unsigned int a1, unsigned int a2, unsigned int a3, unsigned int a4);
void __fastcall ExpandCmdParams(BYTE *lpsz, unsigned int a2, CHAR *lpsza);
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd);
int __fastcall Init(HMODULE hModule, const CHAR *a2, int a3);
int __stdcall DoMain();
LRESULT __stdcall MEditSubProc(_LUID_AND_ATTRIBUTES hWnd, ULONG Msg, tagRECT wParam, ULONG lParam);
int __stdcall LicenseDlgProc(_LUID_AND_ATTRIBUTES hDlg, int a2, int a3, int a4);
BOOL __thiscall IsFullPath(int this);
int __stdcall TempDirDlgProc(HWND hDlg, int a2, int a3, int a4);
int __stdcall OverwriteDlgProc(HWND hDlg, int a2, unsigned int nResult, int a4);
int __stdcall ExtractDlgProc(HWND a1, int a2, INT_PTR a3, int a4);
DWORD __thiscall WaitForObject(void *this);
BOOL __thiscall CheckOSVersion(_DWORD *this);
int DisplayLicense();
int ExtractFiles();
int RunInstallCommand();
int __fastcall RunApps(CHAR *lpStartupInfo, struct _STARTUPINFOA *a2);
void __fastcall savAppExitCode(int a1);
HLOCAL __stdcall FinishMessage();
int __stdcall BrowseCallback(_LUID_AND_ATTRIBUTES hWnd, ULONG lParam, int a3, ULONG a4);
BOOL __thiscall BrowseForDir(void *this, int a2, int a3);
BOOL __fastcall CenterWindow(HWND hWnd, HWND a2);
int __fastcall MsgBox2Param(HWND a1, UINT a2, const char *a3, const char *a4, UINT uType, int a6);
DWORD __fastcall GetResource(LPCSTR lpName, void *Destination, rsize_t DestinationSize);
int __fastcall CatDirAndFile(const char *a1, char *a2, char *pszDest);
int __thiscall CheckOverwrite(LPCSTR lpFileName);
int __usercall AddFile@<eax>(STRSAFE_LPSTR pszDest@<ecx>, size_t a2@<ebx>);
HANDLE __fastcall Win32Open(LPCSTR lpFileName, __int16 a2);
void __thiscall MakeDirectory(CHAR *lpPathName);
INT_PTR __cdecl openfunc(const CHAR *pszFile, __int16 oflag);
UINT __cdecl readfunc(INT_PTR hf, void *pv, UINT cb);
UINT __cdecl writefunc(INT_PTR hf, LPCVOID pv, UINT cb);
int __cdecl closefunc(INT_PTR hf);
DWORD __cdecl seekfunc(HKEY hf, LONG dist, int seektype);
BOOL __fastcall AdjustFileTime(int a1, WORD a2, WORD wFatTime);
HGLOBAL __cdecl allocfunc(ULONG cb);
void __cdecl freefunc(DLGPROC pv);
INT_PTR __cdecl fdiNotifyExtract(FDINOTIFICATIONTYPE fdint, PFDINOTIFICATION pfdin);
int __thiscall UpdateCabinetInfo(int this);
BOOL VerifyCabinet();
STRSAFE_LPSTR __stdcall ExtractThread();
int GetUsersPermission();
void __thiscall DeleteExtractedFiles(char *this);
int __fastcall GetNewTempDir(char *lpPathName, CHAR *a2, int a3);
int __fastcall CreateAndValidateSubdir(STRSAFE_LPSTR pszDest, int a2, int a3);
BOOL GetTempDirectory();
int __thiscall IsGoodTempDir(char *lpFileName);
BOOL __fastcall IsEnoughSpace(LPCSTR lpPathName, int a2, int a3);
int __fastcall RemoveLeadTailBlanks(char *a1, _DWORD *a2);
int __fastcall ParseCmdLine(LPSTR lpsz);
void  CheckWinDir();
signed int MyGetLastError();
void __thiscall  TravelUpdatedFiles(
        int (__thiscall *this)(_DWORD, _DWORD, _DWORD, const char *, const char *),
        int a2);
int __stdcall ProcessUpdatedFile_Size(unsigned int a1, int a2, int a3, int a4);
int __thiscall ProcessUpdatedFile_Write(
        size_t *pcchNewDestLength,
        char *nNumberOfBytesToWrite,
        int a3,
        char *a4,
        const void *a5);
HMODULE __thiscall MyLoadLibrary(size_t *pcchNewDestLength);
INT_PTR __fastcall MyDialogBox(
        int a1,
        const CHAR *a2,
        HWND hWndParent,
        INT_PTR (__stdcall *lpDialogFunc)(HWND, UINT, WPARAM, LPARAM),
        LPARAM dwInitParam,
        int a6);
HRESULT __fastcall AddPath(CHAR *lpszStart, unsigned int a2, STRSAFE_LPSTR pszDest);
int __fastcall GetParentDir(LPCSTR lpszStart);
BOOL __fastcall ChrCmpA_inline(__int16 TestChar, __int16 a2);
LPSTR __fastcall ANSIStrChr(LPSTR lpsz, __int16 a2);
BOOL __thiscall FileExists(LPCSTR lpFileName);
LPSTR __fastcall ANSIStrRChr(LPSTR lpsz, __int16 a2);
BOOL __fastcall ConvertHexStringToIntA(LPCSTR lpsz, int *a2);
BOOL __stdcall EnumResLangProc(HMODULE hModule, LPCSTR lpType, LPCSTR lpName, WORD wLanguage, LONG_PTR lParam);
int __thiscall GetResourceLanguage(HMODULE hModule, int a2, __int16 a3);
int __thiscall IsBiDiLocalizedBinary(void *this, int a2);
int RunningOnWin95BiDiLoc();
int __thiscall GetSpace(LPCSTR lpRootPathName);
int pre_cpp_init();
int WinMainCRTStartup();
int _mainCRTStartup();
int __cdecl _initterm_e(_PIFV *First, _PIFV *Last);
bool check_managed_app();
void __fastcall __security_check_cookie(uintptr_t StackCookie);
BOOL __cdecl __raise_securityfailure(struct _EXCEPTION_POINTERS *a1);
void __cdecl  __report_gsfailure();
void __usercall  __report_rangecheckfailure(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        int a4@<ebx>,
        int a5@<edi>,
        int a6@<esi>,
        int a7);
LONG __stdcall __CxxUnhandledExceptionFilter(struct _EXCEPTION_POINTERS *ExceptionInfo);
int __CxxSetUnhandledExceptionFilter();
// attributes: thunk
int _XcptFilter();
int __stdcall RtlpImageNtHeader(int a1);
int __cdecl _get_image_app_type(int a1);
// attributes: thunk
int __cdecl _amsg_exit(int a1);
int __cdecl _setargv();
int __cdecl _FindPESection(int a1, unsigned int a2);
BOOL __cdecl _IsNonwritableInCurrentImage(int a1);
BOOL __cdecl _ValidateImageBase(int a1);
// bad sp value at call has been detected, the output may be wrong!
// positive sp value has been detected, the output may be wrong!
void __cdecl __security_init_cookie();
// positive sp value has been detected, the output may be wrong!
unsigned int _setdefaultprecision();
// attributes: thunk
void __cdecl _initterm(_PVFV *First, _PVFV *Last);
_DWORD *__cdecl _SEH_prolog4(int a1, int a2);
// positive sp value has been detected, the output may be wrong!
void _SEH_epilog4();
void __cdecl  _except_handler4(int a1, int a2, int a3, int a4);
void _guard_check_icall_nop();
// attributes: thunk
void __cdecl  _except_handler4_common(int a1, int a2, int a3, int a4, int a5, int a6);
// attributes: thunk
void *__cdecl memcpy(void *a1, const void *Src, size_t Size);
// attributes: thunk
void *__cdecl memset(void *a1, int Val, size_t Size);
