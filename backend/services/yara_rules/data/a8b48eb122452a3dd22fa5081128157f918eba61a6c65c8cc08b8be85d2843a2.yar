rule auto_rule_20250726220632_4641 {
  strings:
    $o0 = "aGsyst12111cgcr" wide ascii nocase
  condition:
    all of them
}