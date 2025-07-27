rule auto_rule_20250726230017_6258 {
  strings:
    $o0 = "bAlertable" wide ascii nocase
    $o1 = "xF89C85BA" wide ascii nocase
  condition:
    all of them
}