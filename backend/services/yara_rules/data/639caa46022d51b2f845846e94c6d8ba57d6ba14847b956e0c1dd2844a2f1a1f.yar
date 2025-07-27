rule auto_rule_20250726165817_9128 {
  strings:
    $o0 = "xF89C8532" wide ascii nocase
    $o1 = "GetOpenFileNameA" wide ascii nocase
  condition:
    all of them
}