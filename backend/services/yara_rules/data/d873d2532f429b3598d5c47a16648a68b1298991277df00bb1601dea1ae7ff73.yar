rule auto_rule_20250726175047_2131 {
  strings:
    $o0 = "x23FF" wide ascii nocase
    $o1 = "off_42818F" wide ascii nocase
    $o2 = "x437Eu" wide ascii nocase
    $o3 = "x24C0" wide ascii nocase
  condition:
    4 of ($o*)
}