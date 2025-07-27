rule auto_rule_20250726211455_2534 {
  strings:
    $o0 = "dword_4363B2" wide ascii nocase
    $o1 = "dword_436456" wide ascii nocase
    $o2 = "x8BF8" wide ascii nocase
  condition:
    3 of ($o*)
}