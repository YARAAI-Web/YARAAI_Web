rule auto_rule_20250726093119_1887 {
  strings:
    $o0 = "byte_142C3DA70" wide ascii nocase
  condition:
    all of them
}