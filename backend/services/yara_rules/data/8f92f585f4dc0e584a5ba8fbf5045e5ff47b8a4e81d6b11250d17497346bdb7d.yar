rule auto_rule_20250726075506_4494 {
  strings:
    $o0 = "TrailUp0_0" wide ascii nocase
    $o1 = "dword_45D558" wide ascii nocase
  condition:
    all of them
}