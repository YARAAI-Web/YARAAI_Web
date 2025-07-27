rule auto_rule_20250726200353_7749 {
  strings:
    $o0 = "off_423DFB" wide ascii nocase
    $o1 = "x8602" wide ascii nocase
    $o2 = "dword_42C008" wide ascii nocase
    $o3 = "x2759u" wide ascii nocase
  condition:
    4 of ($o*)
}