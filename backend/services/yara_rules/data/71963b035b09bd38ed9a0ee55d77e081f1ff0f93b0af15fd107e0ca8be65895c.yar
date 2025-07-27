rule auto_rule_20250726161000_2837 {
  strings:
    $o0 = "x5FD8Fu" wide ascii nocase
  condition:
    all of them
}