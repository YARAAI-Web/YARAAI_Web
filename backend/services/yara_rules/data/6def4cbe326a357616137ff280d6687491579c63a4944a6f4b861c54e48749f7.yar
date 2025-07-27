rule auto_rule_20250727022706_8433 {
  strings:
    $o0 = "ppsEditable" wide ascii nocase
  condition:
    all of them
}