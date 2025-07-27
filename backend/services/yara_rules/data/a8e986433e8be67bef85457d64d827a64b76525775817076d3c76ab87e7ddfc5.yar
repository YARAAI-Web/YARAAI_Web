rule auto_rule_20250726095726_7033 {
  strings:
    $o0 = "dword_42EED0" wide ascii nocase
    $o1 = "aSystemCurrentc" wide ascii nocase
    $o2 = "dwDesiredAccess" wide ascii nocase
  condition:
    3 of ($o*)
}