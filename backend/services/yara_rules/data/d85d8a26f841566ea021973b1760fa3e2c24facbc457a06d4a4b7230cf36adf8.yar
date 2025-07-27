rule auto_rule_20250726090515_1862 {
  strings:
    $o0 = "x75BB8891" wide ascii nocase
  condition:
    all of them
}