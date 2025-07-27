rule auto_rule_20250726162848_6609 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "differ" wide ascii nocase
    $o2 = "gu_return" wide ascii nocase
    $o3 = "off_479004" wide ascii nocase
  condition:
    4 of ($o*)
}