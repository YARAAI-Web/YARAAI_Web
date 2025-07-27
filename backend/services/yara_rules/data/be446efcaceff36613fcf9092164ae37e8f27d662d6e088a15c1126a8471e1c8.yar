rule auto_rule_20250726161846_1744 {
  strings:
    $o0 = "FEFh" wide ascii nocase
    $o1 = "FFFEh" wide ascii nocase
  condition:
    all of them
}