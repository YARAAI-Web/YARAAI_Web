rule auto_rule_20250726133643_3949 {
  strings:
    $o0 = "_cfltcvt_l" wide ascii nocase
    $o1 = "negative_x" wide ascii nocase
    $o2 = "dword_4C0D14" wide ascii nocase
  condition:
    3 of ($o*)
}