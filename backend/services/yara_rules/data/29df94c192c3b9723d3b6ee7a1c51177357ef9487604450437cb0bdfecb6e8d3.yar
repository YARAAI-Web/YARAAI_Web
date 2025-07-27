rule auto_rule_20250726072846_2977 {
  strings:
    $o0 = "xDA14B652" wide ascii nocase
  condition:
    all of them
}