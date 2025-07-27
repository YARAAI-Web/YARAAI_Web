rule auto_rule_20250727031219_2627 {
  strings:
    $o0 = "x18006B7A2" wide ascii nocase
  condition:
    all of them
}