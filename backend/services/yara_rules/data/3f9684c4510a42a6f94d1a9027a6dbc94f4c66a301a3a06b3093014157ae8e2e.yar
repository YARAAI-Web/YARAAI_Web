rule auto_rule_20250727040115_2941 {
  strings:
    $o0 = "dwInfoType" wide ascii nocase
    $o1 = "x41C4u" wide ascii nocase
    $o2 = "UnwindUp0_0" wide ascii nocase
    $o3 = "off_476C64" wide ascii nocase
    $o4 = "dword_476770" wide ascii nocase
  condition:
    4 of ($o*)
}