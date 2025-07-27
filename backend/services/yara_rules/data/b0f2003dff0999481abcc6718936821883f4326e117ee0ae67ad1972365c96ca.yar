rule auto_rule_20250727013354_6111 {
  strings:
    $o0 = "x3E8" wide ascii nocase
    $o1 = "Abspwamhlp" wide ascii nocase
  condition:
    all of them
}