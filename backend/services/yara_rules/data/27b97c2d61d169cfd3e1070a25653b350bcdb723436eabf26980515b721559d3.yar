rule auto_rule_20250726071955_7564 {
  strings:
    $o0 = "aesimc" wide ascii nocase
    $o1 = "x667F" wide ascii nocase
    $o2 = "m64_i32" wide ascii nocase
    $o3 = "v549" wide ascii nocase
    $o4 = "v259" wide ascii nocase
  condition:
    4 of ($o*)
}