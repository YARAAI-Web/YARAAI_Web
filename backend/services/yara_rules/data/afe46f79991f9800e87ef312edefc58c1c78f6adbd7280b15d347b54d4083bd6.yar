rule auto_rule_20250726061812_9977 {
  strings:
    $o0 = "dword_456CD8" wide ascii nocase
  condition:
    all of them
}