rule auto_rule_20250726152715_4313 {
  strings:
    $o0 = "byte_443DD8" wide ascii nocase
    $o1 = "__ascii_stricmp" wide ascii nocase
    $o2 = "__sbh_alloc_block" wide ascii nocase
    $o3 = "dodwords" wide ascii nocase
  condition:
    4 of ($o*)
}