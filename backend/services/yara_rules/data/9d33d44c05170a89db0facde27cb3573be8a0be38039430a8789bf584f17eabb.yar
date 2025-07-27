rule auto_rule_20250726232343_0351 {
  strings:
    $o0 = "iCodePage" wide ascii nocase
    $o1 = "CharPrevA" wide ascii nocase
    $o2 = "ulOptions" wide ascii nocase
  condition:
    3 of ($o*)
}