rule auto_rule_20250726125449_1745 {
  strings:
    $o0 = "dword_41D880" wide ascii nocase
    $o1 = "dword_41D888" wide ascii nocase
    $o2 = "dword_404634" wide ascii nocase
  condition:
    3 of ($o*)
}