rule auto_rule_20250726085702_5942 {
  strings:
    $o0 = "x2439u" wide ascii nocase
    $o1 = "x4400" wide ascii nocase
    $o2 = "x1BC7CE72" wide ascii nocase
    $o3 = "x4E91" wide ascii nocase
    $o4 = "x2A54" wide ascii nocase
  condition:
    4 of ($o*)
}