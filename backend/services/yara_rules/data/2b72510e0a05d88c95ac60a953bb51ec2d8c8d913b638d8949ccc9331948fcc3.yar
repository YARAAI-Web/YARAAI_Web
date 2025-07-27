rule auto_rule_20250726065551_0406 {
  strings:
    $o0 = "aGsyst12111cgcr" wide ascii nocase
  condition:
    all of them
}