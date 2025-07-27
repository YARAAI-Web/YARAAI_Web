rule auto_rule_20250726063549_3853 {
  strings:
    $o0 = "LocalFlags" wide ascii nocase
    $o1 = "uiParam" wide ascii nocase
    $o2 = "nBufferSize" wide ascii nocase
  condition:
    3 of ($o*)
}