rule auto_rule_20250726121533_0194 {
  strings:
    $o0 = "memcpy_0" wide ascii nocase
    $o1 = "dword_45CD84" wide ascii nocase
    $o2 = "safely" wide ascii nocase
  condition:
    3 of ($o*)
}