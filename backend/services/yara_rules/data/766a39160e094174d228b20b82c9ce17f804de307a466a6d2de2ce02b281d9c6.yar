rule auto_rule_20250726070619_9512 {
  strings:
    $o0 = "UnwindUp0_0" wide ascii nocase
    $o1 = "_calloc_dbg" wide ascii nocase
    $o2 = "dwInfoType" wide ascii nocase
  condition:
    3 of ($o*)
}