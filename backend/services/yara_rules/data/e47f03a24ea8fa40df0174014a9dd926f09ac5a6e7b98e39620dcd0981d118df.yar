rule auto_rule_20250727003418_7793 {
  strings:
    $o0 = "mixerSetControlDetails" wide ascii nocase
    $o1 = "TrailDown0" wide ascii nocase
    $o2 = "dword_411E50" wide ascii nocase
  condition:
    3 of ($o*)
}