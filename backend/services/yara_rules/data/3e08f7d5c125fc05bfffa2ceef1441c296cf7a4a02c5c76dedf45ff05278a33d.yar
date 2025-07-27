rule auto_rule_20250726200342_3387 {
  strings:
    $o0 = "x83232" wide ascii nocase
  condition:
    all of them
}