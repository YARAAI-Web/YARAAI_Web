rule auto_rule_20250726061724_8317 {
  strings:
    $o0 = "byte_476768" wide ascii nocase
    $o1 = "dword_476E48" wide ascii nocase
  condition:
    all of them
}