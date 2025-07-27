rule auto_rule_20250727043304_0826 {
  strings:
    $o0 = "psSource" wide ascii nocase
  condition:
    all of them
}