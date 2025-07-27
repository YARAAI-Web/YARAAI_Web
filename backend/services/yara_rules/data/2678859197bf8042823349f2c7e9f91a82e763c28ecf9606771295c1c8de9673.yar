rule auto_rule_20250726210526_9015 {
  strings:
    $o0 = "dword_4673BC" wide ascii nocase
  condition:
    all of them
}