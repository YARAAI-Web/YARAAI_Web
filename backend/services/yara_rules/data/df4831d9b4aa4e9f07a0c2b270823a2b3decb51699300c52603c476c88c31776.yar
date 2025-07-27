rule auto_rule_20250726192938_5024 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "x4095C1" wide ascii nocase
    $o2 = "_cftoe" wide ascii nocase
    $o3 = "_CrtDbgReport" wide ascii nocase
  condition:
    4 of ($o*)
}