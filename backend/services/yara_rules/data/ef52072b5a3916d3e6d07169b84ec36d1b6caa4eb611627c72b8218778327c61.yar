rule auto_rule_20250727025439_7718 {
  strings:
    $o0 = "dword_4119B0" wide ascii nocase
    $o1 = "__sbh_alloc_block" wide ascii nocase
    $o2 = "dword_411588" wide ascii nocase
    $o3 = "dword_4119AC" wide ascii nocase
    $o4 = "dword_411738" wide ascii nocase
  condition:
    4 of ($o*)
}