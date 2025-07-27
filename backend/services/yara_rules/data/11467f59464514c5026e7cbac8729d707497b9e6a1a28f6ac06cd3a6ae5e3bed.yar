rule auto_rule_20250726071443_7238 {
  strings:
    $o0 = "_seh_longjmp_unwind" wide ascii nocase
    $o1 = "dword_46444C" wide ascii nocase
    $o2 = "__sbh_alloc_new_region" wide ascii nocase
  condition:
    3 of ($o*)
}