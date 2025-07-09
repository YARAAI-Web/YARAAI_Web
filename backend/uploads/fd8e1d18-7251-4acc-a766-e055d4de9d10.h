#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
int sub_140001000();
int sub_14000103C();
__int64 sub_14000105C();
CWinApp *__fastcall sub_140001090(CWinApp *a1, char a2);
__int64 __fastcall sub_1400010E0(CWinApp *a1);
void __fastcall sub_140001250(_QWORD *a1);
void __fastcall sub_1400012A0(_QWORD *a1);
_QWORD *__fastcall sub_140001370(_QWORD *a1, char a2);
void *__fastcall sub_1400013D0(void *a1, char a2);
int __fastcall sub_140001420(CGdiObject *a1);
__int64 __fastcall sub_140001480(__int64 a1, __int64 a2);
_QWORD *__fastcall sub_1400014E0(_QWORD *a1, char a2);
__int64 __fastcall sub_140001560(_QWORD *a1);
void  sub_140001580();
__int64 __fastcall sub_1400015A0(__int64 a1, __int64 a2);
__int64 __fastcall sub_1400015E0(__int64 a1, __int64 a2);
void  sub_140001620();
__int64 __fastcall sub_140001640(__int64 a1, char a2);
__int64 __fastcall sub_1400016D0(__int64 a1, char a2);
__int64 __fastcall sub_140001790(__int64 a1);
void __fastcall sub_140001860(CWnd *a1, __int16 a2);
void __fastcall sub_1400018F0(__int64 a1);
_QWORD *__fastcall sub_140001A10(_QWORD *a1, _QWORD *a2, __int64 a3);
char __fastcall sub_140001C30(_QWORD *a1);
__int64 __fastcall sub_140001F60(CWnd *a1);
int __fastcall sub_1400021A0(CDialogEx *a1, struct tagMSG *a2);
void __fastcall sub_1400021D0(void **a1);
__int64 __fastcall sub_1400021F0(__int64 a1);
void __fastcall sub_140002250(__int64 a1);
void __fastcall sub_1400022B0(CHAR **a1, const WCHAR *a2, UINT a3);
void **__fastcall sub_140002510(void **a1, void *Src, size_t Size);
void __fastcall sub_140002680(void *a1, void *a2);
void  sub_140002690();
void  sub_1400026C0();
CEdit *__fastcall sub_1400026E0(CEdit *a1, char a2);
void __fastcall  sub_140002750(int a1);
int pre_c_initialization();
__int64 post_pgo_initialization();
void pre_cpp_initialization();
__int64 __fastcall __scrt_common_main_seh();
__int64 start();
char _scrt_acquire_startup_lock();
char __fastcall _scrt_initialize_crt(int a1);
char __fastcall _scrt_initialize_onexit_tables(unsigned int a1);
bool __fastcall _scrt_is_nonwritable_in_current_image(__int64 a1);
__int64 __fastcall _scrt_release_startup_lock(char a1);
char __fastcall _scrt_uninitialize_crt(__int64 a1, char a2);
_onexit_t __cdecl onexit(_onexit_t Func);
int __cdecl atexit(void (__cdecl *a1)());
_QWORD *__fastcall sub_140002FF0(_QWORD *a1, char a2);
// attributes: thunk
void __fastcall operator delete(void *a1);
__int64 __scrt_initialize_thread_safe_statics();
void __fastcall __scrt_uninitialize_thread_safe_statics();
__int64 _security_init_cookie();
__int64 __fastcall charNode::raw_length(charNode *this);
__int64 get_startup_file_mode();
void sub_1400031D8();
char sub_1400031E8();
_QWORD *_scrt_initialize_default_local_stdio_options();
_BOOL8 _scrt_is_user_matherr_present();
void *sub_140003224();
void *sub_14000322C();
LONG __fastcall _scrt_fastfail(unsigned int a1);
WORD _scrt_get_show_window_mode();
// attributes: thunk
int __fastcall j_UserMathErrorFunction(struct _exception *a1);
bool _scrt_is_managed_app();
LPTOP_LEVEL_EXCEPTION_FILTER _scrt_set_unhandled_exception_filter();
__int64 __fastcall _scrt_unhandled_exception_filter(_QWORD *a1);
void sub_14000348C();
void __fastcall sub_1400034C8();
BOOL __fastcall _raise_securityfailure(struct _EXCEPTION_POINTERS *ExceptionInfo);
BOOL __fastcall _report_gsfailure(__int64 a1);
struct _IMAGE_RUNTIME_FUNCTION_ENTRY *__fastcall capture_previous_context(PCONTEXT ContextRecord);
__int64 _isa_available_init();
_BOOL8 _scrt_is_ucrt_dll_in_use();
__int64 __fastcall _GSHandlerCheck(__int64 a1, __int64 a2, __int64 a3, __int64 a4);
__int64 __fastcall _GSHandlerCheckCommon(__int64 a1, __int64 a2);
__int64 __fastcall sub_1400038C0(__int64 a1);
void __fastcall sub_140003968(struct _RTL_CRITICAL_SECTION *a1);
// attributes: thunk
void *__cdecl memset(void *a1, int Val, size_t Size);
// attributes: thunk
__int64 _current_exception(void);
// attributes: thunk
__int64 _current_exception_context(void);
// attributes: thunk
void *__cdecl memmove(void *a1, const void *Src, size_t Size);
// attributes: thunk
void __cdecl free(void *Block);
// attributes: thunk
void __cdecl set_app_type(_crt_app_type Type);
// attributes: thunk
void __cdecl _setusermatherr(_UserMathErrorFunctionPointer UserMathErrorFunction);
// attributes: thunk
errno_t __cdecl configure_wide_argv(_crt_argv_mode mode);
// attributes: thunk
int __cdecl initialize_wide_environment();
// attributes: thunk
wchar_t *__cdecl get_wide_winmain_command_line();
// attributes: thunk
void __cdecl initterm(_PVFV *First, _PVFV *Last);
// attributes: thunk
int __cdecl initterm_e(_PIFV *First, _PIFV *Last);
// attributes: thunk
void __cdecl  exit(int Code);
// attributes: thunk
errno_t __cdecl set_fmode(int Mode);
// attributes: thunk
void __cdecl cexit();
// attributes: thunk
void __cdecl register_thread_local_exe_atexit_callback(_tls_callback_type Callback);
// attributes: thunk
int __cdecl configthreadlocale(int Flag);
// attributes: thunk
int *__cdecl _p__commode();
// attributes: thunk
int __cdecl initialize_onexit_table(_onexit_table_t *Table);
// attributes: thunk
int __cdecl register_onexit_function(_onexit_table_t *Table, _onexit_t Function);
// attributes: thunk
int __cdecl crt_atexit(_PVFV Function);
// attributes: thunk
void  terminate(void);
__int64 __fastcall sub_140003A44(char a1, int a2);
// attributes: thunk
int __stdcall WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd);
__int64 __fastcall _GSHandlerCheck_EH4(__int64 a1, __int64 a2, __int64 a3, __int64 a4);
// attributes: thunk
void *__cdecl memcpy(void *a1, const void *Src, size_t Size);
void __fastcall sub_140003B68(__int64 a1, __int64 a2);
__int64 __fastcall sub_140003B90(__int64 a1, __int64 a2);
// MFC 7-14 64bit
__int64 __fastcall unknown_libname_2(__int64 a1, __int64 a2);
void __fastcall sub_140003D40();
void __fastcall sub_140003D50();
