rule auto_rule_20250727024759_3571 {
  strings:
    $o0 = "dword_4C1310" wide ascii nocase
    $o1 = "CaretCoordMode" wide ascii nocase
  condition:
    all of them
}