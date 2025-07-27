rule auto_rule_20250726162817_1741 {
  strings:
    $o0 = "hmenu" wide ascii nocase
    $o1 = "GetListBoxInfo" wide ascii nocase
    $o2 = "CharLowerBuffW" wide ascii nocase
  condition:
    3 of ($o*)
}