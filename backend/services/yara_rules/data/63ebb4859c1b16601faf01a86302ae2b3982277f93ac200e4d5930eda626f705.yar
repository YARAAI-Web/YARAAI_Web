rule auto_rule_20250726220900_9671 {
  strings:
    $o0 = "dword_41D96C" wide ascii nocase
    $o1 = "ValidateRect" wide ascii nocase
    $o2 = "dword_41D978" wide ascii nocase
    $o3 = "aWmDrawitem" wide ascii nocase
  condition:
    4 of ($o*)
}