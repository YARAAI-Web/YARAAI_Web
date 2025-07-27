rule auto_rule_20250727014244_7576 {
  strings:
    $o0 = "dword_44A3A8" wide ascii nocase
    $o1 = "dword_44A030" wide ascii nocase
    $o2 = "_seh_longjmp_unwind" wide ascii nocase
  condition:
    3 of ($o*)
}