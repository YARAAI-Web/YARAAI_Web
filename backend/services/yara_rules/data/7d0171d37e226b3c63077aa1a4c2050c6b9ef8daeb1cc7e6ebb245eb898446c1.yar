rule auto_rule_20250726071942_1020 {
  strings:
    $o0 = "ServicesReturned" wide ascii nocase
    $o1 = "UuidFromStringW" wide ascii nocase
    $o2 = "x4924923u" wide ascii nocase
  condition:
    3 of ($o*)
}