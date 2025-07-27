rule auto_rule_20250726215454_2525 {
  strings:
    $o0 = "off_455594" wide ascii nocase
    $o1 = "__sbh_alloc_new_region" wide ascii nocase
    $o2 = "dword_4561F0" wide ascii nocase
    $o3 = "off_418178" wide ascii nocase
    $o4 = "__tolower_mt" wide ascii nocase
  condition:
    4 of ($o*)
}