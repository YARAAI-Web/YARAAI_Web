rule auto_rule_20250727025220_6502 {
  strings:
    $o0 = "UnwindUp6_0" wide ascii nocase
    $o1 = "x480u" wide ascii nocase
    $o2 = "dword_44B7D0" wide ascii nocase
    $o3 = "_heap_alloc" wide ascii nocase
  condition:
    4 of ($o*)
}