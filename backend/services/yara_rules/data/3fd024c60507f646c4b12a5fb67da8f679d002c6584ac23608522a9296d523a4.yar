rule auto_rule_20250726135110_3742 {
  strings:
    $o0 = "dword_46E91C" wide ascii nocase
    $o1 = "byte_46EA54" wide ascii nocase
  condition:
    all of them
}