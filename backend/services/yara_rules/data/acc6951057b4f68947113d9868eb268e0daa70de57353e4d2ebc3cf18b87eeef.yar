rule auto_rule_20250726090231_7430 {
  strings:
    $o0 = "FFF4h" wide ascii nocase
    $o1 = "ResourceW" wide ascii nocase
  condition:
    all of them
}