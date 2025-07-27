rule auto_rule_20250726213127_1841 {
  strings:
    $o0 = "_NLG_Notify" wide ascii nocase
    $o1 = "_seh_longjmp_unwind" wide ascii nocase
    $o2 = "dword_4672E4" wide ascii nocase
    $o3 = "main_loop_0" wide ascii nocase
  condition:
    4 of ($o*)
}