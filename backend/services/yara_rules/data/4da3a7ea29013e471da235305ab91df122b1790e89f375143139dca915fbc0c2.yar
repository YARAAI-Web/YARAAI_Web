rule auto_rule_20250726131942_2170 {
  strings:
    $o0 = "off_4751F0" wide ascii nocase
    $o1 = "_SEH_epilog" wide ascii nocase
  condition:
    all of them
}