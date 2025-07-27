rule auto_rule_20250727030557_6766 {
  strings:
    $o0 = "dword_411978" wide ascii nocase
    $o1 = "byte_411A30" wide ascii nocase
    $o2 = "dword_412230" wide ascii nocase
    $o3 = "dword_40E000" wide ascii nocase
  condition:
    4 of ($o*)
}