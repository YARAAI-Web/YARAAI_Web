rule auto_rule_20250726174527_2689 {
  strings:
    $o0 = "hostlonga" wide ascii nocase
  condition:
    all of them
}