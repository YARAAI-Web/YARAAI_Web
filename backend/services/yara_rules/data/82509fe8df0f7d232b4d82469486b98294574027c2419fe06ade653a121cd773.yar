rule auto_rule_20250726174307_7414 {
  strings:
    $o0 = "dbl_459898" wide ascii nocase
    $o1 = "dword_459D30" wide ascii nocase
    $o2 = "lpCharType" wide ascii nocase
    $o3 = "off_4592AC" wide ascii nocase
    $o4 = "_checkTOS_withFB" wide ascii nocase
  condition:
    4 of ($o*)
}