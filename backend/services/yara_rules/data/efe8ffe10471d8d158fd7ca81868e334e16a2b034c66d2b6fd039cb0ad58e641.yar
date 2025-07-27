rule auto_rule_20250726185143_4091 {
  strings:
    $o0 = "dword_1009AF44" wide ascii nocase
    $o1 = "x34E2u" wide ascii nocase
  condition:
    all of them
}