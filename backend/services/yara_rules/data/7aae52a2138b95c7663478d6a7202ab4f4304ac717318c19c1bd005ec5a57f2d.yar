rule auto_rule_20250726075815_3155 {
  strings:
    $o0 = "_cfltcvt_init" wide ascii nocase
    $o1 = "dword_44E468" wide ascii nocase
  condition:
    all of them
}