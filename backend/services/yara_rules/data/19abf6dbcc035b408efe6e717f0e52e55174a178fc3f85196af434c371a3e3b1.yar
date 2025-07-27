rule auto_rule_20250726104330_0269 {
  strings:
    $o0 = "dword_420F1C" wide ascii nocase
    $o1 = "x435u" wide ascii nocase
    $o2 = "dword_429B20" wide ascii nocase
  condition:
    3 of ($o*)
}