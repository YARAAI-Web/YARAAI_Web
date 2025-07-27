rule auto_rule_20250726233817_7317 {
  strings:
    $o0 = "hardware" wide ascii nocase
    $o1 = "YAmount" wide ascii nocase
    $o2 = "wsprintfA" wide ascii nocase
    $o3 = "dword_41D978" wide ascii nocase
    $o4 = "ValidateRect" wide ascii nocase
  condition:
    4 of ($o*)
}