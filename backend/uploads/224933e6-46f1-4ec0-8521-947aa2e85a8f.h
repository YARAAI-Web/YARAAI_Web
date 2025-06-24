#include <windows.h>
#include <stdint.h>
#include <stdio.h>

#include "defs.h"

void JUMPOUT(int a) {
}

unsigned int _bss_start__ = 0;
unsigned int __cxa_finalize = 0;
int sub_10001000();
int sub_10001020();
char *sub_10001030();
unsigned __int8 sub_100011A0();
char *__thiscall sub_100013F0(char *this, int a2);
const char *__thiscall sub_10001420(_DWORD *this);
char *__thiscall sub_10001430(char *Block, char a2);
// Microsoft VisualC 14/net runtime
int __thiscall unknown_libname_1(_DWORD *this);
char *__thiscall sub_10001480(char *this);
void  sub_100014A0();
char *__thiscall sub_100014C0(char *this, int a2);
char *__thiscall sub_10001500(char *this, int a2);
void  sub_10001540();
_DWORD *__stdcall sub_10001550(_DWORD *Src, char *a2, int a3);
void __thiscall sub_100017E0(_DWORD *this);
_DWORD *__thiscall sub_10001830(_DWORD *this, int a2);
_DWORD *__thiscall sub_10001880(_DWORD *this, void *Src);
void *__thiscall sub_100018C0(_DWORD *this, void *Src, size_t Size);
// bad sp value at call has been detected, the output may be wrong!
void **__thiscall sub_100019A0(void **Src, int a2, int a3, char a4);
BOOL __stdcall DllMain(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpvReserved);
_OWORD *__thiscall sub_10001AF0(_OWORD *this);
int sub_10002FE0();
void **__thiscall sub_100030B0(void **this, void *Src, size_t Size);
int sub_100031E0();
_DWORD *__stdcall sub_10003290(_DWORD *a1, _DWORD *Src, int a3, int a4);
_DWORD *__thiscall sub_10003490(_DWORD *this);
_DWORD *__thiscall sub_100034A0(_DWORD *this, _QWORD *a2);
void  sub_10003520();
void  sub_10003530();
void *sub_10003540();
int sub_10003550(char *Buffer, size_t BufferCount, char *Format, ...);
_DWORD *__stdcall sub_10003590(_DWORD *a1);
_DWORD *__stdcall sub_10003A60(_DWORD *a1);
WCHAR *__stdcall sub_10004100(WCHAR *a1);
WCHAR *__stdcall sub_10005470(WCHAR *a1);
_DWORD *__stdcall sub_100067E0(_DWORD *a1);
int __stdcall sub_10008110(int a1);
_DWORD *__stdcall sub_10008500(_DWORD *Src);
_DWORD *__stdcall sub_10008890(_DWORD *Src);
int __stdcall sub_10008CD0(int a1);
int __userpurge sub_10008F90@<eax>(int a1@<ecx>, size_t a2@<ebx>, int a3);
_DWORD *__thiscall sub_10009D00(_DWORD *this);
int __thiscall sub_10009D10(_DWORD *this);
// bad sp value at call has been detected, the output may be wrong!
size_t *__thiscall sub_10009D70(size_t *this, _DWORD *a2);
_DWORD *__thiscall sub_10009E70(_DWORD *this, _DWORD *a2);
_DWORD *__thiscall sub_10009F60(_DWORD *this, void *Src, size_t Size);
int __fastcall sub_10009FC0(int a1, _DWORD *a2, const void **Src);
int __fastcall sub_1000A070(int a1, const char *a2, _DWORD *Src);
// bad sp value at call has been detected, the output may be wrong!
_DWORD *__thiscall sub_1000A170(_DWORD *this, void *Src, unsigned int a3);
// bad sp value at call has been detected, the output may be wrong!
void **__thiscall sub_1000A260(void **Src, unsigned int a2, int a3, const void *a4, size_t Size);
// bad sp value at call has been detected, the output may be wrong!
void **__thiscall sub_1000A3C0(void **this, unsigned int a2, int a3, const void *a4);
char **__thiscall sub_1000A4E0(char **this, int a2, _DWORD *a3, _DWORD *Src);
_DWORD *__thiscall sub_1000A6C0(_DWORD *this, int a2, int a3, const void *a4, size_t Size, const void *a6, size_t a7);
void **__thiscall sub_1000A7B0(void **Src, unsigned int a2, int a3, int a4, const void *a5, size_t Size);
int sub_1000A900(wchar_t *Buffer, unsigned int a2, wchar_t *Format, ...);
int sub_1000A970();
int __stdcall sub_1000AA30(int a1, CHAR *lpMultiByteStr, int a3, int a4, int a5, int cbMultiByte, unsigned int a7);
int __stdcall sub_1000AD50(int a1, WCHAR *lpWideCharStr, int a3, int a4, int a5, int cchWideChar, unsigned int a7);
_DWORD *__stdcall sub_1000B000(_DWORD *a1, _DWORD *a2, int a3, int a4, int a5, unsigned int a6, unsigned int a7);
FILE *__stdcall sub_1000B270(FILE *a1, char *FileName, int a3, int a4, int a5, int a6, unsigned int a7);
_DWORD *__stdcall sub_1000B970(
        _DWORD *a1,
        _DWORD *Block,
        int a3,
        int a4,
        int a5,
        int a6,
        unsigned int a7,
        _DWORD *a8,
        int a9,
        int a10,
        int a11,
        int a12,
        unsigned int a13);
void *__stdcall sub_1000BA90(void *a1, _DWORD *Src, int a3, int a4, int a5, size_t Size, unsigned int a7);
char __stdcall sub_1000C310(
        _DWORD *a1,
        int a2,
        int a3,
        int a4,
        int a5,
        unsigned int a6,
        _DWORD *a7,
        int a8,
        int a9,
        int a10,
        int a11,
        unsigned int a12);
int sub_1000C790();
CHAR *__thiscall sub_1000CE40(_BYTE *this, CHAR *lpPathName);
// positive sp value has been detected, the output may be wrong!
char sub_1000D1E0();
char __thiscall sub_1000D290(_BYTE *this);
char __usercall sub_1000F100@<al>(int a1@<ecx>, size_t a2@<ebx>);
_DWORD *__stdcall sub_100113C0(_DWORD *a1);
char __usercall VelocitySpeed@<al>(size_t a1@<ebx>);
char LOPP();
// bad sp value at call has been detected, the output may be wrong!
void **__thiscall sub_100116D0(void **Src, unsigned int a2, int a3, const void *a4, int a5);
_DWORD *__thiscall sub_10011850(_DWORD *this, int a2, int a3, const void *a4, int a5, const void *a6, int a7);
// bad sp value at call has been detected, the output may be wrong!
void **__thiscall sub_10011950(void **Src, unsigned int a2, int a3, int a4, int a5, int a6);
void  sub_10011AB0();
int __stdcall sub_10011AC0(int a1, __int128 Block, __int64 a3, char a4);
char __thiscall sub_10011D60(
        _DWORD **this,
        int a2,
        int a3,
        void *a4,
        HMODULE a5,
        void *a6,
        _BYTE *a7,
        double *a8,
        HMODULE a9);
int __stdcall sub_10014450(_DWORD *Block, int a2);
void __fastcall sub_10014490(int a1, int a2);
size_t *__thiscall sub_10014500(int *this, int a2, _DWORD *a3);
int __fastcall sub_10014720(int a1, int a2, int a3);
int __thiscall sub_10014790(int *this);
char __stdcall sub_10014800(OLECHAR *psz, int a2, int a3, int a4, int a5, unsigned int a6);
_DWORD *__thiscall sub_10014B54(_DWORD *this);
std::exception *__thiscall std::exception::exception(std::exception *this, const char *a2);
char *__thiscall sub_10014BA1(char *this, int a2);
std::exception *__thiscall sub_10014BBC(std::exception *this, char *a2);
char *__thiscall sub_10014BDB(char *this, int a2);
std::exception *__thiscall sub_10014BF6(std::exception *this, char *a2);
char *__thiscall sub_10014C15(char *this, int a2);
char *__thiscall sub_10014C30(char *this, int a2);
std::exception *__thiscall sub_10014C4B(std::exception *this, char *a2);
char *__thiscall sub_10014C6A(char *this, int a2);
// Microsoft VisualC 14/net runtime
char *__thiscall unknown_libname_2(char *Block, char a2);
void __cdecl  sub_10014CB2(char *a1);
void __cdecl  sub_10014CD2(char *a1);
void __cdecl  sub_10014CF2(char *a1);
_DWORD *__thiscall std::_System_error::_System_error(_DWORD *this, int a2, int a3, _DWORD *a4);
int __thiscall sub_10014D7E(int this, int a2);
std::exception *__thiscall sub_10014DA8(std::exception *this, char *a2);
_DWORD *__thiscall sub_10014DD0(_DWORD *this, int a2);
// Microsoft VisualC 14/net runtime
_DWORD *__thiscall unknown_libname_3(_DWORD *this, int a2, int a3, void *a4);
bool __cdecl std::operator==(_DWORD *a1, _DWORD *a2);
std::_Iostream_error_category2 *__thiscall std::_Iostream_error_category2::`scalar deleting destructor'(
        std::_Iostream_error_category2 *this,
        char a2);
// Microsoft VisualC 14/net runtime
char *__thiscall unknown_libname_4(char *Block, char a2);
_DWORD *__cdecl std::_System_error::_Makestr(_DWORD *a1, int a2, int a3, int a4, int a5, int a6, int a7, int a8);
void __cdecl  std::_Throw_Cpp_error(int a1);
_DWORD *__thiscall std::error_category::default_error_condition(void *this, _DWORD *a2, int a3);
bool __thiscall std::error_category::equivalent(std::error_category *this, const struct std::error_code *a2, int a3);
bool __thiscall std::error_category::equivalent(
        std::error_category *this,
        int a2,
        const struct std::error_condition *a3);
void *(__thiscall ***sub_10014FB9())(std::_Iostream_error_category2 *__hidden this, char);
_DWORD *__stdcall std::_Generic_error_category::message(_DWORD *a1, int a2);
int __thiscall std::error_code::message(_DWORD **this, int a2);
const char *sub_10015004();
int __cdecl _Mtx_lock(_Mtx_t a1);
int __cdecl _Mtx_unlock(_Mtx_t a1);
int __cdecl mtx_do_lock(RTL_SRWLOCK *a1, int a2);
__m128i *__stdcall sub_10015170(__m128i *a1, __m128i *a2, unsigned __int8 a3);
__m128i *__stdcall sub_10015280(__m128i *a1, __m128i *a2, __int16 a3);
__m128i *__stdcall sub_100153A0(__m128i *a1, __m128i *a2, unsigned __int8 a3);
__m128i *__stdcall sub_100153B0(__m128i *a1, __m128i *a2, __int16 a3);
const char *__cdecl std::_Syserror_map(int a1);
// Microsoft VisualC 14/net runtime
int __cdecl unknown_libname_5(int a1);
__int64 __cdecl _Xtime_get_ticks();
int __cdecl initialize_pointers();
void __cdecl `anonymous namespace'::_UCalendar_deleter::operator()(LPFILETIME lpSystemTimeAsFileTime);
void __fastcall __security_check_cookie(uintptr_t StackCookie);
void __cdecl sub_100154EB(void *Block);
_DWORD *__thiscall sub_100154F9(_DWORD *Block, char a2);
void *__cdecl operator new(size_t Size);
struct _IMAGE_SECTION_HEADER *__cdecl find_pe_section(unsigned __int8 *const a1, unsigned int a2);
char __scrt_acquire_startup_lock();
char __scrt_dllmain_after_initialize_c();
bool __scrt_dllmain_before_initialize_c();
char __scrt_dllmain_crt_thread_attach();
char sub_1001561A();
int __cdecl __scrt_dllmain_exception_filter(
        int a1,
        int a2,
        int a3,
        void (__thiscall *a4)(_DWORD, int, _DWORD, int),
        unsigned int ExceptionNum,
        struct _EXCEPTION_POINTERS *ExceptionPtr);
void __scrt_dllmain_uninitialize_c();
__vcrt_bool sub_1001567E();
char __cdecl __scrt_initialize_crt(int a1);
char __cdecl __scrt_initialize_onexit_tables(unsigned int a1);
bool __cdecl __scrt_is_nonwritable_in_current_image(int a1);
__int32 __cdecl __scrt_release_startup_lock(char a1);
char __cdecl __scrt_uninitialize_crt(__vcrt_bool Terminating, char a2);
_onexit_t __cdecl _onexit(_onexit_t Func);
int __cdecl atexit(void (__cdecl *Func)());
BOOL __cdecl __raise_securityfailure(struct _EXCEPTION_POINTERS *ExceptionInfo);
void __cdecl  __report_gsfailure();
void  sub_10015989();
void __usercall  __report_securityfailure(int a1@<ebx>, int a2@<edi>, int a3@<esi>, unsigned int a4);
// Microsoft VisualC 14/net runtime
void *__cdecl unknown_libname_6(size_t a1);
// attributes: thunk
void __cdecl j_j_j___free_base(void *Block);
int __stdcall dllmain_crt_dispatch(HINSTANCE a1, unsigned int a2, void *const a3);
int __cdecl dllmain_crt_process_attach(HINSTANCE a1, void *const a2);
BOOL __cdecl dllmain_crt_process_detach(__vcrt_bool Terminating);
int __cdecl dllmain_dispatch(HINSTANCE hinstDLL, DWORD fdwReason, void *const lpvReserved);
int __stdcall dllmain_raw(HINSTANCE a1, unsigned int a2, void *const a3);
BOOL __stdcall DllEntryPoint(HINSTANCE hinstDLL, DWORD fdwReason, LPVOID lpReserved);
// positive sp value has been detected, the output may be wrong!
void _EH_epilog3();
void _EH_epilog3_GS();
_DWORD *__usercall _EH_prolog3@<eax>(int a1@<eax>);
_DWORD *__usercall _EH_prolog3_GS@<eax>(int a1@<eax>);
_DWORD *__usercall _EH_prolog3_catch@<eax>(int a1@<eax>);
void nullsub_1();
int sub_10015E9C();
unsigned int __stdcall _aulldiv(unsigned __int64 a1, __int64 a2);
unsigned __int64 __stdcall _aullrem(unsigned __int64 a1, __int64 a2);
// attributes: thunk
void __cdecl j_j___free_base(void *Block);
void  sub_100162BA();
int sub_100162D7();
BOOL __scrt_is_ucrt_dll_in_use();
LONG __usercall __scrt_fastfail@<eax>(int a1@<ebx>, int a2@<edi>, int a3@<esi>, unsigned int a4);
void sub_100163FC();
_DWORD *__cdecl _SEH_prolog4(int a1, int a2);
unsigned int __get_entropy();
void __cdecl __security_init_cookie();
void sub_100164ED();
int sub_100164F9();
void *sub_10016505();
_DWORD *__scrt_initialize_default_local_stdio_options();
void *sub_10016528();
void sub_1001652E();
void sub_1001655A();
void __stdcall  sub_10016590(int a1);
_DWORD *__thiscall sub_100165B0(_DWORD *this, int a2);
_DWORD *__thiscall sub_100165F0(_DWORD *this, int a2, int a3, char a4);
HLOCAL __thiscall sub_10016640(void *this);
void *__thiscall sub_100166B0(void *Block, char a2);
void __cdecl  sub_10016740(int a1, int a2);
_DWORD *__cdecl __FrameHandler3::GetRangeOfTrysToCheck(_DWORD *a1, int a2, int a3, int a4, int a5, int a6);
void *__cdecl _CallCatchBlock2(
        struct EHRegistrationNode *a1,
        const struct _s_FuncInfo *a2,
        void *a3,
        int a4,
        unsigned int a5);
int __cdecl _CallSETranslator(
        struct EHExceptionRecord *a1,
        struct EHRegistrationNode *a2,
        void *a3,
        void *a4,
        const struct _s_FuncInfo *a5,
        int a6,
        struct EHRegistrationNode *a7);
void __stdcall _JumpToContinuation(
        void (__stdcall *a1)(void *, struct EHRegistrationNode *),
        struct EHRegistrationNode *a2);
int __userpurge sub_10016951@<eax>(
        struct _EXCEPTION_REGISTRATION_RECORD **a1@<ebx>,
        PVOID TargetFrame,
        PEXCEPTION_RECORD ExceptionRecord);
int __cdecl _CatchGuardHandler(int a1, _DWORD *a2, int a3);
_DWORD *__cdecl _CreateFrameInfo(_DWORD *a1, int a2);
int __cdecl _FindAndUnlinkFrame(int a1);
int __usercall sub_10016A42@<eax>(
        struct _EXCEPTION_REGISTRATION_RECORD **a1@<ebx>,
        PEXCEPTION_RECORD ExceptionRecord,
        _DWORD *TargetFrame,
        int a4);
int __usercall __CxxFrameHandler3@<eax>(int a1@<eax>, int a2, int a3, int a4, int a5);
void __cdecl __DestructExceptionObject(int a1);
void __stdcall _CallMemberFunction0(void *const a1, void (__thiscall *a2)(void *const));
unsigned int __cdecl _FilterSetCurrentException(struct _EXCEPTION_POINTERS *a1, char a2);
int __cdecl _IsExceptionObjectToBeDestroyed(int a1);
int __cdecl __AdjustPointer(int a1, _DWORD *a2);
int __cdecl __FrameUnwindFilter(int a1);
void __cdecl __std_exception_copy(int a1, int a2);
void __cdecl __std_exception_destroy(int a1);
int __cdecl ValidateLocalCookies(int a1);
int __cdecl _except_handler4(PEXCEPTION_RECORD ExceptionRecord, char *TargetFrame, int a3);
wchar_t *__cdecl wcsstr(const wchar_t *Str, const wchar_t *SubStr);
void __stdcall  _CxxThrowException(void *pExceptionObject, _ThrowInfo *pThrowInfo);
void *__cdecl memmove(void *a1, const void *Src, size_t Size);
__vcrt_bool __cdecl __vcrt_initialize();
__vcrt_bool __cdecl __vcrt_thread_attach();
__vcrt_bool __cdecl __vcrt_thread_detach();
__vcrt_bool __cdecl __vcrt_uninitialize(__vcrt_bool Terminating);
__vcrt_bool __cdecl __vcrt_uninitialize_critical();
void *__cdecl memset(void *a1, int Val, size_t Size);
int __cdecl __std_type_info_compare(int a1, int a2);
PSLIST_ENTRY __cdecl __std_type_info_destroy_list(PSLIST_HEADER ListHead);
void __stdcall __vcrt_freefls(void *Block);
void __vcrt_freeptd_for_this_thread();
int __vcrt_getptd();
int __vcrt_getptd_noexit();
char __vcrt_initialize_ptd();
char __vcrt_uninitialize_ptd();
int __cdecl BuildCatchObjectHelperInternal<__FrameHandler3>(int a1, int *a2, int *a3, int a4);
void __cdecl BuildCatchObjectInternal<__FrameHandler3>(int a1, int *a2, int *a3, int a4);
void __cdecl CatchIt<__FrameHandler3>(
        PEXCEPTION_RECORD ExceptionRecord,
        struct EHRegistrationNode *a2,
        int a3,
        void *a4,
        struct _s_FuncInfo *a5,
        int a6,
        int a7,
        int *a8,
        int a9,
        struct EHRegistrationNode *TargetFrame);
int __cdecl FindHandler<__FrameHandler3>(
        struct EHExceptionRecord *ExceptionRecord,
        struct EHRegistrationNode *a2,
        void *a3,
        void *a4,
        struct _s_FuncInfo *a5,
        char a6,
        int a7,
        struct EHRegistrationNode *TargetFrame);
void __cdecl FindHandlerForForeignException<__FrameHandler3>(
        PEXCEPTION_RECORD ExceptionRecord,
        struct EHRegistrationNode *a2,
        void *a3,
        void *a4,
        struct _s_FuncInfo *a5,
        int a6,
        int a7,
        struct EHRegistrationNode *TargetFrame);
int __cdecl TypeMatchHelper<__FrameHandler3>(int a1, int a2, _BYTE *a3);
int __cdecl __InternalCxxFrameHandler<__FrameHandler3>(
        struct EHExceptionRecord *ExceptionRecord,
        struct EHRegistrationNode *a2,
        void *a3,
        void *a4,
        struct _s_FuncInfo *a5,
        int a6,
        struct EHRegistrationNode *TargetFrame,
        unsigned __int8 a8);
int __cdecl __InternalCxxFrameHandlerWrapper<__FrameHandler3>(
        struct EHExceptionRecord *ExceptionRecord,
        struct EHRegistrationNode *a2,
        void *a3,
        void *a4,
        struct _s_FuncInfo *a5,
        int a6,
        struct EHRegistrationNode *TargetFrame,
        unsigned __int8 a8);
char *__thiscall sub_10018359(char *this, int a2);
_DWORD *__thiscall sub_10018374(_DWORD *this);
bool __thiscall type_info::operator==(void *this, int a2);
void *__cdecl sub_100183AB(
        _DWORD *a1,
        struct EHRegistrationNode *a2,
        int a3,
        struct _s_FuncInfo *a4,
        void *a5,
        int a6,
        unsigned int a7);
void __cdecl  CallUnexpected();
int __cdecl ExFilterRethrow(struct _EXCEPTION_POINTERS *a1);
void __cdecl __FrameHandler3::FrameUnwindToEmptyState(
        struct EHRegistrationNode *a1,
        void *a2,
        const struct _s_FuncInfo *a3);
void __cdecl __FrameHandler3::FrameUnwindToState(
        struct EHRegistrationNode *a1,
        void *a2,
        const struct _s_FuncInfo *a3,
        int a4);
char __cdecl IsInExceptionSpec(struct EHExceptionRecord *a1, const struct _s_ESTypeList *a2);
void __stdcall _CallMemberFunction1(void *const a1, void (__thiscall *a2)(void *const, void *const), void *const a3);
void __stdcall _CallMemberFunction2(
        void *const a1,
        void (__thiscall *a2)(void *const, void *const, int),
        void *const a3,
        int a4);
const struct _s_ESTypeList *__cdecl __FrameHandler3::getESTypes(const struct _s_FuncInfo *a1);
int __stdcall _CallSettingFrame(int a1, int a2, int a3);
int (*__cdecl __except_validate_context_record(int a1))();
int __cdecl _local_unwind4(_DWORD *a1, int a2, unsigned int a3);
int __cdecl _unwind_handler4(int a1, int a2, int a3, _DWORD *a4);
int __thiscall _EH4_CallFilterFunc(int (*this)(void));
int __thiscall _EH4_TransferToHandler(int (__fastcall *this)(_DWORD, _DWORD));
void __fastcall _EH4_GlobalUnwind2(PVOID TargetFrame, PEXCEPTION_RECORD ExceptionRecord);
int __fastcall _EH4_LocalUnwind(int a1, unsigned int a2, int a3, _DWORD *a4);
char __vcrt_initialize_locks();
char __vcrt_uninitialize_locks();
FARPROC __cdecl try_get_function(int a1, const CHAR *lpProcName, int *a3, int *a4);
HINSTANCE __cdecl try_load_library_from_system_directory(LPCWSTR lpLibFileName);
DWORD __cdecl __vcrt_FlsAlloc(int a1);
int __cdecl __vcrt_FlsFree(DWORD dwTlsIndex);
LPVOID __cdecl __vcrt_FlsGetValue(DWORD dwTlsIndex);
int __cdecl __vcrt_FlsSetValue(DWORD dwTlsIndex, LPVOID lpTlsValue);
int __cdecl __vcrt_InitializeCriticalSectionEx(LPCRITICAL_SECTION lpCriticalSection, DWORD dwSpinCount, int a3);
void  unexpected();
__ehstate_t __cdecl __FrameHandler3::GetCurrentState(
        struct EHRegistrationNode *a1,
        void *a2,
        const struct _s_FuncInfo *a3);
void __cdecl __FrameHandler3::SetState(struct EHRegistrationNode *a1, const struct _s_FuncInfo *a2, __ehstate_t a3);
void __stdcall sub_10018C90(int a1);
int __userpurge _NLG_Notify@<eax>(int result@<eax>, int a2@<ebp>, int a3);
int __usercall sub_10018CC0@<eax>(int (*a1)(void)@<eax>);
__crt_cached_ptd_host *__thiscall __crt_cached_ptd_host::__crt_cached_ptd_host(
        __crt_cached_ptd_host *this,
        struct __crt_locale_pointers *const a2);
void __thiscall __crt_cached_ptd_host::~__crt_cached_ptd_host(__crt_cached_ptd_host *this);
unsigned int __thiscall __crt_cached_ptd_host::check_synchronize_global_state_index(__crt_cached_ptd_host *this);
struct __acrt_ptd *__thiscall __crt_cached_ptd_host::force_synchronize_per_thread_data(__crt_cached_ptd_host *this);
// Microsoft VisualC universal runtime
int __thiscall unknown_libname_7(__crt_cached_ptd_host *this);
void __usercall __acrt_call_reportfault(int a1@<ebx>, int a2@<edi>, int a3@<esi>, int a4, int a5, int a6);
int __cdecl sub_10018F0C(int a1);
void __cdecl _invalid_parameter(
        wchar_t *Expression,
        wchar_t *FunctionName,
        wchar_t *FileName,
        unsigned int LineNo,
        uintptr_t Reserved);
int __cdecl _invalid_parameter_internal(
        wchar_t *Expression,
        wchar_t *FunctionName,
        wchar_t *FileName,
        unsigned int LineNo,
        uintptr_t Reserved,
        struct __acrt_ptd **a6);
void __cdecl _invalid_parameter_noinfo();
void __cdecl  _invalid_parameter_noinfo_noreturn();
void __cdecl  _invoke_watson(
        const wchar_t *Expression,
        const wchar_t *FunctionName,
        const wchar_t *FileName,
        unsigned int LineNo,
        uintptr_t Reserved);
int __cdecl __acrt_locale_get_ctype_array_value(
        const unsigned __int16 *const Locale_pctype_array,
        const int Char_value,
        const int Mask);
int __cdecl common_vsprintf<__crt_stdio_output::standard_base,char>(
        int a1,
        int a2,
        _DWORD *a3,
        unsigned int a4,
        int a5,
        __crt_cached_ptd_host *a6,
        int a7);
int __cdecl common_vsprintf<__crt_stdio_output::standard_base,wchar_t>(
        int a1,
        int a2,
        _DWORD *a3,
        unsigned int a4,
        int a5,
        __crt_cached_ptd_host *a6,
        int a7);
int __thiscall __crt_stdio_output::formatting_buffer::count<char>(_DWORD *this);
int __thiscall __crt_stdio_output::formatting_buffer::count<wchar_t>(_DWORD *this);
char __thiscall sub_1001937A(_DWORD *this, unsigned int a2, int a3);
char __thiscall sub_100193FA(_DWORD *this, unsigned int a2, int a3);
bool __cdecl __crt_strtox::is_overflow_condition<unsigned long>(char a1, unsigned int a2);
bool __cdecl __crt_stdio_output::is_wide_character_specifier<char>(int a1, int a2, char a3, int a4);
char __cdecl __crt_stdio_output::is_wide_character_specifier<wchar_t>(char a1, int a2, __int16 a3, int a4);
// Microsoft VisualC universal runtime
_DWORD *__cdecl unknown_libname_8(_DWORD *a1, int a2, _DWORD *a3);
int __cdecl sub_10019549(__crt_cached_ptd_host *a1, char *a2, char **a3, int a4, char a5);
int __cdecl sub_1001975C(__crt_cached_ptd_host *a1, _WORD *a2, _DWORD *a3, int a4, char a5);
char *__thiscall __crt_stdio_output::formatting_buffer::scratch_data<char>(_DWORD *this);
char __thiscall sub_10019D5E(int this, int a2);
char __thiscall sub_10019EEB(int this, int a2);
char __thiscall sub_1001A07D(int this, char a2);
char __thiscall sub_1001A20A(int this, char a2);
char __thiscall sub_1001A39C(int this, char a2);
char __thiscall sub_1001A529(int this, char a2);
_BYTE *__thiscall sub_1001A6BB(_DWORD *this, unsigned int a2, int a3);
_WORD *__thiscall sub_1001A71D(_DWORD *this, unsigned int a2, int a3);
_BYTE *__thiscall sub_1001A78E(_DWORD *this, unsigned int a2, char a3);
_WORD *__thiscall sub_1001A80D(_DWORD *this, unsigned int a2, char a3);
_BYTE *__thiscall sub_1001A8A2(_DWORD *this, unsigned int a2, char a3);
_WORD *__thiscall sub_1001A91E(_DWORD *this, unsigned int a2, char a3);
_BYTE *__thiscall sub_1001A9A9(_DWORD *this, unsigned int a2, unsigned int a3, int a4);
_WORD *__thiscall sub_1001AA1D(_DWORD *this, unsigned int a2, unsigned int a3, int a4);
_BYTE *__thiscall sub_1001AA9D(_DWORD *this, unsigned __int64 a2, char a3);
_WORD *__thiscall sub_1001AB2F(_DWORD *this, unsigned int a2, unsigned int a3, char a4);
_BYTE *__thiscall sub_1001ABD4(_DWORD *this, unsigned int a2, unsigned int a3, char a4);
_WORD *__thiscall sub_1001AC5A(_DWORD *this, unsigned int a2, unsigned int a3, char a4);
// Microsoft VisualC universal runtime
_DWORD *__thiscall unknown_libname_9(_DWORD *this, _DWORD *a2, int a3, int a4, int a5, int a6, int a7);
// Microsoft VisualC universal runtime
_DWORD *__thiscall unknown_libname_10(_DWORD *this, _DWORD *a2, int a3, int a4, int a5, int a6, int a7);
void __thiscall __crt_stdio_output::formatting_buffer::~formatting_buffer(void **this);
// Microsoft VisualC universal runtime
void **__thiscall unknown_libname_11(void **this, void **a2);
char __cdecl sub_1001ADFD(char *a1, int a2);
// Microsoft VisualC universal runtime
char __stdcall unknown_libname_12(char a1, char a2);
// Microsoft VisualC universal runtime
char __stdcall unknown_libname_13(__int16 a1, char a2);
unsigned __int8 __cdecl sub_1001AEDC(unsigned __int8 *a1, int *a2);
// Microsoft VisualC universal runtime
char __thiscall unknown_libname_14(_DWORD *this, int *a2);
// Microsoft VisualC universal runtime
char __thiscall unknown_libname_15(_DWORD *this, int *a2);
int __thiscall __crt_stdio_output::output_processor<char,__crt_stdio_output::string_output_adapter<char>,__crt_stdio_output::standard_base<char,__crt_stdio_output::string_output_adapter<char>>>::process(
        int this);
int __thiscall __crt_stdio_output::output_processor<wchar_t,__crt_stdio_output::string_output_adapter<wchar_t>,__crt_stdio_output::standard_base<wchar_t,__crt_stdio_output::string_output_adapter<wchar_t>>>::process(
        int this);
char __cdecl sub_1001B540(int a1, int a2);
char __thiscall sub_1001B699(unsigned __int16 *this);
char __thiscall sub_1001B823(int this);
char __thiscall sub_1001BC62(int this);
int __cdecl sub_1001C178(int a1);
char __thiscall sub_1001C1CC(void *this);
char __thiscall sub_1001C23F(int *this);
char __thiscall sub_1001C2B3(int this);
char __thiscall sub_1001C46A(int this);
char __thiscall sub_1001C637(int this, int a2);
// Microsoft VisualC universal runtime
char __thiscall unknown_libname_16(char *this, int a2);
char __thiscall sub_1001C768(int this);
char __thiscall sub_1001C7ED(_DWORD *this);
char __thiscall sub_1001C80A(_DWORD *this);
char __thiscall sub_1001C827(_DWORD *this);
char __thiscall sub_1001C83D(_DWORD *this);
char __thiscall sub_1001C853(int this);
char __thiscall sub_1001C8C6(void *this);
int __thiscall sub_1001C93B(int this, int a2, int a3);
void __thiscall __crt_strtox::c_string_character_source<char>::unget(_DWORD *this, char a2);
void __thiscall __crt_strtox::c_string_character_source<wchar_t>::unget(_DWORD *this, __int16 a2);
void __thiscall __crt_cached_ptd_host::update_locale_slow(__crt_cached_ptd_host *this);
// Microsoft VisualC universal runtime
char __thiscall unknown_libname_17(_DWORD *this);
// Microsoft VisualC universal runtime
char __thiscall unknown_libname_18(_DWORD *this, __crt_cached_ptd_host *a2);
void __thiscall sub_1001CB07(int *this, void *Src, unsigned int a3, _DWORD *a4, int a5);
_DWORD *__thiscall sub_1001CB76(_DWORD *this, void *Src, unsigned int a3, _DWORD *a4, int a5);
int __cdecl __stdio_common_vsprintf(
        unsigned __int64 Options,
        char *Buffer,
        size_t BufferCount,
        const char *Format,
        _locale_t Locale,
        va_list ArgList);
int __cdecl __stdio_common_vswprintf(
        unsigned __int64 Options,
        wchar_t *Buffer,
        size_t BufferCount,
        const wchar_t *Format,
        _locale_t Locale,
        va_list ArgList);
// attributes: thunk
void __cdecl j___free_base(void *Block);
int __cdecl sub_1001CC90(int a1);
int __cdecl __acrt_convert_wcs_mbs_cp<char,wchar_t,_lambda_62f6974d9771e494a5ea317cc32e971c_,__crt_win32_buffer_internal_dynamic_resizing>(
        LPCCH lpMultiByteStr,
        int a2,
        int a3,
        UINT CodePage);
int __cdecl sub_1001CD4D(LPCCH lpMultiByteStr, int a2, UINT CodePage);
_LocaleUpdate *__thiscall _LocaleUpdate::_LocaleUpdate(_LocaleUpdate *this, struct __crt_locale_pointers *const a2);
int __cdecl __acrt_get_utf8_acp_compatibility_codepage();
// Microsoft VisualC universal runtime
void __thiscall unknown_libname_19(int this);
int __thiscall sub_1001CE45(int this, int a2);
int __cdecl sub_1001CE84(_DWORD *a1, int a2);
int __cdecl _mkdir(const char *Path);
int __cdecl common_fsopen<char>(_BYTE *a1, _BYTE *a2);
FILE *__cdecl fopen(const char *FileName, const char *Mode);
int __cdecl sub_1001CFDD(__int64 a1, __int64 a2, int *a3);
int __cdecl common_fseek(FILE *Stream, int a2, int a3, unsigned int a4, __crt_cached_ptd_host *a5);
char __cdecl common_fseek_binary_mode_read_only_fast_track_nolock(int *a1, __int64 a2, int a3);
int __cdecl common_fseek_nolock(FILE *Stream, __int64 liDistanceToMove, DWORD dwMoveMethod, int a4);
int __cdecl fseek(FILE *Stream, int Offset, int Origin);
int __cdecl common_ftell<long>(FILE *Stream, __crt_cached_ptd_host *a2);
int __cdecl common_ftell_nolock<long>(FILE *Stream, __crt_cached_ptd_host *a2);
unsigned int __cdecl common_ftell_nolock<__int64>(FILE *Stream, __crt_cached_ptd_host *a2);
int __cdecl common_ftell_read_mode_nolock(
        FILE *Stream,
        LARGE_INTEGER liDistanceToMove,
        __int64 a3,
        __crt_cached_ptd_host *a4);
DWORD __cdecl sub_1001D726(FILE *Stream, LARGE_INTEGER liDistanceToMove, __crt_cached_ptd_host *a3);
int __cdecl sub_1001D8EC(_WORD *a1, _WORD *a2, char a3);
unsigned int __cdecl _ftelli64_nolock_internal(FILE *Stream, __crt_cached_ptd_host *a2);
int __cdecl ftell(FILE *Stream);
unsigned int __cdecl sub_1001D990(void *a1, size_t Size, unsigned int a3, unsigned int a4, FILE *Stream);
size_t __cdecl fread(void *Buffer, size_t ElementSize, size_t ElementCount, FILE *Stream);
size_t __cdecl fread_s(void *Buffer, size_t BufferSize, size_t ElementSize, size_t ElementCount, FILE *Stream);
errno_t __cdecl memcpy_s(
        void *const Destination,
        const rsize_t DestinationSize,
        const void *const Source,
        const rsize_t SourceSize);
int __cdecl _fclose_internal(FILE *Stream, struct __crt_cached_ptd_host *a2);
int __cdecl _fclose_nolock_internal(FILE *Stream, struct __crt_cached_ptd_host *a2);
int __cdecl fclose(FILE *Stream);
int __cdecl sub_1001DDF4(char *String2);
const char *__cdecl common_getenv_nolock<char>(char *String2);
int __cdecl sub_1001DEE0(char *String2);
_DWORD *__cdecl sub_1001DEEB(unsigned int a1, int a2, unsigned int a3);
int __cdecl sub_1001DF6A(unsigned int a1);
int *__cdecl __acrt_errno_map_os_error(unsigned int a1);
int __cdecl __acrt_errno_map_os_error_ptd(unsigned int a1, int a2);
void *sub_1001E010();
void *sub_1001E025();
int __cdecl sub_1001E03A(__crt_cached_ptd_host *a1, wint_t *a2, wint_t **a3, int a4, char a5);
int __cdecl sub_1001E65D(int a1, _DWORD *a2, int a3);
int __cdecl __acrt_convert_wcs_mbs_cp<wchar_t,char,_lambda_0fec1a7b3f42a53036604e18c2d5e07e_,__crt_win32_buffer_no_resizing>(
        LPCWCH lpWideCharStr,
        int a2,
        int a3,
        unsigned int a4);
// Microsoft VisualC universal runtime
int __stdcall unknown_libname_20(unsigned int a1, LPCWCH lpWideCharStr, LPSTR lpMultiByteStr, int cbMultiByte);
// Microsoft VisualC universal runtime
int __thiscall unknown_libname_21(int this, int a2);
int __thiscall __crt_win32_buffer<char,__crt_win32_buffer_no_resizing>::set_to_nullptr(int this);
void __cdecl  abort();
int __acrt_initialize_stdio();
void __acrt_uninitialize_stdio();
void __cdecl _lock_file(FILE *Stream);
void __cdecl _unlock_file(FILE *Stream);
int __cdecl sub_1001E950(int a1, int a2);
int __cdecl _callnewh(size_t Size);
int __cdecl sub_1001E9A0(int a1);
_PNH __cdecl _query_new_handler();
_PNH __cdecl _set_new_handler(_PNH NewHandler);
// Microsoft VisualC universal runtime
int __cdecl unknown_libname_22(int a1);
// Microsoft VisualC universal runtime
uintptr_t __cdecl unknown_libname_23(int a1);
int __cdecl _seh_filter_dll(unsigned int ExceptionNum, struct _EXCEPTION_POINTERS *ExceptionPtr);
int __cdecl _seh_filter_exe(unsigned int ExceptionNum, struct _EXCEPTION_POINTERS *ExceptionPtr);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_4fdada1b837b2abbf20876fac97688ad_,_lambda_b57350f2640456a0859d250846f69caf_ &,_lambda_eed5e4f92b5b7d55fa22c48c484aaa54_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
void __thiscall _lambda_6e4b09c48022b2350581041d5f6b0c4c_::operator()(int **this);
void __cdecl common_exit(UINT uExitCode, enum _crt_exit_cleanup_mode a2, enum _crt_exit_return_mode a3);
void __cdecl  sub_1001EE30(UINT uExitCode, char a2);
bool __scrt_is_managed_app();
void __cdecl try_cor_exit_process(unsigned int a1);
int __cdecl sub_1001EF22(int a1);
void __cdecl _cexit();
void __cdecl  _exit(int Code);
int sub_1001EF56();
int __cdecl common_configure_argv<char>(int a1);
_DWORD *__cdecl sub_1001F09A(char *a1, char **a2, char *a3, _DWORD *a4, _DWORD *a5);
int __cdecl __acrt_allocate_buffer_for_argv(unsigned int a1, unsigned int a2, unsigned int a3);
errno_t __cdecl _configure_narrow_argv(_crt_argv_mode mode);
int sub_1001F266();
int common_initialize_environment_nolock<char>();
void *__cdecl sub_1001F2EC(char *Source);
// Microsoft VisualC universal runtime
void __cdecl unknown_libname_24(void **Block);
int initialize_environment_by_cloning_nolock<char>();
void __cdecl sub_1001F483(void ***a1);
void __cdecl sub_1001F49E(void ***a1);
// attributes: thunk
int sub_1001F4B9(void);
void __dcrt_uninitialize_environments_nolock();
// attributes: thunk
int common_initialize_environment_nolock<char>(void);
int __stdcall sub_1001F514(_DWORD *a1, int a2, _DWORD *a3);
int __stdcall sub_1001F56F(_DWORD *a1, int a2, _DWORD *a3);
int __thiscall sub_1001F5CA(int **this);
// Microsoft VisualC universal runtime
int __thiscall unknown_libname_25(_DWORD **this);
int __cdecl sub_1001F7B7(_onexit_t Function);
int __cdecl _execute_onexit_table(_onexit_table_t *Table);
int __cdecl _initialize_onexit_table(_onexit_table_t *Table);
int __cdecl _register_onexit_function(_onexit_table_t *Table, _onexit_t Function);
char sub_1001F867();
char initialize_c();
char sub_1001F88E();
char sub_1001F891();
char __usercall initialize_pointers@<al>(int a1@<esi>);
__vcrt_bool sub_1001F8C7();
char uninitialize_allocated_memory();
char uninitialize_allocated_io_buffers();
// Microsoft VisualC universal runtime
void __stdcall unknown_libname_26(void **a1);
__crt_bool __cdecl __acrt_initialize();
bool sub_1001F977();
char sub_1001F982();
__crt_bool __cdecl __acrt_uninitialize(__crt_bool Terminating);
__crt_bool __cdecl __acrt_uninitialize_critical(__crt_bool Terminating);
void __cdecl _initterm(_PVFV *First, _PVFV *Last);
int __cdecl _initterm_e(_PIFV *First, _PIFV *Last);
void  terminate();
// attributes: thunk
void j_nullsub_1();
errno_t __cdecl strcpy_s(char *Destination, rsize_t SizeInBytes, const char *Source);
int __cdecl strncmp(const char *Str1, const char *Str2, size_t MaxCount);
int __cdecl wcsncmp(const wchar_t *String1, const wchar_t *String2, size_t MaxCount);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_15ade71b0218206bbe3333a0c9b79046_,_lambda_da44e0f8b0f19ba52fefafb335991732_ &,_lambda_207f2d024fc103971653565357d6cd41_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_38edbb1296d33220d7e4dd0ed76b244a_,_lambda_5ce1d447e08cb34b2473517608e21441_ &,_lambda_fb385d3da700c9147fc39e65dd577a8c_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_6affb1475c98b40b75cdec977db92e3c_,_lambda_b8d4b9c228a6ecc3f80208dbb4b4a104_ &,_lambda_608742c3c92a14382c1684fc64f96c88_>(
        _DWORD *a1,
        struct __acrt_ptd *const **a2,
        _DWORD *a3);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_a7e850c220f1c8d1e6efeecdedd162c6_,_lambda_46720907175c18b6c9d2717bc0d2d362_ &,_lambda_9048902d66e8d99359bc9897bbb930a8_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
void __cdecl construct_ptd(struct __acrt_ptd *const a1, struct __crt_locale_data **const a2);
void __stdcall destroy_fls(struct __acrt_ptd *Block);
void __cdecl destroy_ptd(void **a1);
struct __acrt_ptd *sub_1001FE75();
void __cdecl replace_current_thread_locale_nolock(struct __acrt_ptd *const a1, struct __crt_locale_data *const a2);
void sub_1001FF68();
int sub_1001FFAC();
struct __acrt_ptd *sub_1001FFBA();
struct __acrt_ptd *sub_1001FFFD();
char *__cdecl sub_10020089(int a1, int a2);
char sub_100200D2();
char __acrt_uninitialize_ptd();
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_e5124f882df8998aaf41531e079ba474_,_lambda_3e16ef9562a7dcce91392c22ab16ea36_ &,_lambda_e25ca0880e6ef98be67edffd8c599615_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
__int32 sub_10020190();
int __acrt_uninitialize_locale();
struct __crt_locale_data *__cdecl sub_100201C2(int a1, struct __crt_locale_data **a2);
int __cdecl sub_100201EF(int a1, int *a2, int a3);
struct __crt_multibyte_data *__cdecl sub_10020220(int a1, struct __crt_multibyte_data **a2);
int __cdecl sub_1002024D(int a1, int *a2, int a3);
void __cdecl _free_base(void *Block);
HANDLE sub_100202C0();
LPVOID __cdecl sub_100202D0(unsigned int a1);
_BYTE *__cdecl sub_10020321(__m128i *a1, unsigned int a2);
int __cdecl sub_10020456(char *a1, unsigned int a2);
int __cdecl __acrt_fp_classify(int *a1);
char __cdecl fe_to_nearest(const double *a1, unsigned __int64 a2, __int16 a3);
int __cdecl sub_10020720(
        _DWORD *a1,
        char *Str,
        rsize_t a3,
        int a4,
        rsize_t a5,
        signed int Size,
        char a7,
        int a8,
        int a9,
        __crt_cached_ptd_host *a10);
int __cdecl sub_10020A5C(
        __int64 *a1,
        char *a2,
        rsize_t SizeInBytes,
        int a4,
        rsize_t a5,
        int a6,
        char a7,
        int a8,
        int a9,
        __crt_cached_ptd_host *a10);
int __cdecl sub_10020AEC(
        char *a1,
        rsize_t SizeInBytes,
        int a3,
        char a4,
        int a5,
        int a6,
        unsigned __int8 a7,
        __crt_cached_ptd_host *a8);
int __cdecl sub_10020C2F(
        __int64 *a1,
        char *Src,
        unsigned int a3,
        int a4,
        rsize_t SizeInBytes,
        size_t Size,
        int a7,
        __crt_cached_ptd_host *a8);
int __cdecl sub_10020CB8(char *Src, unsigned int a2, signed int Size, int a4, char a5, __crt_cached_ptd_host *a6);
int __cdecl sub_10020D98(
        __int64 *a1,
        char *Src,
        rsize_t SizeInBytes,
        int a4,
        rsize_t a5,
        signed int Size,
        char a7,
        int a8,
        int a9,
        __crt_cached_ptd_host *a10);
errno_t __cdecl fp_format_nan_or_infinity(
        int a1,
        unsigned __int8 a2,
        char *Destination,
        rsize_t SizeInBytes,
        unsigned __int8 a5);
void __cdecl shift_bytes(char *const a1, unsigned int a2, char *const Src, int a4);
char __cdecl should_round_up(double *a1, unsigned __int64 a2, __int16 a3, int a4);
errno_t __cdecl __acrt_fp_format(
        int *a1,
        char *Str,
        rsize_t SizeInBytes,
        int a4,
        rsize_t a5,
        int a6,
        size_t Size,
        char a8,
        int a9,
        int a10,
        __crt_cached_ptd_host *a11);
int __cdecl sub_1002113B(int *a1, LPSTR lpMultiByteStr, size_t Size, WCHAR WideCharStr, __crt_cached_ptd_host *a5);
int __cdecl sub_1002129F(LPWSTR lpWideCharStr, CHAR *lpMultiByteStr, char *a3, struct _Mbstatet *a4);
int __cdecl sub_100213CF(char *a1);
unsigned int __cdecl sub_10021410(unsigned int *a1, char *a2, int a3, __crt_mbstring *a4, struct _Mbstatet *a5);
int __usercall sub_100215C9@<eax>(
        struct __crt_cached_ptd_host *a1@<edi>,
        struct _Mbstatet *a2,
        unsigned __int16 a3,
        __crt_mbstring *a4,
        struct _Mbstatet *a5);
int __stdcall _lambda_0f007d4f94c691a9a85cf1869a09f0c3_::operator()(_BYTE *a1);
unsigned int __cdecl __crt_mbstring::__mbrtowc_utf8(
        __crt_mbstring *this,
        wchar_t *a2,
        const char *a3,
        __crt_mbstring *a4,
        struct _Mbstatet *a5);
unsigned int __cdecl __crt_mbstring::__mbsrtowcs_utf8(
        __crt_mbstring *this,
        wchar_t *a2,
        const char **a3,
        __crt_mbstring *a4,
        struct _Mbstatet *a5);
int __cdecl _fileno(FILE *Stream);
int __cdecl _get_printf_count_output();
void sub_10021832();
void __cdecl initialize_stdio_handles_nolock();
char __acrt_initialize_lowio();
char sub_100219F2();
unsigned int __cdecl filter_mbtowcs_flags(unsigned int a1, unsigned int a2);
int __cdecl __acrt_MultiByteToWideChar(
        UINT CodePage,
        unsigned int a2,
        LPCCH lpMultiByteStr,
        int cbMultiByte,
        LPWSTR lpWideCharStr,
        int cchWideChar);
int sub_10021AE0();
int sub_10021B0A();
int sub_10021B35();
int sub_10021B60();
FARPROC __cdecl sub_10021B8B(int a1, LPCSTR lpProcName, _DWORD *a3, _DWORD *a4);
HINSTANCE __cdecl try_load_library_from_system_directory(LPCWSTR lpLibFileName);
int __stdcall sub_10021CBB(int a1);
int __stdcall __acrt_AreFileApisANSI();
int __stdcall sub_10021D29(
        wchar_t *a1,
        DWORD dwCmpFlags,
        PCNZWCH lpString1,
        int cchCount1,
        PCNZWCH lpString2,
        int cchCount2,
        int a7,
        int a8,
        int a9);
DWORD __stdcall sub_10021D86(void (__stdcall *a1)(PVOID lpFlsData));
BOOL __stdcall sub_10021D92(DWORD a1);
int sub_10021D9E();
PVOID __stdcall sub_10021DAB(DWORD a1);
BOOL __stdcall sub_10021DB7(DWORD a1, void *a2);
BOOL __stdcall sub_10021DC3(struct _RTL_CRITICAL_SECTION *a1, DWORD a2, DWORD a3);
int __stdcall sub_10021DCF(
        wchar_t *a1,
        DWORD dwMapFlags,
        LPCWSTR lpSrcStr,
        int cchSrc,
        LPWSTR lpDestStr,
        int cchDest,
        int a7,
        int a8,
        int a9);
int __stdcall __acrt_LocaleNameToLCID(wchar_t *a1, int a2);
bool __thiscall sub_10021E5D(void *this);
bool sub_10021E80();
int __cdecl __acrt_uninitialize_winapi_thunks(char a1);
char __cdecl __vcrt_uninitialize_winapi_thunks(char a1);
int __cdecl _wmkdir(const wchar_t *Path);
_DWORD *__cdecl __acrt_stdio_allocate_stream(_DWORD *a1);
int __cdecl __acrt_stdio_free_stream(int a1);
FILE **__cdecl find_or_allocate_unused_stream_nolock(FILE **a1);
struct __acrt_stdio_stream_mode *__cdecl sub_10022077(struct __acrt_stdio_stream_mode *a1, _BYTE *a2);
int __cdecl sub_100222B8(char *FileName, _BYTE *a2, int ShareFlag, int a4);
char __cdecl __acrt_stdio_parse_mode_D(struct __acrt_stdio_stream_mode *a1);
char __cdecl __acrt_stdio_parse_mode_T(struct __acrt_stdio_stream_mode *a1);
char __cdecl __acrt_stdio_parse_mode_b(struct __acrt_stdio_stream_mode *a1);
bool __cdecl __acrt_stdio_parse_mode_c(struct __acrt_stdio_stream_mode *a1, bool *a2);
bool __cdecl __acrt_stdio_parse_mode_n(struct __acrt_stdio_stream_mode *a1, bool *a2);
bool __cdecl __acrt_stdio_parse_mode_plus(struct __acrt_stdio_stream_mode *a1, bool *a2);
char __cdecl __acrt_stdio_parse_mode_t(struct __acrt_stdio_stream_mode *a1);
char __cdecl __acrt_stdio_parse_mode_x(struct __acrt_stdio_stream_mode *a1);
int __cdecl sub_1002244F(char *FileName, _BYTE *a2, int ShareFlag, int a4);
int __cdecl common_lseek<__int64>(
        int FileHandle,
        LARGE_INTEGER liDistanceToMove,
        DWORD dwMoveMethod,
        __crt_cached_ptd_host *a4);
DWORD __cdecl common_lseek_nolock<__int64>(int FileHandle, LARGE_INTEGER liDistanceToMove, DWORD dwMoveMethod, int a4);
int __cdecl _lseeki64_internal(
        int FileHandle,
        LARGE_INTEGER liDistanceToMove,
        DWORD dwMoveMethod,
        __crt_cached_ptd_host *a4);
DWORD __cdecl _lseeki64_nolock(int FileHandle, LARGE_INTEGER liDistanceToMove, DWORD dwMoveMethod);
DWORD __cdecl _lseeki64_nolock_internal(int FileHandle, LARGE_INTEGER liDistanceToMove, DWORD dwMoveMethod, int a4);
void __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_2866be3712abc81a800a822484c830d8_,_lambda_39ca0ed439415581b5b15c265174cece_ &,_lambda_2b24c74d71094a6cd0cb82e44167d71b_>(
        FILE **a1,
        FILE ***a2,
        FILE **a3);
int __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_2cc53f568c5a2bb6f192f930a45d44ea_,_lambda_ab61a845afdef5b7c387490eaf3616ee_ &,_lambda_c2ffc0b7726aa6be21d5f0026187e748_>(
        _DWORD *a1,
        FILE ***a2,
        _DWORD *a3);
int __cdecl sub_100227B6(char a1);
char __cdecl common_flush_all_should_try_to_flush_stream(int a1, _DWORD *a2);
bool __cdecl is_stream_flushable_or_commitable(__int16 a1);
int __cdecl __acrt_stdio_flush_nolock(FILE *Stream, __crt_cached_ptd_host *a2);
int __cdecl _fflush_nolock(FILE *Stream);
int sub_10022924();
int __cdecl sub_1002292D(int FileHandle, char *a2, int a3);
unsigned int __cdecl sub_10022A80(int FileHandle, __int16 *a2, int a3);
int __cdecl translate_ansi_or_utf8_nolock(
        int FileHandle,
        char *lpMultiByteStr,
        unsigned int a3,
        LPWSTR lpWideCharStr,
        unsigned int cchWideChar);
unsigned int __cdecl sub_10022D97(int a1, char *a2, int a3);
int __cdecl _read(int FileHandle, void *DstBuf, unsigned int MaxCharCount);
unsigned int __cdecl sub_10022F2D(unsigned int FileHandle, LPWSTR lpWideCharStr, DWORD nNumberOfBytesToRead);
int __cdecl sub_100232B9(FILE *Stream);
int __cdecl sub_10023444(FILE *a1);
int __stdcall __crt_seh_guarded_call<int>::operator()<_lambda_d422a76eb4c3bf3ad751449ab71a6ea4_,_lambda_c9ba49e555ba839a7b07aa3fbecb7617_ &,_lambda_9476263c8ee91a25d21c55370bdb50de_>(
        _DWORD *a1,
        int a2,
        _DWORD *a3);
int __cdecl sub_100234E0(int a1, __crt_cached_ptd_host *a2);
int __cdecl _close_nolock(int FileHandle);
int __cdecl _close_nolock_internal(int FileHandle, int a2);
int __cdecl __acrt_stdio_free_buffer_nolock(int a1);
int __cdecl _strnicoll(const char *String1, const char *String2, size_t MaxCount);
int __cdecl _strnicoll_l(const char *String1, const char *String2, size_t MaxCount, _locale_t Locale);
char sub_10023784();
void __cdecl __acrt_lock(int a1);
char __acrt_uninitialize_locks();
void __cdecl __acrt_unlock(int a1);
int __cdecl iswctype(wint_t C, wctype_t Type);
int __acrt_initialize_timeset();
unsigned int __cdecl filter_wcstomb_flags(unsigned int a1, unsigned int a2);
int __cdecl sub_10023952(
        unsigned int a1,
        unsigned int a2,
        LPCWCH lpWideCharStr,
        int cchWideChar,
        LPSTR lpMultiByteStr,
        int cbMultiByte,
        const CHAR *a7,
        BOOL *a8);
void __cdecl _freea_crt(int a1);
int __stdcall __crt_seh_guarded_call<void (__cdecl *)(int)>::operator()<_lambda_cbab9ec6f41b0180b23cc171c22676b0_,_lambda_44731a7d0e6d81c3e6aa82d741081786_ &,_lambda_4b292cb8dd18144e164572427af410ab_>(
        int *a1,
        int a2,
        int *a3);
void (__cdecl **__cdecl get_global_action_nolock(int a1))(int);
struct __crt_signal_action_t *__cdecl siglookup(int a1, struct __crt_signal_action_t *const a2);
int __acrt_get_sigabrt_handler();
int __cdecl __acrt_initialize_signal_handlers(int a1);
int __cdecl raise(int Signal);
LPVOID __cdecl sub_10023CF0(unsigned int a1, unsigned int a2);
int __cdecl _fcloseall();
char __acrt_app_verifier_enabled();
unsigned int __acrt_is_secure_process();
BOOL __acrt_get_process_end_policy();
// Microsoft VisualC universal runtime
int __cdecl unknown_libname_27(unsigned int a1, unsigned int a2);
int __cdecl sub_10023E5F(LPCWCH lpWideCharStr, int a2, int a3, unsigned int a4);
int __cdecl common_expand_argv_wildcards<char>(unsigned __int8 **a1, int *a2);
int __cdecl copy_and_add_argument_to_buffer<char>(const char *a1, int a2, int a3, int a4);
int __cdecl sub_10024153(unsigned __int8 *Start, unsigned __int8 *Pos, _DWORD *a3);
// Microsoft VisualC universal runtime
void __thiscall unknown_libname_28(void ***this);
int __thiscall sub_10024404(int this, int a2);
// Microsoft VisualC universal runtime
int __thiscall unknown_libname_29(LPVOID *this);
int __cdecl __acrt_expand_narrow_argv_wildcards(unsigned __int8 **a1, int *a2);
int __cdecl __acrt_GetModuleFileNameA(HMODULE hModule, int a2, int a3);
void __stdcall __crt_seh_guarded_call<void>::operator()<_lambda_4fdada1b837b2abbf20876fac97688ad_,_lambda_b57350f2640456a0859d250846f69caf_ &,_lambda_eed5e4f92b5b7d55fa22c48c484aaa54_>(
        int *a1,
        int a2,
        int *a3);
// Microsoft VisualC universal runtime
volatile signed __int32 *__thiscall unknown_libname_30(volatile signed __int32 ****this);
const wchar_t *__cdecl CPtoLocaleName(int a1);
UINT __cdecl getSystemCP(UINT a1);
void __cdecl setSBCS(struct __crt_multibyte_data *a1);
void __cdecl setSBUpLow(struct __crt_multibyte_data *a1);
// bad sp value at call has been detected, the output may be wrong!
int __usercall setmbcp_internal@<eax>(
        void *a1@<ebp>,
        UINT a2,
        bool a3,
        struct __acrt_ptd *const a4,
        struct __crt_multibyte_data **const a5);
struct __crt_multibyte_data *__cdecl update_thread_multibyte_data_internal(
        struct __acrt_ptd *const a1,
        struct __crt_multibyte_data **const a2);
char __usercall __acrt_initialize_multibyte@<al>(void *a1@<ebp>);
struct __crt_multibyte_data *sub_10024B37();
int __cdecl _setmbcp_nolock(UINT a1, struct __crt_multibyte_data *a2);
BOOL __cdecl x_ismbbtype_l(struct __crt_locale_pointers *a1, unsigned __int8 a2, int a3, unsigned __int8 a4);
int __cdecl _ismbblead(unsigned int Ch);
char __acrt_initialize_command_line();
const wchar_t *__cdecl find_end_of_double_null_terminated_sequence(const wchar_t *a1);
const wchar_t *__dcrt_get_narrow_environment_from_os();
int __cdecl common_set_variable_in_environment_nolock<char>(char *Str, int a2);
_BYTE *__cdecl copy_environment<char>(const char **a1);
_BYTE *sub_100251B5();
int __cdecl find_in_environment_nolock<char>(char *String1, size_t MaxCount);
int __cdecl __dcrt_set_variable_in_narrow_environment_nolock(char *a1, int a2);
void *__cdecl _recalloc_base(void *Block, size_t Count, size_t Size);
void *__cdecl _recalloc(void *Block, size_t Count, size_t Size);
HANDLE sub_100252C0();
bool __acrt_initialize_heap();
char sub_100252F0();
HANDLE sub_10025300();
char __cdecl __acrt_execute_initializers(_DWORD *a1, _DWORD *a2);
char __cdecl __acrt_execute_uninitializers(int a1, int a2);
bool __acrt_has_user_matherr();
int __cdecl sub_100253C0(int a1);
int __cdecl sub_100253D0(int a1);
int __cdecl __acrt_add_locale_ref(int a1);
void __cdecl sub_10025486(char *Block);
signed __int32 __cdecl __acrt_locale_add_lc_time_reference(int a1);
void __cdecl __acrt_locale_free_lc_time_if_unreferenced(void **Block);
signed __int32 __cdecl __acrt_locale_release_lc_time_reference(int a1);
signed __int32 __cdecl __acrt_release_locale_ref(signed __int32 a1);
int __acrt_update_thread_locale_data();
int __cdecl _updatetlocinfoEx_nolock(signed __int32 *a1, int a2);
void __cdecl __acrt_locale_free_monetary(void **a1);
void __cdecl __acrt_locale_free_numeric(void **a1);
void __cdecl free_crt_array_internal(void **a1, unsigned int a2);
void __cdecl __acrt_locale_free_time(void **a1);
BOOL __cdecl sub_10025A13(
        struct __crt_locale_pointers *a1,
        DWORD dwInfoType,
        LPCCH lpMultiByteStr,
        int cbMultiByte,
        LPWORD lpCharType,
        UINT CodePage,
        int a7);
int sub_10025B20();
int __cdecl _set_new_mode(int NewMode);
bool __cdecl check_trailing(_BYTE *a1, int a2);
bool __cdecl should_round_up(int a1, char *a2, int a3, int a4, int a5);
int __cdecl __acrt_fp_strflt_to_string(
        char *a1,
        unsigned int a2,
        int a3,
        int a4,
        int a5,
        int a6,
        __crt_cached_ptd_host *a7);
int __cdecl sub_10025D10(int *a1, unsigned int *a2);
int __cdecl sub_100261E7(__int64 a1, int a2, int a3, int *a4, char *a5, rsize_t SizeInBytes);
int sub_100276C0();
unsigned int __usercall sub_100276CF@<eax>(
        struct __crt_cached_ptd_host *a1@<esi>,
        _BYTE *a2,
        unsigned int a3,
        __crt_mbstring *a4,
        struct _Mbstatet *a5);
__crt_mbstring *__cdecl __crt_mbstring::reset_and_return(__crt_mbstring *this, _DWORD *a2);
unsigned int __cdecl __crt_mbstring::return_illegal_sequence(__crt_mbstring *this, struct _Mbstatet *a2);
int __cdecl _isatty(int FileHandle);
char *__acrt_lowio_create_handle_array();
void __cdecl __acrt_lowio_destroy_handle_array(LPCRITICAL_SECTION lpCriticalSection);
int __cdecl __acrt_lowio_ensure_fh_exists(unsigned int a1);
void __cdecl __acrt_lowio_lock_fh(int a1);
int __cdecl __acrt_lowio_set_os_handle(unsigned int a1, struct _RTL_CRITICAL_SECTION_DEBUG *hHandle);
void __cdecl __acrt_lowio_unlock_fh(int a1);
int _alloc_osfhnd();
int __cdecl _free_osfhnd(unsigned int a1);
intptr_t __cdecl _get_osfhandle(int FileHandle);
int __cdecl GetTableIndexFromLocaleName(const wchar_t *a1);
int __cdecl __acrt_DownlevelLocaleNameToLCID(wchar_t *a1);
int __cdecl sub_10027CBD(unsigned __int16 *a1, unsigned __int16 *a2, int a3);
int __cdecl _strnicmp(const char *String1, const char *String2, size_t MaxCount);
int __cdecl _strnicmp_l(const char *String1, const char *String2, size_t MaxCount, _locale_t Locale);
int __cdecl common_sopen_dispatch<char>(LPCCH lpMultiByteStr, int a2, int a3, int a4, int *a5, int a6);
int __cdecl configure_text_mode(int FileHandle, char a2, int a3, int a4, int a5, int a6, int a7, int a8, _BYTE *a9);
HANDLE __cdecl create_file(
        const WCHAR *lpFileName,
        struct _SECURITY_ATTRIBUTES *lpSecurityAttributes,
        int a3,
        DWORD dwDesiredAccess,
        DWORD dwCreationDisposition,
        DWORD dwShareMode,
        int a7,
        int a8);
unsigned int __cdecl decode_open_create_flags(__int16 a1);
int __cdecl sub_1002820F(int a1, int a2, int a3, char a4);
int __cdecl truncate_ctrl_z_if_present(int FileHandle);
int __cdecl _sopen_nolock(int a1, int a2, LPCCH lpMultiByteStr, int a4, int a5, int a6);
errno_t __cdecl _sopen_s(int *FileHandle, const char *FileName, int OpenFlag, int ShareFlag, int PermissionMode);
int __cdecl _wsopen_nolock(_DWORD *a1, int *a2, const WCHAR *a3, unsigned int a4, int a5, char a6);
int __stdcall __crt_seh_guarded_call<int>::operator()<_lambda_9e9de3de5fa147e2223d7db92bc10aa6_,_lambda_38ce7e780aa69e748d6df282ebc68efe_ &,_lambda_8ca6da459f0f6780f1cff60fdc3d00e5_>(
        int *a1,
        int **a2,
        int *a3);
int __cdecl _commit(int FileHandle);
DWORD *__cdecl sub_1002890A(DWORD *a1, int a2, void *a3, int a4, struct _Mbstatet *a5);
DWORD *__cdecl write_double_translated_unicode_nolock(DWORD *a1, unsigned int a2, int a3);
bool __cdecl write_requires_double_translation_nolock(int FileHandle, struct __crt_cached_ptd_host *a2);
DWORD *__cdecl write_text_ansi_nolock(DWORD *a1, int a2, unsigned int a3, int a4);
DWORD *__cdecl write_text_utf16le_nolock(DWORD *a1, int a2, unsigned __int16 *a3, int a4);
DWORD *__cdecl write_text_utf8_nolock(DWORD *a1, int a2, unsigned int a3, int a4);
int __cdecl _write(int FileHandle, const void *Buf, unsigned int MaxCharCount);
int __cdecl _write_internal(int FileHandle, int a2, int a3, __crt_cached_ptd_host *a4);
int __cdecl _write_nolock(int FileHandle, const void *a2, DWORD a3, __crt_cached_ptd_host *a4);
int __cdecl __acrt_stdio_allocate_buffer_nolock(_DWORD *a1);
int __cdecl InternalCompareStringA(
        struct __crt_locale_pointers *a1,
        wchar_t *a2,
        DWORD dwCmpFlags,
        char *String,
        int Count,
        const char *a6,
        int a7,
        UINT CodePage);
int __cdecl __acrt_CompareStringA(
        struct __crt_locale_pointers *a1,
        wchar_t *a2,
        DWORD dwCmpFlags,
        char *String,
        size_t Count,
        char *a6,
        size_t a7,
        UINT CodePage);
BOOL __cdecl __acrt_GetStringTypeW(DWORD dwInfoType, LPCWCH lpSrcStr, int cchSrc, LPWORD lpCharType);
void __cdecl sub_10029770(char *a1, unsigned int a2, int a3, int (__cdecl *a4)(char *, char *));
int __cdecl sub_10029BAC(_BYTE *a1, int a2, int a3, int a4);
int __cdecl sub_10029C77(_BYTE *a1, int a2, int a3, int a4);
char *__cdecl strpbrk(const char *Str, const char *Control);
unsigned __int8 *__cdecl _mbsdec(const unsigned __int8 *Start, const unsigned __int8 *Pos);
unsigned __int8 *__cdecl _mbsdec_l(const unsigned __int8 *Start, const unsigned __int8 *Pos, _locale_t Locale);
int __cdecl __acrt_LCMapStringA_stat(
        struct __crt_locale_pointers *a1,
        wchar_t *a2,
        DWORD dwMapFlags,
        char *String,
        int Count,
        LPWSTR lpDestStr,
        int cchDest,
        UINT CodePage,
        int a9);
int __cdecl sub_10029F61(
        struct __crt_locale_pointers *a1,
        wchar_t *a2,
        DWORD dwMapFlags,
        char *String,
        size_t Count,
        LPWSTR lpDestStr,
        int cchDest,
        UINT CodePage,
        int a9);
int __usercall sub_10029FAA@<eax>(void *a1@<ebp>);
BOOL __cdecl __acrt_SetEnvironmentVariableA(LPCCH lpMultiByteStr, LPCCH a2);
size_t __cdecl _msize(void *Block);
size_t __cdecl sub_1002A090(void *Block);
void *__cdecl _realloc_base(void *Block, size_t Size);
int __cdecl sub_1002A110(_DWORD *a1, int a2, int a3);
int __cdecl fegetenv(fenv_t *Env);
BOOL __cdecl sub_1002A1A0(_DWORD *a1);
int __cdecl sub_1002A200(unsigned int *a1);
__m128d __usercall _libm_sse2_log10_precise@<xmm0>(__m128d result@<xmm0>);
double __usercall sub_1002A550@<st0>(__m128i a1@<xmm0>, const __m128i a2);
unsigned int __cdecl sub_1002A647(unsigned int a1);
unsigned int __cdecl sub_1002A6FD(unsigned int a1);
int __cdecl sub_1002A7AC(unsigned int a1);
unsigned int __cdecl sub_1002A866(unsigned int a1);
int __cdecl sub_1002A91F(unsigned int a1);
unsigned int __acrt_fenv_get_control();
int __usercall __acrt_fenv_get_status@<eax>(unsigned __int16 a1@<fpstat>);
int __cdecl __acrt_fenv_set_control(unsigned int a1);
unsigned int __cdecl __acrt_fenv_set_status(int a1);
int sub_1002ABE3();
int __cdecl __ascii_strnicmp(unsigned __int8 *a1, unsigned __int8 *a2, int a3);
errno_t __cdecl _get_fmode(int *PMode);
int __cdecl sub_1002AC7E(int a1, int a2);
__crt_seek_guard *__thiscall __crt_seek_guard::__crt_seek_guard(__crt_seek_guard *this, int FileHandle, __int64 a3);
int __cdecl _chsize_nolock(int FileHandle, LARGE_INTEGER liDistanceToMove);
int __cdecl _chsize_nolock_internal(int FileHandle, LARGE_INTEGER liDistanceToMove, __crt_cached_ptd_host *a3);
wint_t __cdecl _putwch_nolock(wchar_t Character);
size_t __cdecl __strncnt(const char *String, size_t Count);
int __cdecl sub_1002AFB8(int a1);
int __usercall sub_1002B074@<eax>(char a1@<fpstat>);
int __cdecl sub_1002B18A(int a1, int a2);
int __cdecl sub_1002B4DA(unsigned int a1);
_DWORD *__cdecl __libm_error_support(__int64 *a1, __int64 *a2, __int64 *a3, int a4);
double __usercall _CIlog10@<st0>(double x@<st0>);
int __acrt_initialize_sse2();
double __usercall sub_1002B910@<st0>(double result@<st0>, double a2);
int __acrt_initialize_fmode();
void __cdecl __dcrt_lowio_initialize_console_output();
BOOL sub_1002BA1A();
// Microsoft VisualC universal runtime
HANDLE unknown_libname_31();
// Microsoft VisualC universal runtime
BOOL __cdecl unknown_libname_32(void *lpBuffer, DWORD nNumberOfCharsToWrite, LPDWORD lpNumberOfCharsWritten);
unsigned int __cdecl __set_fpsr_sse2(unsigned int a1);
int __usercall _clrfp@<eax>(__int16 a1@<fpstat>);
int sub_1002BB36();
void _set_statfp();
int __usercall _statfp@<eax>(__int16 a1@<fpstat>);
int __usercall _CIlog10_pentium4@<eax>(__int64 a1@<st0>);
double __usercall start_0@<st0>(__m128d a1@<xmm0>, double a2);
void __usercall sub_1002BE54(char a1@<ch>, int a2@<ebp>);
void zerotoxdone();
void expbigret();
double __fastcall _rtforexpinf(char a1);
// positive sp value has been detected, the output may be wrong!
void __usercall _ffexpm1(int a1@<ebp>, long double a2@<st0>);
int __usercall isintTOS@<eax>(double a1@<st0>);
void isintTOSret();
void notanint();
void evenint();
double __usercall usepowhlp@<st0>(int a1@<ebp>, double a2@<st1>, __int64 a3@<st0>);
double __usercall _twoToTOS@<st0>(double a1@<st0>);
double __usercall _convertTOStoQNaN@<st0>(int a1@<eax>, double result@<st0>);
double __fastcall _fload_withFB(int a1, _DWORD *a2);
int __cdecl _checkTOS_withFB(int a1, int a2);
void _startTwoArgErrorHandling();
double __usercall _startOneArgErrorHandling@<st0>(
        int a1@<eax>,
        int a2@<edx>,
        int a3@<ecx>,
        double a4@<st0>,
        __int16 a5,
        int a6,
        int a7,
        int a8);
double __cdecl _frnd(double a1);
double __usercall sub_1002C4D0@<st0>(int a1@<ebp>, int a2, int a3, int a4, int a5, double a6, int a7);
BOOL __cdecl sub_1002C610(unsigned int a1, __int64 *a2, __int16 a3);
int __cdecl _raise_exc(ULONG_PTR Arguments, int a2, int a3, int a4, int a5, int a6);
unsigned int __usercall sub_1002C970@<eax>(
        __int16 a1@<fpstat>,
        unsigned int *Arguments,
        unsigned int *a3,
        char a4,
        int a5,
        unsigned int *a6,
        unsigned int *a7,
        int a8);
_DWORD *__cdecl _set_errno_from_matherr(int a1);
double __cdecl sub_1002CCE0(int a1, int a2, int a3, int a4, int a5, int a6, double a7);
double __cdecl sub_1002CDE0(double a1, int *a2);
int __cdecl sub_1002CEF0(int a1, int a2);
int __cdecl sub_1002CF70(__int64 a1, double a2, unsigned __int64 *a3);
_DWORD *__usercall _87except@<eax>(int a1@<ebp>, int a2, int a3, __int16 *a4);
int __cdecl sub_1002D277(double a1);
int _alloca_probe_16();
int _alloca_probe_8();
int __cdecl _FindPESection(int a1, unsigned int a2);
BOOL __cdecl _IsNonwritableInCurrentImage(int a1);
BOOL __cdecl _ValidateImageBase(int a1);
unsigned int __stdcall _aulldvrm(unsigned __int64 a1, __int64 a2);
int __stdcall _alldiv(unsigned __int64 a1, __int64 a2);
void *__usercall _alloca_probe@<eax>(unsigned int a1@<eax>, int a2@<ecx>);
unsigned __int64 __stdcall _allmul(__int64 a1, __int64 a2);
int __stdcall _alldvrm(unsigned __int64 a1, __int64 a2);
unsigned __int64 __stdcall _allrem(unsigned __int64 a1, __int64 a2);
unsigned __int64 __usercall _aullshr@<edx:eax>(unsigned __int64 a1@<edx:eax>, unsigned __int8 a2@<cl>);
int __usercall _allshl@<eax>(__int64 a1@<edx:eax>, unsigned __int8 a2@<cl>);
char *__cdecl strrchr(const char *Str, int Ch);
char *__cdecl strchr(const char *Str, int Val);
int __cdecl _filter_x86_sse2_floating_point_exception_default(int a1);
void __cdecl sub_1002F5B0();
void __cdecl sub_1002F610();
