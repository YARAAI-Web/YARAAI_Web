rule auto_rule_20250726071757_7244 {
  strings:
    $o0 = "off_432A38" wide ascii nocase
    $o1 = "off_4363A0" wide ascii nocase
  condition:
    all of them
}