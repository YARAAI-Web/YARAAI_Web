rule auto_rule_20250727000905_8849 {
  strings:
    $o0 = "TrailDown2" wide ascii nocase
    $o1 = "dword_44A040" wide ascii nocase
    $o2 = "dword_449AB0" wide ascii nocase
    $o3 = "dword_449ABC" wide ascii nocase
  condition:
    4 of ($o*)
}