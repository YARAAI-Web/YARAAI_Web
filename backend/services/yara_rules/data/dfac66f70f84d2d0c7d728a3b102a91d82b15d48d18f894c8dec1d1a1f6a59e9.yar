rule auto_rule_20250726090620_5120 {
  strings:
    $o0 = "uValue" wide ascii nocase
    $o1 = "hUser" wide ascii nocase
    $o2 = "DdeQueryConvInfo" wide ascii nocase
    $o3 = "presbits" wide ascii nocase
  condition:
    4 of ($o*)
}