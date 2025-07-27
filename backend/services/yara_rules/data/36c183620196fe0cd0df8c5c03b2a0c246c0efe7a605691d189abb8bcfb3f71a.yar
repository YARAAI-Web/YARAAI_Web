rule auto_rule_20250726233842_2939 {
  strings:
    $o0 = "x6932" wide ascii nocase
    $o1 = "lpAccelDst" wide ascii nocase
    $o2 = "dword_428010" wide ascii nocase
    $o3 = "off_41D48C" wide ascii nocase
    $o4 = "xF89F85B6" wide ascii nocase
  condition:
    4 of ($o*)
}