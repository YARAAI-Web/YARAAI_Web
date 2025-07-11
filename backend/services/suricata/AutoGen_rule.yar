C:\Users\박정빈\new_yara>python main.py 12.json  

===== 생성된 YARA 룰 =====

rule AutoGen_edc0784c : Malware {
    meta:
        description = "Auto-generated YARA rule based on API usage"
        author = "YARRAI AutoGen"
        date = "2025-07-10"
        md5 = "edc0784c522abc4891d9bedac02e0a1c"
        sha256 = "fb2c4271b507256b7472016f29a6da068d394995dad0a9965ec8dc19b026f44c"

    strings:
        $s0 = "BOOL" fullword ascii
        $s1 = "BYREF" fullword ascii
        $s2 = "BYTE4" fullword ascii
        $s3 = "DWORD" fullword ascii
        $s4 = "DllEntryPoint" fullword ascii
        $s5 = "DllMain" fullword ascii
        $s6 = "ExceptionList" fullword ascii
        $s7 = "HINSTANCE" fullword ascii
        $s8 = "IsProcessorFeaturePresent" fullword ascii
        $s9 = "JUMPOUT" fullword ascii
        $s10 = "LABEL_14" fullword ascii
        $s11 = "LABEL_9" fullword ascii
        $s12 = "LOBYTE" fullword ascii
        $s13 = "LPVOID" fullword ascii
        $s14 = "NtCurrentTeb" fullword ascii
        $s15 = "NtTib" fullword ascii
        $s16 = "PVOID" fullword ascii
        $s17 = "SEH_10032100" fullword ascii
        $s18 = "StackBase" fullword ascii
        $s19 = "StackCookie" fullword ascii
        $s20 = "StackLimit" fullword ascii
        $s21 = "ValidateLocalCookies" fullword ascii
        $s22 = "_BYTE" fullword ascii
        $s23 = "_DWORD" fullword ascii
        $s24 = "_EH4_CallFilterFunc" fullword ascii
        $s25 = "_EH4_GlobalUnwind2" fullword ascii
        $s26 = "_EH4_LocalUnwind" fullword ascii
        $s27 = "_EH4_TransferToHandler" fullword ascii
        $s28 = "_IsNonwritableInCurrentImage" fullword ascii
        $s29 = "_NLG_Call" fullword ascii
        $s30 = "_NLG_Notify" fullword ascii
        $s31 = "_SEH_epilog4" fullword ascii
        $s32 = "_SEH_prolog4" fullword ascii
        $s33 = "_ST6" fullword ascii
        $s34 = "_TEB" fullword ascii
        $s35 = "_UNKNOWN" fullword ascii
        $s36 = "_WORD" fullword ascii
        $s37 = "__DestructExceptionObject" fullword ascii
        $s38 = "__FSCALE__" fullword ascii
        $s39 = "__asm" fullword ascii
        $s40 = "__cdecl" fullword ascii
        $s41 = "__except_validate_context_record" fullword ascii
        $s42 = "__fastcall" fullword ascii
        $s43 = "__fastfail" fullword ascii
        $s44 = "__get_entropy" fullword ascii
        $s45 = "__guard_check_icall_fptr" fullword ascii
        $s46 = "__int16" fullword ascii
        $s47 = "__int64" fullword ascii
        $s48 = "__int8" fullword ascii
        $s49 = "__return_address" fullword ascii
        $s50 = "__scrt_dllmain_crt_thread_attach" fullword ascii
        $s51 = "__security_check_cookie" fullword ascii
        $s52 = "__security_cookie" fullword ascii
        $s53 = "__security_init_cookie" fullword ascii
        $s54 = "__stdcall" fullword ascii
        $s55 = "__thiscall" fullword ascii
        $s56 = "__usercall" fullword ascii
        $s57 = "__vcrt_getptd_noexit" fullword ascii
        $s58 = "__vcrt_thread_attach" fullword ascii
        $s59 = "__vcrt_thread_detach" fullword ascii
        $s60 = "_fFEXP" fullword ascii
        $s61 = "_ffexpm1" fullword ascii
        $s62 = "_guard_check_icall_nop" fullword ascii
        $s63 = "_local_unwind2" fullword ascii
        $s64 = "_local_unwind4" fullword ascii
        $s65 = "_unwind_handler" fullword ascii
        $s66 = "_unwind_handler4" fullword ascii
        $s67 = "a62c" fullword ascii
        $s68 = "alloca" fullword ascii
        $s69 = "attributes" fullword ascii
        $s70 = "b31406030a7b" fullword ascii
        $s71 = "b95e" fullword ascii
        $s72 = "been" fullword ascii
        $s73 = "bool" fullword ascii
        $s74 = "break" fullword ascii
        $s75 = "call" fullword ascii
        $s76 = "case" fullword ascii
        $s77 = "const" fullword ascii
        $s78 = "default" fullword ascii
        $s79 = "detected" fullword ascii
        $s80 = "dllmain_crt_dispatch" fullword ascii
        $s81 = "dllmain_crt_process_attach" fullword ascii
        $s82 = "dllmain_crt_process_detach" fullword ascii
        $s83 = "dllmain_dispatch" fullword ascii
        $s84 = "dllmain_raw" fullword ascii
        $s85 = "double" fullword ascii
        $s86 = "dword_10041010" fullword ascii
        $s87 = "dword_10041930" fullword ascii
        $s88 = "dword_10041934" fullword ascii
        $s89 = "dword_100419B8" fullword ascii
        $s90 = "else" fullword ascii
        $s91 = "entropy" fullword ascii
        $s92 = "fabs" fullword ascii
        $s93 = "fdwReason" fullword ascii
        $s94 = "frndint" fullword ascii
        $s95 = "hinstDLL" fullword ascii
        $s96 = "include" fullword ascii
        $s97 = "long" fullword ascii
        $s98 = "lpReserved" fullword ascii
        $s99 = "lpvReserved" fullword ascii
        $s100 = "off_1003B710" fullword ascii
        $s101 = "output" fullword ascii
        $s102 = "positive" fullword ascii
        $s103 = "result" fullword ascii
        $s104 = "retaddr" fullword ascii
        $s105 = "return" fullword ascii
        $s106 = "savedregs" fullword ascii
        $s107 = "struct" fullword ascii
        $s108 = "switch" fullword ascii
        $s109 = "this" fullword ascii
        $s110 = "thunk" fullword ascii
        $s111 = "uintptr_t" fullword ascii
        $s112 = "unk_100416E4" fullword ascii
        $s113 = "unk_100416E8" fullword ascii
        $s114 = "unk_100416EC" fullword ascii
        $s115 = "unsigned" fullword ascii
        $s116 = "value" fullword ascii
        $s117 = "void" fullword ascii
        $s118 = "while" fullword ascii
        $s119 = "wrong" fullword ascii

    condition:
        uint16(0) == 0x5A4D and 120 of them
}

==============================