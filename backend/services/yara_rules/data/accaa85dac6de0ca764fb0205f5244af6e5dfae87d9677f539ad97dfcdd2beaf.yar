rule auto_rule_20250726235438_3163 {
  strings:
    $o0 = "wParam_4b" wide ascii nocase
    $o1 = "xB23u" wide ascii nocase
    $o2 = "x3C94" wide ascii nocase
    $o3 = "xFFFF9B65" wide ascii nocase
    $o4 = "xB91BABF3" wide ascii nocase
  condition:
    4 of ($o*)
}