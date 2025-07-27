rule auto_rule_20250727013724_8001 {
  strings:
    $o0 = "init" wide ascii nocase
    $o1 = "dword_78854" wide ascii nocase
    $o2 = "dword_78770" wide ascii nocase
    $o3 = "word_1F06E" wide ascii nocase
    $o4 = "MmGetSystemRoutineAddress" wide ascii nocase
  condition:
    4 of ($o*)
}