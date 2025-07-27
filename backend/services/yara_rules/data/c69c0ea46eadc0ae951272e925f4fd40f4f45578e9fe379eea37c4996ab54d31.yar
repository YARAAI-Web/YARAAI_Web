rule auto_rule_20250726220735_1854 {
  strings:
    $o0 = "TrailDown0_0" wide ascii nocase
    $o1 = "dwInfoType" wide ascii nocase
    $o2 = "byte_44A181" wide ascii nocase
    $o3 = "dword_44A2A0" wide ascii nocase
    $o4 = "dword_44A3AC" wide ascii nocase
  condition:
    4 of ($o*)
}