rule auto_rule_20250726121201_9794 {
  strings:
    $o0 = "aClasses" wide ascii nocase
    $o1 = "dwShareMode" wide ascii nocase
  condition:
    all of them
}