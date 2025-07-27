rule auto_rule_20250726201326_1310 {
  strings:
    $o0 = "start_byte_3" wide ascii nocase
    $o1 = "dword_411D40" wide ascii nocase
    $o2 = "UnwindUp5_0" wide ascii nocase
    $o3 = "_except_handler3" wide ascii nocase
  condition:
    4 of ($o*)
}