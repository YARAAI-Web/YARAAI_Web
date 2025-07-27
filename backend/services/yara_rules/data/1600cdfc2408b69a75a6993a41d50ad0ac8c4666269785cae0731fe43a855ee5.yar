rule auto_rule_20250726223240_0312 {
  strings:
    $o0 = "x8A29A125" wide ascii nocase
    $o1 = "x338E0000001CLL" wide ascii nocase
    $o2 = "x2409u" wide ascii nocase
    $o3 = "x50B0u" wide ascii nocase
  condition:
    4 of ($o*)
}