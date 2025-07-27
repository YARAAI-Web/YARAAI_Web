rule auto_rule_20250726183029_6678 {
  strings:
    $o0 = "dword_47725C" wide ascii nocase
    $o1 = "dword_47722C" wide ascii nocase
    $o2 = "main_loop_1" wide ascii nocase
  condition:
    3 of ($o*)
}