rule auto_rule_20250726233704_2476 {
  strings:
    $o0 = "off_429B2F" wide ascii nocase
    $o1 = "dword_429157" wide ascii nocase
    $o2 = "off_429E67" wide ascii nocase
    $o3 = "x69E7u" wide ascii nocase
  condition:
    4 of ($o*)
}