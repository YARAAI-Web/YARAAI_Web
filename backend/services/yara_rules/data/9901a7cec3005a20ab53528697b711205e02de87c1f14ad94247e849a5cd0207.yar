rule auto_rule_20250726080800_9642 {
  strings:
    $o0 = "dword_41A820" wide ascii nocase
  condition:
    all of them
}