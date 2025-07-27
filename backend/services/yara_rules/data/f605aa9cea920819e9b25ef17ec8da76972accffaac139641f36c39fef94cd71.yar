rule auto_rule_20250726175209_9064 {
  strings:
    $o0 = "dword_411D9C" wide ascii nocase
    $o1 = "__sbh_alloc_new_region" wide ascii nocase
  condition:
    all of them
}