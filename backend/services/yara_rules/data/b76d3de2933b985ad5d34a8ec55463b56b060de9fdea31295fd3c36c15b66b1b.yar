rule auto_rule_20250726075051_4941 {
  strings:
    $o0 = "hFindVolume" wide ascii nocase
    $o1 = "hMailslot" wide ascii nocase
    $o2 = "hszItem" wide ascii nocase
  condition:
    3 of ($o*)
}