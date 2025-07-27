rule auto_rule_20250726111614_2194 {
  strings:
    $o0 = "dword_427D00" wide ascii nocase
    $o1 = "main_loop_entrance_0" wide ascii nocase
    $o2 = "x7A00001" wide ascii nocase
  condition:
    3 of ($o*)
}