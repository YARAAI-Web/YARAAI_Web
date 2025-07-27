rule auto_rule_20250726180546_0927 {
  strings:
    $o0 = "EnumDesktopsW" wide ascii nocase
    $o1 = "cAccelEntries" wide ascii nocase
    $o2 = "GetAncestor" wide ascii nocase
  condition:
    3 of ($o*)
}