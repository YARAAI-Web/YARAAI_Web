rule auto_rule_20250726112140_0637 {
  strings:
    $o0 = "dword_42B008" wide ascii nocase
    $o1 = "x5ACE" wide ascii nocase
    $o2 = "lpInBuffer" wide ascii nocase
  condition:
    3 of ($o*)
}