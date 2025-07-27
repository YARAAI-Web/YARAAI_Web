rule auto_rule_20250726115041_9143 {
  strings:
    $o0 = "byte_6402D39A" wide ascii nocase
    $o1 = "EF8h" wide ascii nocase
    $o2 = "dword_64030364" wide ascii nocase
  condition:
    3 of ($o*)
}