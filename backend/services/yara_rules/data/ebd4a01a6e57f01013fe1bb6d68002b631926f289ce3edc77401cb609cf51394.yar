rule auto_rule_20250727025550_9354 {
  strings:
    $o0 = "dword_411ED0" wide ascii nocase
    $o1 = "TrailDown1" wide ascii nocase
    $o2 = "_NLG_Notify" wide ascii nocase
    $o3 = "byte_412041" wide ascii nocase
    $o4 = "dword_411DA8" wide ascii nocase
  condition:
    4 of ($o*)
}