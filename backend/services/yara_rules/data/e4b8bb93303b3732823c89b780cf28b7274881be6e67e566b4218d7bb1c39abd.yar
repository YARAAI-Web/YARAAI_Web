rule auto_rule_20250727042652_2004 {
  strings:
    $o0 = "dword_14008D5E0" wide ascii nocase
    $o1 = "_Syserror_map" wide ascii nocase
    $o2 = "dword_14008D3F0" wide ascii nocase
  condition:
    3 of ($o*)
}