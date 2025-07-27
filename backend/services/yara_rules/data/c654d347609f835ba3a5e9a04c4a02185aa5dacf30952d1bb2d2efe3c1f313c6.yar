rule auto_rule_20250726110011_6723 {
  strings:
    $o0 = "dword_44A03C" wide ascii nocase
    $o1 = "VirtualFree" wide ascii nocase
    $o2 = "x41C4u" wide ascii nocase
    $o3 = "_seh_longjmp_unwind" wide ascii nocase
    $o4 = "dword_44A008" wide ascii nocase
  condition:
    4 of ($o*)
}