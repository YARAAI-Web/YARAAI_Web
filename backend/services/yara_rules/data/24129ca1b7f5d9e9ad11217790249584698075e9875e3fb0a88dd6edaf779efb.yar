rule auto_rule_20250726072005_7752 {
  strings:
    $o0 = "x4A52" wide ascii nocase
    $o1 = "x97898797" wide ascii nocase
    $o2 = "off_41D588" wide ascii nocase
    $o3 = "x1248" wide ascii nocase
    $o4 = "dword_429004" wide ascii nocase
  condition:
    4 of ($o*)
}