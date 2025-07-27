rule auto_rule_20250726192716_5990 {
  strings:
    $o0 = "x4F87" wide ascii nocase
    $o1 = "x3DBE" wide ascii nocase
    $o2 = "OutBuffer" wide ascii nocase
  condition:
    3 of ($o*)
}