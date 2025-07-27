rule auto_rule_20250726131340_2777 {
  strings:
    $o0 = "start_3" wide ascii nocase
    $o1 = "off_4BAD8C" wide ascii nocase
    $o2 = "normal_0" wide ascii nocase
    $o3 = "start_5" wide ascii nocase
    $o4 = "_forcdecpt_l" wide ascii nocase
  condition:
    4 of ($o*)
}