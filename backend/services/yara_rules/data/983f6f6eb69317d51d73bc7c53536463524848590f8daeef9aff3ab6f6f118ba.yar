rule auto_rule_20250726085531_1747 {
  strings:
    $o0 = "_ioinit" wide ascii nocase
    $o1 = "dword_45691C" wide ascii nocase
    $o2 = "dword_41A018" wide ascii nocase
    $o3 = "_forcdecpt" wide ascii nocase
  condition:
    4 of ($o*)
}