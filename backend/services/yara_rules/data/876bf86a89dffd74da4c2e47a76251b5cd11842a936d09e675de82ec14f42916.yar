rule auto_rule_20250726095431_0857 {
  strings:
    $o0 = "dword_4118F4" wide ascii nocase
    $o1 = "_ctype" wide ascii nocase
    $o2 = "dword_411D98" wide ascii nocase
    $o3 = "dword_412240" wide ascii nocase
  condition:
    4 of ($o*)
}