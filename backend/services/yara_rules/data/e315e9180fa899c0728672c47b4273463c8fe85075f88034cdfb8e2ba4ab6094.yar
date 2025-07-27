rule auto_rule_20250726172309_1526 {
  strings:
    $o0 = "gu_return" wide ascii nocase
    $o1 = "dword_449964" wide ascii nocase
    $o2 = "memcpy_0" wide ascii nocase
    $o3 = "RtlUnwind" wide ascii nocase
  condition:
    4 of ($o*)
}