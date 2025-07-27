rule auto_rule_20250726063129_6735 {
  strings:
    $o0 = "aS2ftware" wide ascii nocase
    $o1 = "GetInputDesktop" wide ascii nocase
    $o2 = "uMapType" wide ascii nocase
  condition:
    3 of ($o*)
}