rule auto_rule_20250727020104_6948 {
  strings:
    $o0 = "algn_44C5B2" wide ascii nocase
    $o1 = "TrailUp0_0" wide ascii nocase
    $o2 = "dwInfoType" wide ascii nocase
  condition:
    3 of ($o*)
}