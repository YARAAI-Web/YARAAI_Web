rule auto_rule_20250727001103_8791 {
  strings:
    $o0 = "x5A3FC98" wide ascii nocase
  condition:
    all of them
}