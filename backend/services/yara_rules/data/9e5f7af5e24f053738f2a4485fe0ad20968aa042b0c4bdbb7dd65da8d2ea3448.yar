rule auto_rule_20250726091629_9787 {
  strings:
    $o0 = "xmmword_43EE90" wide ascii nocase
  condition:
    all of them
}