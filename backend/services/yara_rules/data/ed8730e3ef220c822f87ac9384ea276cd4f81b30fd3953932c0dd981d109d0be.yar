rule auto_rule_20250726162755_2536 {
  strings:
    $o0 = "Runtime" wide ascii nocase
    $o1 = "lppf" wide ascii nocase
    $o2 = "VirtualFree" wide ascii nocase
    $o3 = "byte_4471C0" wide ascii nocase
    $o4 = "GetLocaleInfoA" wide ascii nocase
  condition:
    4 of ($o*)
}