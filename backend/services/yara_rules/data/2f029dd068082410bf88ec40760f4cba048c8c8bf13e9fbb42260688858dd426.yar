rule auto_rule_20250726154728_9911 {
  strings:
    $o0 = "xFFFFF1FF" wide ascii nocase
    $o1 = "x18000" wide ascii nocase
    $o2 = "TrailUp3" wide ascii nocase
    $o3 = "_IncMan" wide ascii nocase
  condition:
    4 of ($o*)
}