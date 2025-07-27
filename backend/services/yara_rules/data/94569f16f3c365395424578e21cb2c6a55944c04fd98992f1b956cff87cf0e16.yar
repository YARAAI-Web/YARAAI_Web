rule auto_rule_20250727040932_7443 {
  strings:
    $o0 = "LibraryA" wide ascii nocase
    $o1 = "x21C00" wide ascii nocase
    $o2 = "dword_479200" wide ascii nocase
  condition:
    3 of ($o*)
}