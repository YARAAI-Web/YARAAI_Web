rule auto_rule_20250726181049_7207 {
  strings:
    $o0 = "v697" wide ascii nocase
    $o1 = "v637" wide ascii nocase
    $o2 = "x33333333" wide ascii nocase
    $o3 = "x600000006LL" wide ascii nocase
    $o4 = "v693" wide ascii nocase
  condition:
    5 of ($o*)
}