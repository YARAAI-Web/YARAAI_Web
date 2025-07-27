rule auto_rule_20250726091954_3485 {
  strings:
    $o0 = "dword_4C1344" wide ascii nocase
    $o1 = "byte_4BBC18" wide ascii nocase
  condition:
    all of them
}