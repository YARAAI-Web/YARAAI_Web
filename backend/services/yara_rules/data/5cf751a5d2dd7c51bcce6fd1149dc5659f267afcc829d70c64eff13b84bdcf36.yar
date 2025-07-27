rule auto_rule_20250727025015_5323 {
  strings:
    $o0 = "dword_411D68" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
  condition:
    3 of ($o*)
}