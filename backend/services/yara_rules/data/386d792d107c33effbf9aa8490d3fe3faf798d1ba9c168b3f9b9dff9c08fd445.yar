rule auto_rule_20250727021924_4891 {
  strings:
    $o0 = "dword_43641E" wide ascii nocase
    $o1 = "dwDesiredAccess" wide ascii nocase
    $o2 = "x13F6u" wide ascii nocase
    $o3 = "dword_432B30" wide ascii nocase
  condition:
    4 of ($o*)
}