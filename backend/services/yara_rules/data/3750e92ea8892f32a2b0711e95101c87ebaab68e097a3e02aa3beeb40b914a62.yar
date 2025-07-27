rule auto_rule_20250726081143_3993 {
  strings:
    $o0 = "_Error_handling_1" wide ascii nocase
    $o1 = "dword_4C0150" wide ascii nocase
    $o2 = "hInst" wide ascii nocase
    $o3 = "negative_x" wide ascii nocase
  condition:
    4 of ($o*)
}