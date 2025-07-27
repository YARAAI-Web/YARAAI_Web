rule auto_rule_20250726180105_0209 {
  strings:
    $o0 = "x9D50" wide ascii nocase
    $o1 = "x381F7BC3" wide ascii nocase
    $o2 = "x6D05B23D" wide ascii nocase
    $o3 = "v320" wide ascii nocase
  condition:
    4 of ($o*)
}