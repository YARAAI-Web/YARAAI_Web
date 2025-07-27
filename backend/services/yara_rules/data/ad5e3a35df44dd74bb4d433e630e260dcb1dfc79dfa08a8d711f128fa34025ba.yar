rule auto_rule_20250726225130_5340 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "memcpy_0" wide ascii nocase
    $o2 = "dword_449EF0" wide ascii nocase
    $o3 = "Runtime" wide ascii nocase
  condition:
    4 of ($o*)
}