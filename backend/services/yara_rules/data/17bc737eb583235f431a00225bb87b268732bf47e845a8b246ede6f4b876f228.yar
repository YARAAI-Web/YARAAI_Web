rule auto_rule_20250726171219_6859 {
  strings:
    $o0 = "x31C8" wide ascii nocase
    $o1 = "GetTextAlign" wide ascii nocase
  condition:
    all of them
}