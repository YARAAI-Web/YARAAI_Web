rule auto_rule_20250726221420_9747 {
  strings:
    $o0 = "dword_640303EC" wide ascii nocase
    $o1 = "x1D0" wide ascii nocase
  condition:
    all of them
}