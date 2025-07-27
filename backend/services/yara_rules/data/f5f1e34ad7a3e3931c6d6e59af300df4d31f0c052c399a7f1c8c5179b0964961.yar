rule auto_rule_20250727034442_4224 {
  strings:
    $o0 = "_mm_loadl_epi64" wide ascii nocase
    $o1 = "off_47D894" wide ascii nocase
    $o2 = "off_47C5BC" wide ascii nocase
  condition:
    3 of ($o*)
}