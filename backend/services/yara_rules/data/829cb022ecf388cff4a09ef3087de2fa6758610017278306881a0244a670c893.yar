rule auto_rule_20250726080043_2870 {
  strings:
    $o0 = "dword_469BAC" wide ascii nocase
    $o1 = "joyGetDevCapsA" wide ascii nocase
  condition:
    all of them
}