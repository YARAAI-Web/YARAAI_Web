rule auto_rule_20250726105243_9727 {
  strings:
    $o0 = "x60C1" wide ascii nocase
    $o1 = "x4F85" wide ascii nocase
    $o2 = "x2F0Fu" wide ascii nocase
    $o3 = "x6B70" wide ascii nocase
    $o4 = "x8949u" wide ascii nocase
  condition:
    4 of ($o*)
}