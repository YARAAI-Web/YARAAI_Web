rule auto_rule_20250726151800_2669 {
  strings:
    $o0 = "dword_4596FC" wide ascii nocase
    $o1 = "x7FF" wide ascii nocase
  condition:
    all of them
}