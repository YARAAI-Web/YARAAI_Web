rule auto_rule_20250727015405_3510 {
  strings:
    $o0 = "dword_14008D664" wide ascii nocase
    $o1 = "dword_14008D450" wide ascii nocase
    $o2 = "dword_14008D40C" wide ascii nocase
    $o3 = "dword_14008D784" wide ascii nocase
    $o4 = "rewind" wide ascii nocase
  condition:
    4 of ($o*)
}