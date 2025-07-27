rule auto_rule_20250726235644_1506 {
  strings:
    $o0 = "dword_78B8C" wide ascii nocase
    $o1 = "x22C068" wide ascii nocase
    $o2 = "dword_78B14" wide ascii nocase
  condition:
    3 of ($o*)
}