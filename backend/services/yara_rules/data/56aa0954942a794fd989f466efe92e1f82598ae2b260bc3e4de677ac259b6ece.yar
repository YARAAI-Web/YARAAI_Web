rule auto_rule_20250726175933_8888 {
  strings:
    $o0 = "SetDebugErrorLevel" wide ascii nocase
    $o1 = "lpFileSizeHigh" wide ascii nocase
    $o2 = "Addend" wide ascii nocase
  condition:
    3 of ($o*)
}