rule auto_rule_20250726220703_6292 {
  strings:
    $o0 = "ExFreePoolWithTag" wide ascii nocase
    $o1 = "_s_FuncInfo" wide ascii nocase
  condition:
    all of them
}