rule auto_rule_20250726190203_2061 {
  strings:
    $o0 = "iReadWrite" wide ascii nocase
    $o1 = "nIDStaticPath" wide ascii nocase
    $o2 = "lpnTabStopPositions" wide ascii nocase
    $o3 = "nMaxInstances" wide ascii nocase
    $o4 = "lpIconName" wide ascii nocase
  condition:
    4 of ($o*)
}