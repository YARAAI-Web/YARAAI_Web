rule auto_rule_20250727010839_2284 {
  strings:
    $o0 = "byte_73670" wide ascii nocase
    $o1 = "dword_783A0" wide ascii nocase
    $o2 = "swprintf" wide ascii nocase
  condition:
    3 of ($o*)
}