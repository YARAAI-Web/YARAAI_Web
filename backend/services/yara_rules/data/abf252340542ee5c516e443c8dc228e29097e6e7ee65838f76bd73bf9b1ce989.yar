rule auto_rule_20250726061522_5573 {
  strings:
    $o0 = "dword_47566C" wide ascii nocase
  condition:
    all of them
}