rule auto_rule_20250726080141_1625 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_449964" wide ascii nocase
    $o2 = "dword_44994C" wide ascii nocase
    $o3 = "CodePagea" wide ascii nocase
  condition:
    4 of ($o*)
}