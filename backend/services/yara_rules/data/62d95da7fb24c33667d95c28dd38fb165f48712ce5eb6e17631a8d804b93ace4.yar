rule auto_rule_20250726064301_1113 {
  strings:
    $o0 = "dword_6403133C" wide ascii nocase
  condition:
    all of them
}