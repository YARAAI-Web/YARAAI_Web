rule auto_rule_20250726211306_9114 {
  strings:
    $o0 = "dword_467EC8" wide ascii nocase
    $o1 = "xtoa" wide ascii nocase
  condition:
    all of them
}