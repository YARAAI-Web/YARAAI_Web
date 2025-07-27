rule auto_rule_20250726130953_9239 {
  strings:
    $o0 = "cmdInsert" wide ascii nocase
    $o1 = "HiliteMenuItem" wide ascii nocase
    $o2 = "PathIsSameRootW" wide ascii nocase
    $o3 = "StrToIntExA" wide ascii nocase
  condition:
    4 of ($o*)
}