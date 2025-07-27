rule auto_rule_20250727001044_4380 {
  strings:
    $o0 = "stru_140032720" wide ascii nocase
    $o1 = "EHFlags" wide ascii nocase
    $o2 = "sync" wide ascii nocase
    $o3 = "facet" wide ascii nocase
    $o4 = "nIPMapEntries" wide ascii nocase
  condition:
    5 of ($o*)
}