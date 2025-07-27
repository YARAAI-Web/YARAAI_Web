rule auto_rule_20250726171952_8095 {
  strings:
    $o0 = "GetStringTypeW" wide ascii nocase
    $o1 = "stru_40E930" wide ascii nocase
  condition:
    all of them
}