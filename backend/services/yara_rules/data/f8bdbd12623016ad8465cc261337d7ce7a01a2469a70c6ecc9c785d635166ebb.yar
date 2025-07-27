rule auto_rule_20250726215953_7201 {
  strings:
    $o0 = "dword_42D010" wide ascii nocase
    $o1 = "flProtect" wide ascii nocase
    $o2 = "xF89F05B9" wide ascii nocase
  condition:
    3 of ($o*)
}