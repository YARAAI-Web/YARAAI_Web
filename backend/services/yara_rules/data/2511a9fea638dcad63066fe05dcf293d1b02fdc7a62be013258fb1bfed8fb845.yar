rule auto_rule_20250726133119_4123 {
  strings:
    $o0 = "x48D57D47" wide ascii nocase
  condition:
    all of them
}