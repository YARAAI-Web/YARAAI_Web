rule auto_rule_20250726110056_8221 {
  strings:
    $o0 = "dword_411974" wide ascii nocase
    $o1 = "main_loop_0" wide ascii nocase
    $o2 = "dword_40E01C" wide ascii nocase
  condition:
    3 of ($o*)
}