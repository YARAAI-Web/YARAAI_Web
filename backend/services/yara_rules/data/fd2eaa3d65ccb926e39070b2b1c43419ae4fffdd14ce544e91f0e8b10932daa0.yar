rule auto_rule_20250726121553_1044 {
  strings:
    $o0 = "x150u" wide ascii nocase
    $o1 = "dword_42F4C0" wide ascii nocase
  condition:
    all of them
}