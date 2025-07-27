rule auto_rule_20250726165521_0291 {
  strings:
    $o0 = "dword_9248CC" wide ascii nocase
  condition:
    all of them
}