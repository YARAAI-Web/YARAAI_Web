rule auto_rule_20250726170031_3652 {
  strings:
    $o0 = "dword_4C12E0" wide ascii nocase
    $o1 = "Script" wide ascii nocase
    $o2 = "MouseCoordMode" wide ascii nocase
  condition:
    3 of ($o*)
}