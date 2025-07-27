rule auto_rule_20250726071311_6547 {
  strings:
    $o0 = "aSoftware_0" wide ascii nocase
  condition:
    all of them
}