rule auto_rule_20250726063329_0993 {
  strings:
    $o0 = "x10000800" wide ascii nocase
    $o1 = "v404" wide ascii nocase
    $o2 = "v585" wide ascii nocase
    $o3 = "v593" wide ascii nocase
  condition:
    4 of ($o*)
}