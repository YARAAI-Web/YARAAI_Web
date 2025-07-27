rule auto_rule_20250726154505_7619 {
  strings:
    $o0 = "x4ECCu" wide ascii nocase
    $o1 = "dword_428EAB" wide ascii nocase
    $o2 = "x47B3u" wide ascii nocase
    $o3 = "nAtom" wide ascii nocase
  condition:
    4 of ($o*)
}