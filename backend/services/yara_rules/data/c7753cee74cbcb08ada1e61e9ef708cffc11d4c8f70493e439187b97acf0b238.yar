rule auto_rule_20250726174852_2867 {
  strings:
    $o0 = "off_10076504" wide ascii nocase
  condition:
    all of them
}