rule auto_rule_20250726112149_7822 {
  strings:
    $o0 = "lpStruct" wide ascii nocase
    $o1 = "lpmi" wide ascii nocase
    $o2 = "GetBinaryType" wide ascii nocase
  condition:
    3 of ($o*)
}